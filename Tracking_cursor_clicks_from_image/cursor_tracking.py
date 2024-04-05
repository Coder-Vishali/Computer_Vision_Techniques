# importing the module
import cv2, os
import json, sys
import sys, pygame
from pygame.locals import*
import math
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
        prev_x = x
        prev_y = y
# driver function
if __name__=="__main__":
    # reading the image
    img = cv2.imread(r"<path_of_image>", 1)
    # width = 1000
    # height = 500
    screen_color = (0,0,0)
    line_color = (0,0,255)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    height, width = img_gray.shape
    first_time_flag = 1
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
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
            x = datapoint[0]
            y = datapoint[1]
            if first_time_flag == 1:
                prev_x = x
                prev_y = y
                first_time_flag = 0
            else: 
                print(f"Drawing line: \n prev_x: {prev_x} prev_y: {prev_y} x: {x} y: {y}")
                pygame.draw.line(screen,line_color, (prev_x, prev_y), (x, y))
                start = [prev_x, prev_y]
                end = [x, y]
                rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
                trirad = 5
                pygame.draw.polygon(screen, line_color, ((end[0]+trirad*math.sin(math.radians(rotation)), end[1]+trirad*math.cos(math.radians(rotation))), (end[0]+trirad*math.sin(math.radians(rotation-120)), end[1]+trirad*math.cos(math.radians(rotation-120))), (end[0]+trirad*math.sin(math.radians(rotation+120)), end[1]+trirad*math.cos(math.radians(rotation+120)))))
                pygame.display.flip()
            counter += 1
            prev_x = x
            prev_y = y
            
        pygame.image.save(screen, "res.png")
        with open("img_coords.json", "w") as f:
            f.write(json.dumps(data))