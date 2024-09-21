# OCR Service with FastAPI

This project is a simple Optical Character Recognition (OCR) service built with FastAPI. The service extracts text from images and PDF files uploaded via an HTTP endpoint.

## Features

- Extract text from image files (e.g., JPG, PNG)
- Extract text from PDF files with images or text content
- Handle multiple file formats
- FastAPI framework for building APIs

## Getting Started

### Prerequisites

- Python 3.9 or higher
- FastAPI
- Pytesseract (OCR library)
- Tesseract-OCR installed on your system
- Uvicorn (ASGI server)
- Pillow (for image processing)
- PyMuPDF (for handling PDF files)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ocr-service.git
    cd ocr-service
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have Tesseract-OCR installed on your machine:
   - [Download Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
   - For Linux, install via your package manager:

    ```bash
    sudo apt install tesseract-ocr
    ```

### Running the Application

1. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to view the Swagger UI where you can test the API.

### Usage

To extract text from an image or PDF file, you can send a POST request to the `/ocr` endpoint.

Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/ocr" -F "file=@path_to_your_file"
