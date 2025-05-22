#!/usr/bin/env python3
import requests
from app.gemini.telegran_key import TELEGRAM_TOKEN  # Importas tu token como lo tienes actualmente

# Configuración
WEBHOOK_URL = "https://tudominio.com/webhook"  # Reemplaza con tu dominio real
DROP_PENDING_UPDATES = True  # Borra mensajes pendientes no procesados

def set_webhook():
    try:
        print("🔄 Configurando webhook...")
        
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook",
            json={
                'url': WEBHOOK_URL,
                'drop_pending_updates': DROP_PENDING_UPDATES
            },
            timeout=10
        )
        
        result = response.json()
        if result.get('ok'):
            print("✅ Webhook configurado correctamente")
            print(f"🔗 URL: {WEBHOOK_URL}")
            print(f"ℹ️ Info: {result}")
        else:
            print("❌ Error al configurar webhook:")
            print(result)
            
    except Exception as e:
        print(f"🔥 Error inesperado: {str(e)}")

def check_webhook():
    try:
        print("\n🔍 Verificando configuración actual...")
        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getWebhookInfo",
            timeout=5
        )
        print(response.json())
    except Exception as e:
        print(f"⚠️ Error al verificar webhook: {str(e)}")

if __name__ == "__main__":
    set_webhook()
    check_webhook()