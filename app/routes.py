
from flask import  jsonify, request,  render_template

from app.gemini.cliente_ia import generar_respuesta




def configure_routes(app):
    
    @app.route('/chat', methods=['GET'])
    def chat():
        return render_template('chat.html')
    
         
    

    # Ruta para procesar las preguntas (POST)
    @app.route('/chat', methods=['POST'])
    def chat_post():
        data = request.get_json()
        
        if 'pregunta' not in data:
            return jsonify({'error': 'Pregunta no proporcionada'}), 400
        
        pregunta = data['pregunta']
        respuesta = generar_respuesta(pregunta)
        
        return jsonify({'respuesta': respuesta})    








    # Ruta para procesar las preguntas (POST)
    @app.route('/chat/pregunta_ia', methods=['POST'])
    def pregunta_ia():
        # Obtener los datos en formato JSON
        data = request.get_json()

        # Verificar si la 'pregunta' está presente en la solicitud
        if not data or 'pregunta' not in data:
            return jsonify({'error': 'Pregunta no proporcionada'}), 400
        
        pregunta = data['pregunta']
        
        # Llamada a la función para generar la respuesta basada en la pregunta
        try:
            respuesta = generar_respuesta(pregunta)
        except Exception as e:
            return jsonify({'error': f'Error al generar respuesta: {str(e)}'}), 500
        
        # Retornar la respuesta generada en formato JSON
        return jsonify({'respuesta': respuesta}), 200





    # Nueva ruta para verificar el estado del servicio (GET)
    @app.route('/chat/status', methods=['GET'])
    def status():
        return jsonify({'status': 'Servicio en línea', 'message': 'Todo está funcionando correctamente.'})