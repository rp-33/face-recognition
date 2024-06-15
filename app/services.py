import face_recognition
import cv2
import os

class FacialRecognitionService:
    def cargar_imagenes(self, ruta_imagen1, ruta_imagen2):
        imagen1 = face_recognition.load_image_file(ruta_imagen1)
        imagen2 = face_recognition.load_image_file(ruta_imagen2)
        return imagen1, imagen2

    def obtener_codificacion_facial(self, imagen):
        codificacion_facial = face_recognition.face_encodings(imagen)
        if codificacion_facial:
            return codificacion_facial[0]
        else:
            return None

    def comparar_codificaciones(self, codificacion1, codificacion2):
        resultado = face_recognition.compare_faces([codificacion1], codificacion2)
        return resultado[0]

    def extraer_fotograma(self, video_filepath):
        cap = cv2.VideoCapture(video_filepath)
        ret, frame = cap.read()
        cap.release()

        # Obtener el nombre del archivo sin la extensión
        filename_no_extension = os.path.splitext(os.path.basename(video_filepath))[0]

        # Crear la ruta del archivo del fotograma con una extensión válida (por ejemplo, .jpg)
        frame_filepath = os.path.join(os.path.dirname(video_filepath), filename_no_extension + '_frame.jpg')

        cv2.imwrite(frame_filepath, frame)

        return frame_filepath

    