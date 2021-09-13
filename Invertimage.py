import cv2
img = cv2.imread('/home/kornbotdev/pcb1.jpg')
cv2.imshow('image',255-img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to use it in a loop
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('invertImage.jpg',img)
    cv2.destroyAllWindows()
