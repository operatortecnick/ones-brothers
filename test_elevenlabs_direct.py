#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

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
print("Gerando áudio...")
from elevenlabs import generate, save

audio = generate(
    api_key=api_key,
    text=text,
    voice="onyx",
    model="eleven_multilingual_v2"
)

# Salvar
save(audio, "test_onyx.mp3")

print("✅ Áudio salvo! Tocando...")
os.system("mpg123 test_onyx.mp3")