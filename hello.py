from google import genai
print("Santosh and Maya are the best")
client = genai.Client(api_key="AIzaSyCvZYfUDAUvIgrYAhvsrSLbRJHih7JFNQk")
prompt= input("Enter your input :")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt


)

print("response", response.text)