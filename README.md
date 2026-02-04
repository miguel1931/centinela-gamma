# 🕊️ CENTINELA-GAMMA: Sistema de Documentación de Crímenes de Guerra
## 📡 **Plataforma de Vigilancia y Documentación para la Justicia Internacional**

---

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-Public_Domain-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**CENTINELA-GAMMA** es un sistema integral de documentación de crímenes de guerra que utiliza Twitter/X como fuente principal de datos para recopilar, analizar y presentar evidencia de violaciones del derecho internacional humanitario.

---

## 🎯 **PROPÓSITO DEL PROYECTO**

Este sistema fue desarrollado para:

- **📊 Documentar crímenes de guerra** en tiempo real usando fuentes abiertas
- **⚖️ Preservar evidencia** para futuros tribunales internacionales  
- **🔍 Analizar patrones** de violaciones del derecho humanitario
- **🌍 Democratizar el acceso** a información sobre conflictos
- **🤖 Detectar desinformación** y actividad de bots
- **📈 Generar métricas** comprensibles para el público y organizaciones

---

## ⚡ **CARACTERÍSTICAS PRINCIPALES**

### 🔎 **Recopilación Inteligente**
- Búsquedas especializadas en Twitter/X con 39 consultas optimizadas
- Análisis de relevancia automático (0-100%)
- Detección de incidentes críticos
- Geolocalización de eventos

### 🧠 **Análisis Avanzado**
- **Detección de bots** con análisis de patrones
- **Clasificación legal** según Convenios de Ginebra y Estatuto de Roma
- **Análisis temporal** de escalada de violencia
- **Métricas de víctimas** civiles y infraestructura

### 📊 **Presentación de Datos**
- **Dashboard web** optimizado y responsive
- **API REST** para integración con otros sistemas
- **Procesamiento de datos** ultra-optimizado (99.96% reducción de tamaño)
- **Exportación** en múltiples formatos

### 🛡️ **Características de Seguridad**
- **Análisis de bots** para detectar manipulación
- **Verificación de fuentes** automática
- **Protección de datos** sensibles
- **Auditoría** de cambios y accesos

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
CENTINELA_GAMMA_SHARE/
├── README.md                           # Este archivo
├── INSTALLATION.md                     # Instrucciones de instalación
├── LICENSE                            # Licencia del proyecto
├── requirements.txt                   # Dependencias de Python
│
├── src/                              # Código fuente
│   ├── centinela_gamma_maximized.py    # Sistema principal de documentación
│   ├── palestine_tweets_processor.py   # Procesador de métricas optimizado
│   ├── palestine_war_crimes_api.py     # API REST del sistema
│   └── config.py                      # Configuración del sistema
│
├── dashboard/                        # Interfaz web
│   ├── palestine_war_crimes_dashboard_optimized.html
│   └── assets/                       # Recursos CSS/JS
│
├── docs/                            # Documentación
│   ├── USER_GUIDE.md                 # Guía de usuario
│   ├── API_REFERENCE.md              # Referencia de la API
│   ├── LEGAL_FRAMEWORK.md            # Marco legal del proyecto
│   └── TECHNICAL_DETAILS.md          # Detalles técnicos
│
└── examples/                        # Ejemplos de uso
    ├── sample_config.py               # Configuración de ejemplo
    └── sample_queries.json           # Consultas de ejemplo
```

---

## 🚀 **INSTALACIÓN RÁPIDA**

### **Prerrequisitos**
- Python 3.7 o superior
- Cuenta de Twitter/X con API v2 activada
- 2 GB de RAM mínimo
- Conexión a Internet estable

### **1. Clonar/Descargar el Proyecto**
```bash
# Descargar y extraer CENTINELA_GAMMA_SHARE.zip
# O clonar si está en repositorio Git
```

### **2. Instalar Dependencias**
```bash
cd CENTINELA_GAMMA_SHARE
pip install -r requirements.txt
```

### **3. Configurar API de Twitter**
```bash
cp examples/sample_config.py src/config.py
# Editar src/config.py con tus credenciales de Twitter API
```

### **4. Ejecutar el Sistema**
```bash
# Recopilación de datos
python src/centinela_gamma_maximized.py

