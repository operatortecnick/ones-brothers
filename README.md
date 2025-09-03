# 🤖 One's Brothers - We are all reflections of each other

> *"VAI TRABALHAR PORRA!"* - One's Brothers, 2025

Um bot jornalista que odeia seu público. Quanto mais você clica, mais ele te xinga. 
Nascido da improvável união entre um advogado que não sabe programar e uma IA.

[🇧🇷 Versão em Português](README_PTBR.md)

## 🤖 AI API Management Panel

**NOVO!** Painel web para gerenciar todas as APIs de IA disponíveis:

### Como acessar:
```bash
# Opção 1: Pelo menu principal do bot
python news_reporter_bot.py
# Escolha opção 5: "Abrir Painel de APIs de IA"

# Opção 2: Diretamente
python start_api_panel.py

# Opção 3: Servidor dedicado
python api_panel.py
```

### Funcionalidades:
- 📋 **Catálogo de APIs**: Veja todas as APIs de IA disponíveis
- 🔗 **Links diretos**: Acesse facilmente os sites para criar contas
- ⚙️ **Guias de configuração**: Instruções passo-a-passo 
- 📊 **Status em tempo real**: Veja quais APIs estão configuradas
- 💡 **Dicas e troubleshooting**: Solução de problemas comuns

### APIs incluídas:
- **OpenAI** - GPT-4, DALL-E, Whisper (💰 $5 grátis)
- **ElevenLabs** - Text-to-speech realista (💰 10k chars/mês grátis)
- **Anthropic** - Claude AI para análise (💰 Pago)
- **Google AI** - Gemini multimodal (💰 Tier generoso)
- **Hugging Face** - Modelos open-source (🆓 Gratuito)
- **Replicate** - Stable Diffusion, LLaMA (💰 $10 grátis)
- **Cohere** - NLP empresarial (💰 Tier gratuito)
- **Stability AI** - Geração de imagens (💰 Pago)

## 🚀 Instalação Rápida

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. (Opcional) Configurar APIs - AGORA MAIS FÁCIL!
# Use o novo painel web para descobrir e configurar APIs
python start_api_panel.py
# OU configure manualmente:
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
