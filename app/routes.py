
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