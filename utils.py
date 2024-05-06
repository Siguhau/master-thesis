import json
import os

from gpt_api import GPT_Prompt, GPT_system
from template.system_context import get_system_context

# create a function that appends a dict to a given json file
def append_to_json_file(file, data):
    with open(file, "a") as jsonFile:
        json_str = json.dumps(data) + '\n'
        jsonFile.write(json_str)


def files_in_folder(folder):
    files = os.listdir(folder)
    return files

def get_files_of_given_type_in_folder(folder, file_type):
    if file_type[0] != ".":
        file_type = "." + file_type
    files = files_in_folder(folder)
    files_of_type = [os.path.join(folder, file) for file in files if file.endswith(file_type)]

    return files_of_type

def get_file_content(file):
    with open(file, "r") as f:
        content = f.read()
    return content



def generate_basic_prompt_for_file(file):
    prompt = GPT_Prompt()
    context = get_system_context()
    prompt.set_system_context(context)
    file_content = get_file_content(file)
    prompt.add_user_message(file_content)
    return file, prompt

def generate_basic_prompts_to_folder(folder_path, file_types):
    files = get_files_of_given_type_in_folder(folder_path, file_types)
    for file in files:
        file, prompt = generate_basic_prompt_for_file(file)
        basic_prompt = {
            "prompt_type": "basic",
            "file": file,
            "prompt": prompt.get_prompt()
            }
        append_to_json_file("prompts/basic.jsonl", basic_prompt)

def use_prompts_from_file(file):
    with open(file, "r") as f:
        for line in f:
            prompt_dic = json.loads(line)
            # ask the GPT model and save the chat
            prompt_type = prompt_dic["prompt_type"]
            prompt_file = prompt_dic["file"]
            prompt_list = prompt_dic["prompt"]
            prompt = GPT_Prompt()
            prompt.messages = prompt_list
            model = GPT_system()
            model.set_prompt(prompt)
            completion = model.ask_gpt()
            response = {
                "prompt_type": prompt_type,
                "file": prompt_file,
                "prompt": prompt_list,
                "response": completion
            }
            append_to_json_file("results/basic.jsonl", response)
            print(file)

