#!/usr/bin/env python3
"""
🤖 AI API Management Panel - One's Brothers
Painel para gerenciar todas as APIs de IA disponíveis
"""

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

class AIAPIManager:
    def __init__(self):
        self.apis_data = {
            'openai': {
                'name': 'OpenAI',
                'description': 'API de IA mais popular do mundo. GPT-4, DALL-E, Whisper e mais.',
                'logo_url': 'https://openai.com/favicon.ico',
                'website': 'https://openai.com',
                'signup_url': 'https://platform.openai.com/signup',
                'docs_url': 'https://platform.openai.com/docs',
                'pricing_url': 'https://openai.com/pricing',
                'free_tier': 'Sim - $5 de crédito grátis',
                'main_use': 'Texto, Imagens, Áudio',
                'api_key_name': 'OPENAI_API_KEY',
                'integration_status': self._check_integration('OPENAI_API_KEY'),
                'features': [
                    'GPT-4 e GPT-3.5 para texto',
                    'DALL-E para geração de imagens',
                    'Whisper para transcrição de áudio',
                    'TTS (Text-to-Speech)',
                    'Embeddings para busca semântica'
                ]
            },
            'elevenlabs': {
                'name': 'ElevenLabs',
                'description': 'A melhor API de voz sintética do mundo. Vozes ultra-realistas.',
                'logo_url': 'https://elevenlabs.io/favicon.ico',
                'website': 'https://elevenlabs.io',
                'signup_url': 'https://elevenlabs.io/sign-up',
                'docs_url': 'https://elevenlabs.io/docs',
                'pricing_url': 'https://elevenlabs.io/pricing',
                'free_tier': 'Sim - 10,000 caracteres/mês',
                'main_use': 'Text-to-Speech',
                'api_key_name': 'ELEVENLABS_API_KEY',
                'integration_status': self._check_integration('ELEVENLABS_API_KEY'),
                'features': [
                    'Vozes ultra-realistas',
                    'Clonagem de voz',
                    'Múltiplos idiomas',
                    'Controle de emoção',
                    'API simples e rápida'
                ]
            },
            'anthropic': {
                'name': 'Anthropic (Claude)',
                'description': 'Claude AI - IA segura e útil. Excelente para análise de texto.',
                'logo_url': 'https://www.anthropic.com/favicon.ico',
                'website': 'https://www.anthropic.com',
                'signup_url': 'https://console.anthropic.com',
                'docs_url': 'https://docs.anthropic.com',
                'pricing_url': 'https://www.anthropic.com/pricing',
                'free_tier': 'Não - Pago desde o início',
                'main_use': 'Análise de texto, Raciocínio',
                'api_key_name': 'ANTHROPIC_API_KEY',
                'integration_status': self._check_integration('ANTHROPIC_API_KEY'),
                'features': [
                    'Claude 3 (Haiku, Sonnet, Opus)',
                    'Análise de documentos longos',
                    'Raciocínio complexo',
                    'Segurança avançada',
                    'Excelente para código'
                ]
            },
            'google': {
                'name': 'Google AI (Gemini)',
                'description': 'Gemini AI do Google. Multimodal (texto, imagem, vídeo).',
                'logo_url': 'https://ai.google.dev/static/site-assets/images/share.png',
                'website': 'https://ai.google.dev',
                'signup_url': 'https://makersuite.google.com',
                'docs_url': 'https://ai.google.dev/docs',
                'pricing_url': 'https://ai.google.dev/pricing',
                'free_tier': 'Sim - Generoso limite gratuito',
                'main_use': 'Texto, Imagem, Vídeo',
                'api_key_name': 'GOOGLE_API_KEY',
                'integration_status': self._check_integration('GOOGLE_API_KEY'),
                'features': [
                    'Gemini Pro e Ultra',
                    'Análise multimodal',
                    'Integração com Google Workspace',
                    'Limite gratuito generoso',
                    'Excelente para programação'
                ]
            },
            'huggingface': {
                'name': 'Hugging Face',
                'description': 'Plataforma open-source com milhares de modelos de IA gratuitos.',
                'logo_url': 'https://huggingface.co/favicon.ico',
                'website': 'https://huggingface.co',
                'signup_url': 'https://huggingface.co/join',
                'docs_url': 'https://huggingface.co/docs',
                'pricing_url': 'https://huggingface.co/pricing',
                'free_tier': 'Sim - Muitos modelos gratuitos',
                'main_use': 'Modelos Open Source',
                'api_key_name': 'HUGGINGFACE_API_KEY',
                'integration_status': self._check_integration('HUGGINGFACE_API_KEY'),
                'features': [
                    'Milhares de modelos gratuitos',
                    'Transformers para NLP',
                    'Modelos de imagem e áudio',
                    'Datasets públicos',
                    'AutoTrain para fine-tuning'
                ]
            },
            'replicate': {
                'name': 'Replicate',
                'description': 'Execute modelos de IA na nuvem. Stable Diffusion, LLaMA e mais.',
                'logo_url': 'https://replicate.com/favicon.ico',
                'website': 'https://replicate.com',
                'signup_url': 'https://replicate.com/signin',
                'docs_url': 'https://replicate.com/docs',
                'pricing_url': 'https://replicate.com/pricing',
                'free_tier': 'Sim - $10 de crédito grátis',
                'main_use': 'Modelos de Imagem, LLMs',
                'api_key_name': 'REPLICATE_API_TOKEN',
                'integration_status': self._check_integration('REPLICATE_API_TOKEN'),
                'features': [
                    'Stable Diffusion para imagens',
                    'LLaMA e outros LLMs',
                    'Modelos de vídeo',
                    'API simples',
                    'Pay-per-use'
                ]
            },
            'cohere': {
                'name': 'Cohere',
                'description': 'API de NLP empresarial. Excelente para embeddings e busca.',
                'logo_url': 'https://cohere.com/favicon.ico',
                'website': 'https://cohere.com',
                'signup_url': 'https://dashboard.cohere.ai/register',
                'docs_url': 'https://docs.cohere.com',
                'pricing_url': 'https://cohere.com/pricing',
                'free_tier': 'Sim - Tier gratuito',
                'main_use': 'NLP, Embeddings, Busca',
                'api_key_name': 'COHERE_API_KEY',
                'integration_status': self._check_integration('COHERE_API_KEY'),
                'features': [
                    'Modelos de linguagem Command',
                    'Embeddings de alta qualidade',
                    'Classificação de texto',
                    'Sumarização',
                    'Busca semântica'
                ]
            },
            'stability': {
                'name': 'Stability AI',
                'description': 'Criadores do Stable Diffusion. APIs para geração de imagens.',
                'logo_url': 'https://stability.ai/favicon.ico',
                'website': 'https://stability.ai',
                'signup_url': 'https://platform.stability.ai/account',
                'docs_url': 'https://platform.stability.ai/docs',
                'pricing_url': 'https://platform.stability.ai/pricing',
                'free_tier': 'Não - Pago desde o início',
                'main_use': 'Geração de Imagens',
                'api_key_name': 'STABILITY_API_KEY',
                'integration_status': self._check_integration('STABILITY_API_KEY'),
                'features': [
                    'Stable Diffusion XL',
                    'Upscaling de imagens',
                    'Edição de imagens',
                    'API rápida e confiável',
                    'Múltiplos estilos'
                ]
            }
        }
    
    def _check_integration(self, api_key_name):
        """Verifica se a API está configurada"""
        api_key = os.getenv(api_key_name)
        if api_key and api_key.strip() and api_key != 'sua_chave_aqui':
            return 'Configurada'
        return 'Não configurada'
    
    def get_all_apis(self):
        """Retorna todas as APIs"""
        return self.apis_data
    
    def get_api(self, api_id):
        """Retorna uma API específica"""
        return self.apis_data.get(api_id)
    
    def get_configured_apis(self):
        """Retorna apenas APIs configuradas"""
        return {k: v for k, v in self.apis_data.items() 
                if v['integration_status'] == 'Configurada'}
    
    def get_unconfigured_apis(self):
        """Retorna apenas APIs não configuradas"""
        return {k: v for k, v in self.apis_data.items() 
                if v['integration_status'] == 'Não configurada'}

