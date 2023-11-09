#Ici on crée la classe JeuMexicain:

from Domino import *
from pilefile import *
import random

class JeuMexicain:
    '''Classe qui modélise le jeu mexicain ainsi que les différentes méthodes pour le manipuler'''
    
    def __init__(self, trainMexicain, pioche, dominoDepart=None):
        '''JeuMexicain, Pile, list(Domino), Domino -> Rien
        Constructeur de la classe JeuMexicain, le jeu mexicain est caractérisé
        par un domino de départ, le train mexicain ainsi que la pioche
        '''
        self.__dominoDepart = dominoDepart
        self.__trainMexicain = trainMexicain
        self.__pioche = pioche
    
    def strpioche(self):
        return self.__pioche
    
    def len_pioche(self):
        '''JeuMexicain -> int
        Retourne la taille de la pioche
        (sert ici à tester mes autres méthodes et à m'assurer que l'application fonctionne)'''
        return len(self.__pioche)
    
    def domino_depart_est_choisi(self):
        '''JeuMexicain -> Boolean
        Teste si un domino de départ a été choisi'''
        if(self.__dominoDepart == None):
            return False
        return True
    
    def domino_depart(self):
        '''JeuMexicain -> Domino
        retourne le domino de départ'''
        return self.__dominoDepart
    
    def placer_domino_depart(self, domino):
        '''JeuMexicain, Domino -> Rien
        place un domino comme domino de départ'''
        self.__dominoDepart = domino
    
    def dernier_domino_train_mexicain(self):
        '''JeuMexicain -> Domino
        retourne le dernier domino du train mexicain
        '''
        assert not self.__trainMexicain.est_vide()
        res = self.__trainMexicain.depiler()
        self.__trainMexicain.empiler(res)
        return res
    
    def placer_domino_sur_train_mexicain(self, domino):
        '''JeuMexicain, Domino -> Rien
        pose une domino sur le train mexicain (en supposant qu'il est correct)'''
        self.__trainMexicain.empiler(domino)
        
    def piocher_domino(self):
        '''JeuMexicain -> Domino
        retourne une domino au hasard de la pioche et l'enlève de la liste'''
        assert len(self.__pioche) != 0
        random_index = random.randint(0, len(self.__pioche)-1)
        domino = self.__pioche[random_index]
        del self.__pioche[random_index]
        return domino
    
    def pioche_est_vide(self):
        '''JeuMexicain -> Boolean
        teste si la pioche est vide'''
        return (len(self.__pioche) == 0)
    
    def train_mexicain_demarre(self):
        '''JeuMexicain -> Boolean
        teste si le train mexicain a démarré'''
        return not (self.__trainMexicain.est_vide())