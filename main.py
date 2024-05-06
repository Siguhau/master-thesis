from gpt_api import ask_test
from utils import *


path = r"C:\Users\sigur\Downloads\master-applications\scarf-beta"
php_files = get_files_of_given_type_in_folder(path, "php")


#generate_basic_prompts_to_folder(path, "php")

use_prompts_from_file("prompts/basic.jsonl")




#file = php_files[0]

#print(file)
#print(get_file_content(file))



# Get the chat from the GPT model
#ask = ask_test()


# Save the chat to a json file
#append_to_json_file("results/chats.jsonl", ask)
#append_to_json_file("results/chats.jsonl", ask)