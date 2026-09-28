import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class GeminiDocumentGenerator:

    @staticmethod
    def generate_document(data):
        model = genai.GenerativeModel("gemini-1.5-pro")

        prompt = f"""
        Create a professional {data.document_type}.

        Parties:
        {data.parties}

        Terms:
        {data.terms}

        Effective Date:
        {data.date}

        Format properly with sections, headings, and clauses.
        """

        response = model.generate_content(prompt)
        return response.text
