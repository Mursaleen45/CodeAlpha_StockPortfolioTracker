# Basic Chatbot
# CodeAlpha Python Programming Internship

import datetime

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I am fine! Thank you for asking."

    elif "your name" in user_input:
        return "My name is Python Chatbot."

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return "Current time is " + current_time

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return "Today's date is " + current_date

    elif "help" in user_input:
        return "You can ask me about my name, time, date, or say hello."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand. Please try something else."


print("\n================================")
print("       PYTHON CHATBOT")
print("================================")

print("Chatbot: Hello! I am your Python chatbot.")
print("Chatbot: Type 'bye' to exit the conversation.")

while True:

    user_message = input("\nYou: ")

    response = chatbot_response(user_message)

    print("Chatbot:", response)

    if user_message.lower().strip() in ["bye", "exit", "quit"]:
        break

print("\nChat ended. Thank you!")