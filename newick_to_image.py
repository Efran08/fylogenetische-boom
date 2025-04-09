import matplotlib
matplotlib.use('Agg')  # Headless backend, no GUI pop-up
import matplotlib.pyplot as plt
from Bio import Phylo
import argparse

def newick_to_image(newick_file, output_image="newick.png"):
    tree = Phylo.read(newick_file, "newick")
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=ax)
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render Newick tree to image")
    parser.add_argument("newick_file", help="Input .nw file")
    parser.add_argument("output_image", help="Output image file (e.g. tree.png)")
    args = parser.parse_args()

    newick_to_image(args.newick_file, args.output_image)