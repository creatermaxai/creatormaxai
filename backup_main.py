import os
import time
from fastapi import FastAPI, UploadFile, HTTPException
from datetime import datetime

app = FastAPI()

# Storage folder setup
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# AI Analysis Logic (Comedy, Horror, etc.)
def analyze_content(filename):
    # Dummy logic for analysis
    return {"status": "Horror/Comedy Detected", "tags": "#viral #shorts #horror #comedy"}

# Auto-Delete Logic (Every 5 Hours)
def clean_storage():
    now = time.time()
    for f in os.listdir(UPLOAD_DIR):
        f_path = os.path.join(UPLOAD_DIR, f)
        if os.stat(f_path).st_mtime < now - (5 * 3600):
            os.remove(f_path)

@app.get("/")
def home():
    return {"message": "AI Shorts Master Server is Running"}

@app.post("/upload")
async def upload_video(file: UploadFile):
    # Security check: Hack protection
    if not file.filename.endswith(('.mp4', '.mov')):
        raise HTTPException(status_code=400, detail="Sirf Video files allow hain!")
    
    clean_storage() # Har upload par purana data check karega
    return analyze_content(file.filename)
