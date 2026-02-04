# 🛠️ GUÍA DE INSTALACIÓN - CENTINELA-GAMMA
## 📋 **Instrucciones Paso a Paso para Configurar el Sistema**

---

## 🔧 **PRERREQUISITOS**

### **1. Python 3.7 o Superior**
```bash
# Verificar versión de Python
python --version

# Si no tienes Python, descargar desde:
# https://www.python.org/downloads/
```

### **2. Cuenta de Twitter/X con API v2**
- Crear cuenta de desarrollador en: https://developer.twitter.com/
- Solicitar acceso a API v2 (Essential - Gratuito)
- Obtener las siguientes claves:
  - `API_KEY`
  - `API_SECRET` 
  - `BEARER_TOKEN`

### **3. Dependencias del Sistema**
```bash
# Windows
# Asegurar que pip esté actualizado
python -m pip install --upgrade pip

# Linux/macOS
sudo apt update  # Ubuntu/Debian
pip3 install --upgrade pip
```

---

## 📥 **INSTALACIÓN**

### **Paso 1: Descargar el Proyecto**
```bash
# Opción A: Descarga directa
# Descargar y extraer CENTINELA_GAMMA_SHARE.zip

# Opción B: Git (si disponible)
git clone https://github.com/your-repo/centinela-gamma.git
cd centinela-gamma
```

### **Paso 2: Crear Entorno Virtual (Recomendado)**
```bash
# Navegar al directorio del proyecto
cd CENTINELA_GAMMA_SHARE

# Crear entorno virtual
python -m venv centinela_env

# Activar entorno virtual
# Windows:
centinela_env\Scripts\activate
# Linux/macOS:
source centinela_env/bin/activate
```

### **Paso 3: Instalar Dependencias**
```bash
# Instalar todas las dependencias requeridas
pip install -r requirements.txt

# Verificar instalación
pip list
```

---

## ⚙️ **CONFIGURACIÓN**

### **Paso 1: Crear Archivo de Configuración**
```bash
# Copiar el archivo de ejemplo
cp examples/sample_config.py src/config.py

# Windows:
copy examples\sample_config.py src\config.py
```

### **Paso 2: Editar Configuración**
Abrir `src/config.py` y completar:

```python
# API de Twitter/X
TWITTER_API_KEY = "tu_api_key_aqui"
TWITTER_API_SECRET = "tu_api_secret_aqui"
TWITTER_BEARER_TOKEN = "tu_bearer_token_aqui"

# Configuración regional (opcional)
TARGET_REGIONS = ["Gaza", "West Bank", "East Jerusalem", "Palestine", "Israel"]

# Límites de procesamiento
MAX_TWEETS_PER_EXECUTION = 50000
PROCESSING_BUDGET_USD = 2.00

# Configuración de base de datos (opcional)
DATABASE_PATH = "data/centinela_gamma.db"
EXPORT_FORMAT = "json"  # json, csv, xlsx
```

### **Paso 3: Crear Estructura de Datos**
```bash
# Crear carpetas necesarias
mkdir data
mkdir exports
mkdir logs

# Windows:
mkdir data & mkdir exports & mkdir logs
```

---

## 🚀 **PRIMERA EJECUCIÓN**

### **Paso 1: Probar Conexión a Twitter**
```bash
python src/test_twitter_connection.py
```

### **Paso 2: Ejecutar Recopilación de Datos**
```bash
# Ejecución completa (50K tweets)
python src/centinela_gamma_maximized.py

# Ejecución de prueba (500 tweets)
python src/centinela_gamma_maximized.py --test-mode
```

### **Paso 3: Procesar Datos (Optimización)**
```bash
# Convertir datos crudos en métricas optimizadas
python src/palestine_tweets_processor.py
```

### **Paso 4: Iniciar Dashboard**
```bash
# Iniciar API y servidor web
python src/palestine_war_crimes_api.py
```

### **Paso 5: Acceder al Dashboard**
Abrir navegador en: `http://localhost:8081/palestine_war_crimes_dashboard_optimized.html`

---

## 🔍 **VERIFICACIÓN DE INSTALACIÓN**

### **Checklist de Verificación**
- [ ] Python 3.7+ instalado y funcionando
- [ ] Todas las dependencias instaladas sin errores
- [ ] Archivo de configuración creado y completado
- [ ] Conexión a Twitter API exitosa
- [ ] Primera recopilación de datos completada
- [ ] Procesamiento de datos funcionando
- [ ] Dashboard accesible en navegador
- [ ] API respondiendo correctamente

### **Comandos de Verificación**
```bash
# Verificar versión de Python
python --version

# Verificar dependencias críticas
python -c "import tweepy, json, datetime; print('Dependencias OK')"

# Verificar estructura de archivos
ls src/
ls dashboard/
ls docs/

# Probar API
curl http://localhost:8081/api/palestine/overview
```

