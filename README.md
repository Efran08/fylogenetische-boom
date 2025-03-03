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