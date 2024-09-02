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

4. **Configura la base de datos**:

    - Crea la carpeta `data` si no existe:

      ```bash
      mkdir data
      ```

    - Usa el plugin de MySQL con soporte para SQLite para crear la base de datos y la tabla `users` en `data/users.db`. Aquí está el SQL que necesitas ejecutar:

      ```sql
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL,
          p TEXT NOT NULL,
          a TEXT NOT NULL,
          c1 TEXT NOT NULL
      );
      ```

## Ejecución de la API

1. **Inicia la aplicación**:

    ```bash
    flask run
    ```

2. **Endpoints Disponibles**:

    - **Registro de Usuario**
      - **Método**: `POST`
      - **Endpoint**: `/api/register`
      - **Descripción**: Registra un nuevo usuario en el sistema.
      - **Cuerpo de la Solicitud**: JSON con el siguiente formato:
        ```json
        {
          "username": "tu_usuario_aqui",
          "password": "tu_contraseña_aqui"
        }
        ```

    - **Inicio de Sesión**
      - **Método**: `POST`
      - **Endpoint**: `/api/login`
      - **Descripción**: Autentica un usuario comparando la contraseña ingresada con la almacenada.
      - **Cuerpo de la Solicitud**: JSON con el siguiente formato:
        ```json
        {
          "username": "tu_usuario_aqui",
          "password": "tu_contraseña_aqui"
        }
        ```

## Notas Adicionales

- Asegúrate de que el archivo [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fluill%2FDocuments%2FmiGit%2Felgamal-api%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\luill\Documents\miGit\elgamal-api\requirements.txt") esté actualizado con las últimas dependencias usando [`pip freeze > requirements.txt`](command:_github.copilot.openSymbolFromReferences?%5B%22pip%20freeze%20%3E%20requirements.txt%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cluill%5C%5CDocuments%5C%5CmiGit%5C%5Celgamal-api%5C%5CREADME.md%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fluill%2FDocuments%2FmiGit%2Felgamal-api%2FREADME.md%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fluill%2FDocuments%2FmiGit%2Felgamal-api%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A66%2C%22character%22%3A426%7D%7D%5D%5D "Go to definition").
- Consulta la [documentación de Flask](https://flask.palletsprojects.com/) para más detalles sobre el framework.

## Contribuciones

Si deseas contribuir a este proyecto, por favor envía un pull request con tus cambios.
