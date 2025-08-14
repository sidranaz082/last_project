Final Report – AI Resume Generator Project
1. Project Overview

The AI Resume Generator is a Flask-based web application that uses an AI language model from Hugging Face to generate professional resumes based on user inputs.
Users provide their personal details, professional summary, skills, work experience, and education, and the application formats them into a well-structured resume .

2. Project Files

app.py

Main Flask application file.

Handles routes / (home) and /generate (resume generation).

Renders index.html and passes the generated resume to be displayed.

llm_wrapper.py

Handles communication with the Hugging Face InferenceClient.

Defines multiple resume templates (classic, modern, creative).

Sends user data as a prompt to the AI model and returns formatted output.

index.html

HTML front-end template styled with Bootstrap.

Contains form fields for all required resume details.

Displays the generated resume in a styled box.

3. Setup Instructions
Step 1 – Create Project Files

Save the app.py, llm_wrapper.py, and index.html in the same directory.

Place index.html inside a templates folder (Flask default).

Step 2 – Install Required Packages
pip install flask huggingface_hub

Step 3 – Set Up Hugging Face API Key

Create a Hugging Face account at https://huggingface.com.

Generate an API key from account.

Replace the placeholder in llm_wrapper.py:

HF_API_KEY = "my_api_key_here"

Step 4 – Run the Application
python app.py


The application will start on: http://127.0.0.1:5000/.

Step 5 – Use the Application

Open the URL in your browser.

Fill out the form with personal and professional details.

Select a resume template.

Click "Generate Resume" to see your AI-generated resume.

4. Key Features

✅ AI-Powered Resume Generation – Uses Hugging Face’s Mistral-7B-Instruct model for realistic, professional text output.
✅ Multiple Resume Templates – Currently includes Classic, with placeholders for Modern and Creative.
✅ Responsive Design –  a clean and mobile-friendly interface.
✅ Dynamic Rendering – Generated resume is displayed instantly without page reload.
✅ Customizable – Templates and AI prompt can be easily modified for better personalization.

5. Reflection and Learnings

Working on this project gave me hands-on experience in integrating AI models into a Flask application. I learned how to:

Send structured prompts to AI models and parse the response for clean output.

Build a user-friendly web interface with HTML, CSS, and Bootstrap.

Connect Python backend with AI services using API keys and client libraries.

Organize a Flask project into modular files for maintainability.

Handle form data in Flask and pass it to templates.

This project strengthened my understanding of Flask routing, template rendering, and API integration. It was rewarding to see how quickly AI can produce high-quality resumes with minimal manual effort, and it gave me insights into building real-world AI-powered tools.


Problems Faced

Repetitive Resume Content – The generated text often contained repeated words and phrases, making it sound less professional. This required post-processing to improve quality.

Environment Variable Issues – Initially, the .env file was not being loaded correctly, causing the API key to be “not found” and halting the program.

Model Output Quality Variability – The quality of generated resumes varied significantly. While some results were clear and professional, others lacked proper structure.

Minimal Input Test Results – When only keywords were provided in the input (e.g., skills and job titles), the LLM sometimes failed to structure the resume in a fully professional format. Instead, it produced fragmented or less coherent sections.

Dependency Setup Problems – Missing packages like python-dotenv caused execution failures until installed.


live link:https://last-project-virid.vercel.app/
I have attempted multiple times to deploy project on Vercel. Although the deployment eventually succeeded, I encountered recurring issues with the build cache. The cached builds sometimes caused errors such as “Skipping cache upload because no files were prepared” or outdated function code being served. 
