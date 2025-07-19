#!/usr/bin/env python3
"""
📰 News Reporter Simple Tray - Versão simplificada
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import threading

class NewsReporterTray:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("News Reporter")
        self.root.geometry("250x150")
        
        # Título
        title = tk.Label(self.root, text="📰 News Reporter", font=("Arial", 16))
        title.pack(pady=10)
        
        # Botão principal
        btn_play = tk.Button(
            self.root, 
            text="🎙️ Ouvir Notícias Agora",
            command=self.play_news,
            bg="#3498db",
            fg="white",
            font=("Arial", 12),
            height=2
        )
        btn_play.pack(fill=tk.X, padx=20, pady=5)
        
        # Minimizar ao invés de fechar
        self.root.protocol("WM_DELETE_WINDOW", self.minimize)
        
        # Iniciar minimizado
        self.root.withdraw()
        self.create_tray_icon()
    
    def create_tray_icon(self):
        """Cria ícone minimalista na bandeja"""
        # Criar janela pequena que fica sempre visível
        self.icon_window = tk.Toplevel(self.root)
        self.icon_window.geometry("40x40+10+10")  # Pequeno e no canto
        self.icon_window.overrideredirect(True)  # Sem bordas
        self.icon_window.attributes('-topmost', True)  # Sempre no topo
        
        # Botão que simula ícone
        icon_btn = tk.Button(
            self.icon_window,
            text="📰",
            font=("Arial", 20),
            command=self.toggle_window,
            relief=tk.FLAT,
            bg="#3498db"
        )
        icon_btn.pack(fill=tk.BOTH, expand=True)
    
    def toggle_window(self):
        if self.root.winfo_viewable():
            self.minimize()
        else:
            self.root.deiconify()
    
    def minimize(self):
        self.root.withdraw()
    
    def play_news(self):
        """Executa o bot de notícias"""
        def run():
            subprocess.run(['notify-send', '📰 Notícias', 'Preparando suas notícias...'])
            script_path = os.path.join(os.path.dirname(__file__), 'news_now.py')
            subprocess.run(['python3', script_path])
            subprocess.run(['notify-send', '✅ Pronto!', 'Notícias reproduzidas!'])
        
        thread = threading.Thread(target=run)
        thread.start()
        self.minimize()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NewsReporterTray()
    app.run()