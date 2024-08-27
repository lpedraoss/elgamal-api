# ElGamal API

Este proyecto proporciona una API para cifrado y autenticación usando el algoritmo ElGamal.

## Requisitos

Asegúrate de tener [Python](https://www.python.org/downloads/) instalado en tu sistema. Se recomienda usar un entorno virtual para gestionar las dependencias.

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/lpedraoss/elgamal-api.git
    cd elgamal-api
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de la API

1. **Ejecuta la aplicación**:

    ```bash
    python run.py
    ```

    Esto iniciará el servidor Flask en `http://127.0.0.1:5000/`.

2. **Prueba las rutas**:

    - **Registro**: Envía una solicitud POST a `/register` con un JSON que contenga una contraseña para registrarla.
    - **Inicio de sesión**: Envía una solicitud POST a `/login` con las credenciales necesarias para autenticarte.

## Notas Adicionales

- Asegúrate de que el archivo `requirements.txt` esté actualizado con las últimas dependencias usando `pip freeze > requirements.txt`.
- Consulta la [documentación de Flask](https://flask.palletsprojects.com/) para más detalles sobre el framework.

## Contribuciones

Si deseas contribuir a este proyecto, por favor envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
