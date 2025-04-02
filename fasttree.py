import subprocess

class FastTree:
    def __init__(self, file):
        self.file = file
        self.output_file = "output.nw"
        self.output_newick = "newick.png"
    
    def run_fasttree(self):
        with open(self.output_file, "w") as nw_out:
            subprocess.run(["FastTree", self.file], stdout=nw_out, check=True)
        print(f"FastTree finished. Output saved to {self.output_file}")
        
    def run_ete_toolkit(self):
        with open(self.output_newick, "w") as img_out:
            subprocess.run(["/homes/hjwilts/ete_env/bin/ete3", "view", "-t", self.output_file], stdout=img_out, check=True)
        
    def __str__(self):
        return f"FastTree instance processing file: {self.file}"