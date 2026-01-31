import os
from openai import OpenAI
from keywordsai_tracing.decorators import workflow, task
from keywordsai_tracing import KeywordsAITelemetry

# Initialize Keywords AI Telemetry
os.environ["KEYWORDSAI_API_KEY"] = "yf4XScSu.BddinxnSGyk0oy28sEvuV6PAN35ldkBj"
os.environ["KEYWORDSAI_BASE_URL"] = "https://api.keywordsai.co/api"
os.environ["OPENAI_API_KEY"] = "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"

k_tl = KeywordsAITelemetry()
# Initialize OpenAI client
client = OpenAI()

@workflow(name="hello_world")
def hello_world():
    @task(name="compute")
    def compute():
        return "Hello Tracing"
    return compute()

print(hello_world())

@workflow(name="joke_agent", method_name="run")
class JokeAgent:
    @task(name="joke_creation")
    def create_joke(self):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Tell me a joke about tracing"}],
        )
        return completion.choices[0].message.content

    def run(self):
        return self.create_joke()

print(JokeAgent().run())
