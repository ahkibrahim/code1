class Livre : 
    def __init__(self,titre , auteur) -> None:
        self.titre = titre 
        self.auteur = auteur 
        
class Auteur:
    def __init__(self,nom) -> None:
        self.nom = nom 
        

myauteur = Auteur("aut1")
myauteur2 = Auteur("uuc")
mylivre = Livre("livre test1",myauteur)
mylivre2=Livre("livre test2",myauteur2)

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
res = mybib.ajouter_livre(mylivre2)
res = mybib.emprunter_livre(mylivre2)
print(res)
        