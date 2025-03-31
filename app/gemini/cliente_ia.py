import sys
import google.generativeai as genai
from app.gemini.api_key import API_KEY


# Configura la API de Google AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def generar_respuesta(pregunta: str) -> str:
    """
    Genera una respuesta usando la API de Google AI.

    :param pregunta: La pregunta del usuario.
    :return: La respuesta generada por la IA.
    """
    try:
        # Configuración de generación
        generation_config = genai.GenerationConfig(
            temperature=0.7,
            top_p=1,
            top_k=32,
            max_output_tokens=256,
        )
        
        # Generar la respuesta
        respuesta = model.generate_content(pregunta, generation_config=generation_config)
        return respuesta.text
    except Exception as e:
        return f"Error al generar la respuesta: {str(e)}"







if __name__ == "__main__":
    # Verifica si se proporcionó un argumento de línea de comandos
    if len(sys.argv) > 1:
        pregunta = ' '.join(sys.argv[1:])  # Une todos los argumentos en un solo string
        respuesta = generar_respuesta(pregunta)
        print(respuesta)
    else:
        print("Por favor, ingresa una pregunta como argumento.")    