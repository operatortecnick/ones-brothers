#!/usr/bin/env python3
"""
🎙️ Teste de Vozes ElevenLabs - Qual é a mais FODA?
"""

import os
from dotenv import load_dotenv

# Carregar .env
load_dotenv()

# Configurar API
from elevenlabs.client import ElevenLabs
client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))

def test_voices():
    # Texto de teste com humor pesado
    test_text = "E aí, desgraça! Acordou pra mais um dia nesse hospício chamado Brasil? Bolsonaro de tornozeleira, dólar nas alturas, e você aí pagando imposto. Pelo menos temos cachaça pra aguentar essa merda toda!"
    
    # Vozes populares da ElevenLabs
    voices = {
        'adam': 'Adam - Narrador profissional',
        'antoni': 'Antoni - Voz amigável',
        'arnold': 'Arnold - Voz grave (Terminator)',
        'callum': 'Callum - Britânico sarcástico',
        'charlie': 'Charlie - Voz casual',
        'clyde': 'Clyde - Voz de guerra',
        'daniel': 'Daniel - Apresentador de notícias',
        'dave': 'Dave - Voz conversacional',
        'drew': 'Drew - Voz bem-humorada',
        'ethan': 'Ethan - Voz jovem',
        'fin': 'Fin - Irlandês',
        'freya': 'Freya - Feminina britânica',
        'gigi': 'Gigi - Feminina jovem',
        'giovanni': 'Giovanni - Italiano',
        'glinda': 'Glinda - Bruxa boa',
        'grace': 'Grace - Feminina sulista',
        'harry': 'Harry - Nervoso/ansioso',
        'james': 'James - Repórter',
        'jeremy': 'Jeremy - Nerd/intelectual',
        'jessie': 'Jessie - Homem velho',
        'josh': 'Josh - Jovem e profundo',
        'liam': 'Liam - Narrador',
        'matilda': 'Matilda - Warm audiobook',
        'matthew': 'Matthew - Britânico/Audiobook',
        'michael': 'Michael - Audiobook',
        'mimi': 'Mimi - Feminina jovem',
        'nicole': 'Nicole - Sussurrante',
        'onyx': 'Onyx - Rádio hip-hop',
        'paula': 'Paula - Agradável',
        'prem': 'Prem - Indiano',
        'rachel': 'Rachel - Calma americana',
        'ryan': 'Ryan - Soldado',
        'sam': 'Sam - Conversacional',
        'serena': 'Serena - Agradável',
        'thomas': 'Thomas - Meditação calma',
        'wayne': 'Wayne - Homem do Kansas'
    }
    
    print("🎙️ TESTE DE VOZES ELEVENLABS")
    print("Encontrando a voz perfeita pro humor negro brasileiro!")
    print("=" * 60)
    
    # Listar algumas vozes recomendadas
    print("\n🔥 RECOMENDADAS PARA HUMOR PESADO:")
    print("- clyde: Voz de guerra (tipo sargento puto)")
    print("- harry: Nervoso/ansioso (perfeito pro Brasil)")
    print("- onyx: Rádio hip-hop (atitude)")
    print("- drew: Bem-humorada")
    print("- jessie: Velho ranzinza")
    
    print("\n🎭 VOZES DISPONÍVEIS:")
    for voice_id, description in voices.items():
        print(f"  {voice_id}: {description}")
    
    while True:
        print("\n" + "="*60)
        voice = input("\n🎤 Digite o nome da voz para testar (ou 'sair'): ").lower()
        
        if voice == 'sair':
            break
            
        if voice not in voices:
            print("❌ Voz não encontrada! Tente novamente.")
            continue
        
        print(f"\n🔊 Gerando áudio com {voice} ({voices[voice]})...")
        
        try:
            # Gerar áudio
            audio = client.generate(
                text=test_text,
                voice=voice,
                model="eleven_multilingual_v2"
            )
            
            # Salvar
            filename = f"test_{voice}.mp3"
            with open(filename, 'wb') as f:
                for chunk in audio:
                    f.write(chunk)
            
            print(f"✅ Áudio salvo: {filename}")
            
            # Tocar
            os.system(f'mpg123 {filename} 2>/dev/null')
            
            # Feedback
            rating = input("\n⭐ Avaliação (1-5): ")
            if rating == '5':
                print("🏆 ESSA É A CAMPEÃ!")
                save_choice = input("Salvar como padrão? (s/n): ")
                if save_choice.lower() == 's':
                    # Atualizar .env
                    with open('.env', 'r') as f:
                        content = f.read()
                    content = content.replace(f"VOICE_NAME=adam", f"VOICE_NAME={voice}")
                    with open('.env', 'w') as f:
                        f.write(content)
                    print(f"✅ Voz {voice} configurada como padrão!")
            
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    # Limpar arquivos de teste
    print("\n🗑️ Limpando arquivos de teste...")
    os.system('rm -f test_*.mp3')
    print("✅ Pronto!")

if __name__ == "__main__":
    print("""
    🎤 ELEVENLABS VOICE TESTER 🎤
    Encontre a voz perfeita pro seu 
    bot jornalista politicamente incorreto!
    """)
    test_voices()