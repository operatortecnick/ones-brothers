#!/usr/bin/env python3
"""
📰 News Reporter Tray - Ícone na bandeja do sistema
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
import os
import subprocess
import threading

class NewsReporterTray:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            'news-reporter',
            'microphone',
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        
        # Tentar usar nosso ícone
        icon_path = os.path.join(os.path.dirname(__file__), 'news-icon.svg')
        if os.path.exists(icon_path):
            self.indicator.set_icon(icon_path)
        
        # Criar menu
        self.create_menu()
    
    def create_menu(self):
        menu = Gtk.Menu()
        
        # Opção principal - Ouvir notícias
        item_news = Gtk.MenuItem('🎙️ Ouvir Notícias Agora')
        item_news.connect('activate', self.play_news)
        menu.append(item_news)
        
        # Separador
        menu.append(Gtk.SeparatorMenuItem())
        
        # Agendar
        item_schedule = Gtk.MenuItem('⏰ Agendar Notícias')
        item_schedule.connect('activate', self.schedule_news)
        menu.append(item_schedule)
        
        # Configurações
        item_config = Gtk.MenuItem('⚙️ Configurações')
        item_config.connect('activate', self.open_config)
        menu.append(item_config)
        
        # Separador
        menu.append(Gtk.SeparatorMenuItem())
        
        # Sair
        item_quit = Gtk.MenuItem('❌ Sair')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)
        
        menu.show_all()
        self.indicator.set_menu(menu)
    
    def play_news(self, widget):
        """Executa o bot de notícias"""
        def run():
            subprocess.run(['notify-send', '📰 Notícias', 'Preparando suas notícias...'])
            subprocess.run(['python3', os.path.join(os.path.dirname(__file__), 'news_now.py')])
            subprocess.run(['notify-send', '✅ Pronto!', 'Notícias reproduzidas com sucesso!'])
        
        # Executar em thread separada para não travar a interface
        thread = threading.Thread(target=run)
        thread.start()
    
    def schedule_news(self, widget):
        subprocess.run(['notify-send', '⏰ Em breve!', 'Função de agendamento chegando...'])
    
    def open_config(self, widget):
        # Abrir pasta do projeto
        subprocess.run(['xdg-open', os.path.dirname(__file__)])
    
    def quit(self, widget):
        Gtk.main_quit()

def main():
    # Criar indicador
    NewsReporterTray()
    
    # Notificação de início
    subprocess.run(['notify-send', '📰 News Reporter', 'Rodando na bandeja do sistema!'])
    
    # Rodar GTK
    Gtk.main()

if __name__ == "__main__":
    main()