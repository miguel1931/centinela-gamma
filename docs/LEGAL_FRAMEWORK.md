# ⚖️ MARCO LEGAL - CENTINELA-GAMMA
## 🏛️ **Base Jurídica y Ética del Proyecto**

---

## 📜 **FUNDAMENTOS LEGALES INTERNACIONALES**

### **Convenios de Ginebra (1949)**
CENTINELA-GAMMA se basa en las definiciones establecidas en los Convenios de Ginebra:

#### **🏥 Protección de Civiles (IV Convenio)**
- **Art. 3**: Protección mínima en conflictos no internacionales
- **Art. 27**: Trato humano de personas protegidas  
- **Art. 33**: Prohibición de castigos colectivos
- **Art. 49**: Prohibición de deportaciones y traslados forzosos
- **Art. 53**: Prohibición de destrucción de bienes civiles

#### **🔴 Infracciones Graves (Art. 147)**
- Homicidio intencional
- Tortura o tratos inhumanos  
- Causar intencionalmente grandes sufrimientos
- Destrucción extensa de bienes
- Deportación o traslado ilegal

### **Protocolos Adicionales (1977)**
#### **📍 Protocolo I (Conflictos Internacionales)**
- **Art. 48**: Distinción entre civiles y combatientes
- **Art. 51**: Protección de la población civil
- **Art. 52**: Protección de bienes civiles
- **Art. 57**: Precauciones en el ataque

---

## 🏛️ **ESTATUTO DE ROMA (1998)**

### **Crímenes Bajo Jurisdicción de la CPI**

#### **🔪 Crímenes de Guerra (Art. 8)**
CENTINELA-GAMMA clasifica incidentes según estas definiciones:

```
a) INFRACCIONES GRAVES:
   - Homicidio intencional
   - Tortura o tratos inhumanos
   - Causar grandes sufrimientos
   - Destrucción extensa de bienes
   - Toma de rehenes

b) OTRAS VIOLACIONES GRAVES:
   - Dirigir ataques contra civiles
   - Atacar bienes civiles
   - Atacar personal de asistencia humanitaria
   - Causar daños ambientales excesivos
   - Utilizar niños soldados
```

#### **🌍 Crímenes de Lesa Humanidad (Art. 7)**
- Asesinato como parte de un ataque sistemático
- Exterminio de población civil
- Deportación o traslado forzoso
- Persecución por motivos políticos, raciales o religiosos
- Otros actos inhumanos

#### **🔥 Genocidio (Art. 6)**  
- Intención de destruir un grupo nacional, étnico, racial o religioso
- Matanza de miembros del grupo
- Lesión grave física o mental
- Sometimiento a condiciones de destrucción
- Medidas para impedir nacimientos

---

## 🌍 **MARCO DE DERECHOS HUMANOS**

### **Declaración Universal de DDHH (1948)**
#### **Derechos Fundamentales Monitoreados**
- **Art. 3**: Derecho a la vida, libertad y seguridad
- **Art. 5**: Prohibición de torturas y tratos crueles
- **Art. 9**: Prohibición de detención arbitraria
- **Art. 12**: Derecho a la privacidad
- **Art. 13**: Libertad de movimiento
- **Art. 17**: Derecho a la propiedad
- **Art. 18**: Libertad de pensamiento y religión
- **Art. 19**: Libertad de expresión e información

### **Pacto Internacional de Derechos Civiles y Políticos (1966)**
- **Art. 6**: Derecho a la vida
- **Art. 7**: Prohibición de tortura
- **Art. 9**: Libertad y seguridad personales
- **Art. 12**: Libertad de circulación
- **Art. 14**: Derecho a un juicio justo
- **Art. 18**: Libertad de religión

---

## ⚖️ **APLICACIÓN EN CENTINELA-GAMMA**

### **🔍 Sistema de Clasificación Legal**

