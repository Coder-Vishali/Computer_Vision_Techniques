# importing the module
import cv2, os
import json, sys

json_data = []

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        json_data.append((x,y))
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        # drawing a small circle
        cv2.circle(img, (x,y), radius=2, color=(0,0,255), thickness=-1)

        # cv2.putText(img, str(x) + ',' +str(y), (x,y), font,1, (0, 0, 255), 2)
        cv2.imshow('image', img)

# driver function
if __name__=="__main__":
    # changing working directory 
    # os.chdir(os.path.dirname(__file__))
    
    path = input("Camera Saved Image Path: ")
    # path = r"camera_feed_test.jpg"
    # reading the image
    img = cv2.imread(path, 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
    # 
    if len(json_data) > 0:
        os.chdir(os.getcwd())
        data = {}
        counter = 0
        for datapoint in json_data:
            data[f"point_{counter}"] = datapoint
            counter += 1
        with open("img_coords.json", "w") as f:
            f.write(json.dumps(data))
