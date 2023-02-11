import openai
openai.api_key = "paste api key"

def conversational_pipeline(conversation_starts):
    model = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation_starts,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = model.choices[0].text
    print("AI: " + response)

while True:
    user_input = input("You: ")
    if user_input == 'q':
        break
    conversational_pipeline(user_input)

