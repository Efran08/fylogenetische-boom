# The Magic Tree

Version 1.0 03/03/25

### Product description
This readme belongs to a website called The Magic Tree. The Magic Tree is able to display a phylogenetic tree. This 
tree is customizable through files the user is able to upload and the user can choose different parameters from a given 
selection. The changeable parameters are the speed, the model and how the first line will be read. The user can choose
between a standard, faster or slower speed. The  slower the speed, the more accurate the tree will be. The model is 
decided from the type of sequence the user uploads. When the user uploads an aminoacid sequence, the CLI will use the 
WAG model. When the user uploads a nucleotide sequence, the CLI will use the GTR model. More explanation on these 
models can be found on the website. The last parameter to choose is when the program stops with reading the first line. 
For instance when the user uploads a FASTA file. In the FASTA file the first line contains information about the 
sequence and it starts with ">". The default here is to quit reading the line that starts with ">" after the first word. 
If the upload does not have a ">", the default setting is to read the whole line. 

First, the uploaded file will be formatted to a Newick file. This file will be formatted with the tool Fasttree and
when the Newick file is made, it will be visualised by ETE Toolkit. ETE Toolkit will return a SVG that will be 
displayed on the website.

### Install instructions
Voor het installeren van het programma ETE toolkit gebruiken we de commando’s:
* python3 -m venv ete_env
* source ete_env/bin/activate
* pip install ete3

Dit zorgt ervoor dat we ETE toolkit kunnen installeren zonder admin privileges

Voor het installeren van het programma Fasttree gebruiken we:
* wget http://www.microbesonline.org/fasttree/FastTree -O ~/FastTree
* chmod +x ~/FastTree
* echo 'export PATH=$HOME:$PATH' >> ~/.bashrc 
* source ~/.bashrc

### System requirements
* Debian-gebaseerde versie van Linux
* Python 3

### Commandline arguments
Step 1: Generating a Phylogenetic Tree with FastTree
A basic phylogenetic tree for nucleotide sequences can be generated with:
FastTree -nt input.fasta > output.tree
This command reads the FASTA file (input.fasta), calculates a phylogenetic tree, and saves it in output.tree.

If you prefer a more accurate tree at the cost of speed, you can use the -slower option along with the GTR model, which is more advanced than the default Jukes-Cantor model:
FastTree -nt -gtr -slower input.fasta > output.tree

On the other hand, if you're working with protein sequences and want a faster analysis, you can use the WAG model with the -faster option:
FastTree -wag -faster input.fasta > output.tree

Sometimes, FASTA headers contain spaces, and by default, FastTree only reads the first word. To ensure the full header is used, include the -quote option:
FastTree -nt -quote input.fasta > output.tree

Step 2: Visualizing the Tree with ETE Toolkit
Now that we have a tree in Newick format, we need a way to visualize it. This is where ETE Toolkit comes into play.

To generate a PNG image of the tree, run:
ete3 view -t output.tree -o tree.png --format png

If you prefer an SVG file and want to adjust the image size (e.g., 800x600 pixels), use:
ete3 view -t output.tree -o tree.svg --format svg --width 800 --height 600

For a PDF version, simply use:

ete3 view -t output.tree -o tree.pdf --format pdf

### Authors
Herke Wilts: hj.wilts@st.hanze.nl
Gea Bakker: g.a.bakker@st.hanze.nl
Efran Huliselan: ee.huliselan@st.hanze.nl
Alana Hummel: a.e.hummel@st.hanze.nl
Wytze Meijer: wh.meijer@st.hanze.nl

### References and licenses
To build the phylogenetic trees we use fasttree. Fasttree is a program that builds phylogenetic trees to compare species or determine what species organism belong to.
Fasttree is an CLI tool and uses FASTA- or phylipfiles to build Newick phylogenetic tree formats.

We also use visualization tool ETE Toolkit. This tool can read a Newick file and save or change it as an SVG, PNG, or PDF.
