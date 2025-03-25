import os
import uuid
from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import shutil

app = FastAPI(title="Scene Text Recognition")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="src/templates")

# Create upload and results directories if they don't exist
os.makedirs("static/uploads", exist_ok=True)
os.makedirs("static/results", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recognize")
async def recognize_text(request: Request, file: UploadFile = File(...)):
    # Generate a unique filename
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    
    # Save the uploaded file
    upload_path = f"static/uploads/{unique_filename}"
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Process the image using the inference function
    result_path = f"static/results/{unique_filename}"
    
    # Call the inference function
    # inference(upload_path, result_path)
    
    
    # Return the result page
    return templates.TemplateResponse(
        "result.html", 
        {
            "request": request, 
            "input_image": f"/static/uploads/{unique_filename}",
            "output_image": f"/static/results/{unique_filename}"
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
