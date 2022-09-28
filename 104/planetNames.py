import cv2
img = cv2.imread("solarSystem.jpg")
print(img)
cv2.putText(img,  
           "Sun",
           (70, 50),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL ,
           fontScale=2,  
           thickness = 4,
           color=(5, 145, 252)
           )
cv2.putText(img,  
           "Mercury",
           (110, 160),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL ,
           fontScale=1,  
           thickness = 2,
           color=( 203, 227, 198)
           )
cv2.putText(img,  
           "Venus",
           (175, 280),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(0, 131, 255)
           )
cv2.putText(img,  
           "Earth",
           (275, 160),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL ,
           fontScale=1,  
           thickness = 2,
           color=(95, 29, 42)
           )
cv2.putText(img,  
           "Mars",
           (375, 280),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(61, 61, 247)
           )
cv2.putText(img,  
           "Jupiter",
           (550, 50),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL ,
           fontScale=1,  
           thickness = 2,
           color=(101, 216, 250)
           )
cv2.putText(img,  
           "Saturn",
           (750, 300),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(252, 204, 251)
           )
cv2.putText(img,  
           "Uranus",
           (950, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL ,
           fontScale=1,  
           thickness = 2,
           color=(247, 213, 173)
           )
cv2.putText(img,  
           "Neptune",
           (1100, 290),  
           fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX ,
           fontScale=1,  
           thickness = 2,
           color=(155, 57, 50)
           )
cv2.imshow("Solar System", img)
cv2.waitKey(0)
