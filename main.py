# Extract text from pdf using function
import fitz # using pymupdf
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

pdf_path='data/Samin_Chowdhury_SWE.pdf'
def extract_text_from_pdf(pdf_path):
    doc=fitz.open(pdf_path)
    text=""
    for page in doc:
        text+=page.get_text() # fill in the text string
    return text # returns the appended raw text

extracted_raw_text=extract_text_from_pdf(pdf_path)
# print(extracted_raw_text)

# Function to extract data from the extracted_raw_text

def gemini_raw_text_extractor(raw_text):
    # Initialize model
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f""" 
    You are an information extractor. Based on the given resume text, extract the following fields:
    - Name
    - Email
    - Education
    - Graduation Date/Expected Graduation 
    - Skills
    - Roles worked in
    - Role currently seeking

    Return the result as a valid JSON object with these keys only.

    Resume text:
    {raw_text}       
    """

    # Calling the model
    response = model.generate_content(prompt)

    return response.text  # LLM's JSON output


gemini_json_output=gemini_raw_text_extractor(extracted_raw_text)

# save to json
import json


def save_to_json(data, filename="resume_output.json"):
    """Save Python dict or raw JSON string to a JSON file"""
    # If Gemini gave a JSON string, try parsing it first
    if isinstance(data, str):
        try:
            data = json.loads(data)  # convert string → dict
        except json.JSONDecodeError:
            print("⚠️ Gemini output was not valid JSON, saving raw text instead.")
            with open(filename, "w") as f:
                f.write(data)
            return

    # Save dict as pretty JSON
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Example usage
gemini_json_output = gemini_raw_text_extractor(extracted_raw_text)
save_to_json(gemini_json_output, "resume_extracted.json")


# Main function
def main():
    print(gemini_json_output)

# Calling main function
if __name__ == "__main__":
    main()

















