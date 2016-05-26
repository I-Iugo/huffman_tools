from heapq import *

#  distribution de proba sur les letrres
charList = [
    ' ', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']

proba = [
    0.1835, 0.0640, 0.0064, 0.0259, 0.0260, 0.1486, 0.0078,
    0.0083, 0.0061, 0.0591, 0.0023, 0.0001, 0.0465, 0.0245,
    0.0623, 0.0459, 0.0256, 0.0081, 0.0555, 0.0697, 0.0572,
    0.0506, 0.0100, 0.0000, 0.0031, 0.0021, 0.0008]


def frequencies():
    table = {}
    n = len(charList)
    for i in range(n):
        table[charList[i]] = proba[i]
    return table

F = frequencies()


#  la classe tree
class Tree:
    def __init__(self, letter, left=None, right=None):
        self.left = left
        self.right = right
        self.letter = letter

    def isLeaf(self):
        return self.left is None and self.right is None

    def isEmpty(self):
        return self is None

    def __str__(self):
        return '<' + str(self.letter) + '.'
        + str(self.left) + '.' + str(self.right) + '>'


#  Ex.1  construction de l'tree d'Huffamn utilisant la structure
# de "tas binaire"
def huffman_tree(frequencies):
    # construction d'un tas dont les éléments sont des tuples (triplets)
    # un triplet est de la forme (proba,etiquette,tree)

    # initialisation de la collection de triplets
    heap = [(
            proba,
            letter,
            Tree(letter)
            ) for (letter, proba) in frequencies.items()]

    # mise en "tas"
    heapify(heap)

    # création de l'arbre
    while len(heap) >= 2:
        # on extrait l'arbre a1 de plus petite proba p1 étiqueté l1
        p1, l1, a1 = heappop(heap)
        # on extrait l'arbre a2 de deuxième plus petite proba p2 étiqueté l2
        p2, l2, a2 = heappop(heap)

        # on ajoute au tas le tuple corresopndant à l'tree obtenu
        # par assemblage des 2 précédents
        heappush(heap, (p1+p2, l1+l2, Tree(l1+l2, a1, a2)))

    # on retourne l'arbre d'Huffman
    return heappop(heap)[2]

#  Ex.2  construction du code d'Huffamn
def browse(tree, prefix, code):
    # sur une feuille, on peut associer son "code" à une lettre
    if Tree.isLeaf(tree):
        code[tree.letter] = prefix
        return code

    # sinon, on parcourt l'arbre en mémorisant le chemin pris
    # dans la variable prefixe
    if not tree.left.isEmpty():
        browse(tree.left, prefix + '0', code)
    if not tree.right.isEmpty():
        browse(tree.right, prefix + '1', code)


def code_huffman(tree):
    # on remplit le dictionnaire du code d'Huffman en parcourant l'arbre
    code = {}
    browse(tree, '', code)
    return code
