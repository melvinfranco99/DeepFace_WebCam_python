from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["cv2"],  # Agrega aquí las librerías que necesites
    "include_files": ["C:/Users/Melvin/Documents/Melvin/DeepFace_WebCam/DeepFace_WebCam_python/haarcascade_frontalface_default.xml"],  # Archivos adicionales si es necesario
}

# Cambia "mi_script.py" por el nombre de tu script
executables = [Executable("pruebaGrafica.py", base="Win32GUI")]

setup(
    name="Prueba Grafica reconocimiento WebCam",
    version="0.1",
    description="Descripción de mi aplicación",
    executables=executables,
    options={"build_exe": build_exe_options}
)
