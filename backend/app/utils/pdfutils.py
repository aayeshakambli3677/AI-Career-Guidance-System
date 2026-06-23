import os
import uuid
import logging
from typing import Optional

from PyPDF2 import PdfReader

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =========================
# CONFIGURATION
# =========================
ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE_MB = 5  # adjust if needed
UPLOAD_FOLDER = "uploads/resumes"


# =========================
# UTIL: FILE VALIDATION
# =========================
def is_allowed_file(filename: str) -> bool:
    """Check if file has allowed extension (.pdf only)."""
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS


def validate_file_size(file_size: int) -> bool:
    """Validate file size (in bytes)."""
    max_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
    return file_size <= max_bytes


# =========================
# UTIL: SAVE FILE
# =========================
def save_pdf(file) -> str:
    """
    Save uploaded PDF file securely and return stored file path.
    Works with FastAPI/Flask file-like objects.
    """

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Generate unique filename
    unique_name = f"{uuid.uuid4().hex}.pdf"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.read())

        logger.info(f"PDF saved at {file_path}")
        return file_path

    except Exception as e:
        logger.error(f"Error saving PDF: {str(e)}")
        raise Exception("Failed to save PDF file")


# =========================
# UTIL: EXTRACT TEXT
# =========================
def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    Returns cleaned plain text.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("PDF file not found")

    text_content = []

    try:
        reader = PdfReader(file_path)

        if len(reader.pages) == 0:
            raise ValueError("Empty PDF file")

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()

            if text:
                text_content.append(text)

        full_text = "\n".join(text_content)

        # Basic cleaning
        cleaned_text = clean_text(full_text)

        logger.info("PDF text extraction successful")

        return cleaned_text

    except Exception as e:
        logger.error(f"Error extracting PDF text: {str(e)}")
        raise Exception("Failed to extract text from PDF")


# =========================
# UTIL: TEXT CLEANING
# =========================
def clean_text(text: str) -> str:
    """
    Clean extracted PDF text for AI processing.
    """

    if not text:
        return ""

    # Remove excessive whitespace
    text = " ".join(text.split())

    # Normalize line breaks
    text = text.replace("\n", " ")

    return text.strip()


# =========================
# MAIN PIPELINE FUNCTION
# =========================
def process_pdf(file, file_size: Optional[int] = None) -> str:
    """
    Full pipeline:
    1. Validate file
    2. Save file
    3. Extract text
    4. Return cleaned text
    """

    filename = getattr(file, "filename", None)

    if not filename:
        raise ValueError("Invalid file input")

    # Validate extension
    if not is_allowed_file(filename):
        raise ValueError("Only PDF files are allowed")

    # Validate file size (if provided)
    if file_size and not validate_file_size(file_size):
        raise ValueError(f"File too large. Max allowed is {MAX_FILE_SIZE_MB}MB")

    # Reset file pointer (important for FastAPI/Flask uploads)
    try:
        file.seek(0)
    except Exception:
        pass

    # Step 1: Save PDF
    saved_path = save_pdf(file)

    # Step 2: Extract text
    extracted_text = extract_text_from_pdf(saved_path)

    if not extracted_text:
        raise ValueError("No readable text found in PDF")

    return extracted_text