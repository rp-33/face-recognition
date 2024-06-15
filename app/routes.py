import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app import app
from app.services import FacialRecognitionService

UPLOAD_FOLDER = 'uploads'  # Carpeta donde se guardarán las imágenes
ALLOWED_EXTENSIONS_IMAGE = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS_VIDEO = {'mp4', 'avi', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/face_recognition_image', methods=['POST'])
def face_recognition_image():
    if 'profile_url' not in request.files or 'image_url' not in request.files:
        return jsonify({"error": "Se requieren dos imágenes para comparar"}), 400

    file1 = request.files['profile_url']
    file2 = request.files['image_url']

    if file1 and allowed_file(file1.filename,ALLOWED_EXTENSIONS_IMAGE) and file2 and allowed_file(file2.filename,ALLOWED_EXTENSIONS_IMAGE):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

        filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)

        file1.save(filepath1)
        file2.save(filepath2)

        # Instanciar la clase
        facial_recognition_service = FacialRecognitionService()

        # Cargar imágenes
        imagen1, imagen2 = facial_recognition_service.cargar_imagenes(filepath1,filepath2)

        # Obtener codificaciones faciales
        codificacion1 = facial_recognition_service.obtener_codificacion_facial(imagen1)
        codificacion2 = facial_recognition_service.obtener_codificacion_facial(imagen2)

        if codificacion1 is not None and codificacion2 is not None:
            resultado_comparacion = facial_recognition_service.comparar_codificaciones(codificacion1, codificacion2)
            if resultado_comparacion:
                return jsonify({"message":"Mismo usuario"}), 201
            else:
               return jsonify({"message":"Usuario Diferente"}), 400       
        else:
            return jsonify({"error": "No se pudo obtener la codificación facial de al menos una de las imágenes"}), 500
    else:
        return jsonify({"error": "Formato de archivo no permitido"}), 400

@app.route('/face_recognition_video', methods=['POST'])
def comparar_imagen_video():
    if 'video' not in request.files or 'image' not in request.files:
        return jsonify({"error": "Se requiere un video y una imagen para comparar"}), 400

    video_file = request.files['video']
    image_file = request.files['image']

    if video_file and allowed_file(video_file.filename, ALLOWED_EXTENSIONS_VIDEO) and \
       image_file and allowed_file(image_file.filename, ALLOWED_EXTENSIONS_IMAGE):

        video_filename = secure_filename(video_file.filename)
        image_filename = secure_filename(image_file.filename)

        video_filepath = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
        image_filepath = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

        video_file.save(video_filepath)
        image_file.save(image_filepath)

        # Extraer fotograma del video
        facial_recognition_service = FacialRecognitionService()
        frame_filepath = facial_recognition_service.extraer_fotograma(video_filepath)

        # Cargar imágenes
        imagen_video, imagen_subida = facial_recognition_service.cargar_imagenes(frame_filepath, image_filepath)

        # Obtener codificaciones faciales
        codificacion_video = facial_recognition_service.obtener_codificacion_facial(imagen_video)
        codificacion_subida = facial_recognition_service.obtener_codificacion_facial(imagen_subida)

        if codificacion_video is not None and codificacion_subida is not None:
            resultado_comparacion = facial_recognition_service.comparar_codificaciones(codificacion_video, codificacion_subida)
            if resultado_comparacion:
                return jsonify({"message": "Mismo usuario"}), 201
            else:
                return jsonify({"message": "Usuario Diferente"}), 400       
        else:
            return jsonify({"error": "No se pudo obtener la codificación facial de al menos una de las imágenes"}), 500
    else:
        return jsonify({"error": "Formato de archivo no permitido"}), 400
