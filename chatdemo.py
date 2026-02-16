# Chat Conversation History
# -> User
# -> System/Bot Chat

from google import genai
from google.genai import types

client = genai.Client()

print("Chat begins here...type endchat to close")

userinput = input("User: ")

while userinput!= 'endchat':
    systemoutput = client.models.generate_content(
        contents = userinput,
        model = 'gemini-2.5-flash-lite',
        config = types.GenerateContentConfig(
            system_instruction="Answer in 1 line, within 50 characters"
        )
    )
    print("Statbot : ", systemoutput.text)
    userinput = input("User: ")