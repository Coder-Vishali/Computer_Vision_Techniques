# import the necessary packages
import cv2
import mediapipe as mp
from tkinter import *
from tkinter import colorchooser

a = Tk()

# Face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=3)

# Function to pick the color from the user
def mcolor():
    color = colorchooser.askcolor()
    label = Label(text='your chosen color', bg=color[1]).pack()
    return (color[0])

# define a video capture object
vid = cv2.VideoCapture(0)
# Utils to print the face landmark numbers
draw = mp.solutions.drawing_utils

# Ask the user to pick a color
# r,g,b=mcolor()
r, g, b = 255, 0, 0
while (True):

    # Capture the video frame by frame
    ret, frame = vid.read()
    # Print the rows, columns and channels of the image/frame
    # print(frame.shape)
    rgb = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
    # print(rgb)
    # Use detector to find landmarks
    faces = face_mesh.process(rgb)
    for face in faces.multi_face_landmarks:
        # Draw the face landmarks
        # draw.draw_landmarks(frame,face)
        # Loop through all the points, 0-468. the below for loop only goes through lip points 49-60.
        for i in range(0, 468):
            x = face.landmark[i].x * 640
            y = face.landmark[i].y * 480
            z = face.landmark[i].z * 640
            cv2.circle(img=frame, center=(int(x), int(y)), radius=1, color=(255, 255, 255), thickness=-2)

    cv2.imshow('Captured frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the window
