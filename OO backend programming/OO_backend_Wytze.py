"""
Author: Wytze Meijer
Date: 25-03-2025
Script: OO backend programming die een fylogenetische demo boom maakt."
Tools used: ETE Toolkit
"""

from ete3 import Tree

class TreeManager:
    def __init__(self):
        """Initialiseert een lege boom."""
        self.tree = Tree()

    def create_tree(self):
        """Maakt een basisboom met een vaste structuur."""
        self.tree = Tree()  # Nieuwe lege boom
        A = self.tree.add_child(name="A")
        B = self.tree.add_child(name="B")
        C = A.add_child(name="C")
        D = C.add_sister(name="D")
        R = A.add_child(name="R")
        # Voeg 6 bladeren toe aan R
        R.populate(6, names_library=["r1", "r2", "r3", "r4", "r5", "r6"])

    def populate_tree(self, n):
        """Voegt n extra willekeurige bladeren toe aan de boom."""
        self.tree.populate(n)

    def print_tree(self):
        """Print de boomstructuur."""
        print(self.tree)

    def save_tree(self, filename="tree.nw"):
        """Slaat de boom op als een Newick-bestand."""
        self.tree.write(format=1, outfile=filename)
        print(f"Tree saved as {filename}")

# Voorbeeld van hoe je de klasse gebruikt
if __name__ == "__main__":
    manager = TreeManager()
    manager.create_tree()  # Maak een standaardboom
    manager.print_tree()  # Print de boom
    manager.populate_tree(1)  # Voeg 100 willekeurige bladeren toe
    manager.print_tree()  # Print opnieuw de boom
    manager.save_tree("my_tree.nw")  # Sla de boom op
