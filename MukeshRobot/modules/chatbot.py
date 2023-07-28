def get_response(user_input):
    # Dictionary of predefined responses
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a chatbot, but thanks for asking!",
        "what is your name": "I am ChatGPT, a logic-based chatbot.",
        "bye": "Goodbye! Have a great day!",
        "S": "Oh yeah"
        # Add more predefined responses here
    }

    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if there is a predefined response for the user input
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?"

def main():
    print("Chatbot: Hello! How can I assist you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
