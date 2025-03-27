from ete3 import Tree

class PhyloTree:
    def __init__(self, name="Root"):
        """Initialiseer een boom met een naam."""
        self.tree = Tree(name=name)

    def create_basic_tree(self):
        """Maakt een basisboomstructuur."""
        A = self.tree.add_child(name="A")
        B = self.tree.add_child(name="B")
        C = A.add_child(name="C")
        D = C.add_sister(name="D")
        self.R = A.add_child(name="R")
        self.R.populate(6, names_library=["r1", "r2", "r3", "r4", "r5", "r6"])

    def populate_branch(self, n, branch_name="R"):
        """Voegt n extra bladeren toe aan een specifieke tak."""
        branch = self.tree.search_nodes(name=branch_name)
        if branch:
            branch[0].populate(n, random_branches=False)
        else:
            print(f"Tak '{branch_name}' niet gevonden!")

    def print_tree(self):
        """Print de boomstructuur."""
        print(self.tree.get_ascii(show_internal=True))

    def save_tree(self, filename="tree.nw"):
        """Slaat de boom op als een Newick-bestand."""
        self.tree.write(format=1, outfile=filename)
        print(f"Tree saved as {filename}")

# Gebruik de klasse
tree = PhyloTree()
tree.create_basic_tree()  # Maak een basisboom
tree.print_tree()  # Print de boom
tree.populate_branch(5, branch_name="R")  # Voeg 5 extra bladeren toe aan R
tree.print_tree()  # Print opnieuw
tree.save_tree("flexible_tree.nw")  # Sla de boom op
