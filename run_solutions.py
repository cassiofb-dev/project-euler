import os, sys, subprocess

class SolutionRunner:

    def __init__(self, enable_benchmark=False):
        self.solved_problems = 5
        self.ran_commands = []
        self.enable_benchmark = enable_benchmark
        self.solution_variations = ["", "_optimized"]

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
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["gcc", "-o", f"{program_path}.bin", program_path])

        command = [f"{program_path}.bin"]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_rust(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["rustc", "-o", f"{program_path}.bin", program_path])

        command = [f"{program_path}.bin"]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_java(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        subprocess.check_output(["javac", program_path])

        class_path = program_path[:program_path.rfind('/')]

        command = [
            "java",
            "-cp",
            class_path,
            "Main",
        ]

        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_python(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        command = ["python", program_path]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_javascript(self, program_path: str):
        if os.path.isfile(program_path) == False: return

        command = ["node", program_path]
        self.ran_commands.append(" ".join(command))

        output = subprocess.check_output(command)

        self.write_output(program_path, output)

    def run_benchmark(self):
        if len(self.ran_commands) < 1: return

        output = subprocess.check_output([
            "hyperfine",
            "--shell=none",
            "--warmup",
            "100",
            "--runs",
            "100",
            *self.ran_commands,
            "--export-markdown",
            "run_solutions.md",
        ])

    def run_solution(self, problem: int):
        program_path = f"solutions/{problem}/{problem}"

        for variation in self.solution_variations:
            self.run_c(f"{program_path}{variation}.c")
            self.run_rust(f"{program_path}{variation}.rs")
            self.run_java(f"{program_path}{variation}.java")
            self.run_python(f"{program_path}{variation}.py")
            self.run_javascript(f"{program_path}{variation}.js")

    def run(self):
        open("run_solutions.txt", "w").close()

        for problem in range(1, self.solved_problems + 1):
            self.run_solution(problem)

        if self.enable_benchmark:
            self.run_benchmark()

def main():
    enable_benchmark = len(sys.argv) > 1 and sys.argv[1] == "benchmark"

    solutionRunner = SolutionRunner(enable_benchmark=enable_benchmark)
    solutionRunner.run()

if __name__ == "__main__":
    main()
