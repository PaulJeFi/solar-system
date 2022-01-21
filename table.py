'''
Les tables permettant de calculer les éléments orbitaux des planètes.

Structure :
(remplacer par 0 si des a0, a1, a2,... ne sont pas définis ex: voir l'élément a de Mercure)

nom_planète = {
    "L": [a0, a1, a2, a3],
    "a": [a0, a1, a2, a3],
}

Pour aller plus vite, utiliser la structure type :

Planete = {
    "L": [],
    "a": [],
    "e": [],
    "i": [],
    "omega": [],
    "pi": []
}
'''

Mercure = {
    "L": [252.250_906, 149_474.072_249_1, 0.000_303_50, 0.000_000_018],
    "a": [0.387_098_310, 0, 0, 0],
    "e": [0.205_631_75, 0.000_020_407, -0.000_000_028_3, -0.000_000_000_18],
    "i": [7.004_986, 0.001_821_5, -0.000_018_10, 0.000_000_056],
    "omega": [48.330_893, 1.186_188_3, 0.000_175_42, 0.000_000_215],
    "pi": [77.456_119, 1.556_477_6, 0.000_295_44, 0.000_000_009]
}

planetes = {'mercure': Mercure}