from analyzer import analyze_results
from gpt_api import ask_test
from utils import *
from logger import log


path = r"C:\Users\sigur\Downloads\master-applications\scarf-beta"
php_files = get_files_of_given_type_in_folder(path, "php")


run_tasks(path, "scarf-beta-test-4", ["php"])