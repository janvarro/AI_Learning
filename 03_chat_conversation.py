from openai import OpenAI

client = OpenAI()

# Első kérdés
response1 = client.responses.create(
    model="gpt-5.5",
    input="A Mars a Naprendszer hányadik bolygója?"
)

print("1. válasz:")
print(response1.output_text)

# Második kérdés ugyanabban a beszélgetésben
response2 = client.responses.create(
    model="gpt-5.5",
    previous_response_id=response1.id,
    input="És melyik bolygó követi?"
)

print("\n2. válasz:")
print(response2.output_text)