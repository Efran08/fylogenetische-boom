import subprocess, sys

class FastTree:
    def __init__(self, file, output_file="output.nw", output_image="newick.png"):
        self.file = file
        self.output_file = output_file
        self.output_image = output_image

    def run_fasttree(self):
        with open(self.output_file, "w") as nw_out:
            subprocess.run(["FastTree", self.file], stdout=nw_out, check=True)

    def render_tree_image(self):
        subprocess.run(
            [sys.executable, "newick_to_image.py", self.output_file, self.output_image],
            check=True)