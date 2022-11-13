import cv2


# define a video capture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(1280))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(720))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while(True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    #encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 0]
    #result, encimg = cv2.imencode('.jpg', frame, encode_param)
    #print(str(result))
    # Display the resulting frame
    #decimg = cv2.imdecode(encimg, 1)
    #cv2.imshow('frame', decimg)
    winname = "Test"
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, 40,30)
    cv2.imshow(winname, frame)


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()