---

## ⚠️ **SOLUCIÓN DE PROBLEMAS COMUNES**

### **Error: "ModuleNotFoundError: No module named 'tweepy'"**
```bash
# Solución: Instalar tweepy
pip install tweepy>=4.14.0
```

### **Error: "Twitter API Authentication Failed"**
```bash
# Verificar credenciales en src/config.py
# Asegurar que Bearer Token esté correcto
# Verificar límites de API en Twitter Developer Portal
```

### **Error: "Permission Denied" al crear archivos**
```bash
# Linux/macOS: Dar permisos
chmod +x src/*.py
sudo chown $USER:$USER data/

# Windows: Ejecutar como administrador
```

### **Error: "Port 8081 already in use"**
```bash
# Opción 1: Cambiar puerto en src/config.py
API_PORT = 8082

# Opción 2: Cerrar proceso existente
# Windows:
netstat -ano | findstr :8081
taskkill /PID [PID_NUMBER] /F

# Linux/macOS:
lsof -i :8081
kill [PID_NUMBER]
```

### **Dashboard no carga correctamente**
```bash
# Verificar que la API esté ejecutándose
curl http://localhost:8081/api/palestine/overview

# Verificar permisos de archivos
chmod 644 dashboard/*.html

# Limpiar caché del navegador
Ctrl+Shift+R (refresh forzado)
```

---

## 🔄 **ACTUALIZACIONES**

### **Actualizar el Sistema**
```bash
# Respaldar configuración
cp src/config.py config_backup.py

# Descargar nueva versión
# Sobrescribir archivos del sistema

# Restaurar configuración
cp config_backup.py src/config.py

# Actualizar dependencias
pip install -r requirements.txt --upgrade
```

### **Migración de Datos**
```bash
# Respaldar datos existentes
cp -r data/ data_backup_$(date +%Y%m%d)/

# Ejecutar script de migración (si existe)
python src/migrate_data.py
```

---

## 📊 **CONFIGURACIONES AVANZADAS**

### **Configuración Multi-Región**
```python
# En src/config.py
REGIONS = {
    "Palestine": {
        "keywords": ["Gaza", "West Bank", "Palestine"],
        "languages": ["en", "ar", "es"],
        "max_tweets": 30000
    },
    "Ukraine": {
        "keywords": ["Ukraine", "Kyiv", "Donbas"],
        "languages": ["en", "uk", "ru"],
        "max_tweets": 20000
    }
}
```

### **Configuración de Base de Datos**
```python
# Para usar PostgreSQL en lugar de SQLite
DATABASE_CONFIG = {
    "type": "postgresql",
    "host": "localhost",
    "port": 5432,
    "database": "centinela_gamma",
    "username": "your_username",
    "password": "your_password"
}
```

### **Configuración de Alertas**
```python
# Notificaciones por email
ALERT_CONFIG = {
    "enabled": True,
    "email_smtp": "smtp.gmail.com",
    "email_port": 587,
    "email_user": "your_email@gmail.com",
    "email_password": "your_app_password",
    "recipients": ["alert1@example.com", "alert2@example.com"],
    "threshold_critical": 100  # Alertar si más de 100 incidentes críticos
}
```

---

## 🏃‍♂️ **EJECUCIÓN AUTOMATIZADA**

### **Programar Ejecución Diaria**
```bash
# Linux/macOS (crontab)
crontab -e
# Agregar línea:
0 9 * * * /path/to/python /path/to/CENTINELA_GAMMA_SHARE/src/centinela_gamma_maximized.py

# Windows (Task Scheduler)
# Crear tarea que ejecute:
# C:\Python\python.exe "C:\path\to\CENTINELA_GAMMA_SHARE\src\centinela_gamma_maximized.py"
```

### **Script de Monitoreo Continuo**
```bash
# Crear src/monitor.py para ejecución continua
python src/monitor.py --interval 4h --auto-process --auto-alerts
```

---

## 📞 **SOPORTE TÉCNICO**

Si encuentras problemas durante la instalación:

1. **📖 Revisa la documentación** en `docs/`
2. **🔍 Busca en problemas conocidos** arriba
3. **📧 Contacta soporte**: centinela.gamma.support@protonmail.com
4. **💬 Únete al Discord**: [Servidor CENTINELA-GAMMA](https://discord.gg/centinela)

### **Información a Incluir en Reportes de Problemas**
- Versión de Python (`python --version`)
- Sistema operativo y versión
- Mensaje de error completo
- Pasos que llevaron al error
- Archivos de log relevantes

---

**✅ ¡Instalación Completada! Ya puedes comenzar a documentar crímenes de guerra y contribuir a la justicia internacional.**