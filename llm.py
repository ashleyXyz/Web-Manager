import os
from openai import OpenAI
from keywordsai_tracing.decorators import workflow, task
from keywordsai_tracing.main import KeywordsAITelemetry

# Initialize Keywords AI Telemetry
os.environ["KEYWORDSAI_API_KEY"] = "yf4XScSu.BddinxnSGyk0oy28sEvuV6PAN35ldkBj"
k_tl = KeywordsAITelemetry()

# Initialize OpenAI client
client = OpenAI()

@task(name="joke_creation")
def create_joke():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Tell me a joke about AI"}],
        temperature=0.7,
        max_tokens=100,
    )
    return completion.choices[0].message.content

@workflow(name="simple_joke_workflow")
def joke_workflow():
    joke = create_joke()
    return joke

if __name__ == "__main__":
    result = joke_workflow()
    print(result)