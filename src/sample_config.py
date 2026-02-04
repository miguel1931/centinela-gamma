# 🔧 CONFIGURACIÓN DE EJEMPLO - CENTINELA-GAMMA
# 📋 Copia este archivo como src/config.py y personaliza según tus necesidades

"""
CONFIGURACIÓN PRINCIPAL DE CENTINELA-GAMMA
Personaliza estos valores según tu caso de uso específico
"""

# ===================================================================
# CREDENCIALES DE TWITTER API v2 (REQUERIDO)
# ===================================================================
# Obtener desde: https://developer.twitter.com/
TWITTER_API_KEY = "tu_api_key_aqui"
TWITTER_API_SECRET = "tu_api_secret_aqui"  
TWITTER_BEARER_TOKEN = "tu_bearer_token_aqui"

# Opcional: Para funcionalidades avanzadas
TWITTER_ACCESS_TOKEN = "tu_access_token_aqui"
TWITTER_ACCESS_TOKEN_SECRET = "tu_access_token_secret_aqui"

# ===================================================================
# CONFIGURACIÓN REGIONAL
# ===================================================================
# Palabras clave principales para búsqueda
MAIN_KEYWORDS = [
    "Palestine", "Gaza", "West Bank", "East Jerusalem",
    "Israel", "IDF", "war crimes", "civilian casualties"
]

# Regiones geográficas a monitorear
TARGET_REGIONS = {
    "Gaza": {
        "keywords": ["Gaza", "غزة", "Gazans"],
        "coordinates": "31.5,34.4,31.6,34.5",  # lat,lon,lat,lon
        "priority": "HIGH"
    },
    "West Bank": {
        "keywords": ["West Bank", "Ramallah", "Jenin", "Nablus"],
        "coordinates": "32.0,35.0,32.5,35.3",
        "priority": "HIGH"  
    },
    "East Jerusalem": {
        "keywords": ["East Jerusalem", "Al-Aqsa", "Sheikh Jarrah"],
        "coordinates": "31.7,35.2,31.8,35.3", 
        "priority": "MEDIUM"
    }
}

# Idiomas a incluir en búsquedas
SEARCH_LANGUAGES = ["en", "ar", "es", "fr"]  # inglés, árabe, español, francés

# ===================================================================
# LÍMITES DE PROCESAMIENTO
# ===================================================================
# Límites por ejecución
MAX_TWEETS_PER_EXECUTION = 50000
MAX_TWEETS_PER_QUERY = 1500
PROCESSING_BUDGET_USD = 2.00

# Límites de tiempo
EXECUTION_TIMEOUT_MINUTES = 30
API_RATE_LIMIT_DELAY = 1  # segundos entre requests

# ===================================================================
# CONFIGURACIÓN DE ANÁLISIS
# ===================================================================
# Umbrales de relevancia
RELEVANCE_THRESHOLDS = {
    "critical": 85,    # Considerar crítico si relevancia > 85%
    "high": 70,        # Alta relevancia si > 70%
    "medium": 50,      # Media relevancia si > 50%
    "low": 30          # Baja relevancia si < 30%
}

# Palabras clave críticas (incrementan relevancia)
CRITICAL_KEYWORDS = [
    "killed", "dead", "murdered", "executed", "assassinated",
    "bombing", "airstrike", "shelling", "explosion", 
    "hospital bombed", "school destroyed", "mosque attacked",
    "children killed", "civilians killed", "family killed",
    "war crime", "genocide", "ethnic cleansing", "crimes against humanity"
]

# Indicadores de bot (para análisis de autenticidad)
BOT_INDICATORS = {
    "high_volume_threshold": 30,        # >30 tweets del mismo autor
    "content_similarity_threshold": 0.7, # <70% contenido único
    "timing_cluster_window": 300,       # 5 minutos para detección de clusters
    "low_engagement_threshold": 1       # <1 engagement promedio
}

# ===================================================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================================================
# Archivo de base de datos local
DATABASE_PATH = "data/centinela_gamma.db"

# Configuración avanzada (opcional)
# Para usar PostgreSQL en lugar de SQLite:
# DATABASE_CONFIG = {
#     "type": "postgresql",
#     "host": "localhost", 
#     "port": 5432,
#     "database": "centinela_gamma",
#     "username": "your_username",
#     "password": "your_password"
# }

# ===================================================================
# CONFIGURACIÓN DE EXPORTACIÓN
# ===================================================================
# Formato por defecto para exportaciones
DEFAULT_EXPORT_FORMAT = "json"  # json, csv, xlsx, pdf

