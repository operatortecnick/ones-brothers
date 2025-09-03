#!/usr/bin/env python3
"""
🤖 One's Brothers - AI API Panel Launcher
Iniciador rápido para o painel de APIs de IA
"""

import sys
import os

def main():
    print("""
    🤖 One's Brothers - AI API Management Panel
    ===========================================
    
    Este é o painel de gerenciamento de APIs de IA!
    Aqui você pode descobrir e configurar todas as APIs disponíveis.
    
    """)
    
    # Verificar se está na pasta correta
    if not os.path.exists('news_reporter_bot.py'):
        print("❌ Erro: Execute este script na pasta do projeto One's Brothers!")
        print("📁 Certifique-se de estar na pasta onde está o news_reporter_bot.py")
        return
    
    try:
        print("🚀 Iniciando painel...")
        from api_panel import run_panel
        run_panel()
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("💡 Certifique-se de que o Flask está instalado:")
        print("   pip install flask")
    except KeyboardInterrupt:
        print("\n\n👋 Painel encerrado pelo usuário!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("💡 Tente executar: python api_panel.py")

if __name__ == '__main__':
    main()