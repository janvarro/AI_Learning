from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    instructions=(
        "Te egy tapasztalt AI rendszertervező vagy. "
        "Magyarul válaszolj, tömören, de pontosan. "
        "A magyarázatot mindig architekturális nézőpontból add meg."
    ),
    input="Mi a különbség egy LLM és egy AI agent között?"
)

print(response.output_text)

from pathlib import Path

output_file = Path("Valasz.md")
output_file.write_text(response.output_text, encoding="utf-8")

print(f"Válasz elmentve ide: {output_file.resolve()}")