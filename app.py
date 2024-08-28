from flask import Flask
from routes.register import register_blueprint
from routes.login import login_blueprint

app = Flask(__name__)
app.register_blueprint(register_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)