print("Simple Chatbot")
print("Type 'bye' to exit")
print("------------------")

while True:
    message = input("You: ").lower()
    
    if message == "hello":
        print("Bot: Hi there!")
    
    elif message == "how are you":
        print("Bot: I am fine, thank you!")
    
    elif message == "what is your name":
        print("Bot: I am a simple Python chatbot.")
    
    elif message == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")