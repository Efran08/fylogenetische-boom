import matplotlib
matplotlib.use('Agg')  # Headless backend, no GUI pop-up (sourced via ChatGPT)
import matplotlib.pyplot as plt
from Bio import Phylo
import argparse


def newick_to_image(newick_file, output_image="newick.png"):
    """
    This function converts a Newick file into a PNG image using Biopython and Matplotlib.

    :param newick_file: Path to the input file in Newick format
    :param output_image: Filename for the generated image (default: newick.png)
    :return: No explicit return; image is saved to disk
    """
    tree = Phylo.read(newick_file, "newick")  # Read the phylogenetic tree from the Newick file
    fig = plt.figure(figsize=(10, 5))         # Create a figure with size 10x5 inches
    ax = fig.add_subplot(1, 1, 1)             # Add a single subplot (axes) to the figure
    Phylo.draw(tree, axes=ax)                 # Draw the tree structure in the axes
    plt.savefig(output_image, dpi=300, bbox_inches='tight')  # Save the image with high resolution
    plt.close()                               # Close the figure to free memory

if __name__ == "__main__":
    """
    Makes the script runnable from the command line with two arguments:
    a Newick-format input file and the desired filename for the output image.
    """
    parser = argparse.ArgumentParser(description="Render Newick tree to image")
    parser.add_argument("newick_file", help="Input .nw file")  # The Newick file to read
    parser.add_argument("output_image", help="Output image file (e.g. tree.png)")  # Filename for the image
    args = parser.parse_args()

    newick_to_image(args.newick_file, args.output_image)  # Call the function with the given arguments
