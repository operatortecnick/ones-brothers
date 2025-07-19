#!/bin/bash
# 🎙️ News Reporter Bot - Installer
# O bot de notícias mais politicamente incorreto do Brasil!

echo "🤖 NEWS REPORTER BOT - INSTALADOR"
echo "================================="
echo "O jornalista mais sincero do Brasil!"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado! Instale primeiro."
    exit 1
fi

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
echo "📥 Instalando dependências..."
pip install requests beautifulsoup4 python-dotenv feedparser pydub gtts schedule PyGObject elevenlabs

# Criar .env
if [ ! -f .env ]; then
    echo "⚙️ Configurando..."
    cp .env.example .env
    echo ""
    echo "🔑 CONFIGURAÇÃO NECESSÁRIA:"
    echo "1. Edite o arquivo .env"
    echo "2. Adicione sua API key da ElevenLabs (opcional)"
    echo "   - Sem API: voz robótica grátis"
    echo "   - Com API: vozes profissionais fodas"
    echo ""
fi

# Tornar executáveis
chmod +x news_reporter_bot.py
chmod +x news_tray.py
chmod +x news_now.py

# Criar atalho desktop
echo "🖥️ Criando ícone no desktop..."
cp NewsReporter.desktop ~/Desktop/ 2>/dev/null || \
cp NewsReporter.desktop ~/Área\ de\ Trabalho/ 2>/dev/null || \
echo "   Desktop não encontrado, copie manualmente"

# Autostart
mkdir -p ~/.config/autostart
cp news-reporter-startup.desktop ~/.config/autostart/

echo ""
echo "✅ INSTALAÇÃO COMPLETA!"
echo ""
echo "🚀 COMO USAR:"
echo "1. Execute: python3 news_tray.py"
echo "2. Procure o ícone na bandeja do sistema"
echo "3. Clique em 'Ouvir Notícias Agora'"
echo ""
echo "💡 DICAS:"
echo "- Edite news_summarizer.py para customizar o humor"
echo "- Vozes disponíveis: callum, charlie, roger, liam"
echo "- Adicione mais sites em news_scraper.py"
echo ""
echo "🔥 Aproveite seu jornalista politicamente incorreto!"