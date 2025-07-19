#!/usr/bin/env python3
"""
🚀 NEWS NOW - Execução direta do bot de notícias
Roda tudo automaticamente e toca o áudio!
"""

import sys
from news_reporter_bot import NewsReporterBot

def main():
    print("""
    📰 NEWS NOW - Notícias Instantâneas! 📰
    =====================================
    """)
    
    # Criar e executar o bot
    bot = NewsReporterBot()
    
    # Executar relatório direto
    bot.run_daily_report()
    
    print("\n🎉 Pronto! Suas notícias foram preparadas e tocadas!")

if __name__ == "__main__":
    main()