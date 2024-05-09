from analyzer import analyze_results
from gpt_api import ask_test
from utils import *
from logger import log


path = r"C:\Users\sigur\Downloads\master-applications\scarf-beta"
php_files = get_files_of_given_type_in_folder(path, "php")

"""
generate_basic_prompts_for_folder(
    path, "php", "prompts/scarf-beta/basic.jsonl")
generate_in_context_random_prompts_for_folder(
    path, "php", "prompts/scarf-beta/in_context_random.jsonl")
generate_in_context_pair_prompts_for_folder(
    path, "php", "prompts/scarf-beta/in_context_pair.jsonl")


use_prompts_from_file(
    "prompts/scarf-beta/basic.jsonl", "results/scarf-beta/basic.jsonl")
use_prompts_from_file(
    "prompts/scarf-beta/in_context_random.jsonl", "results/scarf-beta/in_context_random.jsonl")
use_prompts_from_file(
    "prompts/scarf-beta/in_context_pair.jsonl", "results/scarf-beta/in_context_pair.jsonl")

"""

#log("done")

analyze_results("results/scarf-beta/basic.jsonl")
analyze_results("results/scarf-beta/in_context_random.jsonl")
analyze_results("results/scarf-beta/in_context_pair.jsonl")





# Get the chat from the GPT model
#ask = ask_test()


# Save the chat to a json file
#append_to_json_file("results/chats.jsonl", ask)
#append_to_json_file("results/chats.jsonl", ask)