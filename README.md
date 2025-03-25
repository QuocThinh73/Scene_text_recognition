# Scene Text Recognition Web Application

A web-based application for scene text detection and recognition using YOLO and CRNN models.

## Features

- Upload images containing text
- Detect text regions using YOLO model
- Recognize text in each detected region using CRNN model
- Display results with bounding boxes and recognized text
- Modern UI built with Bootstrap 5
- Backend powered by FastAPI

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/QuocThinh73/Scene_text_recognition.git
   cd Scene_text_recognition
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the web server:
   ```
   cd src
   python main.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

3. Upload an image containing text and click "Recognize Text"

4. View the results with detected text regions and recognized text

## Project Structure

```
Scene_text_recognition/
├── model/                  # Pre-trained models
│   ├── best.pt             # YOLO text detection model
│   └── ocr_crnn.pt         # CRNN text recognition model
├── src/                    # Source code
│   ├── static/             # Static files
│   │   ├── css/            # CSS files
│   │   ├── js/             # JavaScript files
│   │   ├── uploads/        # Uploaded images
│   │   └── results/        # Processed images
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Home page
│   │   └── result.html     # Results page
│   ├── main.py             # FastAPI application
│   └── model_inference.py  # Inference logic
└── requirements.txt        # Dependencies
```

## Technologies Used

- FastAPI: Web framework
- Bootstrap 5: Frontend UI
- PyTorch: Deep learning framework
- YOLO: Text detection model
- CRNN: Text recognition model
- Jinja2: HTML templating
- Uvicorn: ASGI server