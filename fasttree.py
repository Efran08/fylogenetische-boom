import subprocess

class FastTree:
    def __init__(self, file):
        self.file = file
    
    def run_fasttree(self):
        output_file = "output.nw"
        with open(self.output_file,"w") as out:
            subprocess.run(["FastTree", self.file], stdout=out, check=True)
        print(f"FastTree finished. Output saved to {output_file}")

    def __str__(self):
        return f"FastTree instance processing file: {self.file}"