import os
import google.generativeai as genai
from keywordsai_tracing.decorators import workflow, task
from keywordsai_tracing import KeywordsAITelemetry
from dotenv import load_dotenv
load_dotenv()  # reads .env into os.environ


# Initialize Keywords AI Telemetry
# os.environ["KEYWORDSAI_API_KEY"]
# os.environ["KEYWORDSAI_BASE_URL"]
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

k_tl = KeywordsAITelemetry()

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
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Tell me a joke")
        return response.text

    def run(self):
        return self.create_joke()

print(JokeAgent().run())
