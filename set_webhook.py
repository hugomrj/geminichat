#!/usr/bin/env python3
import requests
from app.gemini.telegran_key import TELEGRAM_TOKEN  # Importas tu token como lo tienes actualmente




# Configuración con tu dominio real
WEBHOOK_URL = "https://bonsaiki.duckdns.org/chat/webhook"
DROP_PENDING_UPDATES = True

def set_webhook():
    try:
        print("🔄 Configurando webhook sin token secreto...")
        
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
        else:
            print("❌ Error al configurar webhook:")
            print(result)
            
    except Exception as e:
        print(f"🔥 Error inesperado: {str(e)}")

def check_webhook():
    try:
        print("\n🔍 Verificando webhook...")
        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getWebhookInfo",
            timeout=5
        )
        info = response.json()
        
        print(f"URL actual: {info.get('result', {}).get('url')}")
        print(f"Estado: {'Activo ✅' if info.get('result', {}).get('url') else 'Inactivo ❌'}")
        
    except Exception as e:
        print(f"⚠️ Error al verificar: {str(e)}")

if __name__ == "__main__":
    set_webhook()
    check_webhook()