import json
import os
import random

from gpt_api import GPT_Prompt, GPT_system
from logger import log
from template.system_context import get_system_context, get_user_task

# create a function that appends a dict to a given json file
def append_to_json_file(file, data):
    with open(file, "a") as jsonFile:
        json_str = json.dumps(data) + '\n'
        jsonFile.write(json_str)

def files_in_folder_recursive(folder):
    all_files = []  # Use a different name than 'files' to avoid conflict
    for root, dirs, files in os.walk(folder):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def files_in_folder(folder):
    files = os.listdir(folder)
    return files

def get_files_of_given_type_in_folder(folder, file_type):
    if file_type[0] != ".":
        file_type = "." + file_type
    files = files_in_folder_recursive(folder)
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
    prompt.add_user_message(get_user_task() + " " + file_content)
    return file, prompt

def generate_basic_prompts_for_folder(folder_path, file_types, save_path):
    files = []
    if type(file_types) == str:
        files = get_files_of_given_type_in_folder(folder_path, file_types)
    if type(file_types) == list:
        for file_type in file_types:
            files += get_files_of_given_type_in_folder(folder_path, file_type)
    id = 0
    for file in files:
        id += 1
        file, prompt = generate_basic_prompt_for_file(file)
        basic_prompt = {
            "id": id,
            "prompt_type": "basic",
            "file": file,
            "prompt": prompt.get_prompt()
            }
        append_to_json_file(save_path, basic_prompt)

def generate_in_context_random_prompt_for_file(file):
    prompt = GPT_Prompt()
    context = get_system_context()
    prompt.set_system_context(context)
    file_content = get_file_content(file)

    random_numbers = random.sample(range(10), 3)
    examples = [load_example_prompt_json(n) for n in random_numbers]

    for example in examples:
        prompt.add_user_message(get_user_task() + " " + example["code"])
        prompt.add_assistant_message(example["answer"])
    prompt.add_user_message(get_user_task() + file_content)
    return file, prompt

def generate_in_context_random_prompts_for_folder(folder_path, file_types, save_path):
    files = []
    if type(file_types) == str:
        files = get_files_of_given_type_in_folder(folder_path, file_types)
    if type(file_types) == list:
        for file_type in file_types:
            files += get_files_of_given_type_in_folder(folder_path, file_type)
    id = 0
    for file in files:
        id += 1
        file, prompt = generate_in_context_random_prompt_for_file(file)
        in_context_random_prompt = {
            "id": id,
            "prompt_type": "in_context_random",
            "file": file,
            "prompt": prompt.get_prompt()
            }
        append_to_json_file(save_path, in_context_random_prompt)

def generate_in_context_pair_prompt_for_file(file):
    prompt = GPT_Prompt()
    context = get_system_context()
    prompt.set_system_context(context)
    file_content = get_file_content(file)

    random_numbers = random.sample(range(5), 2)
    pairs = []
    for n in random_numbers:
        pairs.append(n*2)
        pairs.append((n*2)+1)
    examples = [load_example_prompt_json(n) for n in pairs]

    for example in examples:
        prompt.add_user_message(get_user_task() + " " + example["code"])
        prompt.add_assistant_message(example["answer"])
    prompt.add_user_message(get_user_task() + file_content)
    return file, prompt

def generate_in_context_pair_prompts_for_folder(folder_path, file_types, save_path):
    files = []
    if type(file_types) == str:
        files = get_files_of_given_type_in_folder(folder_path, file_types)
    if type(file_types) == list:
        for file_type in file_types:
            files += get_files_of_given_type_in_folder(folder_path, file_type)
    id = 0
    for file in files:
        id += 1
        file, prompt = generate_in_context_pair_prompt_for_file(file)
        in_context_pair_prompt = {
            "id": id,
            "prompt_type": "in_context_pair",
            "file": file,
            "prompt": prompt.get_prompt()
            }
        append_to_json_file(save_path, in_context_pair_prompt)

def load_example_prompt_json(id):
    example_prompt = get_line_from_jsonl_file("CWE-examples/examples.jsonl", id)
    return example_prompt

def get_line_from_jsonl_file(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i == line_number:
                    return json.loads(line)
            raise ValueError("Line number exceeds the number of lines in the file.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def use_prompts_from_file(file, file_save_path):
    with open(file, "r") as f:
        for line in f:
            prompt_dic = json.loads(line)
            # ask the GPT model and save the chat
            prompt_id = prompt_dic["id"]
            prompt_type = prompt_dic["prompt_type"]
            prompt_file = prompt_dic["file"]
            prompt_list = prompt_dic["prompt"]
            prompt = GPT_Prompt()
            prompt.messages = prompt_list
            model = GPT_system()
            model.set_prompt(prompt)
            completion = model.ask_gpt()
            response = {
                "id": prompt_id,
                "prompt_type": prompt_type,
                "file": prompt_file,
                "prompt": prompt_list,
                "response": completion
            }
            append_to_json_file(file_save_path, response)
            log(file)

