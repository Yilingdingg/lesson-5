import cv2, numpy

ghost=cv2.imread("ghost.png")
g_grey=cv2.imread("ghost.png", 0)
blur=cv2.blur(g_grey,(3,3))
detection=cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT,1,20,param1=50, param2=30, minRadius=15, maxRadius=40 )

numpy_detection=numpy.uint16(numpy.around(detection))
print(numpy_detection)

for pt in numpy_detection[0,:]:
    print(pt)
    x=pt[0]
    y=pt[1]
    r=pt[2]
    cv2.circle(ghost, (x,y),r, (100,100,170), 6)
    cv2.imshow("Result", ghost)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



