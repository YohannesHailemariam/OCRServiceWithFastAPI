import pytesseract
import fitz  # PyMuPDF
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import shutil
import os
import io

app = FastAPI()

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    # Create a temporary directory to store the uploaded file
    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)

    # Save the uploaded file temporarily
    file_path = os.path.join(temp_dir, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        # If the file is an image, process it
        if file.content_type.startswith("image/"):
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            return {"text": text}

        # If the file is a PDF, extract images from each page and run OCR on them
        elif file.content_type == "application/pdf":
            # Open the PDF file
            pdf_doc = fitz.open(file_path)
            extracted_text = ""

            for page_num in range(pdf_doc.page_count):
                page = pdf_doc.load_page(page_num)
                pix = page.get_pixmap()  # Convert page to image

                # Convert the pixmap (image) to a PIL Image object
                img = Image.open(io.BytesIO(pix.tobytes("png")))

                # Extract text using Tesseract
                text = pytesseract.image_to_string(img)
                extracted_text += f"\n--- Page {page_num + 1} ---\n{text}"

            pdf_doc.close()
            return {"text": extracted_text}

        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")

    finally:
        # Cleanup the temporary file
        os.remove(file_path)
