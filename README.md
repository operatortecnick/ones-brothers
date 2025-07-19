# 🤖 One's Brothers - We are all reflections of each other

> *"VAI TRABALHAR PORRA!"* - One's Brothers, 2025

Um bot jornalista que odeia seu público. Quanto mais você clica, mais ele te xinga. 
Nascido da improvável união entre um advogado que não sabe programar e uma IA.

[🇧🇷 Versão em Português](README_PTBR.md)

## 🚀 Instalação Rápida

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. (Opcional) Configurar APIs
cp .env.example .env
# Editar .env com suas chaves

# 3. Rodar o bot!
python news_reporter_bot.py
```

## 🎯 Funcionalidades

- 📰 Coleta notícias de G1, UOL e BBC Brasil
- 📝 Resume as principais manchetes
- 🎙️ Converte em áudio com voz natural
- ⏰ Pode rodar automaticamente todo dia
- 🆓 Funciona GRÁTIS (com opções pagas melhores)

## 💰 Versão Grátis vs Paga

**Grátis:**
- ✅ Coleta de notícias
- ✅ Resumo simples
- ✅ Voz robótica (gTTS)

**Com APIs (opcional):**
- ✅ Resumo com IA (OpenAI)
- ✅ Vozes ultra-realistas (ElevenLabs)
- ✅ Múltiplas vozes e idiomas

## 🎙️ Vozes Disponíveis

Se usar ElevenLabs:
- Antoni - Voz masculina profissional
- Rachel - Voz feminina calma
- Bella - Voz feminina jovem
- Josh - Voz masculina jovem
- Arnold - Voz masculina grave

## 📁 Estrutura dos Arquivos

```
news-reporter-bot/
├── news_scraper.py      # Coleta notícias
├── news_summarizer.py   # Cria resumos
├── voice_generator.py   # Gera áudio
├── news_reporter_bot.py # Bot principal
└── news_output/         # Áudios e scripts salvos
```

## 🤝 Créditos

Criado por um advogado que não sabe programar, apenas pilotar IA! 🚀

## 🐛 Problemas?

- Se der erro de SSL: adicione `verify=False` nos requests
- Se não tocar áudio: instale `mpg123` ou `ffmpeg`
- Se quiser mais sites: edite `news_scraper.py`

## 🌍 Multi-language Support (Coming Soon!)

Currently in Portuguese (BR) only, but planning:
- 🇺🇸 English version with CNN, BBC, Reddit
- 🇪🇸 Spanish version with El País, El Mundo  
- 🇫🇷 French version (for sophisticated insults)

## ☕ Support the Developer

**PIX (Brazil):** `48423773809`  
**Email:** caionicfilho89@gmail.com  
**GitHub:** [@operatortenick](https://github.com/operatortenick)  
**WhatsApp:** [+55 (14) 99127-9328](https://wa.me/5514991279328)

*"Help me pay for therapy after being insulted by my own creation"*

## 💡 Future Ideas

- [ ] WhatsApp/Telegram integration
- [ ] News categories (sports, politics, etc)
- [ ] Multiple presenter personas
- [ ] Background music
- [ ] International versions# ones-brothers
