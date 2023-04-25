import cv2
vid = cv2.VideoCapture(0)
while True :
    ret, frame = vid.read()
    image = cv2.putText(frame,"WELCOME TO ML CLASS",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,
                                      cv2.LINE_AA)
    cv2.imshow("live video", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("i am hear")
        break
vid.release()
cv2.destroyAllWindows()

