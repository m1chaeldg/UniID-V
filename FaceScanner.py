import cv2


class FaceScanner:
    def Scan(self):
        print("Scan Face")
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
                #print(check) #prints true as long as the webcam is running
                #print(frame) #prints matrix values of each framecd 
                cv2.imshow("Capturing", frame)
                cv2.moveWindow("Capturing", 200, 25)
                key = cv2.waitKey(1)
                if key == ord('s'): 
                    cv2.imwrite(filename='FaceScanned.jpg', img=frame)
                    webcam.release()
                    img_new = cv2.imread('FaceScanned.jpg', cv2.IMREAD_GRAYSCALE)
                    #img_new = cv2.imshow("Captured Image", img_new)
                    cv2.waitKey(1650)
                    cv2.destroyAllWindows()
                    print("Processing image...")
                    img_ = cv2.imread('FaceScanned.jpg', cv2.IMREAD_ANYCOLOR)
                    #print("Converting RGB image to grayscale...")
                    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    #print("Converted RGB image to grayscale...")
                    #print("Resizing image to 28x28 scale...")
                    img_ = cv2.resize(gray,(28,28))
                    #print("Resized...")
                    #img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                    #print("Scan Your ID")
                    print("Face Image saved!")
                
                    break
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break
                
            except KeyboardInterrupt:
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
    
