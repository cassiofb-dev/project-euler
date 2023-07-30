import subprocess

def run_c(program_path: str):
    subprocess.check_output(['gcc', '-o', f"{program_path}.bin", program_path])
    return subprocess.check_output([f"{program_path}.bin"])

def run_python(program_path: str):
    return subprocess.check_output(['python', program_path])

def run_javascript(program_path: str):
    return subprocess.check_output(['node', program_path])

def run_solutions():
    SOLVED_PROBLEMS = 3
    LANGUAGES = [
        {
            'extension': 'c',
            'run': run_c,
        },
        {
            'extension': 'py',
            'run': run_python,
        },
        {
            'extension': 'js',
            'run': run_javascript,
        },
    ]

    for problem in range(1, SOLVED_PROBLEMS + 1):
        for language in LANGUAGES:
            extension = language.get('extension')

            program_path = f"src/{problem}/{problem}.{extension}"

            output = language.get('run')(program_path)

            file = open(f"{program_path}.txt", 'wb')

            file.write(output)

if __name__ == '__main__':
    run_solutions()
