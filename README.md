# Object Tracking APP

## Project Overview

This repository contains a Streamlit-based object tracking application that uses OpenCV for motion detection and visualization. The app accepts `.mp4` and `.avi` video uploads, processes each frame using background subtraction, identifies moving objects with contour detection, and renders both the processed output and the foreground mask.

The current implementation is designed for proof-of-concept object motion tracking, including applications such as workplace monitoring, simple surveillance, or video analytics demonstrations.

## Key Features

- Upload video files directly through a Streamlit interface
- Process video frames using OpenCV's MOG2 background subtraction algorithm
- Detect motion by extracting foreground contours from the background mask
- Draw bounding boxes around moving objects in the video
- Display both the original processed frame and the foreground mask side by side
- Customize bounding box color using a color picker
- Control processing speed with an adjustable slider

## File Structure

- `app.py`: Main Streamlit application with UI controls and OpenCV video processing logic.
- `requirements.txt`: Project dependency list for Python package installation.
- `README.md`: Project documentation and usage instructions.

## Detailed Architecture

### User Interface

The Streamlit UI is built with a main page and a sidebar.
- Main page: title, app description, and the video upload widget.
- Sidebar: controls for bounding box color and frame processing speed.

### Video Processing Pipeline

1. The user uploads a video file via `st.file_uploader`.
2. Uploaded bytes are written to a temporary file to make the video accessible to OpenCV.
3. `cv2.VideoCapture` opens the temporary file and learns the total frame count.
4. `cv2.createBackgroundSubtractorMOG2()` creates a background subtraction model.
5. Each frame is read from the video and passed to the background subtractor.
6. The resulting foreground mask is analyzed using `cv2.findContours()`.
7. Contours with area above a threshold are drawn as bounding boxes on the video frame.
8. The processed frame and the grayscale foreground mask are displayed in real time.

### Detection Logic

- Background subtractor: OpenCV MOG2 algorithm with default parameters.
- Contour retrieval: `cv2.RETR_EXTERNAL` extracts external contours only.
- Contour approximation: `cv2.CHAIN_APPROX_SIMPLE` reduces contour points for efficiency.
- Bounding box filter: only contours with area greater than `500` pixels are visualized.
- Color conversion: selected hex color is converted to BGR integers for OpenCV drawing.

## Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Open the provided local URL in your browser.
4. Upload a video file (`.mp4` or `.avi`).
5. Adjust the bounding box color and processing speed.
6. Watch the app display the tracked motion and corresponding foreground mask.

## Notes and Limitations

- The app performs frame-by-frame motion detection and does not maintain unique object IDs between frames.
- It is best suited for videos with moderate camera movement; heavy camera shake may produce noisy masks.
- Performance depends on video size, frame rate, and selected slider speed.
- The current `requirements.txt` contains Python package names; if installation issues occur, use `opencv-python` instead of `opencv-python-headless`.

## Future Improvements

- Add a minimum area slider to fine-tune contour filtering.
- Add a toggle to display or hide the foreground mask.
- Implement object tracking with identity assignment across frames.
- Support additional video file formats and batch processing.
- Add logging and download options for processed video output.


