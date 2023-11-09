#Ici on crée la classe Domino:

class Domino:
    '''Classe qui modélise un domino ainsi que les différentes méthodes pour manipuler les dominos'''
    
    def __init__(self, face_a, face_b):
        '''Domino, int, int -> Rien
        Constructeur de la classe domino, un domino est caractérisé par sa valeur à gauche et à droite
        '''
        self.__face_a = face_a
        self.__face_b = face_b
        
    def faceA(self):
        '''Domino -> int
        retourne la valeur de la face a du domino'''
        return self.__face_a
    
    def faceB(self):
        '''Domino -> int
        retourne la valeur de la face b du domino'''
        return self.__face_b
        
    def estDouble(self):
        '''Domino -> Boolean
        Teste qui le domino est double'''
        return (self.__face_a == self.__face_b)
    
    def peutEtrePlaceApres(self, domino):
        '''Domino, Objet -> Boolean
        Teste si le domino courant peut être placé après domino'''
        return ((domino.__face_b == self.__face_a) or(domino.__face_b == self.__face_b))
    
    def str(self):
        '''Domino -> str
        Affiche un domino sous la forme "face A | face B"'''
        chaine = ""
        chaine += str(self.__face_a)
        chaine += " | "
        chaine += str(self.__face_b)
        return chaine
    
    def str_img(self):
        '''Domino -> str
        Affiche le nom du domino sous la forme face_a/face_b'''
        chaine = ""
        chaine += str(self.__face_a)
        chaine += "/"
        chaine += str(self.__face_b)
        return chaine
    
    def permute(self):
        '''Domino -> Rien
        Permute les deux faces d'un domino'''
        self.__face_a, self.__face_b = self.__face_b, self.__face_a