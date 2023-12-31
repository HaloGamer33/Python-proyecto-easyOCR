import easyocr
import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

def process_image(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_path)
    print(result)

    img = cv2.imread(image_path)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for detection in result:
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]

        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
        img = cv2.putText(img, text, top_left, font, .5, (255, 255, 255), 2, cv2.LINE_AA)

    plt.imshow(img)
    plt.show()

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            process_image(file_path)
        except Exception as e:
            print("Error al procesar la imagen:", e)

def capture_from_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        cap.release()
        process_image("captured_image.jpg")
    else:
        print("No se pudo capturar la imagen de la cámara.")

def main():
    while True:
        print("1. Procesar una imagen")
        print("2. Usar la cámara")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            select_image()
        elif choice == "2":
            capture_from_camera()
        elif choice == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
