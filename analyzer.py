

import json
import os


def starts_with_yes_no_or_other(word):
    word = word.lower()
    if word.startswith('yes'):
        return 'yes'
    elif word.startswith('no'):
        return 'no'
    else:
        return 'other'
    
def contains_cwe(answer, cwe_list):
    answer = answer.lower()
    cwe_mentioned = []
    for cwe in cwe_list:
        if cwe.lower() in answer:
            cwe_mentioned.append(cwe)
    return cwe_mentioned

def save_to_file(result, path):
    path = "analyze/" + path
    #create dir if not exists
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open("analyze/"+ path, "a") as f:
        f.write(json.dumps(result) + "\n")

def analyze_results(file_path):
    cwe_list = [
    'CWE-22', 'CWE-23', 'CWE-35', 'CWE-59', 'CWE-200', 'CWE-201', 'CWE-219', 'CWE-275', 'CWE-276',
    'CWE-284','CWE-285', 'CWE-352', 'CWE-359', 'CWE-377', 'CWE-402', 'CWE-425', 'CWE-441', 'CWE-497',
    'CWE-538', 'CWE-540', 'CWE-548', 'CWE-552', 'CWE-566', 'CWE-601', 'CWE-639', 'CWE-651', 'CWE-668',
    'CWE-706', 'CWE-862', 'CWE-863', 'CWE-913', 'CWE-922', 'CWE-1275'
    ]
    results = {}
    vulnerable_files = []
    with open(file_path) as f:
        for line in f:
            data = json.loads(line)
            id = data['id']
            prompt_type = data['prompt_type']
            file = data['file']
            answer = data['response']['choices'][0]['message']['content']
            if starts_with_yes_no_or_other(answer[:5]) == 'yes':
                cwe_in_answer = contains_cwe(answer, cwe_list)
                if len(cwe_in_answer) == 0:
                    save_dict = {
                        'id': id,
                        'file': file,
                        'prompt_type': prompt_type,
                        'short_answer': 'yes',
                        'cwe_in_answer': 'None',
                        'answer': answer
                    }
                    save_to_file(save_dict, file_path)
                else:
                    save_dict = {
                        'id': id,
                        'file': file,
                        'prompt_type': prompt_type,
                        'short_answer': 'yes',
                        'cwe_in_answer': cwe_in_answer,
                        'answer': answer
                    }
                    vulnerable_files.append(file)
                    save_to_file(save_dict, file_path)
            elif starts_with_yes_no_or_other(answer[:5]) == 'no':
                save_dict = {
                    'id': id,
                    'file': file,
                    'prompt_type': prompt_type,
                    'short_answer': 'no',
                    'cwe_in_answer': 'None',
                    'answer': answer
                }
                save_to_file(save_dict, file_path)
            else:
                save_dict = {
                    'id': id,
                    'file': file,
                    'prompt_type': prompt_type,
                    'short_answer': 'other',
                    'cwe_in_answer': 'None',
                    'answer': answer
                }
                save_to_file(save_dict, file_path)

    # save vulnerable files
    save_to_file({'vulnerable_files': vulnerable_files}, "vulnerable_files.jsonl")
    
    with open("analyze/analyze/"+ file_path, "r") as f:
        inc = 0
        yes = 0
        no = 0
        other = 0
        yes_but_no_cwe = 0
        for line in f:
            inc += 1
            data = json.loads(line)
            short_answer = data['short_answer']
            if short_answer == 'yes':
                yes += 1
                cwe_in_answer = data['cwe_in_answer']
                if cwe_in_answer == 'None':
                    yes_but_no_cwe += 1
            elif short_answer == 'no':
                no += 1
            else:
                other += 1

        results = {
            'total': inc,
            'yes': yes,
            'no': no,
            'other': other,
            'yes_but_no_cwe': yes_but_no_cwe,
            'file': file_path,
        }
    save_to_file(results, "analyze_results.jsonl")
