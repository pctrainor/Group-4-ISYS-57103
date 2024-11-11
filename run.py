from flask import Flask
from flask_cors import CORS
from flasgger import Swagger # Only required if you want to use Swagger UI
import yaml
from API.routes import api_bp
from pathlib import Path

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)

    # If you have provided an openapi.yaml file in the docs folder, load it
    if Path.exists(Path("drone-api.yaml")):
        with open("drone-api.yaml", "r") as file:
            openapi_spec = yaml.safe_load(file)

        swagger = Swagger(app, template=openapi_spec)

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)