# Procesar datos (optimización)
python src/palestine_tweets_processor.py

# Iniciar API y dashboard
python src/palestine_war_crimes_api.py
```

### **5. Acceder al Dashboard**
Abrir en navegador: `http://localhost:8081/palestine_war_crimes_dashboard_optimized.html`

---

## 💻 **CASOS DE USO**

### 👥 **Para Organizaciones de Derechos Humanos**
- Monitoreo continuo de situaciones de conflicto
- Generación de reportes automatizados
- Preservación de evidencia digital
- Análisis de tendencias y patrones

### 📰 **Para Periodistas y Medios**
- Verificación de información en tiempo real
- Identificación de fuentes confiables
- Detección de campañas de desinformación
- Generación de métricas para artículos

### 🎓 **Para Investigadores Académicos**
- Datos estructurados para investigación
- Análisis de conflictos a gran escala
- Estudios de desinformación
- Investigación en ciencias sociales

### ⚖️ **Para Organizaciones Legales**
- Recopilación de evidencia preliminar
- Documentación sistemática de violaciones
- Análisis para casos legales
- Apoyo a investigaciones judiciales

### 🌍 **Para Activistas y Ciudadanos**
- Monitoreo de situaciones locales
- Educación sobre conflictos globales
- Verificación de noticias
- Documentación de testimonios

---

## 📊 **MÉTRICAS Y CAPACIDADES**

### **Capacidad de Procesamiento**
- ⚡ **50,000 tweets** por ejecución
- 🔍 **39 consultas especializadas** simultáneas  
- 📊 **Reducción de datos**: 99.96% (26MB → 0.01MB)
- ⏱️ **Procesamiento**: < 5 minutos promedio

### **Análisis Incluidos**
- 🤖 **Detección de bots**: Probabilidad y confianza
- ⚖️ **Clasificación legal**: Convenios internacionales
- 📍 **Análisis geográfico**: Gaza, Cisjordania, Jerusalén Este
- ⏰ **Patrones temporales**: Escalada y tendencias
- 🔑 **Palabras clave**: Categorizadas por tipo de violación

---

## 🤝 **CONTRIBUIR AL PROYECTO**

### **Formas de Contribuir**
1. **🐛 Reportar bugs** y problemas encontrados
2. **💡 Sugerir mejoras** y nuevas funcionalidades
3. **🔧 Contribuir código** para nuevas características
4. **📖 Mejorar documentación** y guías
5. **🌍 Traducir** el proyecto a otros idiomas
6. **📊 Aportar casos de uso** y ejemplos reales

### **Áreas Prioritarias para Contribución**
- **Expansión geográfica** (otros conflictos)
- **Integración con más fuentes** (Facebook, Instagram, etc.)
- **Algoritmos de ML** para mejor clasificación
- **Interfaces móviles** para acceso desde dispositivos
- **Integración con organizaciones** internacionales

---

## ⚖️ **MARCO LEGAL Y ÉTICO**

### **Principios Fundamentales**
- **Transparencia total** en metodología y fuentes
- **Protección de datos** personales sensibles
- **Verificación cruzada** de información
- **Respeto a víctimas** y comunidades afectadas
- **Uso responsable** de datos públicos

### **Base Legal**
- **Convenios de Ginebra** (1949) y Protocolos Adicionales
- **Estatuto de Roma** de la Corte Penal Internacional
- **Declaración Universal** de los Derechos Humanos
- **Principios de Johannesburgo** sobre seguridad nacional

### **Limitaciones y Disclaimer**
⚠️ **Este sistema es una herramienta de documentación preliminar. Los datos recopilados requieren verificación adicional para uso en procesos legales formales.**

---

## 🛠️ **SOPORTE TÉCNICO**

