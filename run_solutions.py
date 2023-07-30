import sys, subprocess

class SolutionRunner:

    def __init__(self, benchmark=False):
        self.solved_problems = 3
        self.ran_commands = []
        self.benchmark = benchmark

    def write_output(self, program_path: str, output: str):
        output_file = open(f"{program_path}.txt", "wb")
        output_file.write(output)
        output_file.close()

        results_file = open("run_solutions.txt", "a")
        results_file.write("----------------------------------------------------------------\n")
        results_file.write(f"Program: {program_path}\n")
        results_file.write(f"Output: {output}\n")
        results_file.close()

    def run_c(self, program_path: str):
        subprocess.check_output(["gcc", "-o", f"{program_path}.bin", program_path])

        command = f"{program_path}.bin"
        self.ran_commands.append(command)

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_python(self, program_path: str):
        command = ["python", program_path]
        self.ran_commands.append(command)

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_javascript(self, program_path: str):
        command = ["node", program_path]
        self.ran_commands.append(command)

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run(self):
        open("run_solutions.txt", "w").close()

        for problem in range(1, self.solved_problems + 1):
            program_path = f"src/{problem}/{problem}"

            self.run_c(f"{program_path}.c")
            self.run_python(f"{program_path}.py")
            self.run_javascript(f"{program_path}.js")

def main():
    solutionRunner = SolutionRunner()
    solutionRunner.run()

if __name__ == "__main__":
    main()
