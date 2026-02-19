print("🤖 Harshit's  AI Chatbot")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye! Have a great day 😊")
        break

    # greetings
    elif "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you today?")

    elif "good morning" in user:
        print("Bot: Good morning! Hope you have a productive day!")

    elif "good evening" in user:
        print("Bot: Good evening! How was your day?")

    # personal questions
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking 😊")

    elif "your name" in user:
        print("Bot: I am Harshit's AI Chatbot.")

    elif "who made you" in user:
        print("Bot: I was created by a Harshit Porwal 😎")

    elif "what can you do" in user:
        print("Bot: I can chat with you and answer simple questions!")

    # fun questions
    elif " tell me a joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs 😄")

    elif "motivate me " in user or "motivation" in user:
        print("Bot: Success comes from consistency. Keep going 💪")

    elif "quote something" in user:
        print("Bot: Believe you can and you're halfway there.")

    # time/date
    elif "time" in user:
        import datetime
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif "date" in user:
        import datetime
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    # internship
    elif "internship" in user:
        print("Bot: Internships help you gain real-world experience!")

    elif "ai" in user:
        print("Bot: Artificial Intelligence is the future 🚀")

    # thanks
    elif "thank" in user:
        print("Bot: You're welcome 😊")

    # help
    elif "help" in user:
        print("Bot: You can ask me about time, jokes, motivation, AI, or greetings!")

    # default
    else:
        print("Bot: Hmm… I’m not sure about that. Try asking something else!")
