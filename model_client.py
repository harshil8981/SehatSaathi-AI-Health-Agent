import os
try:
    from google import genai
except Exception:
    genai = None

class MockClient:
    def generate(self, prompt: str):
        if 'urgency' in prompt.lower():
            return '{"urgency": "LOW", "reason": "Symptoms appear mild.", "next_steps": ["Rest", "Hydrate"]}'
        return 'Mock reply: ' + prompt[:200]

class GeminiClient:
    def __init__(self):
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key or genai is None:
            self.client = MockClient()
            self.is_mock = True
        else:
            self.client = genai.Client(api_key=api_key)
            self.is_mock = False

    def generate(self, prompt: str):
        if self.is_mock:
            return self.client.generate(prompt)
        resp = self.client.models.generate_content(model='gemini-1.5', content=prompt)
        try:
            return resp.text
        except Exception:
            return str(resp)
