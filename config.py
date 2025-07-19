"""
Configurações de idioma do One's Brothers
"""

LANGUAGES = {
    'pt-br': {
        'sources': ['g1', 'uol', 'bbc_brasil', 'reddit_brasil', 'sensacionalista'],
        'voice_language': 'pt-br',
        'default_voice': 'callum'
    },
    'en': {
        'sources': ['bbc', 'cnn', 'reddit_worldnews', 'theonion'],
        'voice_language': 'en',
        'default_voice': 'callum'
    },
    'es': {
        'sources': ['elpais', 'reddit_spain', 'elmundo'],
        'voice_language': 'es',
        'default_voice': 'giovanni'
    }
}

# Intros internacionais
INTROS = {
    'en': {
        1: [
            "Good morning! It's {date}, and here we go again with this shit.",
            "Hello! Ready for today's disasters? Spoiler: no, you're not.",
            "Sup! Another day in this dumpster fire we call Earth."
        ],
        3: [
            "Fuck, {clicks} times today? You addicted to misery?",
            "Jesus Christ, you again? Here's more fresh shit.",
            "Back again? GO GET A JOB! But first, the news."
        ],
        5: [
            "YOU'RE SICK! {clicks} FUCKING TIMES! Here's your overdose:",
            "SEEK THERAPY! But first, more news for your syndrome.",
            "{clicks} TIMES! You're the reason everything sucks!"
        ]
    },
    'es': {
        1: [
            "¡Buenos días! Es {date}, y aquí vamos con esta mierda.",
            "¡Hola! ¿Listo para los desastres de hoy? No, no lo estás."
        ],
        3: [
            "¡Coño, {clicks} veces hoy! ¿Eres adicto a la desgracia?",
            "¡Joder, tú otra vez! Toma más mierda fresca."
        ]
    }
}

# Comentários sarcásticos internacionais
COMMENTS = {
    'en': {
        'trump': ["Here we go again...", "Someone take his phone away!"],
        'biden': ["Grandpa's at it again", "Someone check if he's awake"],
        'economy': ["Time to sell a kidney!", "Monopoly money worth more"],
        'crisis': ["Which one? Lost count", "Crisis is our middle name"]
    },
    'es': {
        'crisis': ["¿Cuál? Perdí la cuenta", "Crisis es nuestro apellido"],
        'economía': ["Hora de vender un riñón", "El Monopoly vale más"]
    }
}