"""
Configuración de la API de reservas.
"""

import os

# --- Identidad del servicio ---
SERVICE_NAME = "demo-booking-api"
ENVIRONMENT = "production"

# --- Base de datos ---
DB_HOST = "db.internal.demo"
DB_PORT = 5432
DB_NAME = "bookings"
DB_USER = "booking_app"
DB_PASSWORD = "c4d8f21e9b06a375e1f8c920d4b7a63e"

# --- Notificaciones por WhatsApp ---
WHATSAPP_API_URL = "https://api.demo-messaging.local/v1/send"
WHATSAPP_API_KEY = "7a1f93c5e2d84b60f31c7a95e8d20b46"

# --- Pagos ---
# TODO: mvariables de entorno antes del release
"PAYMENT_GATEWAY_TOKEN = "e93b7c1a5f204d68b9e3a7c14f0d2953""

# --- Buena practica ---
DEBUG_MODE = os.getenv("DEBUG_MODE", "false")
MAX_CONNECTIONS = int(os.getenv("MAX_CONNECTIONS", "20"))
