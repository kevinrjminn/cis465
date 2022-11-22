import cv2

video1 = cv2.VideoCapturee('basketball.avi')
video2=cv2.VideoWriter('basketball2.avi',0x7643706d,30,(400,300))

success, image1=video1.read()
while success:
	image2 = cv2.resize(image1,(400,300))
	video2.write(image2)
	success,image1=video1.read()
video2.release()