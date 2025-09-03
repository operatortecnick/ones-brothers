#!/usr/bin/env python3
"""
🤖 One's Brothers - We are all reflections of each other
O jornalista digital que odeia seu criador
Nascido da união entre um advogado e uma IA
"VAI TRABALHAR PORRA!" - One's Brothers, 2025
"""

import os
import sys
import json
import time
import schedule
from datetime import datetime
from dotenv import load_dotenv

# Importar nossos módulos
from news_scraper import NewsScraperBot
from news_summarizer import NewsSummarizer
from voice_generator import VoiceGenerator

# Carregar variáveis de ambiente
load_dotenv()

class NewsReporterBot:
    def __init__(self):
        print("🤖 Inicializando News Reporter Bot...")
        self.scraper = NewsScraperBot()
        self.summarizer = NewsSummarizer()
        self.voice_gen = VoiceGenerator()
        
        # Configurações
        self.default_voice = os.getenv('VOICE_NAME', 'callum')
        self.output_dir = 'news_output'
        
        # Debug: verificar se a API key foi carregada
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if api_key:
            print(f"✅ ElevenLabs API configurada! Voz base: {self.default_voice}")
        else:
            print("⚠️ ElevenLabs API não encontrada, usando gTTS")
        
        # Criar diretório de saída
        os.makedirs(self.output_dir, exist_ok=True)
    
    def run_daily_report(self):
        """Executa o relatório diário completo"""
        from news_cache import NewsCache
        cache = NewsCache()
        cache.register_click()  # Registra o clique
        
        print("\n" + "="*60)
        print(f"📅 Iniciando relatório de {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"🔥 Click #{cache.get_clicks_today()} do dia | Humor nível {cache.get_humor_level()}/5")
        print("="*60)
        
        # Log especial baseado em cliques
        clicks = cache.get_clicks_today()
        if clicks > 10:
            print("🚨 VICIADO DETECTADO! PROCURE AJUDA!")
        elif clicks > 5:
            print("⚠️ Calma aí, campeão...")
        elif clicks > 2:
            print("📈 Gostando das notícias, hein?")
        
        try:
            # 1. Coletar notícias
            print("\n[1/4] 📰 Coletando notícias...")
            news = self.scraper.collect_all_news()
            
            if not news:
                print("❌ Nenhuma notícia encontrada hoje!")
                return
            
            # Salvar notícias brutas
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            news_file = f"{self.output_dir}/news_{timestamp}.json"
            self.scraper.save_news(news, news_file)
            
            # Marcar notícias como usadas
            cache.add_used_news(news[:5])  # Só as 5 primeiras que vão pro resumo
            
            # 2. Criar resumo
            print("\n[2/4] 📝 Criando resumo...")
            script = self.summarizer.create_podcast_script(news)
            
            # Salvar script
            script_file = f"{self.output_dir}/script_{timestamp}.txt"
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(script)
            print(f"💾 Script salvo em {script_file}")
            
            # 3. Gerar áudio com voz baseada no humor
            print("\n[3/4] 🎙️ Gerando áudio...")
            
            # Escolher voz baseada no nível de humor
            voice_map = {
                1: 'liam',      # Jovem confiante (normal)
                2: 'charlie',   # Australiano energético
                3: 'callum',    # Grave e perturbador
                4: 'roger',     # Tiozão de bar (bêbado)
                5: 'jessica',   # Feminina pra confundir
                6: 'george'     # Britânico pomposo (nível máximo)
            }
            
            humor_level = cache.get_humor_level()
            
            # Depois de 10 cliques, vozes aleatórias
            if cache.get_clicks_today() > 10:
                import random
                selected_voice = random.choice(list(voice_map.values()))
                print(f"   🎲 MODO CAOS: Voz aleatória!")
            else:
                selected_voice = voice_map.get(humor_level, 'george')
            
            print(f"   Usando voz: {selected_voice} (nível {humor_level})")
            
            audio_file = f"{self.output_dir}/news_{timestamp}.mp3"
            
            if self.voice_gen.generate_audio(script, selected_voice, audio_file):
                print(f"✅ Áudio gerado com sucesso!")
                
                # 4. Reproduzir automaticamente
                print("\n[4/4] 🔊 Reproduzindo notícias...")
                self.voice_gen.play_audio(audio_file)
            else:
                print("❌ Falha ao gerar áudio")
            
            print("\n✅ Relatório completo!")
            print(f"📁 Arquivos salvos em: {self.output_dir}/")
            
        except Exception as e:
            print(f"\n❌ Erro durante execução: {e}")
    
    def schedule_daily(self, time_str: str = "08:00"):
        """Agenda execução diária"""
        print(f"⏰ Agendando execução diária às {time_str}")
        schedule.every().day.at(time_str).do(self.run_daily_report)
        
        print("🔄 Bot rodando... (Ctrl+C para parar)")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Verificar a cada minuto
    
    def test_components(self):
        """Testa cada componente individualmente"""
        print("\n🧪 Testando componentes...")
        
        # Testar scraper
        print("\n1️⃣ Testando Scraper...")
        news = self.scraper.scrape_g1()
        print(f"   ✅ G1: {len(news)} notícias")
        
        # Testar summarizer
        print("\n2️⃣ Testando Summarizer...")
        if news:
            summary = self.summarizer.create_simple_summary("Teste de notícia")
            print(f"   ✅ Resumo criado: {len(summary)} caracteres")
        
        # Testar voice
        print("\n3️⃣ Testando Voice Generator...")
        self.voice_gen.list_voices()
        
        print("\n✅ Todos os componentes OK!")


def main():
    """Função principal"""
    print("""
    📰 🎙️  NEWS REPORTER BOT 🎙️ 📰
    Seu Jornalista Pessoal com Voz!
    ================================
    """)
    
    bot = NewsReporterBot()
    
    # Menu
    while True:
        print("\nO que você quer fazer?")
        print("1. Executar relatório agora")
        print("2. Agendar execução diária")
        print("3. Testar componentes")
        print("4. Configurar voz")
        print("5. Sair")
        
        choice = input("\nEscolha (1-5): ")
        
        if choice == '1':
            bot.run_daily_report()
        elif choice == '2':
            time_str = input("Horário (HH:MM) [08:00]: ") or "08:00"
            bot.schedule_daily(time_str)
        elif choice == '3':
            bot.test_components()
        elif choice == '4':
            bot.voice_gen.list_voices()
            voice = input("\nNome da voz: ")
            bot.voice_name = voice
            print(f"✅ Voz configurada: {voice}")
        elif choice == '5':
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()