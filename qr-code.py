import qrcode
import webbrowser
import cv2
import time

# Create a QR code reader object
qr_code_reader = cv2.QRCodeDetector()

# Start the camera
camera = cv2.VideoCapture(0)

# Wait for the camera to warm up
time.sleep(2)

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Detect the QR code in the frame
    decoded_text, points, _ = qr_code_reader.detectAndDecode(frame)

    # If a QR code was detected, open the corresponding URL in a web browser
    if points is not None:
        print("Decoded text:", decoded_text)
        webbrowser.open(decoded_text)
        break

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
