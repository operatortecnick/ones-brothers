import os
from typing import Optional
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Tentar importar ElevenLabs (nova API)
try:
    from elevenlabs import VoiceSettings
    from elevenlabs.client import ElevenLabs
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False
    print("⚠️ ElevenLabs não disponível. Usando gTTS como fallback.")

class VoiceGenerator:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
        if self.api_key and ELEVENLABS_AVAILABLE:
            print(f"🎤 ElevenLabs inicializado com sucesso!")
            self.client = ElevenLabs(api_key=self.api_key)
        else:
            print(f"⚠️ ElevenLabs não inicializado. API key: {'SIM' if self.api_key else 'NÃO'}, Available: {ELEVENLABS_AVAILABLE}")
            self.client = None
        
        # Vozes disponíveis (você pode listar mais com voices())
        self.available_voices = {
            'rachel': 'Rachel - Voz feminina calma',
            'antoni': 'Antoni - Voz masculina profissional',
            'bella': 'Bella - Voz feminina jovem',
            'josh': 'Josh - Voz masculina jovem',
            'arnold': 'Arnold - Voz masculina grave'
        }
    
    def list_voices(self):
        """Lista todas as vozes disponíveis"""
        if not self.api_key or not self.client:
            print("❌ API key da ElevenLabs não configurada!")
            print("💡 Usando voz gTTS (português brasileiro)")
            return
        
        try:
            print("🎙️ Vozes pré-configuradas:")
            print("=" * 50)
            for voice_id, description in self.available_voices.items():
                print(f"- {voice_id}: {description}")
        except Exception as e:
            print(f"❌ Erro ao listar vozes: {e}")
    
    def generate_audio(self, text: str, voice_name: str = "antoni", output_file: str = "news_audio.mp3") -> bool:
        """Gera áudio a partir do texto"""
        if not self.api_key or not self.client:
            print("💡 Usando voz local gTTS...")
            return self.generate_local_audio(text, output_file)
        
        try:
            print(f"🎙️ Gerando áudio com ElevenLabs ({voice_name})...")
            
            # Nova API da ElevenLabs (2025)
            voice_id = voice_name  # Pode ser ID ou nome
            
            # IDs das vozes mais fodas
            voice_map = {
                'callum': 'N2lVS1w4EtoT3dr4eOWO',  # Grave e perturbador
                'charlie': 'IKne3meq5aSn9XLyUdCD',  # Australiano energético
                'roger': 'bIHbv24MWmeRgasZH58o',  # Conversacional/tiozão
                'liam': 'TX3LPaxmHKxFdv7VOQHJ',  # Jovem confiante
                'eric': 'cjVigY5qzO86Huf0OWal',  # Smooth tenor
                'jessica': 'cgSgspJ2msm6clMCkdW9',  # Feminina jovem
                'giovanni': 'iP95p4xoKVk53GoZ742B',  # Italiano (tipo Chaves?)
                'george': 'JBFqnCBsd6RMkjVDRZzb'  # Britânico pomposo
            }
            
            # Usar ID se fornecido no mapa
            if voice_name.lower() in voice_map:
                voice_id = voice_map[voice_name.lower()]
            
            audio_stream = self.client.text_to_speech.convert(
                voice_id=voice_id,
                text=text,
                model_id="eleven_multilingual_v2"
            )
            
            # Salvar arquivo
            with open(output_file, 'wb') as f:
                for chunk in audio_stream:
                    f.write(chunk)
            
            print(f"✅ Áudio salvo em: {output_file}")
            return True
            
        except Exception as e:
            print(f"❌ Erro com ElevenLabs: {e}")
            print("💡 Tentando com gTTS...")
            return self.generate_local_audio(text, output_file)
    
    def generate_local_audio(self, text: str, output_file: str) -> bool:
        """Fallback: usa gTTS para gerar áudio local"""
        try:
            from gtts import gTTS
            
            print("🎙️ Gerando áudio com gTTS (voz local)...")
            tts = gTTS(text=text, lang='pt-br')
            tts.save(output_file)
            print(f"✅ Áudio salvo em: {output_file}")
            return True
            
        except ImportError:
            print("❌ gTTS não instalado. Execute: pip install gtts")
            return False
        except Exception as e:
            print(f"❌ Erro ao gerar áudio local: {e}")
            return False
    
    def play_audio(self, audio_file: str):
        """Reproduz o áudio gerado"""
        try:
            if os.path.exists(audio_file):
                print(f"🔊 Tocando suas notícias...")
                print("🎵 ♪ ♫ ♪ ♫ ♪ ♫")
                
                import platform
                system = platform.system()
                
                # Tentar vários players no Linux
                if system == 'Linux':
                    # Lista de players comuns no Linux
                    players = [
                        f'mpg123 "{audio_file}"',
                        f'ffplay -nodisp -autoexit "{audio_file}"',
                        f'cvlc --play-and-exit "{audio_file}"',
                        f'play "{audio_file}"',  # sox
                        f'mplayer "{audio_file}"',
                        f'xdg-open "{audio_file}"'  # Abre com player padrão
                    ]
                    
                    for player in players:
                        try:
                            result = os.system(player + " 2>/dev/null")
                            if result == 0:
                                print("\n✅ Reprodução concluída!")
                                return
                        except:
                            continue
                    
                    print("❌ Nenhum player de áudio encontrado!")
                    print("💡 Instale um destes: sudo apt install mpg123 ffmpeg vlc sox")
                    print(f"📁 Áudio salvo em: {audio_file}")
                    
                elif system == 'Darwin':  # macOS
                    os.system(f'afplay "{audio_file}"')
                    print("\n✅ Reprodução concluída!")
                    
                elif system == 'Windows':
                    os.system(f'start "{audio_file}"')
                    print("\n✅ Reprodução concluída!")
                    
            else:
                print(f"❌ Arquivo {audio_file} não encontrado!")
                
        except Exception as e:
            print(f"❌ Erro ao reproduzir áudio: {e}")
            print(f"📁 Mas o áudio foi salvo em: {audio_file}")


# Teste do gerador de voz
if __name__ == "__main__":
    # Carregar script
    try:
        with open('news_script.txt', 'r', encoding='utf-8') as f:
            script = f.read()
        
        generator = VoiceGenerator()
        
        # Listar vozes disponíveis
        generator.list_voices()
        
        # Gerar áudio
        print("\n🎙️ Gerando áudio do resumo de notícias...")
        if generator.generate_audio(script, voice_name="antoni"):
            generator.play_audio("news_audio.mp3")
        
    except FileNotFoundError:
        print("❌ Arquivo news_script.txt não encontrado! Execute news_summarizer.py primeiro.")