import random
import json 
import os
class ChatLogic:
    def __init__(self):
       self.file_path = "responses.json"
       self.responses = self.load_responses()

    def load_responses(self):
        if os.path.exists(self.file_path):
          with open(self.file_path,"r") as file:   
                return json.load(file)
        else:
          return()
        
    def save_responses(self):
       with open(self.file_path,"w") as file:
          json.dump(self.responses,file,indent=4) 


    def get_response(self, user_input, name):
        if user_input.startswith("teach:"):
           try:
            data = user_input.replace("teach:", "").strip()
            key, value = data.split("=")
            key = key.strip().lower()
            value = value.strip()

            if key not in self.responses:
             self.responses[key] = []

            self.responses[key].append(value)
            self.save_responses()
            return f"Learned new response for '{key}'!"
           except:
            return "Invalid format. Use: teach: keyword = response"
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