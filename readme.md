
### Descripción de Carpetas y Archivos

- **app/**: Contiene todo el código de la aplicación.
  - **application/**: Lógica de la aplicación.
    - `reconocimiento_facial_service.py`: Servicio que coordina el reconocimiento facial.
  - **domain/**: Define las entidades y la lógica de negocio.
    - `reconocimiento_facial.py`: Clase base para el reconocimiento facial.
  - **adapters/**: Adaptadores que conectan el núcleo con el mundo exterior.
    - `flask_adapter.py`: Adaptador para la interfaz web con Flask.
    - `file_adapter.py`: Adaptador para el manejo de archivos.
  - **interfaces/**: Define las interfaces para la comunicación entre capas.
    - `reconocimiento_facial_interface.py`: Interfaz para el reconocimiento facial.
- **uploads/**: Carpeta para almacenar temporalmente los archivos subidos.
- **.gitignore**: Archivos y carpetas a ignorar por Git.
- **app.py**: Archivo principal para ejecutar la aplicación Flask.

## Requisitos

- Python 3.x
- Flask
- OpenCV
- face_recognition

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/rp-33/face-recognition.git
    cd reconocimiento_facial_hexagonal
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    **Nota:** Asegúrate de tener `opencv-python` y `face_recognition` instalados:
    ```bash
    pip install opencv-python face_recognition
    ```

3. Crea las carpetas necesarias:
    ```bash
    mkdir uploads
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

2. Abre tu navegador y navega a `http://127.0.0.1:5000/`.

3. Sube una imagen para verificar el reconocimiento facial.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees hacer.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
