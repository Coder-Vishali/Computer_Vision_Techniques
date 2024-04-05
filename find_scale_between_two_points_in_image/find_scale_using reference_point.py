import cv2
import numpy as np
def calculate_scale(image_path, pointer_position, reference_object_position, real_world_size):
    # Load the image
    image = cv2.imread(image_path)
    # Calculate the distance between the pointer and the reference object
    pixel_distance = np.linalg.norm(np.array(pointer_position) - np.array(reference_object_position))
    # Calculate the scale
    scale = real_world_size / pixel_distance
    return scale
# Example usage:
image_path = r"C:\Project_Files\template_matching\source_images\test_images\FMS_Plan_4_Full.bmp"  # Replace with the path to your image
image = cv2.imread(image_path)
pointer_position = (354,246)  # Replace with the pointer's position (x, y)
reference_object_position = (379,246) # Replace with the reference object's position (x, y)
real_world_size = 10  # Replace with the known real-world size of the reference object (e.g., 10 cm)
# Calculate the scale
scale = calculate_scale(image_path, pointer_position, reference_object_position, real_world_size)
# Green color in BGR 
color = (0, 0, 255) 
# Line thickness of 9 px 
thickness = 2
# Using cv2.line() method 
# Draw a diagonal green line with thickness of 9 px 
image = cv2.line(image, pointer_position, reference_object_position, color, thickness) 
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (364-10,246-10)
  
# fontScale 
fontScale = 0.5
   
# Blue color in BGR 
color = (0, 0, 255) 
  
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.putText() method 
image = cv2.putText(image, str(scale), org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
  
# Displaying the image  
cv2.imshow("image", image)  
# wait for a key to be pressed to exit
cv2.waitKey(0)
# Print the calculated scale
print("Calculated Scale:", scale)