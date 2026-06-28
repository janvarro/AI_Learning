from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Magyarázd el 3 rövid mondatban, mi az OpenAI API."
)

print("=" * 60)
print("1. A response objektum típusa")
print("=" * 60)
print(type(response))

print("\n" + "=" * 60)
print("2. A teljes Response objektum")
print("=" * 60)
print(response)

print("\n" + "=" * 60)
print("3. A szöveges válasz (output_text)")
print("=" * 60)
print(response.output_text)

print("\n" + "=" * 60)
print("4. A teljes JSON reprezentáció")
print("=" * 60)
print(response.model_dump_json(indent=2))

print("\n" + "=" * 60)
print("5. Response ID")
print("=" * 60)
print(response.id)

print("\n" + "=" * 60)
print("6. Model")
print("=" * 60)
print(response.model)

print("\n" + "=" * 60)
print("7. Usage")
print("=" * 60)
print(response.usage)