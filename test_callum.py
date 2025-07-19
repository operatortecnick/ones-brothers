#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()
client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))

text = "E aí, desgraça! Acordou pra mais um dia nesse hospício chamado Brasil? Bolsonaro de tornozeleira, Lula bebendo cachaça, e você aí comendo mortadela com bafo de onça. Pelo menos o circo tá completo!"

print("🎤 Testando voz CALLUM (grave e perturbadora)...")

try:
    audio_stream = client.text_to_speech.convert(
        voice_id="N2lVS1w4EtoT3dr4eOWO",  # Callum
        text=text,
        model_id="eleven_multilingual_v2"
    )
    
    with open("test_callum.mp3", "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    
    print("✅ Tocando...")
    os.system("mpg123 test_callum.mp3")
    
except Exception as e:
    print(f"❌ Erro: {e}")