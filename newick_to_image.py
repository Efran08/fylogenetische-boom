"""
This script turns a newick file into an image. This script gets the information from fasttree.py and plots it.

Author: Herke Wilts, Alana Hummel
Date: 09/04/2025
Version: 1.0
"""


import matplotlib #import the tools
matplotlib.use('Agg')  # Headless backend, no GUI pop-up
import matplotlib.pyplot as plt
from Bio import Phylo
import argparse

def newick_to_image(newick_file, output_image="newick.png"):
    """
    This function plots the information from the newick file into an image.

    :param newick_file:
    :param output_image:
    :return: image
    """
    tree = Phylo.read(newick_file, "newick")
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=ax)
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    """
    This function addresses the information given in the command line given by the user. 
    """
    parser = argparse.ArgumentParser(description="Render Newick tree to image")
    parser.add_argument("newick_file", help="Input .nw file")
    parser.add_argument("output_image", help="Output image file (e.g. tree.png)")
    args = parser.parse_args()

    newick_to_image(args.newick_file, args.output_image)