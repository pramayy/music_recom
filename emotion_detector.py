from deepface import DeepFace
import cv2

def capture_image(filename='captured.jpg'):
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture image...")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(filename, frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return filename

def detect_emotion_from_image(image_path='captured.jpg'):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'])
        emotion = result[0]['dominant_emotion']
        return emotion
    except Exception as e:
        print(f"Error: {e}")
        return None
