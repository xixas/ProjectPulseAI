import json
import argparse
import sys
import logging
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)

# Function to initialize OpenAI client


def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logging.error("API key is not set in the environment.")
        sys.exit(1)
    return openai.OpenAI(api_key=api_key)

# Function to enhance comments


def enhance_comment(
        client,
        comment_text,
        comment_type,
        model,
        temperature,
        max_tokens):
    # Templates integrated within the prompts for structured enhancements
    prompts = {
        "task_description": """
Directly enhance this brief task description into a detailed and structured format suitable for a software development project, without adding any irrelevant details. Follow this template:
Task Title: [Task Title]
Description: [Brief description of the task]
Objectives:
  - Objective 1: [Objective detail]
  - Objective 2: [Objective detail]
Expected Outcomes: [Describe the expected outcomes of completing the task]
Technical Requirements:
  - Requirement 1: [Detail of the technical requirement]
  - Requirement 2: [Detail of the technical requirement]
Additional Notes: [Any other relevant information or context for the task]

Your task description to enhance:
""" + comment_text,
        "worklog": """
Directly convert this brief worklog into a detailed and structured entry that focuses on the tasks completed and the hours spent on each. Avoid adding any irrelevant information. Follow this template:
Date: [Date of worklog entry]
Tasks Completed:
  - Task 1: [Description of the task and hours spent]
    Hours Spent: [Number]
  - Task 2: [Description of the task and hours spent]
    Hours Spent: [Number]
Challenges Encountered: [Description of any challenges encountered during the tasks]
Learnings: [Any new insights or learnings gained while working on the tasks]
Next Steps: [Planned tasks or objectives for the next period]

Your worklog entry to enhance:
""" + comment_text,
        "normal": "Directly enhance this comment for clarity and detail, ensuring no irrelevant information is added:\n" + comment_text}
    # Retrieve the specific prompt based on the comment type
    prompt = prompts.get(comment_type, "normal")

    try:
        # Create the completion request with the structured messages
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "system",
                    "content": "Don't add any extra notes or comments from your side."},
                {"role": "user", "content": comment_text}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=0.2,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Correctly extract the enhanced text from the response
        enhanced_text = response.choices[0].message.content.strip()
        return enhanced_text
    except Exception as e:
        print(f"Error enhancing comment: {e}")
        return None

# Main function with improved CLI


def main():
    parser = argparse.ArgumentParser(
        description="Enhance a comment using OpenAI.")
    parser.add_argument(
        "input_file",
        help="Path to the JSON input file containing the comment.")
    args = parser.parse_args()

    # Load configuration from environment variables
    model = os.getenv('MODEL', 'gpt-3.5-turbo')
    temperature = float(os.getenv('TEMPERATURE', 0.5))
    max_tokens = int(os.getenv('MAX_TOKENS', 300))

    client = get_openai_client()

    try:
        with open(args.input_file, "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        logging.error(f"Error reading input file: {e}")
        sys.exit(1)

    enhanced_text = enhance_comment(
        client,
        data['text'],
        data['comment_type'],
        model,
        temperature,
        max_tokens)

    if enhanced_text:
        print(enhanced_text)
        # Save the enhanced text to results.md
        with open("results.md", "w") as result_file:
            result_file.write(enhanced_text)
    else:
        logging.info("No enhanced text was generated.")


if __name__ == "__main__":
    main()
