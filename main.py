from bot.memory import Memory
from bot.logic import ChatLogic

def main():
    memory = Memory()
    logic = ChatLogic()

    print("AI: Hello! Type 'bye' to exit.")
    name = input("AI: What is your name?\nYou: ")
    memory.set_name(name)

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("AI: Goodbye 👋")
            break

        elif user_input == "history":
            print("AI: Conversation history:")
            for msg in memory.get_messages():
                print("-", msg)
            continue

        elif user_input == "count":
            print("AI: You have sent", len(memory.get_messages()), "messages.")
            continue

        memory.add_message(user_input)

        response = logic.get_response(user_input, memory.get_name())
        print("AI:", response)

if __name__ == "__main__":
    main()