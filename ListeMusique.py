from Constellation_map_class import*

class Musique:
    def __init__(self, nom, auteur, filename,constellation:Constellation):
        self.nom = nom
        self.auteur = auteur
        self.filename = filename
        self.constellation = []
        
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
        
    def ajouter_Nmusiques_from_filenames(songs:list):
        """songs est une liste de dictionnaire contenant le nom de la chanson, l'auteur et le chemin du fichier"""
        for song in songs:
            song_name=


