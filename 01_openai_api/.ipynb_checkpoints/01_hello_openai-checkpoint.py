from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Magyarázd el 3 rövid mondatban, mi az OpenAI API."
)

print(response.output_text)