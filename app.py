
import numpy as np
import cv2
import streamlit as st
import tempfile
from PIL import Image
import time

st.set_page_config(page_title='Object Tracking App', layout='wide', page_icon='📷')

st.title('Object Tracking Dashboard')
st.markdown(
    'Upload a video to detect moving objects using OpenCV background subtraction and display both the processed output and the foreground mask.'
)

with st.sidebar:
    st.header("🎯 Object Tracking App")
    st.markdown(
        """
        This app allows you to upload a video and see object tracking in action using OpenCV's Background Subtraction method.
        """)
    st.markdown("---")
    st.header("🎨 Customization")
    color = st.color_picker("Pick a color")
    st.markdown("---")
    st.header("speed")
    speed = st.slider("Processing Speed", 1, 60, 30)



# with st.sidebar:
#     st.header('Settings')
#     min_area = st.slider('Minimum contour area', min_value=100, max_value=5000, value=500, step=100)
#     show_mask = st.checkbox('Show foreground mask', value=True)
#     color = st.color_picker('Pick a color for bounding boxes', '#FF0000')
#     hexa = color.lstrip('#')
#     rgb = tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))
#     # color hexa ---> rgb tuple

#     speed_ = st.slider('Processing speed (ms per frame)', min_value=0, max_value=1000, value=100, step=50)

#     st.markdown('---')
#     st.markdown('**Instructions:**')
#     st.write('1. Upload an `.mp4` or `.avi` video file.')
#     st.write('2. Wait while frames are processed.')
#     st.write('3. View the detections and mask output.')


# ############################## Code
# file = st.file_uploader('Upload Video', type=['mp4', 'avi'])

# if file is not None:
#     tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.' + file.name.split('.')[-1])
#     tfile.write(file.read())

#     capture = cv2.VideoCapture(tfile.name)
#     frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
#     fps = capture.get(cv2.CAP_PROP_FPS) or 25

#     background_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

#     left_col, middle_col, right_col = st.columns([1, 1, 1])

#     with left_col:
#         st.subheader('Original Video')
#         st.video(file)

#     with middle_col:
#         st.subheader('Detection Output')
#         frame_ph = st.empty()

#     with right_col:
#         st.subheader('Foreground Mask')
#         mask_ph = st.empty()

#     progress_bar = st.progress(0)
#     status_text = st.empty()

#     frame_index = 0
#     while capture.isOpened():
#         ret, frame = capture.read()
#         if not ret:
#             break

#         frame_index += 1
#         fg_mask = background_subtractor.apply(frame)
#         contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         for contour in contours:
#             if cv2.contourArea(contour) > min_area:
#                 x, y, w, h = cv2.boundingRect(contour)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), rgb, 2)

#         display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_ph.image(display_frame, caption=f'Frame {frame_index}', use_column_width=True)

#         if show_mask:
#             mask_ph.image(fg_mask, caption='Foreground Mask', channels='GRAY', use_column_width=True)

#         if frame_count > 0:
#             progress = min(int(frame_index / frame_count * 100), 100)
#             progress_bar.progress(progress)
#             status_text.info(f'Processing frame {frame_index} of {frame_count} ({progress}%)')
#         else:
#             status_text.info(f'Processing frame {frame_index}')

#     capture.release()
#     status_text.success('Video processing complete.')
#     progress_bar.empty()



################################
def convert_color(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



upload_file = st.file_uploader('Upload Video', type=['mp4', 'avi'])

if upload_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(upload_file.read())
    tfile.close()

    capture = cv2.VideoCapture(tfile.name)

    if not capture.isOpened():
        st.error('Error opening video file')
    
    else:
        st.success("Video file opend successfully, preprocessing....")

        col1 , col2 = st.columns(2)

        with col1:
            st.subheader('Orignal video')
            stframe1 = st.empty()

        with col2:
            st.subheader('Processed video')
            stframe2 = st.empty()

        background_subtractor = cv2.createBackgroundSubtractorMOG2()
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        progress_bar = st.progress(0)
        frame_idx = 0

        # conver color hex to BGR
        hex_color = color.lstrip("#")
        color = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        
        
        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break
            fg_mask = background_subtractor.apply(frame)
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            

            stframe1.image(convert_color(frame),channels = 'RGB')
            stframe2.image(fg_mask,channels = 'GRAY')
            frame_idx +=1
            progress_bar.progress(min(frame_idx/frame_count , 1.0))
            time.sleep(1/speed)
        
        capture.release()
        st.success('Video Processing completed')
















# background_subtractor = cv2.createBackgroundSubtractorMOG2()
# capture = cv2.VideoCapture(r'D:\Route_AI\Sessions_DL\Session_15_CV\Project3_ObjectDetection\Copy of vtest.avi')


