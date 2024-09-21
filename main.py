from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    # Open the image from the file contents
    image = Image.open(io.BytesIO(contents))
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    # Return the extracted text in JSON format
    return {"extracted_text": text}
