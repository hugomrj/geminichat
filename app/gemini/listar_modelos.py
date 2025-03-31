import google.generativeai as genai
from app.gemini.api_key import API_KEY


genai.configure(api_key=API_KEY) 


for model in genai.list_models():
    print(model.name)



#python -m app.gemini.listar_modelos    