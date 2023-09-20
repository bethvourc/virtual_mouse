import cv2
from pyzbar.pyzbar import decode

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            print("QR Code Data:", data)

        cv2.imshow('Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
