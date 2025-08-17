# Extract text from pdf using function
import fitz # using pymupdf

pdf_path='data/Samin_Chowdhury_SWE.pdf'
def extract_text_from_pdf(pdf_path):
    doc=fitz.open(pdf_path)
    text=""
    for page in doc:
        text+=page.get_text() # fill in the text string
    return text # returns the appended raw text

extracted_raw_text=extract_text_from_pdf(pdf_path)
# print(extracted_raw_text)