#### **Nivel 1: Infracciones Graves (Críticas)**
```python
CRITICAL_VIOLATIONS = {
    "homicidio_intencional": ["killed", "murdered", "executed"],
    "ataques_a_civiles": ["civilians killed", "civilian casualties"],
    "destruccion_bienes": ["hospital bombed", "school destroyed"],
    "tortura": ["torture", "ill-treatment"],
    "deportacion": ["forced displacement", "ethnic cleansing"]
}
```

#### **Nivel 2: Violaciones Serias (Altas)**
```python  
SERIOUS_VIOLATIONS = {
    "ataques_indiscriminados": ["bombing", "shelling", "airstrike"],
    "uso_fuerza_excesiva": ["excessive force", "disproportionate"],
    "restriccion_movimiento": ["blockade", "siege", "closure"],
    "destruccion_propiedad": ["home demolition", "property destruction"]
}
```

#### **Nivel 3: Preocupaciones (Medianas)**
```python
CONCERNING_ACTS = {
    "arrestos_masivos": ["mass arrests", "detention"],
    "restriccion_acceso": ["access denied", "humanitarian blocked"],
    "intimidacion": ["intimidation", "harassment"],
    "censura": ["media censorship", "journalist targeted"]
}
```

---

## 📊 **METODOLOGÍA DE ANÁLISIS LEGAL**

### **Criterios de Evaluación**

#### **🎯 Relevancia Legal (0-100)**
```python
def calculate_legal_relevance(tweet_data):
    score = 0
    
    # Infracciones graves (+40 puntos)
    if contains_grave_breach_indicators(tweet_data):
        score += 40
    
    # Evidencia específica (+30 puntos)  
    if contains_specific_evidence(tweet_data):
        score += 30
        
    # Fuente confiable (+20 puntos)
    if is_reliable_source(tweet_data):
        score += 20
        
    # Contexto geográfico (+10 puntos)
    if has_geographic_context(tweet_data):
        score += 10
        
    return min(score, 100)
```

#### **⚖️ Clasificación de Crímenes**
```python
CRIME_CATEGORIES = {
    "war_crimes": {
        "geneva_articles": [3, 27, 33, 49, 53],
        "rome_statute": "Article 8",
        "keywords": ["war crime", "geneva violation"]
    },
    "crimes_against_humanity": {
        "rome_statute": "Article 7", 
        "keywords": ["crimes against humanity", "systematic attack"]
    },
    "genocide": {
        "rome_statute": "Article 6",
        "keywords": ["genocide", "ethnic cleansing"]
    }
}
```

---

## 🛡️ **PROTECCIONES LEGALES IMPLEMENTADAS**

### **Protección de Fuentes**
```python
PRIVACY_PROTECTIONS = {
    "anonymize_personal_data": True,
    "hash_user_identifiers": True,
    "remove_location_metadata": True,
    "protect_witness_identity": True,
    "secure_data_storage": True
}
```

### **Verificación de Información**
```python
VERIFICATION_PROTOCOLS = {
    "cross_reference_sources": True,
    "timestamp_verification": True,
    "geolocation_confirmation": True,
    "source_credibility_check": True,
    "content_authenticity": True
}
```

---

## 🌐 **JURISDICCIÓN Y COMPETENCIA**

### **Corte Penal Internacional**
#### **Requisitos de Admisibilidad**
- **Gravedad**: Suficiente para justificar acción de la CPI
- **Complementariedad**: Estados no pueden/quieren investigar
- **Jurisdicción**: Crímenes en territorio de Estado Parte
- **Temporales**: Posteriores al 1 julio 2002

#### **Estados Relevantes**
- **Palestina**: Estado Parte desde 2015
- **Israel**: No es Estado Parte
- **Jurisdicción Territorial**: Territorios Palestinos Ocupados

### **Otros Mecanismos Legales**
- **Comisión de Investigación de la ONU**
- **Corte Internacional de Justicia**
- **Tribunales nacionales (jurisdicción universal)**
- **Comités de Derechos Humanos de la ONU**

