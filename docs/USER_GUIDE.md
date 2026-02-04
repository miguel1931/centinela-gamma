# 📖 GUÍA DE USUARIO - CENTINELA-GAMMA
## 🎯 **Manual Completo para Uso del Sistema**

---

## 🚀 **INTRODUCCIÓN RÁPIDA**

CENTINELA-GAMMA es un sistema de documentación de crímenes de guerra que te permite:
- 📊 Recopilar datos de Twitter/X sobre conflictos
- ⚖️ Analizar violaciones del derecho internacional
- 🤖 Detectar actividad de bots y desinformación  
- 📈 Visualizar datos en dashboard interactivo

**⏱️ Tiempo estimado para primer uso: 15-30 minutos**

---

## 🎮 **FLUJO DE TRABAJO BÁSICO**

```
1. CONFIGURAR → 2. RECOPILAR → 3. PROCESAR → 4. ANALIZAR → 5. COMPARTIR
     ⚙️              📡            🔄           📊           📤
```

### **1. Configuración (Una sola vez)**
- Configurar credenciales de Twitter API
- Personalizar regiones y palabras clave
- Establecer límites de procesamiento

### **2. Recopilación (Diaria/Semanal)**
- Ejecutar búsquedas automatizadas
- Recopilar hasta 50,000 tweets
- Clasificar por relevancia y criticidad

### **3. Procesamiento (Automático)**
- Optimizar datos (reducir de 26MB a 0.01MB)
- Generar métricas esenciales
- Analizar patrones de bots

### **4. Análisis (Dashboard)**
- Visualizar métricas en tiempo real
- Explorar distribución geográfica
- Revisar ejemplos representativos

### **5. Compartir (Organizaciones)**
- Exportar datos para organizaciones
- Generar reportes automatizados
- Preservar evidencia para tribunales

---

## 📊 **USO DEL DASHBOARD**

### **Interfaz Principal**
El dashboard está dividido en secciones:

#### **📈 Métricas Generales**
- **Total de Tweets**: Documentos recopilados
- **Incidentes Críticos**: Violaciones graves detectadas
- **Fuentes Únicas**: Número de cuentas analizadas
- **Nivel de Alerta**: BAJO/MEDIO/ALTO/EXTREMO

#### **🤖 Análisis de Bots**
- **Probabilidad de Bots**: Porcentaje de actividad automatizada
- **Nivel de Confianza**: HIGH/MEDIUM/LOW
- **Indicadores Sospechosos**: Patrones detectados
- **Recomendaciones**: Acciones sugeridas

#### **⚖️ Indicadores de Crímenes**
- **Víctimas Civiles**: Reportes de bajas civiles
- **Ataques a Infraestructura**: Hospitales, escuelas, etc.
- **Víctimas Menores**: Niños afectados
- **Índice de Severidad**: Escalamiento del conflicto

#### **🗺️ Distribución Geográfica**
- **Gaza**: Porcentaje de incidentes
- **Cisjordania**: Distribución territorial
- **Jerusalén Este**: Actividad reportada
- **Otros**: Regiones adicionales

### **Navegación del Dashboard**

```bash
# Acceder al dashboard
http://localhost:8081/palestine_war_crimes_dashboard_optimized.html

# Secciones disponibles:
├── 📊 Métricas Generales
├── 🤖 Análisis de Bots  
├── ⚖️ Crímenes de Guerra
├── ⏰ Patrones Temporales
├── 📍 Distribución Geográfica
├── 🔑 Palabras Clave
└── 📝 Ejemplos Representativos
```

---

## 🔧 **CONFIGURACIONES AVANZADAS**

### **Personalizar Búsquedas**
Editar `src/config.py`:

```python
# Palabras clave personalizadas
CUSTOM_KEYWORDS = [
    "war crimes",
    "civilian casualties", 
    "hospital bombing",
    "school attack",
    "your_custom_terms"
]

# Idiomas a incluir
LANGUAGES = ["en", "ar", "es", "fr"]  # inglés, árabe, español, francés

# Filtros geográficos
GEOGRAPHIC_FILTERS = {
    "include": ["Gaza", "Palestine", "West Bank"],
    "exclude": ["spam_location", "irrelevant_place"]
}
```

### **Ajustar Límites de Recopilación**
```python
# Límites por ejecución
LIMITS = {
    "max_tweets_total": 50000,      # Total máximo
    "max_tweets_per_query": 1500,   # Por búsqueda individual
    "max_budget_usd": 2.00,         # Presupuesto Twitter API
    "timeout_minutes": 30           # Tiempo máximo de ejecución
}
```

### **Configurar Alertas Automáticas**
```python
# Sistema de alertas
ALERTS = {
    "enabled": True,
    "critical_incident_threshold": 50,   # Alertar si >50 incidentes críticos
    "bot_activity_threshold": 80,        # Alertar si >80% actividad de bots
    "notification_methods": ["email", "discord", "telegram"]
}
```

---

## 📈 **INTERPRETACIÓN DE MÉTRICAS**

### **Relevancia Score (0-100)**
- **90-100**: Incidente crítico confirmado
- **80-89**: Alta probabilidad de violación
- **70-79**: Relevante para investigación
- **60-69**: Contexto importante
- **<60**: Información de trasfondo

### **Criticidad (True/False)**
- **True**: Violación grave del derecho internacional
- **False**: Información contextual o menor relevancia

### **Probabilidad de Bots (%)**
- **>80%**: Alta actividad automatizada, verificación requerida
- **60-80%**: Actividad sospechosa, analizar patrones
- **40-60%**: Actividad mixta, monitorear tendencias
- **<40%**: Actividad mayormente orgánica

