# Usage Guide

## Prerequisites

Ensure you have properly set up and configured Project Pulse AI following the [Development Setup](./development_setup.md) document.

## Using Project Pulse AI

To enhance task descriptions or worklog entries, use the following command:

```bash
python enhance_comment.py examples/task.json
```


## Enhancement Output

The output will be a refined and structured version of the input text, based on the specified `comment_type`:

- **Task Descriptions:** Detailed objectives, expected outcomes, and technical requirements.
- **Worklog Entries:** Clarified tasks completed with hours spent, challenges encountered, and learnings.
- **General Comments:** Enhanced clarity and detail for better understanding.

## Examples

Given a `task.json` file with a brief task description:

```json
{
  "text": "Implement login feature using OAuth",
  "comment_type": "task_description"
}
```

The enhancement might look like:

```bash
$ python enhance_comment.py examples/task.json
```

Output:

```
Task Title: Implement Login Feature
Description: Develop a secure login feature using OAuth authentication protocol.
Objectives:
  - Objective 1: Ensure secure user authentication.
  - Objective 2: Support multiple OAuth providers.
Expected Outcomes: A fully functional login feature that allows users to authenticate using their preferred OAuth provider.
Technical Requirements:
  - Requirement 1: Integration with OAuth 2.0.
  - Requirement 2: Support for Google and Facebook login.
Additional Notes: Prioritize security and user data privacy.
```

For a `worklog.json`:

```json
{
  "text": "Fixed bug in payment processing module and updated documentation.",
  "comment_type": "worklog"
}
```

Enhanced worklog entry:

```bash
$ python enhance_comment.py examples/worklog.json
```

Output:

```
Date: [Current Date]
Tasks Completed:
  - Task 1: Identified and resolved a critical bug in the payment processing module that prevented transaction completion.
    Hours Spent: 3
  - Task 2: Updated the technical documentation to reflect changes made to the payment module and added troubleshooting tips for common issues.
    Hours Spent: 2
Challenges Encountered: Debugging the payment module was challenging due to outdated documentation.
Learnings: Gained a deeper understanding of the payment process flow and improved documentation practices.
Next Steps: Conduct thorough testing with multiple payment methods to ensure all transactions proceed without issues.
```
The results are also saved in `results.md` file.

These examples demonstrate how Project Pulse AI can be used to enhance project communications, making them clearer and more structured.