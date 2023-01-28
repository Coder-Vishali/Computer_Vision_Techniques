# import the necessary packages
import os, cv2, io, glob
import mediapipe as mp
import numpy as np

def resize_image(image):
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    cv2.imshow("Resized image", resized)
    cv2.waitKey()

# Face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
mp_drawing_styles = mp.solutions.drawing_styles

# Utils to print the face landmark numbers
draw = mp.solutions.drawing_utils

# define a video capture object
vid = cv2.VideoCapture(0)

i = 0
while (True):
    i = i + 1
    # Capture the video frame by frame
    ret, img = vid.read()
    rgb = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mesh = np.zeros_like(img)
    # Use detector to find landmarks
    faces=face_mesh.process(rgb)
    for face in faces.multi_face_landmarks:
        draw.draw_landmarks(
            image=mesh,
            landmark_list=face,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
    cv2.imwrite(r"img_" + str(i) + r".jpg", mesh)
    cv2.imshow('Face Mesh',mesh)
    # cv2.waitKey()
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
