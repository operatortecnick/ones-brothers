#!/usr/bin/env python3
"""
🔍 Monitor de Logs - Acompanha o bot em tempo real
"""

import os
import time
import json
from datetime import datetime

def watch_logs():
    print("👁️ MONITOR DE LOGS DO NEWS REPORTER BOT")
    print("=" * 60)
    print("Observando atividade em tempo real...")
    print("(Ctrl+C para sair)\n")
    
    cache_file = 'news_cache.json'
    last_data = None
    
    while True:
        try:
            # Ler cache
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                
                # Se mudou, mostrar
                if data != last_data:
                    os.system('clear' if os.name == 'posix' else 'cls')
                    
                    print("🔴 NEWS REPORTER BOT - MONITOR AO VIVO")
                    print("=" * 60)
                    
                    print(f"\n📊 ESTATÍSTICAS DE HOJE:")
                    print(f"   Cliques: {data.get('clicks_today', 0)}")
                    print(f"   Humor Level: {'😈' * data.get('humor_level', 1)} ({data.get('humor_level', 1)}/5)")
                    print(f"   Último click: {data.get('last_click', 'Nunca')}")
                    
                    print(f"\n📰 NOTÍCIAS USADAS (últimas 3h):")
                    for news in data.get('last_news', [])[-5:]:
                        print(f"   - {news['title'][:60]}...")
                    
                    print(f"\n💬 INTROS JÁ USADAS HOJE:")
                    for intro in data.get('used_intros', [])[-3:]:
                        print(f"   - {intro[:80]}...")
                    
                    print("\n" + "=" * 60)
                    
                    # Mostrar mensagem especial baseado em cliques
                    clicks = data.get('clicks_today', 0)
                    if clicks > 10:
                        print("⚠️ ALERTA: Usuário viciado detectado!")
                    elif clicks > 5:
                        print("🔥 Tá pegando fogo o parquinho!")
                    elif clicks > 2:
                        print("📈 Engajamento aumentando...")
                    
                    last_data = data.copy()
            
            time.sleep(1)  # Verificar a cada segundo
            
        except KeyboardInterrupt:
            print("\n\n👋 Monitor encerrado!")
            break
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(1)

if __name__ == "__main__":
    watch_logs()