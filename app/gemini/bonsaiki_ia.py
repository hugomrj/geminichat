import sys
import google.generativeai as genai
from google.genai import types
from app.gemini.api_key import API_KEY




print(API_KEY)  # Esto imprimirá la clave


genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-lite')




def generate(pregunta: str) -> str:
    """
    Genera una respuesta usando la API de Google AI para consultas sobre Bonsái Ki.

    :param pregunta: La pregunta del usuario sobre bonsáis o plantas medicinales.
    :return: La respuesta generada por la IA.
    """
    try:
        # Configuración de generación
        generation_config = genai.GenerationConfig(
            temperature=0.7,
            top_p=1,
            top_k=32,
            max_output_tokens=250,
        )
        
        # Generar la respuesta con system_instruction
        respuesta = model.generate_content(
            pregunta,
            generation_config=generation_config
        )
        return respuesta.text
    except Exception as e:
        return f"Error al generar la respuesta: {str(e)}"



# Ejemplo de uso
# pregunta_usuario = "¿Cómo se poda un bonsái de la especie Arce Palmatum?"
# respuesta_generada = generate(pregunta_usuario)
#  print(respuesta_generada)