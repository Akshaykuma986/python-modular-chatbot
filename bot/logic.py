import random

class ChatLogic:
    def __init__(self):
        self.responses = {
            "hi": ["Hello 👋", "Hey there!"],
            "hello": ["Hi!", "Nice to see you!"],
            "how are you": ["I'm doing great!", "All good here!"]
        }

    def get_response(self, user_input, name):
        if "sad" in user_input:
            return "I'm sorry to hear that. Want to talk about it?"

        if "happy" in user_input:
            return "That’s great to hear! 😄"

        if "tired" in user_input:
            return "Maybe you should take some rest 💤"

        words = user_input.split()

        for key in self.responses:
            if key in words:
                reply = random.choice(self.responses[key])
                if key in ["hi", "hello"]:
                    reply += " " + name + " 😄"
                return reply

        return "I don't understand yet."