import subprocess, sys

class FastTree:
    def __init__(self, file, output_file="output.nw", output_image="newick.png"):
        self.file = file
        self.output_file = output_file
        self.output_image = output_image

    def run_fasttree(self, **kwargs):
        # Extract options from kwargs (with default values if not provided)
        gvn_args1 = kwargs.get('speed', '')  # Default to empty string if no speed is provided
        gvn_args2 = kwargs.get('model', '')  # Default to empty string if no model is provided

        # Make sure that you only add arguments that are not empty
        cmd = ["FastTree"]

        # Only add options if they are not empty
        if gvn_args1:  # e.g., '-faster' or '-slower'
            cmd.append(gvn_args1)

        if gvn_args2:  # e.g., '-gtr', '-jc', etc.
            cmd.append(gvn_args2)

        # Add the input file path at the end of the command
        cmd.append(self.file)

        # Run the FastTree command and write output to the output file
        with open(self.output_file, "w") as nw_out:
            subprocess.run(cmd, stdout=nw_out, check=True)
    def render_tree_image(self):
        subprocess.run(
            [sys.executable, "newick_to_image.py", self.output_file, self.output_image],
            check=True)