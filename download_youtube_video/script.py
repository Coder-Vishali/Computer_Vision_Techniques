import os
import cv2
import pafy
from moviepy.editor import *

image_height, image_width = 64, 64

##################################################
# Function to Download YouTube Videos:
##################################################

# Let us start by testing on some YouTube videos. This function will
# use pafy library to download any youtube video and return its title. We just need to pass the URL.

def download_youtube_videos(youtube_video_url, output_directory):
    # Creating a Video object which includes useful information regarding the youtube video.
    video = pafy.new(youtube_video_url)

    # Getting the best available quality object for the youtube video.
    video_best = video.getbest()

    # Constructing the Output File Path
    output_file_path = f'{output_directory}/{video.title}.mp4'

    # Downloading the youtube video at the best available quality.
    video_best.download(filepath = output_file_path, quiet = True)

    # Returning Video Title
    return video.title

def convert_video_to_image(video_file_path):
    # Reading the Video File using the VideoCapture Object
    video_reader = cv2.VideoCapture(video_file_path)
    i = 0
    while True:

        # Reading The Frame
        status, frame = video_reader.read()

        if not status:
            break

        # Resize the Frame to fixed Dimensions
        resized_frame = cv2.resize(frame, (image_height, image_width))

        data_file = os.path.join(os. getcwd(), dataset_directory)
        outfile = os.path.join(data_file, 'Frame' + str(i) + '.jpg')
        cv2.imshow('Predicted Frames', resized_frame)
        cv2.imwrite(outfile, resized_frame)
        i +=1
        key_pressed = cv2.waitKey(10)

        if key_pressed == ord('q'):
             break

    cv2.destroyAllWindows()

    # Closing the VideoCapture and VideoWriter objects and releasing all resources held by them.
    video_reader.release()

################################
# Download a Test Video:
################################
# Creating The Output directories if it does not exist
output_directory = 'Youtube_Videos_for_aiml'
os.makedirs(output_directory, exist_ok = True)

dataset_directory = 'dataset'
os.makedirs(dataset_directory, exist_ok = True)

# Downloading a YouTube Video
video_title = download_youtube_videos('https://www.youtube.com/watch?v=jG8l9-ojow4', output_directory)

# Getting the YouTube Video's path you just downloaded
input_video_file_path = f'{output_directory}/{video_title}.mp4'

# Calling the convert video to image method
convert_video_to_image(input_video_file_path)