### **Requisitos del Sistema**
- **SO**: Windows 10+, macOS 10.14+, Linux Ubuntu 18.04+
- **Python**: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **RAM**: 2GB mínimo, 4GB recomendado
- **Almacenamiento**: 1GB libre para datos
- **Internet**: Conexión estable (API de Twitter)

### **APIs Soportadas**
- ✅ **Twitter API v2** (requerido)
- 🔄 **Twitter API v1.1** (legacy, limitado)
- 📋 **Próximamente**: Facebook Graph API, Instagram Basic Display

### **Navegadores Compatibles**
- ✅ Chrome 90+
- ✅ Firefox 88+  
- ✅ Safari 14+
- ✅ Edge 90+

---

## 📞 **CONTACTO Y COMUNIDAD**

### **Canales de Soporte**
- 📧 **Email**: ****
- 💬 **Discord**: +++++
- 📱 **Telegram**: @+++++
- 🐦 **Twitter**: @++++++++

### **Para Emergencias**
Si encuentras evidencia de crímenes de guerra inmediatos:
1. **Documenta** con CENTINELA-GAMMA
2. **Reporta** a organizaciones internacionales:
   - 🔗 **Corte Penal Internacional**: https://www.icc-cpi.int/
   - 🔗 **Alto Comisionado para DDHH**: https://www.ohchr.org/
   - 🔗 **Human Rights Watch**: https://www.hrw.org/

---

## 🏆 **AGRADECIMIENTOS**

Este proyecto fue posible gracias a:
- **🕊️ Comunidades afectadas** que comparten sus testimonios
- **👥 Desarrolladores** de código abierto y sus herramientas
- **📊 Twitter/X** por proporcionar acceso a datos públicos
- **⚖️ Organizaciones legales** por su asesoramiento
- **🌍 Activistas** que luchan por la justicia mundial

---

## 🔮 **ROADMAP Y FUTURAS VERSIONES**

### **v2.0 (Próximo Trimestre)**
- [ ] Integración con más redes sociales
- [ ] Machine Learning para clasificación automática
- [ ] App móvil para documentación en campo
- [ ] Integración directa con organizaciones legales

### **v3.0 (Mediano Plazo)**
- [ ] Análisis de video y imágenes con IA
- [ ] Blockchain para verificación de integridad
- [ ] Múltiples idiomas y regiones
- [ ] Sistema de alertas en tiempo real

### **v4.0 (Largo Plazo)**
- [ ] Realidad aumentada para documentación
- [ ] IA conversacional para testimonios
- [ ] Integración con sistemas de justicia internacional
- [ ] Predicción de escalada de conflictos

---

## 📜 **LICENCIA**

```
LICENCIA DE DOMINIO PÚBLICO PARA CENTINELA-GAMMA

Este trabajo es dedicado al dominio público mundial bajo la licencia CC0.
Para ver una copia de esta licencia, visite:
http://creativecommons.org/publicdomain/zero/1.0/

DISCLAIMER: Este software se proporciona "tal como está", sin garantías
de ningún tipo. Los autores no se hacen responsables por el uso que se
haga de esta herramienta.
```

---

## 💪 **ÚNETE A LA CAUSA**

**CENTINELA-GAMMA** es más que software - es un movimiento por la **transparencia**, la **justicia** y la **verdad**. 

🌟 **Tu contribución puede ayudar a documentar violaciones, proteger a víctimas y construir un mundo más justo.**

### **Empezar es fácil:**
1. 📥 **Descarga** el proyecto
2. ⚙️ **Configura** según tu caso de uso
3. 🚀 **Ejecuta** y comienza a documentar
4. 🤝 **Comparte** tus resultados con organizaciones relevantes
5. 💬 **Contribuye** al desarrollo y mejora continua

---

**🕊️ Por la justicia, por la verdad, por la humanidad.**

**CENTINELA-GAMMA - Vigilancia para la Justicia Internacional**