### **Nivel de Alerta**
- **EXTREMO**: Crisis humanitaria, intervención urgente
- **ALTO**: Escalada significativa, atención inmediata  
- **MEDIO**: Situación tensa, monitoreo continuo
- **BAJO**: Situación estable, seguimiento rutinario

---

## 🔍 **CASOS DE USO ESPECÍFICOS**

### **👥 Para Organizaciones de Derechos Humanos**

#### **Monitoreo Diario**
```bash
# Ejecución automática diaria
python src/centinela_gamma_maximized.py --daily-monitor

# Generar reporte para organizaciones
python src/generate_report.py --format ngo --recipient "human_rights_org"
```

#### **Alertas de Crisis**
```python
# Configurar umbrales específicos
NGO_ALERTS = {
    "civilian_casualties_threshold": 20,  # >20 víctimas civiles
    "infrastructure_attacks_threshold": 5, # >5 ataques a infraestructura
    "children_casualties_threshold": 3     # >3 niños afectados
}
```

### **📰 Para Periodistas**

#### **Verificación de Información**
```bash
# Verificar tweet específico
python src/verify_tweet.py --tweet-id "1234567890"

# Analizar tendencias por período
python src/analyze_trends.py --period "last_24h" --focus "civilian_casualties"
```

#### **Detectar Desinformación**
```bash
# Análisis de bots en trending topics
python src/bot_analysis.py --hashtag "#trending_topic"

# Verificar coordinación de cuentas
python src/coordination_analysis.py --time-window "2h"
```

### **🎓 Para Investigadores**

#### **Análisis Académico**
```bash
# Exportar datos para análisis estadístico
python src/export_research_data.py --format csv --anonymize True

# Generar métricas longitudinales
python src/longitudinal_analysis.py --period "6_months" --metrics "all"
```

#### **Estudios de Conflicto**
```python
# Configuración para investigación académica
RESEARCH_CONFIG = {
    "anonymize_users": True,            # Anonimizar datos personales
    "focus_on_patterns": True,          # Analizar patrones, no casos específicos
    "statistical_significance": 0.05,   # Nivel de significancia estadística
    "sample_size_minimum": 1000         # Tamaño mínimo de muestra
}
```

---

## 📊 **EXPORTACIÓN DE DATOS**

### **Formatos Disponibles**
```bash
# JSON (completo, para desarrolladores)
python src/export_data.py --format json --complete

# CSV (tabular, para análisis)
python src/export_data.py --format csv --metrics-only

# Excel (presentación, para organizaciones)
python src/export_data.py --format xlsx --dashboard-summary

# PDF (reporte, para distribución)
python src/export_data.py --format pdf --executive-summary
```

### **Personalizar Exportaciones**
```python
# Configurar exportación personalizada
EXPORT_CONFIG = {
    "include_raw_tweets": False,        # No incluir tweets completos
    "include_metrics": True,            # Incluir métricas procesadas  
    "include_analysis": True,           # Incluir análisis de IA
    "anonymize_sources": True,          # Anonimizar fuentes
    "focus_critical_only": False,      # Incluir todos los niveles
    "time_range": "last_30_days"       # Período específico
}
```

---

## ⚠️ **CONSIDERACIONES ÉTICAS**

### **Protección de Fuentes**
- **Nunca compartir** información personal de víctimas
- **Anonimizar** datos antes de distribuir
- **Verificar** información sensible antes de usar
- **Respetar** privacidad de testimonios

### **Uso Responsable**
- **Verificación cruzada** con múltiples fuentes
- **Contexto adecuado** en interpretación de datos
- **Transparencia** sobre limitaciones del sistema
- **Coordinación** con organizaciones establecidas

### **Limitaciones del Sistema**
⚠️ **IMPORTANTE**: Los datos recopilados son preliminares y requieren verificación adicional para uso legal formal.

- Los algoritmos pueden tener sesgos
- La información de redes sociales puede ser manipulada
- Se requiere expertise humano para interpretación final
- No sustituye la investigación profesional

---

## 🔧 **MANTENIMIENTO**

### **Tareas Regulares**
```bash
# Limpiar datos antiguos (mensual)
python src/cleanup_old_data.py --older-than 90days

# Actualizar algoritmos de detección (semanal)
python src/update_detection_algorithms.py

# Verificar salud del sistema (diario)
python src/system_health_check.py
```

### **Respaldos**
```bash
# Respaldar configuración
cp -r src/config.py backups/config_$(date +%Y%m%d).py

# Respaldar datos críticos  
tar -czf backups/data_backup_$(date +%Y%m%d).tar.gz data/

# Respaldar exportaciones
cp -r exports/ backups/exports_$(date +%Y%m%d)/
```

---

## 📞 **OBTENER AYUDA**

### **Documentación Adicional**
- 📖 `docs/API_REFERENCE.md` - Referencia completa de la API
- ⚖️ `docs/LEGAL_FRAMEWORK.md` - Marco legal del proyecto  
- 🔧 `docs/TECHNICAL_DETAILS.md` - Detalles técnicos avanzados

### **Soporte Comunitario**
- 💬 **Discord**: Comunidad activa 24/7
- 📧 **Email**: Soporte técnico especializado
- 📱 **Telegram**: Alertas y actualizaciones
- 🐦 **Twitter**: Noticias del proyecto

### **Contribuir al Proyecto**
```bash
# Reportar problemas
# Crear issue en repositorio con detalles

# Sugerir mejoras
# Contactar al equipo de desarrollo

# Contribuir código
# Seguir guías de contribución en CONTRIBUTING.md
```

---

**✅ Con esta guía ya puedes utilizar CENTINELA-GAMMA de manera efectiva para documentar violaciones del derecho internacional y contribuir a la justicia mundial.**