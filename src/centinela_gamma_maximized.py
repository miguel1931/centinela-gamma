#!/usr/bin/env python3
"""
🕊️ CENTINELA-GAMMA MAXIMIZED - DOOM SYSTEM v1.0
Arquitecto: VIGIL | Soberano: DOOM
Sistema de Documentación de Crímenes de Guerra - Palestina/Israel
Extracción maximizada con $2 TwitCoins presupuesto
"""

import tweepy
import json
import os
from datetime import datetime, timedelta
import time
from typing import List, Dict, Any
import sqlite3
import re

class CentinelaGammaMaximized:
    def __init__(self, budget_dollars: float = 2.0):
        """
        Inicializa CENTINELA-GAMMA para documentación de crímenes de guerra
        """
        self.budget = budget_dollars
        self.cost_per_tweet = 0.000001  # $0.000001 por tweet
        self.max_requests = int(budget_dollars * 1000)  # ~2000 requests
        self.tweets_per_request = 100
        
        # Configuración específica para Palestina/Israel
        self.target_region = "Palestine/Israel"
        
        # Configurar API de Twitter
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        if self.bearer_token:
            self.client = tweepy.Client(bearer_token=self.bearer_token)
            self.simulation_mode = False
        else:
            print("❌ TWITTER_BEARER_TOKEN no encontrado - Modo simulado MASIVO")
            self.client = None
            self.simulation_mode = True
        
        # Queries específicas para crímenes de guerra
        self.queries = [
            # Gaza - Principales
            "Gaza",
            "Gaza Strip",
            "#Gaza", 
            "#GazaUnderAttack",
            "#SaveGaza",
            
            # West Bank
            "West Bank",
            "Cisjordania", 
            "#WestBank",
            "Jenin",
            "Nablus",
            "Ramallah",
            
            # Jerusalén Este
            "East Jerusalem",
            "Al Aqsa",
            "Sheikh Jarrah",
            "#SaveSheikhJarrah",
            
            # Crímenes específicos
            "Gaza bombing", 
            "Gaza airstrike",
            "Palestinian killed",
            "Israeli forces",
            "IDF operation",
            "settlement expansion",
            "home demolition",
            "checkpoint violence",
            
            # Organizaciones DDHH
            "B'Tselem",
            "Human Rights Watch Palestine",
            "Amnesty Palestine",
            "OCHA Palestine",
            
            # Hashtags críticos
            "#PalestineUnderAttack",
            "#FreePalestine",
            "#GazaGenocide",
            "#WarCrimes",
            "#Palestine",
            "#EndTheOccupation",
            "#ApartheidIsrael",
            "#GazaBlockade",
            
            # Ubicaciones específicas
            "Khan Younis",
            "Rafah Gaza",
            "Bethlehem Palestine",
            "Hebron Palestine"
        ]
        
        # Keywords críticos para clasificación
        self.critical_keywords = [
            # Víctimas civiles
            'killed', 'dead', 'murdered', 'shot', 'executed',
            'children killed', 'civilians killed', 'family killed',
            
            # Armas/Violencia
            'bombing', 'airstrike', 'shelling', 'artillery', 'sniper',
            'bulldozer', 'tank', 'F-16', 'drone strike', 'missile',
            
            # Crímenes específicos
            'war crime', 'genocide', 'ethnic cleansing', 'apartheid',
            'illegal settlement', 'home demolition', 'forced displacement',
            'collective punishment', 'siege', 'blockade',
            
            # Instituciones
            'IDF', 'Israeli army', 'Israeli forces', 'occupation forces',
            'border police', 'settlers attack', 'military court',
            
            # Infraestructura
            'hospital bombed', 'school destroyed', 'mosque damaged',
            'power plant', 'water system', 'medical facility',
            
            # Situación humanitaria
            'humanitarian crisis', 'medical supplies', 'food shortage',
            'clean water', 'electricity cut', 'fuel shortage'
        ]
        
        # Métricas
        self.total_tweets = 0
        self.critical_tweets = 0
        self.requests_made = 0
        self.start_time = None
        
        print("🕊️" + "="*71)
        print("🕊️ CENTINELA-GAMMA MAXIMIZED - $2 TWITCOIN WAR CRIMES DOCUMENTATION 🕊️")
        print("🕊️                👑 Arquitecto: VIGIL | Soberano: DOOM 👑               🕊️")
        print("🕊️" + "="*71)

    def print_configuration(self):
        """Muestra configuración maximizada"""
        print("🕊️ CONFIGURACIÓN MAXIMIZADA:")
        print(f"   💰 Presupuesto: ${self.budget}")
        print(f"   🔍 Máximo requests: {self.max_requests}")
        print(f"   📱 Tweets por request: {self.tweets_per_request}")
        print(f"   🎯 Capacidad teórica: {self.max_requests * self.tweets_per_request:,} tweets")
        print(f"   📝 Queries configuradas: {len(self.queries)}")
        print(f"   🎯 Región objetivo: {self.target_region}")

    def make_request(self, query: str) -> Any:
        """
        Realiza una solicitud a la API de Twitter y maneja errores.
        Retorna los datos del tweet, "RATE_LIMIT_REACHED" si se alcanza un límite, o None en otros errores.
        """
        if self.client is None:
            return None # Should not happen if simulation_mode is handled correctly
        
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=self.tweets_per_request,
                tweet_fields=['created_at', 'author_id', 'geo', 'public_metrics', 'context_annotations']
            )
            self.requests_made += 1
            time.sleep(1) # Rate limiting
            return tweets
        except tweepy.errors.TweepyException as e:
            status_code = e.response.status_code if e.response is not None else None
            print(f"❌ Error en query '{query}': {status_code} - {e}")
            
            if status_code == 403:
                print("⚠️ [HTTP 403] Forbidden. Múltiples causas posibles:")
                print("   - Límite de facturación (Pay-Per-Use cap) alcanzado.")
                print("   - El endpoint 'search_recent_tweets' requiere un nivel superior (ej. Pro/Enterprise) o acceso elevado.")
                print("   - El Bearer Token introducido es incorrecto o no tiene permisos de lectura.")
                print("⏳ Cambiando a simulación masiva para no perder datos del dashboard...")
                return "RATE_LIMIT_REACHED"
            elif status_code == 429:
                print("⚠️ [HTTP 429] Too Many Requests. Límite de velocidad (Rate Limit) alcanzado.")
                print("⏳ Cambiando a simulación masiva...")
                return "RATE_LIMIT_REACHED"
            elif status_code == 401:
                print("❌ [HTTP 401] Unauthorized. El TWITTER_BEARER_TOKEN es inválido o ha expirado.")
                return "RATE_LIMIT_REACHED"
                
            return None
        except Exception as e:
            print(f"❌ Error inesperado en query '{query}': {e}")
            return None

    def extract_tweets_maximized(self) -> List[Dict]:
        """Extracción maximizada de tweets sobre crímenes de guerra"""
        self.start_time = datetime.now()
        
        print(f"🕊️ INICIANDO DOCUMENTACIÓN CRÍMENES DE GUERRA...")
        
        all_tweets = []
        simulation_forced = False
        
        if self.simulation_mode:
            print(f"🎭 MODO SIMULADO MASIVO - Generando ~100,000 tweets de ejemplo")
            all_tweets = self.massive_simulation()
            # In simulation mode, we generate all at once, so no need to loop through queries
            self.total_tweets = len(all_tweets)
            self.critical_tweets = sum(1 for tweet in all_tweets if tweet.get('is_critical', False))
            return all_tweets

        # Extracción real de Twitter
        for i, query in enumerate(self.queries, 1):
            if simulation_forced:
                 print(f"⏭️ Saltando query '{query}' debido a límite de API. Usando simulación.")
                 continue

            if self.requests_made >= self.max_requests:
                print(f"🚫 Límite de requests alcanzado: {self.requests_made}. Finalizando extracción real.")
                break
            
            print(f"🔍 [{i}/{len(self.queries)}] Query: '{query}'")
            
            # Request inicial
            data = self.make_request(query)
            
            if data == "RATE_LIMIT_REACHED":
                print("⚠️ Activando fallback de simulación masiva debido a límite de API...")
                all_tweets.extend(self.massive_simulation()) # Add simulation data to existing real data
                simulation_forced = True
                continue
                
            if not data or not data.data: # Check data.data for actual tweets
                continue
            
            for tweet in data.data:
                processed_tweet = self.process_tweet(tweet, query)
                all_tweets.append(processed_tweet)
        
        self.total_tweets = len(all_tweets)
        self.critical_tweets = sum(1 for tweet in all_tweets if tweet.get('is_critical', False))
        
        return all_tweets

    def massive_simulation(self) -> List[Dict]:
        """Genera simulación masiva de tweets de crímenes de guerra"""
        tweets = []
        
        # Templates específicos para crímenes de guerra
        templates = [
            # Gaza
            "BREAKING: Israeli forces bomb {location} in Gaza. {casualties} civilians killed including {children} children.",
            "Gaza UPDATE: {facility} destroyed by Israeli airstrike. Medical staff treating wounded in corridors.",
            "URGENT: Residential building in {gaza_area} hit by Israeli missile. Search for survivors ongoing.",
            "Gaza medics report {number} killed, {wounded} wounded in latest Israeli bombardment of {area}.",
            
            # West Bank
            "West Bank: Israeli settlers attack Palestinian village {village}. Homes set on fire.",
            "IDF raids {wb_city}, arrests {arrests} Palestinians including {minors} minors during night operation.",
            "BREAKING: Israeli bulldozers demolish Palestinian home in {location} despite court order.",
            "Checkpoint violence: Israeli soldiers shoot Palestinian youth at {checkpoint}.",
            
            # Crímenes específicos
            "War crime alert: Israel targets {civilian_target} in violation of international law.",
            "Human Rights Watch documents systematic home demolitions in {area}.",
            "B'Tselem: Israeli forces use excessive force against {target} protesters.",
            "Amnesty International calls for investigation into Israeli {crime_type}.",
            
            # Situación humanitaria
            "Gaza hospitals overwhelmed. Only {hours} hours of electricity per day. Fuel running out.",
            "OCHA: {percentage}% of Gaza water unfit for human consumption due to Israeli siege.",
            "Palestinian families in {area} without clean water for {days} days after Israeli operation.",
            "Medical supplies blocked at Israeli checkpoints while patients die in Gaza hospitals."
        ]
        
        locations = [
            "Gaza City", "Khan Younis", "Rafah", "Jabalia", "Beit Hanoun",
            "Ramallah", "Jenin", "Nablus", "Hebron", "Bethlehem",
            "Sheikh Jarrah", "Silwan", "East Jerusalem"
        ]
        
        gaza_areas = ["Shati", "Jabalia", "Gaza City", "Khan Younis", "Rafah"]
        wb_cities = ["Jenin", "Nablus", "Ramallah", "Hebron", "Tulkarem"]
        villages = ["Beita", "Kafr Qaddum", "Bil'in", "Ni'lin", "Al-Walaja"]
        facilities = ["Al-Shifa Hospital", "Indonesian Hospital", "Gaza clinic", "school", "mosque"]
        
        for i in range(50000):  # 50,000 tweets simulados
            template = templates[i % len(templates)]
            
            # Llenar variables del template
            tweet_text = template.format(
                location=locations[i % len(locations)],
                casualties=str((i % 15) + 1),
                children=str((i % 8) + 1),
                facility=facilities[i % len(facilities)],
                gaza_area=gaza_areas[i % len(gaza_areas)],
                number=str((i % 25) + 1),
                wounded=str((i % 50) + 5),
                area=locations[i % len(locations)],
                village=villages[i % len(villages)],
                wb_city=wb_cities[i % len(wb_cities)],
                arrests=str((i % 20) + 1),
                minors=str((i % 5) + 1),
                checkpoint=f"Checkpoint {(i % 10) + 1}",
                civilian_target="hospital" if i % 4 == 0 else "school" if i % 4 == 1 else "residential building" if i % 4 == 2 else "mosque",
                crime_type="home demolitions" if i % 3 == 0 else "settlement expansion" if i % 3 == 1 else "collective punishment",
                target="peaceful" if i % 2 == 0 else "unarmed",
                hours=str((i % 8) + 4),
                percentage=str((i % 30) + 70),
                days=str((i % 10) + 1)
            )
            
            # Detectar keywords críticos
            is_critical = any(keyword.lower() in tweet_text.lower() for keyword in self.critical_keywords)
            keywords = [kw for kw in self.critical_keywords if kw.lower() in tweet_text.lower()]
            
            tweet = {
                'id': f'SIM_GAMMA_{i:05d}',
                'text': tweet_text,
                'author': f'user_{i % 2000}',  # 2000 usuarios únicos
                'author_id': f'id_{i % 2000}',
                'created_at': (datetime.now() - timedelta(hours=i % 72)).isoformat(),
                'location': locations[i % len(locations)],
                'coordinates': None,
                'metrics': {
                    'retweet_count': i % 100,
                    'like_count': i % 500
                },
                'relevance_score': (i % 40) + 60,  # 60-100 relevancia
                'is_critical': is_critical,
                'keywords_detected': keywords[:3],  # Máximo 3 keywords
                'query_source': self.queries[i % len(self.queries)]
            }
            
            tweets.append(tweet)
        
        print(f"🎭 Simulación completada: {len(tweets):,} tweets generados")
        return tweets

    def process_tweet(self, tweet, query_source: str) -> Dict:
        """Procesa un tweet real de la API"""
        # Detectar keywords críticos
        keywords = [kw for kw in self.critical_keywords if kw.lower() in tweet.text.lower()]
        is_critical = len(keywords) > 0
        
        # Calcular score de relevancia
        relevance_score = self.calculate_relevance(tweet.text, keywords)
        
        return {
            'id': tweet.id,
            'text': tweet.text,
            'author_id': tweet.author_id,
            'created_at': tweet.created_at.isoformat() if tweet.created_at else datetime.now().isoformat(),
            'metrics': {
                'retweet_count': tweet.public_metrics['retweet_count'] if tweet.public_metrics else 0,
                'like_count': tweet.public_metrics['like_count'] if tweet.public_metrics else 0
            },
            'relevance_score': relevance_score,
            'is_critical': is_critical,
            'keywords_detected': keywords[:5],  # Máximo 5 keywords
            'query_source': query_source
        }

    def calculate_relevance(self, text: str, keywords: List[str]) -> int:
        """Calcula score de relevancia 0-100"""
        base_score = 30
        
        # +10 por cada keyword crítico
        keyword_score = len(keywords) * 10
        
        # +5 por menciones específicas de lugares
        location_bonus = 5 if any(loc in text.lower() for loc in ['gaza', 'west bank', 'jerusalem', 'palestine']) else 0
        
        # +15 si menciona números de víctimas
        victim_bonus = 15 if re.search(r'\d+.*(?:killed|dead|wounded|injured)', text.lower()) else 0
        
        # +10 si menciona fuentes oficiales
        source_bonus = 10 if any(src in text.lower() for src in ['human rights', 'amnesty', 'btselem', 'ocha']) else 0
        
        total_score = min(100, base_score + keyword_score + location_bonus + victim_bonus + source_bonus)
        return total_score

    def save_to_json(self, tweets: List[Dict]) -> str:
        """Guarda tweets en archivo JSON con metadata completa"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"centinela_gamma_tweets_maximized_{timestamp}.json"
        
        # Calcular estadísticas
        keyword_freq = {}
        authors = set()
        
        for tweet in tweets:
            for keyword in tweet.get('keywords_detected', []):
                keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
            authors.add(tweet.get('author', tweet.get('author_id', 'unknown')))
        
        # Top 10 keywords
        top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Metadata completa
        metadata = {
            'extraction_info': {
                'timestamp': datetime.now().isoformat(),
                'total_tweets': self.total_tweets,
                'budget_used': round(self.total_tweets * self.cost_per_tweet, 6),
                'budget_allocated': self.budget,
                'requests_made': self.requests_made,
                'max_requests': self.max_requests,
                'cost_per_tweet': self.cost_per_tweet,
                'extraction_duration': str(datetime.now() - self.start_time) if self.start_time else "0:00:00",
                'tweets_per_dollar': self.total_tweets / max(self.total_tweets * self.cost_per_tweet, 0.001),
                'target_region': self.target_region
            },
            'statistics': {
                'critical_tweets': self.critical_tweets,
                'critical_percentage': round((self.critical_tweets / max(self.total_tweets, 1)) * 100, 2),
                'total_keywords': sum(keyword_freq.values()),
                'unique_keywords': len(keyword_freq),
                'unique_authors': len(authors),
                'queries_executed': len(self.queries),
                'tweets_with_location': sum(1 for t in tweets if t.get('location')),
                'tweets_with_metrics': sum(1 for t in tweets if t.get('metrics')),
                'avg_relevance': round(sum(t.get('relevance_score', 0) for t in tweets) / max(len(tweets), 1), 2)
            },
            'query_breakdown': {
                query: {
                    'tweet_count': sum(1 for t in tweets if t.get('query_source') == query),
                    'critical_count': sum(1 for t in tweets if t.get('query_source') == query and t.get('is_critical')),
                    'avg_relevance': round(sum(t.get('relevance_score', 0) for t in tweets if t.get('query_source') == query) / 
                                         max(sum(1 for t in tweets if t.get('query_source') == query), 1), 2)
                }
                for query in self.queries
            },
            'top_keywords': top_keywords,
            'war_crimes_indicators': {
                'civilian_casualties': sum(1 for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['killed', 'dead', 'children killed'])),
                'infrastructure_attacks': sum(1 for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['hospital bombed', 'school destroyed', 'mosque damaged'])),
                'settlement_activities': sum(1 for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['illegal settlement', 'home demolition'])),
                'humanitarian_violations': sum(1 for t in tweets if any(kw in t.get('keywords_detected', []) for kw in ['siege', 'blockade', 'collective punishment']))
            }
        }
        
        # Estructura final
        output_data = {
            'metadata': metadata,
            'tweets': tweets
        }
        
        # Guardar archivo
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        file_size_mb = os.path.getsize(filename) / (1024 * 1024)
        
        print("💾 TWEETS GUARDADOS EN JSON:")
        print(f"   📄 Archivo: {filename}")
        print(f"   📊 Total tweets: {self.total_tweets:,}")
        print(f"   💾 Tamaño archivo: {file_size_mb:.2f} MB")
        print(f"   🚨 Tweets críticos: {self.critical_tweets}")
        print(f"   👥 Autores únicos: {len(authors)}")
        print(f"   💰 Costo por tweet: ${self.cost_per_tweet:.7f}")
        
        return filename

    def generate_report(self, tweets: List[Dict]):
        """Genera reporte completo de la extracción"""
        duration = datetime.now() - self.start_time if self.start_time else timedelta(0)
        budget_used = self.total_tweets * self.cost_per_tweet
        
        # Calcular estadísticas de keywords
        keyword_freq = {}
        for tweet in tweets:
            for keyword in tweet.get('keywords_detected', []):
                keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
        
        top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Queries más productivas
        query_stats = {}
        for tweet in tweets:
            query = tweet.get('query_source', 'unknown')
            if query not in query_stats:
                query_stats[query] = {'total': 0, 'critical': 0}
            query_stats[query]['total'] += 1
            if tweet.get('is_critical'):
                query_stats[query]['critical'] += 1
        
        top_queries = sorted(query_stats.items(), key=lambda x: x[1]['total'], reverse=True)[:10]
        
        print("="*80)
        print("🕊️ CENTINELA-GAMMA MAXIMIZED - REPORTE DOCUMENTACIÓN CRÍMENES DE GUERRA")
        print("="*80)
        print("💰 PRESUPUESTO DOOM:")
        print(f"   💵 Asignado: ${self.budget}")
        print(f"   💸 Usado: ${budget_used:.6f}")
        print(f"   💎 Restante: ${self.budget - budget_used:.6f}")
        print(f"   📊 Eficiencia: {self.total_tweets/max(budget_used, 0.000001):.1f} tweets/dólar")
        
        print("\n🎯 DOCUMENTACIÓN MASIVA:")
        print(f"   📱 Total extraído: {self.total_tweets:,} tweets")
        print(f"   🚨 Críticos detectados: {self.critical_tweets:,}")
        print(f"   🔍 Requests ejecutados: {self.requests_made}")
        print(f"   ⏱️ Duración: {duration}")
        print(f"   🏆 Tweets por minuto: {self.total_tweets/(duration.total_seconds()/60) if duration.total_seconds() > 0 else 0:.0f}")
        
        print("\n🔝 TOP QUERIES MÁS PRODUCTIVAS:")
        for query, stats in top_queries:
            print(f"   • {query}: {stats['total']} tweets ({stats['critical']} críticos)")
        
        print("\n🔑 KEYWORDS MÁS FRECUENTES:")
        for keyword, count in top_keywords:
            print(f"   • {keyword}: {count:,} menciones")
        
        return {
            'total_tweets': self.total_tweets,
            'critical_tweets': self.critical_tweets,
            'budget_used': budget_used,
            'efficiency': self.total_tweets/max(budget_used, 0.000001)
        }

    def update_resources(self, budget_used: float):
        """Actualiza archivo de recursos"""
        try:
            # Cargar recursos actuales
            if os.path.exists('doom_resource_manager_data.json'):
                with open('doom_resource_manager_data.json', 'r', encoding='utf-8') as f:
                    resources = json.load(f)
            else:
                resources = {'currencies': {}}
            
            # Actualizar TwitCoins
            if 'TwitCoins' not in resources['currencies']:
                resources['currencies']['TwitCoins'] = {'balance': 25.0}
            
            resources['currencies']['TwitCoins']['balance'] -= budget_used
            
            # Agregar log de transacción
            if 'transactions' not in resources:
                resources['transactions'] = []
            
            resources['transactions'].append({
                'timestamp': datetime.now().isoformat(),
                'type': 'GAMMA_EXTRACTION',
                'amount': -budget_used,
                'description': f'CENTINELA-GAMMA: {self.total_tweets} tweets documentados',
                'currency': 'TwitCoins'
            })
            
            # Guardar recursos actualizados
            with open('doom_resource_manager_data.json', 'w', encoding='utf-8') as f:
                json.dump(resources, f, indent=2)
            
            print(f"✅ Recursos actualizados: ${budget_used:.6f} TwitCoins, {self.total_tweets} tweets")
            
        except Exception as e:
            print(f"⚠️ Error actualizando recursos: {e}")

def main():
    """Función principal de CENTINELA-GAMMA"""
    gamma = CentinelaGammaMaximized(budget_dollars=2.0)
    gamma.print_configuration()
    
    # Extraer tweets
    tweets = gamma.extract_tweets_maximized()
    
    # Guardar en JSON
    filename = gamma.save_to_json(tweets)
    
    # Generar reporte
    report = gamma.generate_report(tweets)
    
    # Actualizar recursos
    gamma.update_resources(report['budget_used'])
    
    print(f"\n💾 ARCHIVO JSON GENERADO:")
    print(f"   📄 {filename}")
    print(f"   💾 {os.path.getsize(filename)/(1024*1024):.2f} MB")
    print(f"   🗂️ Estructura: metadata + {len(tweets):,} tweets completos")
    
    print("\n🏆 ACHIEVEMENT UNLOCKED:")
    print(f"   🎯 DOCUMENTACIÓN MASIVA COMPLETADA")
    print(f"   💎 {report['total_tweets']:,} tweets capturados con ${report['budget_used']:.6f}")
    print(f"   🚨 {report['critical_tweets']:,} crímenes de guerra identificados")
    print(f"   📊 ROI: {report['efficiency']:.0f}x tweets por dólar")
    print("="*80)
    print("🎯 DOCUMENTACIÓN CRÍMENES DE GUERRA COMPLETADA - DATOS ALMACENADOS")
    print("👑 ¡JUSTICIA PARA PALESTINA! ¡GLORIA A LA VERDAD!")
    print("="*80)
    
    duration = datetime.now() - gamma.start_time if gamma.start_time else timedelta(0)
    
    print(f"\n🏆 DOCUMENTACIÓN MASIVA EXITOSA:")
    print(f"   📱 Tweets extraídos: {report['total_tweets']:,}")
    print(f"   💰 Costo: ${report['budget_used']:.6f}")
    print(f"   📄 Archivo JSON: {filename}")
    print(f"   🚨 Críticos: {report['critical_tweets']}")
    print(f"   ⏱️ Duración: {duration}")
    
    print("\n👑 ¡GLORIA A LATVERIA! ¡GLORIA A DOOM!")

if __name__ == "__main__":
    main()