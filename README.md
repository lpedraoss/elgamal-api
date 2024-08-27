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
1. **Endpoints Disponibles**:

    - **Registro de Usuario**
      - **Método**: `POST`
      - **Endpoint**: `/register`
      - **Descripción**: Registra una nueva contraseña cifrada en el sistema.
      - **Cuerpo de la Solicitud**: JSON con el siguiente formato:
        ```json
        {
          "password": "tu_contraseña_aqui"
        }
        ```

    - **Inicio de Sesión**
      - **Método**: `POST`
      - **Endpoint**: `/login`
      - **Descripción**: Autentica un usuario comparando la contraseña ingresada con la almacenada.
      - **Cuerpo de la Solicitud**: JSON con el siguiente formato:
        ```json
        {
          "password": "tu_contraseña_aqui"
        }
        ```


## Notas Adicionales

- Asegúrate de que el archivo `requirements.txt` esté actualizado con las últimas dependencias usando `pip freeze > requirements.txt`.
- Consulta la [documentación de Flask](https://flask.palletsprojects.com/) para más detalles sobre el framework.

## Contribuciones

Si deseas contribuir a este proyecto, por favor envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
