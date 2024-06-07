import cv2

# Open the webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Get the default resolution
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Default resolution: {width} x {height}")

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
    
#     # Draw the coordinate system on the frame
#     cv2.line(frame, (0, 0), (width, 0), (0, 255, 0), 2)  # Top line
#     cv2.line(frame, (0, 0), (0, height), (0, 255, 0), 2)  # Left line
#     cv2.line(frame, (0, height-1), (width, height-1), (0, 255, 0), 2)  # Bottom line
#     cv2.line(frame, (width-1, 0), (width-1, height), (0, 255, 0), 2)  # Right line
    
#     # Display coordinates on the frame
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, '(0, 0)', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#     cv2.putText(frame, f'({width-1}, 0)', (width-250, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#     cv2.putText(frame, f'({0}, {height-1})', (10, height-10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#     cv2.putText(frame, f'({width-1}, {height-1})', (width-300, height-10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
#     # Display the resulting frame
#     cv2.imshow('Webcam', frame)

#     # Get the default frame rate
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     print(f"Default resolution: {int(width)} x {int(height)}")
#     print(f"Default frame rate: {fps} FPS")

#     if cv2.waitKey(1) == ord('q'):
#         break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
