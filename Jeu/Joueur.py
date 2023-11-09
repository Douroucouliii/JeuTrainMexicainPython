#Ici on crée la classe Joueur:

from Domino import *
from pilefile import *
from JeuMexicain import *

class Joueur:
    '''Classe qui modélise un joueur ainsi que les différentes méthodes pour l'intéraction du joueur avec le jeu'''
    
    def __init__(self, train, reserve):
        '''Joueur, Pile, list(Domino) -> Rien
        Constructeur de la classe Joueur, un joueur est
        caractarisé par son train et la réserve'''
        self.__train = train
        self.__reserve = reserve
    
    def len_reserve(self):
        '''Joueur -> int
        retourne la longueur de la réserve du joueur'''
        return len(self.__reserve)
    
    def reserve(self):
        '''Joueur -> list(Domino)
        retourne la réserve du joueur'''
        return self.__reserve
    
    def ind_plus_grand_domino_double(self):
        '''Joueur -> int
        retourne la valeur du plus grand domino double du joueur (-1) si il n'en a pas'''
        cpt=0
        maxi=-1
        ind=-1
        for domino in self.__reserve:
            if domino.estDouble() and domino.faceA() > maxi:
                ind=cpt
                maxi=domino.faceA()
            cpt+=1
        return ind
    
    def plus_grand_domino_double(self):
        '''Joueur -> Domino
        retourne le plus grand domino double du joueur None si il n'en a pas'''
        domino = None
        maxi = 0
        for i in self.__reserve:
            if i.estDouble() and i.faceA() > maxi:
                domino = i
                maxi = i.faceA()
        return domino
    
    def premier_domino_sur_train(self):
        '''Joueur -> Domino
        retourne le premier domino qui peut être posé sur le train du joueur'''
        for domino in self.__reserve:
            domino_train = self.__train.depiler()
            if domino.peutEtrePlaceApres(domino_train):
                self.__train.empiler(domino_train)
                return domino
            self.__train.empiler(domino_train)
        return None
    
    def premier_domino_sur_train_mexicain(self, jeu):
        '''Joueur, JeuMexicain -> Domino
        retourne le premier domino qui peut être posé sur le train mexicain'''
        for domino in self.__reserve:
            domino_train_mexicain = jeu.dernier_domino_train()
            if domino.peutEtrePlaceApres(domino_train_mexicain):
                return domino
        return None
    
    def train_demarre(self):
        '''Joueur -> Boolean
        teste si le train du joueur a démarré ou non'''
        return not (self.__train.est_vide())
    
    def placer_domino_sur_train(self, domino):
        '''Joueur, Domino -> Rien
        pose une domino sur le train (en supposant qu'il est correct)'''
        self.__train.empiler(domino)
        
    def nombre_de_domino_restant(self):
        '''Joueur -> int
        retourne le nombre de domino restant dans la réserve du joueur'''
        cpt=0
        for domino in self.__reserve:
            cpt+=1
        return cpt
            
    def i_eme_domino_de_la_reserve(self, i):
        '''Joueur, int -> Domino
        retourne le i ème domino de la réserve'''
        return self.__reserve[i]
    
    def piocher_et_actualiser_reserve(self, jeu):
        '''Joueur, JeuMexicain -> Domino
        pioche un domino de la pioche du JeuMexicain et actualise la réserve du joueur'''
        domino_pioche = jeu.piocher_domino()
        self.__reserve.append(domino_pioche)
        return domino_pioche
    
    def dernier_domino_train(self):
        '''Joueur -> Domino
        retourne le dernier domino du train du joueur'''
        assert not self.__train.est_vide()
        res = self.__train.depiler()
        self.__train.empiler(res)
        return res