import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

hf_api_key = os.getenv("HF_API_KEY")
if not hf_api_key:
    raise ValueError("Hugging Face API key not found. Please set HF_API_KEY in the .env file.")


# Load .env from the same folder as this file
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Read the API key
HF_API_KEY = os.getenv("HF_API_KEY")

# Debugging print (optional, remove in production)
if HF_API_KEY:
    print("Hugging Face API key loaded successfully.")
else:
    raise ValueError("Hugging Face API key not found. Please set HF_API_KEY in the .env file.")

# Initialize Hugging Face client
client = InferenceClient(api_key=HF_API_KEY)

# Resume templates
template_styles = {
    "classic": """--- CLASSIC RESUME FORMAT ---\n""",
    "modern": """--- MODERN RESUME FORMAT ---
[Name] | [Title]
[Contact Info: Phone | Email | LinkedIn]
[Summary]
[Core Skills]
[Professional Experience]
[Education]
""",
    "creative": """--- CREATIVE RESUME FORMAT ---
[Full Name]
[Contact Info]
[Tagline / Personal Statement]
[Experience Highlights]
[Key Skills]
[Education & Certifications]
"""
}

def generate_resume(name, email, phone, summary, skills, experience, education, template_choice="classic"):
    prompt = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Professional Summary: {summary}
    Skills: {skills}
    Work Experience: {experience}
    Education: {education}
    """
    try:
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": "You are a professional resume writer. Create a well-formatted resume in plain text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800
        )

        model_output = response.choices[0].message["content"].strip()
        final_resume = f"{template_styles.get(template_choice, template_styles['classic'])}\n{model_output}"
        return final_resume
    except Exception as e:
        return f"Error generating resume: {str(e)}"
