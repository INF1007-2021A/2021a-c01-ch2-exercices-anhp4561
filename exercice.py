#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    nouveau_mot = ""
    for i in range (len(mot)):
        min = ord(mot[i])
        lettre_min = chr(min)
        maj = min - 32
        lettre_maj = chr (maj)
        #print (lettre_min)
        #print (lettre_maj)
        #upper_case = mot.replace(lettre_min,lettre_maj)
        nouveau_mot +=lettre_maj
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
