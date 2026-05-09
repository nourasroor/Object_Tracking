# Object Detection App

A simple Streamlit application for objects tracking using OpenCV background subtraction.

## Overview

This project lets users upload a video file and view:

- the original uploaded video
- a processed video with detected objects highlighted
- the foreground mask used for object detection

The app uses OpenCV's `BackgroundSubtractorMOG2` to detect moving objects and draw bounding boxes around them.

## Features

- Video upload support (`.mp4`, `.avi`)
- Real-time frame processing using OpenCV
- Display of both processed video frames and foreground mask
- Simple web interface powered by Streamlit

## Requirements

- Python 3.7+
- `streamlit`
- `opencv-python`
- `numpy`

These requirements are already listed in `requirements.txt`.

## Setup

1. Create a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

## Run the app

From the project directory, run:

```powershell
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Usage

1. Open the Streamlit app in your browser.
2. Upload a video file in `.mp4` or `.avi` format.
3. The app displays the original video, the detected objects video, and the foreground mask.

## Notes

- The current detection method uses background subtraction and contour filtering.
- Very small contours are ignored using an area threshold of `500`.
- This app is best for videos with a relatively static background and moving objects.

## Improvements

Potential enhancements include:

- adding object classification or tracking IDs
- improving detection with deep learning models
- adding controls for threshold and detection sensitivity
- supporting more video formats

## Files

- `app.py` � main Streamlit application
- `requirements.txt` � Python dependencies
- `README.md` � project documentation
