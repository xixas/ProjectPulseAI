# Development Setup

## Prerequisites

Before setting up Project Pulse AI, ensure you have Python installed on your system. This project also requires an OpenAI API key for AI-powered enhancements. If you do not already have one, sign up and obtain an API key from the OpenAI platform.

## Installation

Follow these steps to install and set up Project Pulse AI on your local machine:

1. Clone the Project Pulse AI repository:

   ```bash
   git clone https://github.com/xixas/ProjectPulseAI
   cd project-pulse-ai
   ```

2. Create a Python virtual environment to manage the project's dependencies:

   ```bash
   python -m venv venv
   ```

   Here, the first `venv` is the module for creating virtual environments, and the second `venv` is the name of the virtual environment. You can choose a different name for your environment if you prefer.

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   Your command prompt should now indicate that the virtual environment is active, usually by showing its name.

4. Install the required Python packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary dependencies, including the `openai` library, within your virtual environment.

5. Configure your `.env` file for environment variables:

   - Create a new file named `.env` in the root directory of the project.
   - Refer to a `.env.example` file if provided, or simply add your OpenAI API key in the `.env` file like so:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

   Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key.

## Deactivating Virtual Environment

To exit the virtual environment when you've finished working with Project Pulse AI:

- On Windows:

  ```bash
  deactivate
  ```

- On macOS and Linux:

  ```bash
  deactivate
  ```

Exiting the virtual environment ensures that any further Python commands you run will use your system's global Python environment, keeping dependencies for Project Pulse AI isolated.