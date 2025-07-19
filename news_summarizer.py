import json
import openai
from typing import List, Dict
import os
from datetime import datetime

class NewsSummarizer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
    
    def create_news_summary(self, news_list: List[Dict]) -> str:
        """Cria um resumo das notícias do dia"""
        if not news_list:
            return "Não há notícias para resumir hoje."
        
        # Agrupar notícias por fonte
        news_by_source = {}
        for article in news_list:
            source = article['source']
            if source not in news_by_source:
                news_by_source[source] = []
            news_by_source[source].append(article['title'])
        
        # Criar texto para resumo
        news_text = "Principais manchetes de hoje:\n\n"
        for source, titles in news_by_source.items():
            news_text += f"{source}:\n"
            for title in titles:
                news_text += f"- {title}\n"
            news_text += "\n"
        
        return self.generate_ai_summary(news_text)
    
    def generate_ai_summary(self, news_text: str) -> str:
        """Gera resumo usando IA (OpenAI ou fallback)"""
        if self.api_key:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é um apresentador de jornal profissional brasileiro. Crie um resumo falado das notícias do dia, como se estivesse apresentando um podcast de notícias. Seja conciso mas informativo. Use linguagem clara e acessível."},
                        {"role": "user", "content": f"Crie um resumo falado dessas notícias:\n\n{news_text}"}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"❌ Erro na API OpenAI: {e}")
                return self.create_simple_summary(news_text)
        else:
            return self.create_simple_summary(news_text)
    
    def create_simple_summary(self, news_text: str) -> str:
        """Cria resumo simples sem IA"""
        date_str = datetime.now().strftime("%d de %B de %Y")
        
        summary = f"""Bom dia! Aqui estão as principais notícias de hoje, {date_str}.

No nosso resumo de hoje, trazemos as principais manchetes dos maiores portais de notícias do Brasil.

{news_text}

Essas foram as principais notícias do momento. Mantenha-se informado e tenha um excelente dia!"""
        
        return summary
    
    def create_funny_summary(self, news_list: List[Dict]) -> str:
        """Cria resumo com humor (modo Porta dos Fundos)"""
        date_str = datetime.now().strftime("%d de %B de %Y")
        
        # Sistema de intros progressivas baseado no humor_level
        from news_cache import NewsCache
        cache = NewsCache()
        
        humor_level = cache.get_humor_level()
        clicks = cache.get_clicks_today()
        
        # Intros por nível de humor
        intros_by_level = {
            1: [  # Primeira vez do dia
                f"Bom dia! É {date_str}, e cá estamos nós pra falar das notícias. Sim, já começou errado.",
                f"Olá! Dia {date_str}. Preparado? Spoiler: não, você não está.",
                f"E aí! Acordou? Ótimo, porque {date_str} já começou pegando fogo."
            ],
            2: [  # Segunda/terceira vez
                f"De volta? {date_str} continua uma merda. Surpresa: zero.",
                f"Opa, você de novo! As notícias pioraram desde a última vez.",
                f"Voltou pra mais? Masoquista. Bora ver o que mais deu ruim."
            ],
            3: [  # Ficando pesado
                f"Porra, {clicks} vezes hoje? Tá viciado em desgraça?",
                f"Caralho, tu não cansa não? Toma mais merda fresquinha.",
                f"De novo aqui? Vai trabalhar, porra! Mas primeiro, as notícias."
            ],
            4: [  # Humor nível hard
                f"PUTA QUE PARIU, {clicks} VEZES! Tu é masoquista profissional?",
                f"Mano, {clicks}x num dia só? Teu psicólogo sabe disso?",
                f"Foda-se, você pediu. Prepara o cu que lá vem notícia."
            ],
            5: [  # Nível máximo de loucura
                f"VOCÊ TÁ DOENTE! {clicks} FUCKING VEZES! Toma essa overdose de merda:",
                f"PROCURA UM PSIQUIATRA! Mas antes, mais notícias pra sua síndrome.",
                f"{clicks} VEZES CARALHO! Você é o motivo do Brasil estar assim!"
            ]
        }
        
        # Pegar intros do nível atual
        level_intros = intros_by_level.get(humor_level, intros_by_level[5])
        
        # Escolher uma que não foi usada ainda
        import random
        unused_intros = [i for i in level_intros if i not in cache.cache.get('used_intros', [])]
        
        if unused_intros:
            intro = random.choice(unused_intros)
        else:
            # Se todas foram usadas, pega qualquer uma e adiciona algo
            intro = random.choice(level_intros) + f" (Sim, {clicks}ª vez hoje. Procure ajuda.)"
        
        cache.add_used_intro(intro)
        
        summary = f"{intro}\n\n"
        
        # Adicionar notícias com comentários
        for i, article in enumerate(news_list[:5], 1):
            title = article['title']
            source = article['source']
            
            # Adicionar comentário baseado em palavras-chave
            comment = self.get_funny_comment(title)
            
            # Formato mais natural para fala
            if comment:
                summary += f"No {source}, temos: {title}. {comment} "
            else:
                summary += f"O {source} informa que {title}. "
        
        # Finalizações engraçadas
        endings = [
            "É isso aí, trouxa. Agora vai trabalhar pra pagar os impostos desses fdp.",
            "Resumo do resumo: tamo fudido mas tamo rindo. Chora não que piora.",
            "Brasil: o país onde a piada já vem pronta. Bom dia e boa sorte, vai precisar.",
            "E lembrem-se: aqui é Brasil, porra. Baixa a expectativa e segue o jogo."
        ]
        
        summary += f"\n{random.choice(endings)}"
        
        return summary
    
    def get_funny_comment(self, title: str) -> str:
        """Gera comentário engraçado baseado na notícia"""
        import random
        
        title_lower = title.lower()
        
        # Dicionário de palavras-chave e comentários
        comments = {
            'bolsonaro': [
                "Mito virou lenda. Lenda urbana de tornozeleira eletrônica.",
                "Patriota preso em casa. A ironia tá rindo sozinha.",
                "Acabou a mamata. Literalmente."
            ],
            'lula': [
                "Nove dedos, zero noção.",
                "O cara voltou do inferno pra fazer turismo.",
                "Cachaça subiu 20 porcento desde a posse."
            ],
            'dólar': [
                "Real valendo menos que moeda de truco.",
                "Tá na hora de virar agiota ou traficante.",
                "Paulo Guedes tá rindo em Miami."
            ],
            'política': [
                "Ladrão roubando ladrão são 200 anos de perdão.",
                "Brasília é tipo Gotham, só que sem o Batman.",
                "Todo mundo sabe quem roubou, ninguém sabe onde tá o dinheiro."
            ],
            'operação': [
                "PF trabalhando mais que Uber em dia de chuva.",
                "Nome criativo: Operação Óbvio Ululante.",
                "Spoiler: vai dar em pizza."
            ],
            'aumento': [
                "Única coisa que não aumenta é teu salário, otário.",
                "Inflação subiu tanto que tá fazendo bungee jump.",
                "Governo: a gente rouba mas faz."
            ],
            'crise': [
                "Brasil em crise é pleonasmo.",
                "Crise aqui é patrimônio cultural.",
                "Se não tivesse crise, não seria Brasil."
            ],
            'corrupção': [
                "Água molhada, fogo quente, político rouba.",
                "Corrupção no Brasil é tipo arroz no prato.",
                "Honestidade virou artigo de luxo."
            ]
        }
        
        # Procurar palavra-chave na notícia
        for keyword, comment_list in comments.items():
            if keyword in title_lower:
                return random.choice(comment_list)
        
        # Comentários genéricos se não achar palavra-chave
        generic = [
            "Cada dia uma desgraça diferente.",
            "2025 veio pra fuder mesmo.",
            "Deus tá testando até onde a gente aguenta.",
            "Por isso que cachaça vende mais que leite.",
            "Brasil não é pra amadores.",
            "Nem o capeta quer mais saber desse país.",
            "Tá explicado porque brasileiro só ri pra não chorar."
        ]
        
        # 50% de chance de comentário genérico
        if random.random() > 0.5:
            return random.choice(generic)
        
        return None
    
    def create_podcast_script(self, news_list: List[Dict]) -> str:
        """Cria um script estilo podcast"""
        # SEMPRE usar versão com humor!
        summary = self.create_funny_summary(news_list)
        
        # Remover emojis e caracteres especiais para voz mais natural
        script = summary
        # Remover emojis
        import re
        script = re.sub(r'[^\w\s\.,!?;:\-\(\)áàâãéèêíìîóòôõúùûçÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ]', '', script)
        # Remover múltiplos espaços
        script = re.sub(r'\s+', ' ', script)
        # Remover números dos itens
        script = re.sub(r'^\d+\.', '', script, flags=re.MULTILINE)
        
        return script


# Teste do summarizer
if __name__ == "__main__":
    # Carregar notícias do arquivo
    try:
        with open('daily_news.json', 'r', encoding='utf-8') as f:
            news = json.load(f)
        
        summarizer = NewsSummarizer()
        summary = summarizer.create_podcast_script(news)
        
        print("📝 Resumo das Notícias:")
        print("=" * 50)
        print(summary)
        
        # Salvar script
        with open('news_script.txt', 'w', encoding='utf-8') as f:
            f.write(summary)
        print("\n💾 Script salvo em news_script.txt")
        
    except FileNotFoundError:
        print("❌ Arquivo daily_news.json não encontrado! Execute news_scraper.py primeiro.")