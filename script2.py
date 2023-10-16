class Livre : 
    def __init__(self,titre , auteur) -> None:
        self.titre = titre 
        self.auteur = auteur 
        
class Auteur:
    def __init__(self,nom) -> None:
        self.nom = nom 
        

myauteur = Auteur("aut1")
mylivre = Livre("livre test1",myauteur)

class Bibliotheque :
    def __init__(self) -> None:
        self.collection = []
        
    def emprunter_livre(self,livre):
        if livre in self.collection :
            self.collection.remove(livre)
            return f"{livre.titre} a ete emprunte"
        else :
            return "le livre n'est pas disponible"
    
    
    def ajouter_livre(self,livre):
        self.collection.append(livre)
        
    
    
        
        

mybib = Bibliotheque()
res = mybib.ajouter_livre(mylivre)
res = mybib.emprunter_livre(mylivre)
print(res)
        