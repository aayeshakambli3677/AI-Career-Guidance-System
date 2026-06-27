from app.utils.pdfutils import process_pdf
import os

file_path = os.path.join(os.path.dirname(__file__), "sample.pdf")

# simulate a PDF file
# file_path = "sample.pdf"

class FakeFile:
    def __init__(self, path):
        self.filename = path
        self.file = open(path, "rb")

    def read(self):
        return self.file.read()

    def seek(self, pos):
        self.file.seek(pos)


fake_file = FakeFile(file_path)

text = process_pdf(fake_file)

print("\n===== EXTRACTED TEXT =====\n")
print(text)