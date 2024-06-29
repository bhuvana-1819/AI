#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching
    
    # Define predefined rules and responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm good, thank you!",
        "what is your name": "I'm a chatbot. You can call me ChatGPT!",
        "bye": "Goodbye! Have a nice day.",
        "default": "I'm sorry, I don't understand that.",
    }
    
    # Check user input against predefined rules
    if user_input in responses:hi
        return responses[user_input]
    else:
        return responses["default"]

# Example usage:
print("Welcome to the Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        bot_response = chatbot_response(user_input)
        print("Chatbot:", bot_response)


# In[ ]:




