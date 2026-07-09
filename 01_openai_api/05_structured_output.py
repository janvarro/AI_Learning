from openai import OpenAI
from pydantic import BaseModel


class PlanetInfo(BaseModel):
    planet: str
    order_from_sun: int
    previous_planet: str
    next_planet: str
    short_explanation: str


client = OpenAI()

response = client.responses.parse(
    model="gpt-5.5",
    input="Adj strukturált információt a Mars bolygóról.",
    text_format=PlanetInfo,
)

planet_info = response.output_parsed

print("Parsed Python object:")
print(planet_info)

print("\nFields:")
print(f"Planet: {planet_info.planet}")
print(f"Order from Sun: {planet_info.order_from_sun}")
print(f"Previous planet: {planet_info.previous_planet}")
print(f"Next planet: {planet_info.next_planet}")
print(f"Explanation: {planet_info.short_explanation}")