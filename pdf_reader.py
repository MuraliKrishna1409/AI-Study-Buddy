import PyPDF2

def extract_text_from_pdf(file_path):

    try:
        text = ""

        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text() or ""

        if not text.strip():
            return "Error: No text found in PDF"

        return text

    except Exception as e:
        return f"Error: {str(e)}"