from google import genai
from google.genai import types
from PIL import Image
import os
print(os.environ.get("GOOGLE_API_KEY"))
print("Santosh and Maya are the best")
client = genai.Client()
prompt= input("Enter your input :")

image = Image.open("images/cat1.jpg")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config = types.GenerateContentConfig(
        system_instruction = "Response should be negative and response should be 20 words",
        temperature = 2

    )


)

print("response", response.text)