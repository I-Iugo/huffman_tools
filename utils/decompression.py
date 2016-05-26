from utils.build import *


#  Ex.4  décodage d'un fichier compressé
def decodage(textCompressed):
    tree = huffman_tree(F)
    huffman = tree
    text = ''

    # parcours de l'arbre d'Huffman en fonction du bit lu
    for bit in textCompressed:
        if bit == '0':
            tree = tree.left
        else:
            tree = tree.right

        # sur une feuille, on décode une lettre
        if Tree.isLeaf(tree):
            text = text + tree.letter
            tree = huffman
    return text