---

## 📋 **ESTÁNDARES DE EVIDENCIA**

### **Niveles de Evidencia**
```
1. EVIDENCIA PRIMA FACIE (Inicial)
   - Testimonios de redes sociales
   - Información de fuentes abiertas
   - Indicadores preliminares

2. EVIDENCIA CORROBORATIVA (Confirmación)
   - Múltiples fuentes independientes  
   - Verificación por organizaciones
   - Análisis técnico adicional

3. EVIDENCIA JUDICIAL (Legal)
   - Testimonios bajo juramento
   - Evidencia forense certificada
   - Cadena de custodia establecida
```

### **Cadena de Custodia Digital**
```python
EVIDENCE_CHAIN = {
    "collection_timestamp": "ISO format",
    "source_platform": "Twitter/X API",
    "collection_method": "Automated search",
    "processing_algorithms": "CENTINELA-GAMMA v1.0",
    "hash_verification": "SHA-256",
    "storage_location": "Encrypted database",
    "access_log": "All access logged"
}
```

---

## ⚠️ **LIMITACIONES LEGALES**

### **Restricciones del Sistema**
1. **No constituye evidencia judicial definitiva**
2. **Requiere verificación profesional adicional**
3. **Limitado a información de fuentes abiertas**
4. **Sujeto a sesgos de algoritmos y plataformas**
5. **No sustituye investigaciones oficiales**

### **Disclaimer Legal**
⚠️ **IMPORTANTE**: Los datos recopilados por CENTINELA-GAMMA son de naturaleza preliminar y están destinados a:
- Documentación inicial de posibles violaciones
- Apoyo a organizaciones de derechos humanos
- Investigación académica y periodística  
- Preservación de información para futuros procesos

**NO deben utilizarse como evidencia legal directa sin verificación y procesamiento adicional por profesionales calificados.**

---

## 📞 **RECURSOS LEGALES**

### **Organizaciones Internacionales**
- **🏛️ Corte Penal Internacional**: https://www.icc-cpi.int/
- **🌍 Alto Comisionado para DDHH**: https://www.ohchr.org/
- **⚖️ Corte Internacional de Justicia**: https://www.icj-cij.org/
- **🏢 Consejo de Derechos Humanos**: https://www.ohchr.org/en/hr-bodies/hrc

### **Organizaciones de DDHH**
- **🔍 Human Rights Watch**: https://www.hrw.org/
- **🛡️ Amnistía Internacional**: https://www.amnesty.org/
- **📊 Al-Haq**: http://www.alhaq.org/
- **⚖️ FIDH**: https://www.fidh.org/

### **Organizaciones Legales Especializadas**
- **🏛️ International Commission of Jurists**: https://www.icj.org/
- **⚖️ Lawyers for Palestinian Human Rights**: https://www.lphr.org.uk/
- **🌍 International Federation for Human Rights**: https://www.fidh.org/

---

## 📚 **REFERENCIAS LEGALES**

### **Documentos Fundacionales**
1. Convenios de Ginebra (12 agosto 1949)
2. Protocolos Adicionales I y II (8 junio 1977)  
3. Estatuto de Roma (17 julio 1998)
4. Declaración Universal de DDHH (10 diciembre 1948)

### **Jurisprudencia Relevante**
- **CPI c. Bemba** (crímenes de guerra)
- **CPI c. Katanga** (uso de niños soldados)
- **CIJ - Muro Israel** (opinión consultiva 2004)
- **TEDH - Al-Skeini** (jurisdicción extraterritorial)

### **Informes de Comisiones**
- Comisión Goldstone (2009)
- Comisión de Investigación Gaza (2021)
- Relatores Especiales de la ONU
- Comité contra la Tortura

---

**⚖️ El marco legal de CENTINELA-GAMMA está diseñado para apoyar la justicia internacional y la rendición de cuentas por violaciones graves del derecho humanitario y los derechos humanos.**