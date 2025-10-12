from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)