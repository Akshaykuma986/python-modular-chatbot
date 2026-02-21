class Memory:
    def __init__(self):
        self.messages = []
        self.name = None

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name