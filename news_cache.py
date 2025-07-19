import json
import os
from datetime import datetime, timedelta
from typing import List, Dict

class NewsCache:
    def __init__(self, cache_file='news_cache.json'):
        self.cache_file = cache_file
        self.cache = self.load_cache()
        
    def load_cache(self) -> Dict:
        """Carrega cache do disco"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {
            'last_news': [],
            'used_intros': [],
            'clicks_today': 0,
            'last_click': None,
            'humor_level': 1  # 1-5, vai aumentando
        }
    
    def save_cache(self):
        """Salva cache no disco"""
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def is_new_day(self) -> bool:
        """Verifica se é um novo dia"""
        if not self.cache['last_click']:
            return True
        last = datetime.fromisoformat(self.cache['last_click'])
        return last.date() != datetime.now().date()
    
    def register_click(self):
        """Registra um clique"""
        if self.is_new_day():
            # Novo dia, reseta contadores
            self.cache['clicks_today'] = 1
            self.cache['humor_level'] = 1
            self.cache['used_intros'] = []
        else:
            self.cache['clicks_today'] += 1
            # Aumenta humor a cada 2 cliques
            if self.cache['clicks_today'] % 2 == 0:
                self.cache['humor_level'] = min(5, self.cache['humor_level'] + 1)
        
        self.cache['last_click'] = datetime.now().isoformat()
        self.save_cache()
    
    def get_humor_level(self) -> int:
        """Retorna nível de humor (1-5)"""
        return self.cache['humor_level']
    
    def get_clicks_today(self) -> int:
        """Retorna quantos cliques hoje"""
        if self.is_new_day():
            return 0
        return self.cache['clicks_today']
    
    def is_news_used(self, news_title: str) -> bool:
        """Verifica se notícia já foi usada nas últimas 3 horas"""
        # Limpar notícias antigas (mais de 3 horas)
        three_hours_ago = (datetime.now() - timedelta(hours=3)).isoformat()
        self.cache['last_news'] = [
            n for n in self.cache['last_news'] 
            if n['timestamp'] > three_hours_ago
        ]
        
        # Verificar se já foi usada
        titles = [n['title'] for n in self.cache['last_news']]
        return news_title in titles
    
    def add_used_news(self, news_list: List[Dict]):
        """Adiciona notícias usadas ao cache"""
        for news in news_list:
            self.cache['last_news'].append({
                'title': news['title'],
                'timestamp': datetime.now().isoformat()
            })
        self.save_cache()
    
    def get_used_intro_count(self) -> int:
        """Quantas intros já foram usadas hoje"""
        if self.is_new_day():
            return 0
        return len(self.cache['used_intros'])
    
    def add_used_intro(self, intro: str):
        """Marca intro como usada"""
        if intro not in self.cache['used_intros']:
            self.cache['used_intros'].append(intro)
            self.save_cache()