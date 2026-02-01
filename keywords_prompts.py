from openai import OpenAI

client = OpenAI(
  base_url="https://api.keywordsai.co/api/",
  api_key="yf4XScSu.BddinxnSGyk0oy28sEvuV6PAN35ldkBj",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",  # This will be overridden by prompt config
    messages=[{"role": "user", "content": "placeholder"}],  # This will be overridden
    extra_body={
      "prompt": {
        "prompt_id": "dd51578d370543e0b254b66d84507701",
        "variables": {
            "User": "",
            "schedule": "",
            "preferences": ""
        },
        "override": True
      }
    }
)

print(response.choices[0].message.content)