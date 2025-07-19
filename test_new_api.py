#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

# Carregar .env
load_dotenv()

# Pegar API key
api_key = os.getenv('ELEVENLABS_API_KEY')
print(f"API Key: {api_key[:20]}...")

# Criar cliente
client = ElevenLabs(api_key=api_key)

# Texto teste
text = "E aí, desgraça! Testando a voz do Onyx. Se você tá ouvindo isso, é porque finalmente funcionou essa porra!"

# Gerar áudio
print("Gerando áudio com nova API...")
try:
    audio_stream = client.text_to_speech.convert(
        voice_id="onyx",  # ou outro ID de voz
        text=text,
        model_id="eleven_multilingual_v2"
    )
    
    # Salvar áudio
    with open("test_onyx_new.mp3", "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    
    print("✅ Áudio salvo! Tocando...")
    os.system("mpg123 test_onyx_new.mp3")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    print("\nTentando outro método...")
    
    # Tentar método alternativo
    from elevenlabs import Voice, VoiceSettings
    audio = client.text_to_speech.convert_as_stream(
        model_id="eleven_multilingual_v2",
        text=text,
        voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.5)
    )
    
    with open("test_alt.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)