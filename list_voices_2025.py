#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

# Carregar .env
load_dotenv()

# Criar cliente
client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))

print("🎙️ VOZES DISPONÍVEIS NA ELEVENLABS EM 2025:")
print("=" * 60)

try:
    # Listar vozes
    voices = client.voices.get_all()
    
    for voice in voices.voices:
        print(f"\nID: {voice.voice_id}")
        print(f"Nome: {voice.name}")
        if hasattr(voice, 'description'):
            print(f"Descrição: {voice.description}")
        if hasattr(voice, 'labels'):
            print(f"Labels: {voice.labels}")
        print("-" * 40)
        
except Exception as e:
    print(f"❌ Erro: {e}")
    print("\nTentando método alternativo...")
    
    # Tentar outro método
    try:
        response = client.voices.list()
        print(response)
    except Exception as e2:
        print(f"❌ Erro 2: {e2}")