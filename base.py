def creerGrille(nombreLignes, nombreColonnes):
     grid = [[]] * nombreLignes
     for ligne in range(nombreLignes):
        grid[ligne] = [0] * nombreColonnes
     return grid