# Instância global
api_manager = AIAPIManager()

@app.route('/')
def index():
    """Página principal do painel"""
    apis = api_manager.get_all_apis()
    configured = api_manager.get_configured_apis()
    unconfigured = api_manager.get_unconfigured_apis()
    
    stats = {
        'total': len(apis),
        'configured': len(configured),
        'unconfigured': len(unconfigured)
    }
    
    return render_template('index.html', 
                         apis=apis, 
                         stats=stats,
                         configured=configured,
                         unconfigured=unconfigured)

@app.route('/api/<api_id>')
def api_detail(api_id):
    """Página de detalhes de uma API"""
    api = api_manager.get_api(api_id)
    if not api:
        flash(f'API {api_id} não encontrada!', 'error')
        return redirect(url_for('index'))
    
    return render_template('api_detail.html', api=api, api_id=api_id)

@app.route('/configure')
def configure():
    """Página de configuração"""
    return render_template('configure.html')

@app.route('/api/status')
def api_status():
    """API endpoint para status das integrações"""
    apis = api_manager.get_all_apis()
    status = {}
    for api_id, api_data in apis.items():
        status[api_id] = api_data['integration_status']
    return jsonify(status)

def run_panel(host='0.0.0.0', port=5000, debug=True):
    """Executa o painel web"""
    print(f"""
    🤖 AI API Management Panel - One's Brothers
    ==========================================
    
    🌐 Acesse: http://localhost:{port}
    📱 Ou: http://{host}:{port}
    
    Ctrl+C para parar
    """)
    
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run_panel()