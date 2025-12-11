import random
import datetime


# ============================================
# SIMPLE CHATBOT - RULE BASED
# ============================================

def get_greeting_response():

    greetings = [
        "Hi there! ",
        "Hello! How can I help you today?",
        "Hey! Nice to meet you!",
        "Greetings! What's up?"
    ]
    return random.choice(greetings)


def get_howru_response():

    responses = [
        "I'm fine, thanks! How about you?",
        "I'm doing great! Thanks for asking! ",
        "I'm just a bot, but I'm functioning perfectly!",
        "All good here! How are you doing?"
    ]
    return random.choice(responses)


def get_goodbye_response():

    goodbyes = [
        "Goodbye! Have a great day! ",
        "See you later! Take care!",
        "Bye! Come back soon!",
        "Farewell! It was nice chatting with you!"
    ]
    return random.choice(goodbyes)


def get_name_response(user_input):

    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {name}! "
    elif "i'm" in user_input or "i am" in user_input:
        name = user_input.replace("i'm", "").replace("i am", "").strip().capitalize()
        return f"Hello {name}! Pleased to meet you!"
    return "What's your name?"


def get_time_response():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}"


def get_date_response():
    today = datetime.datetime.now()
    return f"Today is {today.strftime('%A, %B %d, %Y')}"


def get_help_response():
    return """
Here's what I can do:
• Greet you (hi, hello, hey)
• Tell you how I'm doing
• Share the time and date
• Have a simple conversation
• Say goodbye (bye, goodbye, exit)

Just type naturally and I'll try to respond!
    """


def process_input(user_input):
    user_input = user_input.lower().strip()

    # Greeting
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return get_greeting_response()

    # How are you
    elif any(phrase in user_input for phrase in ["how are you", "how r u", "how's it going", "what's up", "whats up"]):
        return get_howru_response()

    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit", "see you"]):
        return get_goodbye_response()

    # Name
    elif "my name is" in user_input or (("i'm" in user_input or "i am" in user_input) and len(user_input.split()) <= 4):
        return get_name_response(user_input)

    # Time
    elif any(phrase in user_input for phrase in ["what time", "current time", "time is it"]):
        return get_time_response()

    # Date
    elif any(phrase in user_input for phrase in ["what date", "today's date", "what day"]):
        return get_date_response()

    # Help
    elif "help" in user_input:
        return get_help_response()

    # Thank you
    elif any(word in user_input for word in ["thank", "thanks", "thx"]):
        return random.choice([
            "You're welcome! ",
            "No problem!",
            "Happy to help!",
            "Anytime!"
        ])

    # Age
    elif "how old" in user_input or "your age" in user_input:
        return "I'm timeless! I was created just for you! "

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm ChatBot, your friendly rule-based assistant! "

    # for unrecognized input
    else:
        return random.choice([
            "I'm not sure I understand. Can you rephrase that?",
            "Hmm, I don't know how to respond to that yet.",
            "Interesting! Tell me more.",
            "I'm still learning. Try asking something else!",
            "Type 'help' to see what I can do!"
        ])


def chatbot():

    print("=" * 50)
    print("WELCOME TO CHATBOT!")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("Type 'help' to see what I can do.\n")


    while True:
        user_input = input("You: ").strip()

        # if empty input
        if not user_input:
            print("Bot: Please say something! \n")
            continue

        response = process_input(user_input)

        print(f"Bot: {response}\n")

        #  if user wants to exit
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break

    print("=" * 50)
    print("Thanks for chatting! Have a wonderful day! ")
    print("=" * 50)



if __name__ == "__main__":
    chatbot()

