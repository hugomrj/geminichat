import logging
from run import create_app

# Crear la aplicación
app = create_app()

# Configurar logging si está en producción
if not app.debug:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    app.logger.info("Aplicación en producción.")

if __name__ == "__main__":
    app.run()
