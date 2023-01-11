import cv2


# Create our body classifier
body_classifier=cv2.CascadeClassifier('harrcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 

    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
 
    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,0,255),2)
 
        #Display the resulting frame
        #imshow displays the image or video
    cv2.imshow('frame',frame)


    if cv2.waitKey(1) == 32: 
        break

cap.release()
cv2.destroyAllWindows()
