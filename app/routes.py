
from functools import wraps
import os
from flask import  jsonify, request,  render_template
import requests

from app.gemini.bonsaiki_ia import generate
from app.gemini.cliente_ia import generar_respuesta
from app.gemini.contexto import generar_pregunta


from app.gemini.telegran_key import TELEGRAM_TOKEN
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


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
        
        pregunta = data.get('pregunta', '')
        # respuesta = generate(pregunta)

        historial = data.get('historial', []) # Obtener el historial

        pregunta = generar_pregunta(pregunta, historial)

        print(pregunta)

        respuesta = generate(pregunta)
        
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




    @app.route('/chat/webhook', methods=['POST'])
    def handle_telegram():
        try:
            # 1. Obtener datos del mensaje
            data = request.get_json()
            message = data.get('message', {})
            chat_id = message.get('chat', {}).get('id')
            text = message.get('text', '').strip()

            # 2. Ignorar mensajes vacíos (fotos, stickers, etc.)
            if not text:
                return jsonify({'status': 'ignored'}), 200

            # 3. Generar respuesta con tu IA (Gemini)
            respuesta = generar_respuesta(text)

            # historial = data.get('historial', []) # Obtener el historial
            # pregunta = generar_pregunta(pregunta, historial)

 
            pregunta = generar_pregunta(text,  [])
            respuesta = generate(pregunta)


            # 4. Enviar respuesta a Telegram
            requests.post(
                f"{TELEGRAM_API}/sendMessage",
                json={
                    'chat_id': chat_id,
                    'text': respuesta
                }
            )
            return jsonify({'status': 'success'}), 200

        except Exception as e:
            print(f"⚠️ Error: {str(e)}")  # Log simple (reemplázalo con tu sistema de logs)
            return jsonify({'status': 'error'}), 500






    # Nueva ruta para verificar el estado del servicio (GET)
    @app.route('/chat/status', methods=['GET'])
    def status():
        return jsonify({'status': 'Servicio en línea', 'message': 'Todo está funcionando correctamente.'})