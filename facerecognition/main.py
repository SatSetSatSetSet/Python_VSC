import cv2

# Load Haar Cascade untuk deteksi wajah
face_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Inisialisasi kamera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

def face_detection(frame):
    # Konversi frame ke grayscale
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Deteksi wajah
    faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def close_window():
    # Lepaskan kamera dan tutup jendela
    camera.release()
    cv2.destroyAllWindows()

def drawer_box(frame):
    # Gambar kotak di sekitar wajah yang terdeteksi
    for x, y, w, h in face_detection(frame):  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

def main():
    while True:
        # Baca frame dari kamera
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame from camera.")
            break
        
        # Gambar kotak dan tampilkan frame
        drawer_box(frame)
        cv2.imshow("Face Detection", frame)
                  
        # Berhenti jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Tutup kamera dan jendela
    close_window()

if __name__ == "__main__":
    main()