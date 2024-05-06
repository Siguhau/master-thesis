from openai import OpenAI
from key import api_key

class GPT_Prompt:
    def __init__(self, ):
        self.messages = []
        self.system_context = []

    def create_message(self, role, content):
        return {"role": role, "content": content}
    
    def set_system_context(self, context):
        self.system_context = [self.create_message("system", context)]

    def add_message(self, role, content):
        self.messages.append(self.create_message(role, content))

    def add_user_message(self, content):
        self.add_message("user", content)
    
    def add_assistant_message(self, content):
        self.add_message("assistant", content)
    
    def get_prompt(self):
        return self.system_context + self.messages

class GPT_system:
    def __init__(self, ):
        self.client = OpenAI(api_key = api_key())
        self.model = "gpt-4-turbo-2024-04-09"
        self.prompt = GPT_Prompt()

    def set_prompt(self, prompt):
        self.prompt = prompt

    def ask_gpt(self):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.prompt.get_prompt()
        )
        return completion.to_dict()
    
    def get_chat(self):
        prompt = self.prompt.get_prompt()
        completion = self.ask_gpt()
        chat = {"input_prompt": prompt, "response": completion}
        return chat

"""
def ask_basic(context, question):
    model = GPT_system()
    model.set_system_context(context)
    model.add_message("user", question)
    chat = model.get_chat()
    return chat

def ask_in_context(context, messages):
    model = GPT_system()
    model.set_system_context(context)
    for message in messages:
        model.add_message(message["role"], message["content"])
    chat = model.get_chat()
    return chat
"""

def ask_test():
    model = GPT_system()
    prompt = GPT_Prompt()
    prompt.set_system_context("Act as a math teacher explaining simple concepts to a student.")
    prompt.add_message("user", "how do you add two numbers together? use max five sentences.")
    prompt.add_message("assistant", "take the first number and add to it the second number. The result is the sum of the two numbers.")
    prompt.add_message("user", "how do you subtract two numbers? use max five sentences.")
    chat = model.get_chat()
    return chat

