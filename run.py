from flask import Flask
from app.routes import configure_routes

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)


    # Configurar las rutas
    configure_routes(app)


    return app

if __name__ == '__main__':
    # Crear la aplicación Flask
    app = create_app()

    # Ejecutar la aplicación en modo de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)



