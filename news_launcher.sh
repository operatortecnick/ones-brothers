#!/bin/bash
# 🎙️ News Reporter Launcher

# Notificação de início
notify-send "📰 Notícias do Dia" "Preparando suas notícias..." -i /home/caiofo/news-reporter-bot/news-icon.svg 2>/dev/null

# Executar o bot
cd /home/caiofo/news-reporter-bot
/usr/bin/python3 news_now.py

# Notificação de conclusão
notify-send "✅ Notícias Prontas" "Reprodução concluída!" -i /home/caiofo/news-reporter-bot/news-icon.svg 2>/dev/null

# Manter terminal aberto por 5 segundos
echo ""
echo "🎉 Pressione ENTER para fechar..."
read