# Rutas de exportación
EXPORT_PATHS = {
    "json": "exports/json/",
    "csv": "exports/csv/",
    "xlsx": "exports/excel/",
    "pdf": "exports/reports/"
}

# Configuración de anonimización
ANONYMIZATION = {
    "enabled": True,                    # Anonimizar datos sensibles
    "preserve_metrics": True,           # Preservar métricas estadísticas
    "hash_user_ids": True,              # Hash IDs de usuarios
    "remove_personal_info": True        # Eliminar info personal
}

# ===================================================================
# CONFIGURACIÓN DE SERVIDOR/API
# ===================================================================
# Puerto para el servidor web
API_PORT = 8081
API_HOST = "localhost"

# CORS (para acceso desde otros dominios)
CORS_ENABLED = True
CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

# Configuración de caché
CACHE_ENABLED = True
CACHE_DURATION_MINUTES = 60

# ===================================================================
# SISTEMA DE ALERTAS
# ===================================================================
ALERTS = {
    "enabled": False,  # Cambiar a True para activar alertas
    
    # Umbrales para alertas automáticas
    "thresholds": {
        "critical_incidents": 50,       # Alertar si >50 incidentes críticos
        "civilian_casualties": 100,     # Alertar si >100 víctimas civiles  
        "bot_activity_percentage": 80,  # Alertar si >80% actividad de bots
        "infrastructure_attacks": 10    # Alertar si >10 ataques a infraestructura
    },
    
    # Configuración de email (opcional)
    "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "username": "your_email@gmail.com",
        "password": "your_app_password",  # Usar contraseña de aplicación
        "recipients": [
            "alert1@organization.org",
            "alert2@ngo.org"
        ]
    },
    
    # Configuración de Discord (opcional)
    "discord": {
        "webhook_url": "https://discord.com/api/webhooks/YOUR_WEBHOOK",
        "mention_roles": ["@alertas", "@moderadores"]
    }
}

# ===================================================================
# CONFIGURACIÓN DE LOGGING
# ===================================================================
LOGGING = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "file_path": "logs/centinela_gamma.log",
    "max_file_size": "10MB",
    "backup_count": 5,
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
}

# ===================================================================
# CONFIGURACIÓN AVANZADA
# ===================================================================
# Configuración de proxy (si es necesario)
# PROXY_CONFIG = {
#     "http": "http://proxy.server:port",
#     "https": "https://proxy.server:port"
# }

# Configuración de User-Agent
USER_AGENT = "CENTINELA-GAMMA/1.0 (+https://github.com/your-repo/centinela-gamma)"

# Configuración experimental
EXPERIMENTAL_FEATURES = {
    "ml_classification": False,         # Clasificación con Machine Learning
    "sentiment_analysis": False,        # Análisis de sentimientos
    "image_analysis": False,           # Análisis de imágenes (requiere APIs adicionales)
    "real_time_streaming": False       # Streaming en tiempo real
}

# ===================================================================
# VALIDACIÓN DE CONFIGURACIÓN
# ===================================================================
def validate_config():
    """
    Valida que la configuración esté completa
    Ejecutar: python -c "from config import validate_config; validate_config()"
    """
    errors = []
    
    # Verificar credenciales de Twitter
    if not TWITTER_BEARER_TOKEN or TWITTER_BEARER_TOKEN == "tu_bearer_token_aqui":
        errors.append("❌ TWITTER_BEARER_TOKEN no configurado")
    
    # Verificar rutas de exportación
    import os
    for path in EXPORT_PATHS.values():
        if not os.path.exists(path):
            try:
                os.makedirs(path, exist_ok=True)
                print(f"✅ Creado directorio: {path}")
            except Exception as e:
                errors.append(f"❌ No se pudo crear directorio {path}: {e}")
    
    # Verificar configuración de base de datos
    db_dir = os.path.dirname(DATABASE_PATH)
    if not os.path.exists(db_dir):
        try:
            os.makedirs(db_dir, exist_ok=True)
            print(f"✅ Creado directorio de base de datos: {db_dir}")
        except Exception as e:
            errors.append(f"❌ No se pudo crear directorio de DB {db_dir}: {e}")
    
    # Mostrar resultados
    if errors:
        print("\n⚠️ ERRORES DE CONFIGURACIÓN:")
        for error in errors:
            print(f"   {error}")
        print("\n🔧 Por favor, corrige estos errores antes de ejecutar el sistema.")
        return False
    else:
        print("\n✅ CONFIGURACIÓN VÁLIDA")
        print("🚀 El sistema está listo para ejecutarse.")
        return True

if __name__ == "__main__":
    validate_config()