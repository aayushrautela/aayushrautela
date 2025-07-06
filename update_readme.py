import random
import sys

readme_path = 'README.md'
facts_path = 'fun_facts.txt'
fun_fact_anchor = 'Fun fact:' # finds this text

def get_random_fact():
    with open(facts_path, 'r', encoding='utf-8') as f:
        facts = f.readlines()
    return random.choice(facts).strip()

def update_readme(new_fact_text):
    new_lines = []
    line_found = False

    with open(readme_path, 'r', encoding='utf-8') as f:
        for line in f:
            if fun_fact_anchor in line:
                parts = line.split(fun_fact_anchor)
                before_anchor = parts[0]
                
                # reconstructs the line
                new_line = f"{before_anchor}{fun_fact_anchor} ⚡ {new_fact_text}\n"
                new_lines.append(new_line)
                line_found = True
            else:
                new_lines.append(line)
    
    if not line_found:
        print(f"Error: Could not find a line containing '{fun_fact_anchor}'. Aborting.")
        sys.exit(1)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    new_fact = get_random_fact()
    update_readme(new_fact)
    print(f"Successfully updated README with fact: '{new_fact}'")