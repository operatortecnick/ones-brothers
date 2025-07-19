#!/usr/bin/env python3
"""
🎙️ Testador de Vozes - Descubra qual voz é menos brochante!
"""

from gtts import gTTS
import os
import subprocess

def test_voices():
    test_text = "E aí, desgraça! Hoje o Brasil tá pegando fogo, mas pelo menos a gente tá rindo."
    
    # Opções de idioma/sotaque no gTTS
    voices = {
        'pt-br': 'Português Brasileiro (padrão)',
        'pt': 'Português Portugal (chique)',
        'es': 'Espanhol (caliente)',
        'en': 'Inglês (gringo)',
        'it': 'Italiano (mamma mia)',
        'fr': 'Francês (oui oui baguette)'
    }
    
    print("🎙️ TESTE DE VOZES - Qual brocha menos?")
    print("=" * 50)
    
    for lang, description in voices.items():
        print(f"\n🔊 Testando: {description}")
        
        # Adaptar texto para cada idioma
        if lang == 'en':
            text = "Hey motherfucker! Brazil is on fire today, but at least we're laughing."
        elif lang == 'es':
            text = "¡Hola desgraciado! Brasil está en llamas hoy, pero al menos nos estamos riendo."
        elif lang == 'fr':
            text = "Salut connard! Le Brésil brûle aujourd'hui, mais au moins on rigole."
        elif lang == 'it':
            text = "Ciao stronzo! Il Brasile sta bruciando oggi, ma almeno stiamo ridendo."
        else:
            text = test_text
        
        # Gerar áudio
        filename = f"test_voice_{lang}.mp3"
        tts = gTTS(text=text, lang=lang[:2])  # gTTS só aceita código de 2 letras
        tts.save(filename)
        
        print(f"   Arquivo: {filename}")
        
        # Tocar
        play = input("   Tocar? (s/n): ")
        if play.lower() == 's':
            subprocess.run([f'mpg123 {filename} 2>/dev/null'], shell=True)
        
    print("\n✅ Teste concluído!")
    print("\n💡 OUTRAS OPÇÕES:")
    print("1. espeak - Voz robótica mas configurável")
    print("2. festival - Várias vozes")
    print("3. pyttsx3 - Vozes do sistema")
    print("4. edge-tts - Vozes da Microsoft (MUITO melhores!)")
    
    # Limpar arquivos de teste
    clean = input("\n🗑️ Apagar arquivos de teste? (s/n): ")
    if clean.lower() == 's':
        for lang in voices.keys():
            try:
                os.remove(f"test_voice_{lang}.mp3")
            except:
                pass

if __name__ == "__main__":
    test_voices()