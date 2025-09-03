# Mock openai module for testing
class OpenAI:
    def __init__(self, **kwargs):
        pass
    
    @property
    def chat(self):
        return MockChat()

class MockChat:
    @property 
    def completions(self):
        return MockCompletions()

class MockCompletions:
    def create(self, **kwargs):
        return MockResponse()

class MockResponse:
    def __init__(self):
        self.choices = [MockChoice()]

class MockChoice:
    def __init__(self):
        self.message = MockMessage()

class MockMessage:
    def __init__(self):
        self.content = "Mock AI response: Este é um resumo mockado das notícias."

# Mock module-level functions
def get_api_key():
    return None