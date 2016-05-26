from utils.build import *

#  Ex.3  encodage d'un texte contenu dans un fichier
def encodage(texte):
    F = frequencies()
    H = huffman_tree(F)
    dico = code_huffman(H)
    binary = ''
    for car in texte:
        if car in charList:
            binary = binary + dico[car]
        else:
            binary = binary + dico[' ']
    return binary
