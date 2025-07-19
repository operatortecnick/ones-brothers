import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time
from typing import List, Dict

class NewsScraperBot:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def scrape_g1(self) -> List[Dict]:
        """Scrape G1 principais notícias"""
        print("📰 Buscando notícias do G1...")
        news = []
        try:
            response = requests.get('https://g1.globo.com/', headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar manchetes principais
            articles = soup.find_all('a', class_='feed-post-link', limit=5)
            
            for article in articles:
                title = article.text.strip()
                link = article.get('href', '')
                if title and link:
                    news.append({
                        'source': 'G1',
                        'title': title,
                        'link': link,
                        'timestamp': datetime.now().isoformat()
                    })
                    
        except Exception as e:
            print(f"❌ Erro no G1: {e}")
            
        return news
    
    def scrape_uol(self) -> List[Dict]:
        """Scrape UOL principais notícias"""
        print("📰 Buscando notícias do UOL...")
        news = []
        try:
            response = requests.get('https://www.uol.com.br/', headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar headlines
            articles = soup.find_all('h2', limit=5)
            
            for article in articles:
                link_element = article.find('a')
                if link_element:
                    title = link_element.text.strip()
                    link = link_element.get('href', '')
                    if title and link:
                        news.append({
                            'source': 'UOL',
                            'title': title,
                            'link': link,
                            'timestamp': datetime.now().isoformat()
                        })
                        
        except Exception as e:
            print(f"❌ Erro no UOL: {e}")
            
        return news
    
    def scrape_bbc_brasil(self) -> List[Dict]:
        """Scrape BBC Brasil principais notícias"""
        print("📰 Buscando notícias da BBC Brasil...")
        news = []
        try:
            response = requests.get('https://www.bbc.com/portuguese', headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar artigos principais
            articles = soup.find_all('h2', limit=5)
            
            for article in articles:
                link_element = article.find('a')
                if link_element:
                    title = link_element.text.strip()
                    link = 'https://www.bbc.com' + link_element.get('href', '')
                    if title and link and '/portuguese/' in link:
                        news.append({
                            'source': 'BBC Brasil',
                            'title': title,
                            'link': link,
                            'timestamp': datetime.now().isoformat()
                        })
                        
        except Exception as e:
            print(f"❌ Erro na BBC: {e}")
            
        return news
    
    def scrape_reddit_brasil(self) -> List[Dict]:
        """Scrape Reddit r/brasil - notícias mais caóticas"""
        print("🤪 Buscando loucuras no Reddit...")
        news = []
        try:
            # Reddit via old.reddit (mais fácil de scraper)
            response = requests.get('https://old.reddit.com/r/brasil/hot/.json', headers=self.headers)
            data = response.json()
            
            posts = data.get('data', {}).get('children', [])[:5]
            for post in posts:
                post_data = post.get('data', {})
                title = post_data.get('title', '')
                if title and not post_data.get('is_video'):
                    news.append({
                        'source': 'Reddit r/brasil',
                        'title': title,
                        'link': f"https://reddit.com{post_data.get('permalink', '')}",
                        'timestamp': datetime.now().isoformat()
                    })
        except Exception as e:
            print(f"❌ Erro no Reddit: {e}")
        
        return news
    
    def scrape_sensacionalista(self) -> List[Dict]:
        """Scrape Sensacionalista - humor e sátira"""
        print("😂 Buscando notícias do Sensacionalista...")
        news = []
        try:
            response = requests.get('https://www.sensacionalista.com.br/', headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('h2', class_='entry-title', limit=5)
            
            for article in articles:
                link_element = article.find('a')
                if link_element:
                    title = link_element.text.strip()
                    link = link_element.get('href', '')
                    if title:
                        news.append({
                            'source': 'Sensacionalista',
                            'title': title,
                            'link': link,
                            'timestamp': datetime.now().isoformat()
                        })
                        
        except Exception as e:
            print(f"❌ Erro no Sensacionalista: {e}")
            
        return news
    
    def collect_all_news(self) -> List[Dict]:
        """Coleta notícias de todas as fontes"""
        from news_cache import NewsCache
        cache = NewsCache()
        
        all_news = []
        
        # Variar fontes baseado no número de cliques
        clicks = cache.get_clicks_today()
        
        if clicks <= 2:
            # Primeiros cliques - notícias normais
            all_news.extend(self.scrape_g1())
            time.sleep(1)
            all_news.extend(self.scrape_uol())
            time.sleep(1)
            all_news.extend(self.scrape_bbc_brasil())
        
        elif clicks <= 5:
            # Misturar ordem e pegar páginas diferentes
            import random
            sources = [self.scrape_g1, self.scrape_uol, self.scrape_bbc_brasil]
            random.shuffle(sources)
            for source in sources:
                all_news.extend(source())
                time.sleep(1)
        
        else:
            # Modo caos - buscar notícias bizarras
            print("🔥 Modo CAOS ativado! Buscando notícias obscuras...")
            all_news.extend(self.scrape_reddit_brasil())
            all_news.extend(self.scrape_sensacionalista())
            # Embaralhar todas as notícias
            random.shuffle(all_news)
        
        # Se muitos cliques, buscar mais fontes/páginas
        if cache.get_clicks_today() > 3:
            print("🔥 Buscando notícias mais obscuras...")
            # Pegar mais notícias das páginas internas
            # TODO: implementar scraping de páginas secundárias
        
        # Filtrar notícias já usadas recentemente
        fresh_news = []
        for news in all_news:
            if not cache.is_news_used(news['title']):
                fresh_news.append(news)
        
        # Se não sobrou notícia nova, pega todas mesmo
        if not fresh_news:
            print("⚠️ Sem notícias novas! Reciclando...")
            fresh_news = all_news
        
        print(f"\n✅ Total de notícias: {len(all_news)} (novas: {len(fresh_news)})")
        return fresh_news
    
    def save_news(self, news: List[Dict], filename: str = 'daily_news.json'):
        """Salva as notícias em arquivo JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(news, f, ensure_ascii=False, indent=2)
        print(f"💾 Notícias salvas em {filename}")


# Teste do scraper
if __name__ == "__main__":
    print("🤖 Iniciando News Reporter Bot...")
    print("=" * 50)
    
    bot = NewsScraperBot()
    news = bot.collect_all_news()
    
    if news:
        print("\n📋 Manchetes de Hoje:")
        print("=" * 50)
        for i, article in enumerate(news, 1):
            print(f"\n{i}. [{article['source']}] {article['title']}")
            print(f"   🔗 {article['link']}")
        
        bot.save_news(news)
    else:
        print("❌ Nenhuma notícia encontrada!")