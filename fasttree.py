"""
This script contains a class that runs FastTree and creates an image by calling newick_to_image.py.

Author: Alana Hummel, Herke Wilts
Date: 09/04/2025
Version: 1.0
"""

import subprocess, sys #import the tools

class FastTree:
    """
    This class runs FastTree and creates a phylogenetic tree. To display the image, the script newick_to_image.py is
    called.

    Return: image
    """

    def __init__(self, file, output_file="output.nw", output_image="newick.png"):
        self.file = file
        self.output_file = output_file
        self.output_image = output_image

    def run_fasttree(self, **kwargs):
        """
        This function runs FastTree and the user can specify the options. It returns a newick file.

        Paramerter: kwargs
        Return: Newick file
        """
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
        """
        This function calls the script newick_to_image.py to create an image from the newick file and returns an image.

        Return: Image
        """
        subprocess.run(
            [sys.executable, "newick_to_image.py", self.output_file, self.output_image],
            check=True) #calls the newick_to_image.py script and displays an image