import cv2
import matplotlib.pyplot as plt
import numpy as np
# Reference: https://github.com/deepanshut041/feature-detection/blob/master/sift/sift.ipynb
template_img = cv2.imread('<path of image 1>')
template_gray= cv2.cvtColor(template_img,cv2.COLOR_BGR2GRAY)
source_img = cv2.imread('<path of image 2>')
source_gray= cv2.cvtColor(source_img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
train_keypoints, train_descriptor = sift.detectAndCompute(template_gray, None)
test_keypoints, test_descriptor = sift.detectAndCompute(source_gray, None)
keypoints_without_size = np.copy(template_gray)
keypoints_with_size = np.copy(template_gray)
keypoints_without_size = cv2.drawKeypoints(template_gray, train_keypoints, keypoints_without_size, color = (0, 255, 0))
cv2.imshow("Train keypoints Without Size", keypoints_without_size)
cv2.waitKey(0)
keypoints_with_size = cv2.drawKeypoints(template_gray, train_keypoints, keypoints_with_size, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Train keypoints With Size", keypoints_with_size)
cv2.waitKey(0)
# Print the number of keypoints detected in the training image
print("Number of Keypoints Detected In The Template Image: ", len(train_keypoints))
# Print the number of keypoints detected in the query image
print("Number of Keypoints Detected In The Query Image: ", len(test_keypoints))
# Create a Brute Force Matcher object.
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck = False)
# Perform the matching between the SIFT descriptors of the training image and the test image
matches = bf.match(train_descriptor, test_descriptor)
# The matches with shorter distance are the ones we want.
matches = sorted(matches, key = lambda x : x.distance)
result = cv2.drawMatches(template_img, train_keypoints, source_gray, test_keypoints, matches, source_gray, flags = 2)
# Display the best matching points
cv2.imshow("result", result)
cv2.waitKey(0)
# Print total number of matching points between the training and query images
print("\nNumber of Matching Keypoints Between The Training and Query Images: ", len(matches))