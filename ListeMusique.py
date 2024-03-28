from Constellation_map_class import*

class Musique:
    def __init__(self, nom, auteur, constellation:Constellation):
        self.nom = nom
        self.auteur = auteur
        self.constellation = constellation.get_cmap()
        
class ListeMusiques:
    def __init__(self):
        self.musiques = []

    def ajouter_musique(self, nom, auteur, constellation:Constellation):
        musique = Musique(nom, auteur, constellation)
        self.musiques.append(musique)

    def afficher_infos(self):
        for musique in self.musiques:
            print("Nom:", musique.nom)
            print("Auteur:", musique.auteur)
            print("Constellation:", musique.constellation)
            print()


