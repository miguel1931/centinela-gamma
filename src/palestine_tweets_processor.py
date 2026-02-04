#!/usr/bin/env python3
"""
🕊️ PALESTINE TWEETS PROCESSOR - DOOM SYSTEM v1.0
Arquitecto: VIGIL | Soberano: DOOM
Procesador que extrae métricas, análisis de bots y ejemplos representativos
"""

import json
import os
from datetime import datetime
from collections import Counter, defaultdict
from typing import Dict, List, Any
import re
import glob

class PalestineTweetsProcessor:
    def __init__(self):
        self.bot_indicators = [
            'account_age_days', 'tweets_per_day', 'followers_ratio', 
            'repeated_content', 'timing_patterns', 'engagement_anomalies'
        ]
        
        print("🕊️" + "="*75)
        print("🕊️ PALESTINE TWEETS PROCESSOR - DOOM SYSTEM v1.0")
        print("🕊️ Extrayendo métricas esenciales y análisis de bots")
        print("🕊️" + "="*75)

    def process_latest_tweets(self) -> str:
        """Procesa el archivo más reciente de tweets de Gaza/Palestina"""
        try:
            # Buscar archivo más reciente
            json_files = glob.glob("centinela_gamma_tweets_maximized_*.json")
            if not json_files:
                print("❌ No se encontraron archivos de CENTINELA-GAMMA")
                return None
            
            latest_file = max(json_files, key=os.path.getmtime)
            file_size_mb = os.path.getsize(latest_file) / (1024 * 1024)
            
            print(f"📄 Procesando: {latest_file}")
            print(f"📊 Tamaño original: {file_size_mb:.2f} MB")
            
            # Cargar datos originales
            with open(latest_file, 'r', encoding='utf-8') as f:
                original_data = json.load(f)
            
            # Procesar datos
            processed_data = self.extract_essential_metrics(original_data)
            
            # Guardar archivo procesado
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"palestine_metrics_processed_{timestamp}.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, indent=2, ensure_ascii=False)
            
            output_size_mb = os.path.getsize(output_file) / (1024 * 1024)
            reduction = ((file_size_mb - output_size_mb) / file_size_mb) * 100
            
            print(f"💾 Archivo procesado: {output_file}")
            print(f"📊 Tamaño procesado: {output_size_mb:.2f} MB")
            print(f"🎯 Reducción: {reduction:.1f}%")
            
            return output_file
            
        except Exception as e:
            print(f"❌ Error procesando tweets: {e}")
            return None

    def extract_essential_metrics(self, data: Dict) -> Dict:
        """Extrae métricas esenciales, análisis de bots y ejemplos"""
        tweets = data.get('tweets', [])
        original_metadata = data.get('metadata', {})
        
        print(f"🔍 Procesando {len(tweets):,} tweets...")
        
        # Análisis básico
        basic_metrics = self.calculate_basic_metrics(tweets, original_metadata)
        
        # Análisis de bots
        bot_analysis = self.analyze_bot_patterns(tweets)
        
        # Palabras clave y tendencias
        keywords_analysis = self.analyze_keywords(tweets)
        
        # Ejemplos representativos
        representative_examples = self.select_representative_examples(tweets)
        
        # Análisis temporal
        temporal_analysis = self.analyze_temporal_patterns(tweets)
        
        # Análisis geográfico
        geographic_analysis = self.analyze_geographic_distribution(tweets)
        
        # Análisis de crímenes de guerra
        war_crimes_analysis = self.analyze_war_crimes_indicators(tweets)
        
        processed_data = {
            'metadata': {
                'processing_timestamp': datetime.now().isoformat(),
                'original_file_size_mb': os.path.getsize(glob.glob("centinela_gamma_tweets_maximized_*.json")[0]) / (1024 * 1024),
                'original_tweets_count': len(tweets),
                'processing_version': '1.0',
                'source': 'CENTINELA-GAMMA'
            },
            'basic_metrics': basic_metrics,
            'bot_analysis': bot_analysis,
            'keywords_analysis': keywords_analysis,
            'temporal_analysis': temporal_analysis,
            'geographic_analysis': geographic_analysis,
            'war_crimes_analysis': war_crimes_analysis,
            'representative_examples': representative_examples,
            'dashboard_config': {
                'update_interval': 60000,
                'max_incidents_display': 8,
                'max_keywords_display': 10
            }
        }
        
        return processed_data

    def calculate_basic_metrics(self, tweets: List[Dict], original_metadata: Dict) -> Dict:
        """Calcula métricas básicas"""
        total_tweets = len(tweets)
        critical_tweets = sum(1 for t in tweets if t.get('is_critical', False))
        
        # Métricas de relevancia
        avg_relevance = sum(t.get('relevance_score', 0) for t in tweets) / max(total_tweets, 1)
        high_relevance = sum(1 for t in tweets if t.get('relevance_score', 0) > 80)
        
        # Métricas de engagement
        total_retweets = sum(t.get('metrics', {}).get('retweet_count', 0) for t in tweets)
        total_likes = sum(t.get('metrics', {}).get('like_count', 0) for t in tweets)
        
        # Autores únicos
        unique_authors = len(set(t.get('author', t.get('author_id', 'unknown')) for t in tweets))
        
        return {
            'total_tweets': total_tweets,
            'critical_tweets': critical_tweets,
            'critical_percentage': round((critical_tweets / max(total_tweets, 1)) * 100, 2),
            'unique_authors': unique_authors,
            'avg_tweets_per_author': round(total_tweets / max(unique_authors, 1), 2),
            'avg_relevance_score': round(avg_relevance, 2),
            'high_relevance_count': high_relevance,
            'total_retweets': total_retweets,
            'total_likes': total_likes,
            'avg_engagement': round((total_retweets + total_likes) / max(total_tweets, 1), 2),
            'extraction_info': original_metadata.get('extraction_info', {}),
            'war_crimes_indicators': original_metadata.get('war_crimes_indicators', {})
        }

    def analyze_bot_patterns(self, tweets: List[Dict]) -> Dict:
        """Analiza patrones que sugieren actividad de bots"""
        print("🤖 Analizando patrones de bots...")
        
        # Análisis por autor
        author_stats = defaultdict(list)
        for tweet in tweets:
            author = tweet.get('author', tweet.get('author_id', 'unknown'))
            author_stats[author].append(tweet)
        
        # Detectar patrones sospechosos
        suspicious_patterns = {
            'high_volume_authors': 0,  # Autores con muchos tweets
            'repeated_content': 0,     # Contenido repetitivo
            'timing_clusters': 0,      # Tweets agrupados en tiempo
            'low_engagement_spam': 0   # Muchos tweets, poco engagement
        }
        
        content_similarity = {}
        
        for author, author_tweets in author_stats.items():
            tweet_count = len(author_tweets)
            
            # Autores con volumen alto
            if tweet_count > 30:  # Más de 30 tweets del mismo autor
                suspicious_patterns['high_volume_authors'] += 1
            
            # Contenido repetitivo
            texts = [t.get('text', '').lower()[:50] for t in author_tweets]
            unique_texts = len(set(texts))
            
            if tweet_count > 5 and (unique_texts / tweet_count) < 0.7:
                suspicious_patterns['repeated_content'] += 1
                content_similarity[author] = round((unique_texts / tweet_count), 2)
            
            # Engagement bajo con volumen alto
            total_engagement = sum(
                t.get('metrics', {}).get('retweet_count', 0) + 
                t.get('metrics', {}).get('like_count', 0) 
                for t in author_tweets
            )
            avg_engagement = total_engagement / tweet_count
            
            if tweet_count > 10 and avg_engagement < 1:
                suspicious_patterns['low_engagement_spam'] += 1
        
        # Calcular probabilidad de bots
        total_authors = len(author_stats)
        
        bot_probability = 0
        indicators = []
        
        # Indicador 1: Alto porcentaje de autores con volumen sospechoso
        high_volume_ratio = suspicious_patterns['high_volume_authors'] / max(total_authors, 1)
        if high_volume_ratio > 0.1:  # Más del 10%
            bot_probability += 30
            indicators.append(f"Autores de alto volumen: {high_volume_ratio:.1%}")
        
        # Indicador 2: Contenido repetitivo
        repeated_ratio = suspicious_patterns['repeated_content'] / max(total_authors, 1)
        if repeated_ratio > 0.05:  # Más del 5%
            bot_probability += 25
            indicators.append(f"Contenido repetitivo: {repeated_ratio:.1%}")
        
        # Indicador 3: Promedio de tweets por autor
        total_tweets = len(tweets)
        avg_tweets_per_author = total_tweets / max(total_authors, 1)
        if avg_tweets_per_author > 25:
            bot_probability += 20
            indicators.append(f"Promedio tweets/autor: {avg_tweets_per_author:.1f}")
        
        # Indicador 4: Engagement sospechosamente bajo
        spam_ratio = suspicious_patterns['low_engagement_spam'] / max(total_authors, 1)
        if spam_ratio > 0.08:  # Más del 8%
            bot_probability += 15
            indicators.append(f"Bajo engagement: {spam_ratio:.1%}")
        
        bot_probability = min(bot_probability, 95)
        
        confidence_level = 'HIGH' if bot_probability > 70 else 'MEDIUM' if bot_probability > 40 else 'LOW'
        
        return {
            'bot_probability_percentage': bot_probability,
            'confidence_level': confidence_level,
            'indicators': indicators,
            'suspicious_patterns': suspicious_patterns,
            'total_authors_analyzed': total_authors,
            'content_similarity_samples': dict(list(content_similarity.items())[:5]),  # Top 5 ejemplos
            'recommendations': self.get_bot_recommendations(bot_probability),
            'analysis_details': {
                'avg_tweets_per_author': round(avg_tweets_per_author, 2),
                'high_volume_authors': suspicious_patterns['high_volume_authors'],
                'repeated_content_authors': suspicious_patterns['repeated_content'],
                'spam_like_authors': suspicious_patterns['low_engagement_spam']
            }
        }

    def get_bot_recommendations(self, bot_probability: float) -> List[str]:
        """Genera recomendaciones basadas en probabilidad de bots"""
        if bot_probability > 80:
            return [
                "ALTO RIESGO: Implementar filtros anti-bot inmediatamente",
                "Validar manualmente muestra de usuarios más activos",
                "Incrementar verificación de fuentes",
                "Implementar análisis de red para detectar coordinación"
            ]
        elif bot_probability > 60:
            return [
                "RIESGO MEDIO: Analizar patrones temporales detalladamente", 
                "Verificar autenticidad de cuentas más activas",
                "Implementar alertas automáticas para volumen anómalo",
                "Considerar filtros adicionales de contenido"
            ]
        else:
            return [
                "RIESGO BAJO: Mantener monitoreo regular",
                "Continuar análisis de tendencias",
                "Documentar patrones para referencia futura"
            ]

    def analyze_keywords(self, tweets: List[Dict]) -> Dict:
        """Analiza palabras clave más frecuentes"""
        print("🔑 Analizando palabras clave...")
        
        all_keywords = []
        for tweet in tweets:
            keywords = tweet.get('keywords_detected', [])
            all_keywords.extend(keywords)
        
        keyword_freq = Counter(all_keywords)
        
        # Clasificar keywords por categoría
        categories = {
            'violencia': ['killed', 'dead', 'murdered', 'shot', 'bombing', 'airstrike', 'shelling'],
            'victimas': ['children killed', 'civilians killed', 'family killed', 'women', 'elderly'],
            'infraestructura': ['hospital bombed', 'school destroyed', 'mosque damaged', 'home demolition'],
            'militar': ['IDF', 'Israeli forces', 'Israeli army', 'tank', 'drone strike', 'F-16'],
            'legal': ['war crime', 'genocide', 'ethnic cleansing', 'apartheid', 'illegal settlement'],
            'humanitario': ['siege', 'blockade', 'collective punishment', 'humanitarian crisis']
        }
        
        categorized_keywords = {}
        for category, keywords in categories.items():
            categorized_keywords[category] = {
                kw: keyword_freq.get(kw, 0) for kw in keywords if keyword_freq.get(kw, 0) > 0
            }
        
        return {
            'top_keywords': dict(keyword_freq.most_common(15)),
            'total_keywords_detected': len(all_keywords),
            'unique_keywords': len(keyword_freq),
            'categorized_keywords': categorized_keywords,
            'critical_indicators': {
                'violence_mentions': sum(keyword_freq.get(kw, 0) for kw in categories['violencia']),
                'victim_mentions': sum(keyword_freq.get(kw, 0) for kw in categories['victimas']),
                'war_crimes_mentions': sum(keyword_freq.get(kw, 0) for kw in categories['legal'])
            }
        }

    def analyze_temporal_patterns(self, tweets: List[Dict]) -> Dict:
        """Analiza patrones temporales"""
        print("⏰ Analizando patrones temporales...")
        
        hourly_distribution = defaultdict(int)
        daily_distribution = defaultdict(int)
        
        for tweet in tweets:
            created_at = tweet.get('created_at', '')
            if created_at:
                try:
                    dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    hour = dt.hour
                    date = dt.date().isoformat()
                    
                    hourly_distribution[hour] += 1
                    daily_distribution[date] += 1
                except:
                    continue
        
        # Detectar picos
        peak_hours = sorted(hourly_distribution.items(), key=lambda x: x[1], reverse=True)[:3]
        peak_days = sorted(daily_distribution.items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            'hourly_distribution': dict(hourly_distribution),
            'daily_distribution': dict(daily_distribution),
            'peak_hours': [f"{hour:02d}:00 ({count} tweets)" for hour, count in peak_hours],
            'peak_days': [f"{date} ({count} tweets)" for date, count in peak_days],
            'total_time_span_days': len(daily_distribution)
        }

    def analyze_geographic_distribution(self, tweets: List[Dict]) -> Dict:
        """Analiza distribución geográfica"""
        print("📍 Analizando distribución geográfica...")
        
        location_counter = Counter()
        for tweet in tweets:
            location = tweet.get('location', '').strip()
            if location and location != 'Unknown':
                location_counter[location] += 1
        
        # Clasificar por región
        regions = {
            'Gaza': 0,
            'West Bank': 0,
            'East Jerusalem': 0,
            'Other': 0
        }
        
        for location, count in location_counter.items():
            location_lower = location.lower()
            if 'gaza' in location_lower:
                regions['Gaza'] += count
            elif any(wb in location_lower for wb in ['west bank', 'ramallah', 'jenin', 'nablus', 'hebron']):
                regions['West Bank'] += count
            elif 'jerusalem' in location_lower:
                regions['East Jerusalem'] += count
            else:
                regions['Other'] += count
        
        return {
            'top_locations': dict(location_counter.most_common(10)),
            'regional_distribution': regions,
            'total_locations': len(location_counter),
            'most_affected_region': max(regions.items(), key=lambda x: x[1])[0]
        }

    def analyze_war_crimes_indicators(self, tweets: List[Dict]) -> Dict:
        """Analiza indicadores específicos de crímenes de guerra"""
        print("⚖️ Analizando indicadores de crímenes de guerra...")
        
        indicators = {
            'civilian_casualties': 0,
            'infrastructure_attacks': 0,
            'settlement_activities': 0,
            'humanitarian_violations': 0,
            'children_casualties': 0,
            'medical_attacks': 0,
            'education_attacks': 0,
            'religious_site_attacks': 0
        }
        
        civilian_keywords = ['civilians killed', 'children killed', 'family killed', 'killed', 'dead']
        infrastructure_keywords = ['hospital bombed', 'school destroyed', 'mosque damaged', 'bombing', 'airstrike']
        settlement_keywords = ['illegal settlement', 'home demolition', 'settlers attack']
        humanitarian_keywords = ['siege', 'blockade', 'collective punishment', 'humanitarian crisis']
        
        for tweet in tweets:
            keywords = tweet.get('keywords_detected', [])
            text_lower = tweet.get('text', '').lower()
            
            # Víctimas civiles
            if any(kw in keywords for kw in civilian_keywords):
                indicators['civilian_casualties'] += 1
            
            # Ataques a infraestructura
            if any(kw in keywords for kw in infrastructure_keywords):
                indicators['infrastructure_attacks'] += 1
            
            # Actividades de asentamientos
            if any(kw in keywords for kw in settlement_keywords):
                indicators['settlement_activities'] += 1
            
            # Violaciones humanitarias
            if any(kw in keywords for kw in humanitarian_keywords):
                indicators['humanitarian_violations'] += 1
            
            # Específicos
            if 'children' in text_lower and any(word in text_lower for word in ['killed', 'dead', 'wounded']):
                indicators['children_casualties'] += 1
            
            if 'hospital' in text_lower and any(word in text_lower for word in ['bombed', 'attacked', 'destroyed']):
                indicators['medical_attacks'] += 1
            
            if 'school' in text_lower and any(word in text_lower for word in ['bombed', 'destroyed', 'damaged']):
                indicators['education_attacks'] += 1
            
            if any(site in text_lower for site in ['mosque', 'church', 'religious']) and any(word in text_lower for word in ['bombed', 'attacked', 'destroyed']):
                indicators['religious_site_attacks'] += 1
        
        # Calcular severidad
        total_violations = sum(indicators.values())
        severity_score = min(100, (total_violations / max(len(tweets), 1)) * 1000)
        
        return {
            'indicators': indicators,
            'total_violations': total_violations,
            'severity_score': round(severity_score, 1),
            'severity_level': 'EXTREME' if severity_score > 80 else 'HIGH' if severity_score > 60 else 'MEDIUM' if severity_score > 40 else 'LOW',
            'violations_per_thousand_tweets': round((total_violations / max(len(tweets), 1)) * 1000, 2)
        }

    def select_representative_examples(self, tweets: List[Dict]) -> Dict:
        """Selecciona ejemplos representativos de cada categoría"""
        print("📝 Seleccionando ejemplos representativos...")
        
        examples = {
            'most_critical': [],
            'civilian_casualties': [],
            'infrastructure_attacks': [],
            'war_crimes': [],
            'high_engagement': []
        }
        
        # Tweets más críticos (relevance score alto + crítico)
        critical_tweets = [t for t in tweets if t.get('is_critical') and t.get('relevance_score', 0) > 85]
        critical_tweets.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
        examples['most_critical'] = [self.format_example_tweet(t) for t in critical_tweets[:5]]
        
        # Víctimas civiles
        civilian_tweets = [t for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['civilians killed', 'children killed', 'family killed'])]
        examples['civilian_casualties'] = [self.format_example_tweet(t) for t in civilian_tweets[:3]]
        
        # Ataques a infraestructura
        infrastructure_tweets = [t for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['hospital bombed', 'school destroyed', 'bombing'])]
        examples['infrastructure_attacks'] = [self.format_example_tweet(t) for t in infrastructure_tweets[:3]]
        
        # Crímenes de guerra
        war_crime_tweets = [t for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['war crime', 'genocide', 'ethnic cleansing'])]
        examples['war_crimes'] = [self.format_example_tweet(t) for t in war_crime_tweets[:3]]
        
        # Alto engagement
        engagement_tweets = sorted(tweets, key=lambda x: x.get('metrics', {}).get('retweet_count', 0) + x.get('metrics', {}).get('like_count', 0), reverse=True)
        examples['high_engagement'] = [self.format_example_tweet(t) for t in engagement_tweets[:3]]
        
        return examples

    def format_example_tweet(self, tweet: Dict) -> Dict:
        """Formatea un tweet de ejemplo"""
        return {
            'text': tweet.get('text', '')[:200] + '...' if len(tweet.get('text', '')) > 200 else tweet.get('text', ''),
            'location': tweet.get('location', 'Unknown'),
            'relevance_score': tweet.get('relevance_score', 0),
            'is_critical': tweet.get('is_critical', False),
            'keywords': tweet.get('keywords_detected', [])[:3],  # Solo primeras 3
            'engagement': {
                'retweets': tweet.get('metrics', {}).get('retweet_count', 0),
                'likes': tweet.get('metrics', {}).get('like_count', 0)
            }
        }

def main():
    """Función principal"""
    processor = PalestineTweetsProcessor()
    output_file = processor.process_latest_tweets()
    
    if output_file:
        print("\n🏆 PROCESAMIENTO COMPLETADO:")
        print(f"   📄 Archivo generado: {output_file}")
        print(f"   🎯 Listo para dashboard optimizado")
        print("   ⚡ Carga ultra-rápida garantizada")
        print("\n👑 ¡GLORIA A LA EFICIENCIA SUPREMA DE DOOM!")
    else:
        print("\n❌ PROCESAMIENTO FALLÓ")

if __name__ == "__main__":
    main()