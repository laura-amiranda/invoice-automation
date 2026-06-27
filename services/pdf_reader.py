import pdfplumber


class PDFReader:

    def read_pdf(self, pdf_path: str) -> str:
        with pdfplumber.open(pdf_path) as pdf:

            full_text = ""

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    full_text += text + "\n"

        return full_text.split("\n")