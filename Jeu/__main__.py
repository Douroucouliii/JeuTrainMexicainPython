from Domino import *
from Joueur import *
from JeuMexicain import *
from tkinter import *
from random import randint

class Vue:
    '''Classe qui modélise la Vue du jeu'''
    
    def __init__(self):
        '''Vue, JeuMexicain, Joueur -> Rien
        Constructeur de la classe Vue'''
        
        self.__cpt_fin_partie = 0 #compteur pour la fin de partie quand la pioche est vide
        self.__cpt_train_maurice = 0 #indice de où on en est dans le train de maurice
        self.__cpt_train_albert = 0 #indice de où on en est dans le train d'albert
        self.__cpt_train_ginette = 0 #indice de où on en est dans le train de ginette
        self.__cpt_train_mauricette = 0 #indice de où on en est dans le train de mauricette
        self.__cpt_train_mexicain = 0 #indice de où on en est dans le train mexicain
        self.__les_cpt = [self.__cpt_train_maurice, self.__cpt_train_albert, self.__cpt_train_ginette, self.__cpt_train_mauricette]
        
        #Création d'un objet JeuMexicain et de 4 Joueur
        
        trainMexicain = Pile()
        pioche = self.creer_pioche()
        self.__jeumexicain = JeuMexicain(trainMexicain, pioche)

        train_maurice = Pile()
        self.__reserve_maurice = self.creer_reserve()
        self.__maurice = Joueur(train_maurice, self.__reserve_maurice)
        
        train_albert = Pile()
        self.__reserve_albert = self.creer_reserve()
        self.__albert = Joueur(train_albert, self.__reserve_albert)
        
        train_ginette = Pile()
        self.__reserve_ginette = self.creer_reserve()
        self.__ginette = Joueur(train_ginette, self.__reserve_ginette)
        
        train_mauricette = Pile()
        self.__reserve_mauricette = self.creer_reserve()
        self.__mauricette = Joueur(train_mauricette, self.__reserve_mauricette)
        
        self.__liste_joueur = [self.__maurice, self.__albert, self.__ginette, self.__mauricette]
        
        self.__cptJoueur = randint(0,3)
        
        
        #Création de la fenêtre        

        self.__fenetre = Tk()
        self.__fenetre.title("Jeu de Dominos")
        self.__fenetre.geometry("500x480")
        
        
        #Création de la bibliothèque d'image
        
        self.__img = {}
        for i in range(13):
            for j in range(13):
                self.__img[str(i)+"/"+str(j)] = PhotoImage(file="images/petit-" + str(i)+"-"+str(j)+".gif")
        self.__img["-1--1"] = PhotoImage(file="images/petit--1--1.gif")
        
        
        #Création des différentes frames et de l'affichage du jeu
        
        #Frame titre et domino de départ
        self.__frame_titre = Frame()
        self.__frame_titre.pack()
        
        self.__label_titre = Label(self.__frame_titre, text="Jeu des dominos mexicains - Domino de départ :")
        self.__label_titre.grid(row=0,column=0)
        
        self.__domino_depart = Button(self.__frame_titre, bg="white", image=self.__img["-1--1"])
        self.__domino_depart.grid(row=0,column=1)
        
        #Frame train mexicain et joueur
        self.__frame_joueur = Frame()
        self.__frame_joueur.pack()
        
        #train mexicain
        self.__label_train_mexicain = Label(self.__frame_joueur, text="Train Mexicain")
        self.__label_train_mexicain.grid(row=0,column=0)
        
        self.__boutons_train_mexicain = []
        for i in range(1,6):
            btn = Button(self.__frame_joueur, bg="white", image=self.__img["-1--1"])
            btn.grid(row=0,column=i)
            self.__boutons_train_mexicain.append(btn)
        
        #train maurice
        self.__label_maurice = Label(self.__frame_joueur, text="Maurice")
        self.__label_maurice.grid(row=1,column=0)
        
        self.__boutons_train_maurice = []
        for i in range(1,6):
            btn = Button(self.__frame_joueur, bg="white", image=self.__img["-1--1"])
            btn.grid(row=1,column=i)
            self.__boutons_train_maurice.append(btn)
          
        #train albert
        self.__label_albert = Label(self.__frame_joueur, text="Albert")
        self.__label_albert.grid(row=2,column=0)
        
        self.__boutons_train_albert = []
        for i in range(1,6):
            btn = Button(self.__frame_joueur, bg="white", image=self.__img["-1--1"])
            btn.grid(row=2,column=i)
            self.__boutons_train_albert.append(btn)
            
        #train ginette
        self.__label_ginette = Label(self.__frame_joueur, text="Ginette")
        self.__label_ginette.grid(row=3,column=0)
        
        self.__boutons_train_ginette = []
        for i in range(1,6):
            btn = Button(self.__frame_joueur, bg="white", image=self.__img["-1--1"])
            btn.grid(row=3,column=i)
            self.__boutons_train_ginette.append(btn)
            
        #train mauricette
        self.__label_mauricette = Label(self.__frame_joueur, text="Mauricette")
        self.__label_mauricette.grid(row=4,column=0)
        
        self.__boutons_train_mauricette = []
        for i in range(1,6):
            btn = Button(self.__frame_joueur, bg="white", image=self.__img["-1--1"])
            btn.grid(row=4,column=i)
            self.__boutons_train_mauricette.append(btn)
            
        self.__les_trains = [self.__boutons_train_maurice,self.__boutons_train_albert,self.__boutons_train_ginette,self.__boutons_train_mauricette]
            
        #Frame réserve de joueur
        self.__frame_reserve_titre = Frame()
        self.__frame_reserve_titre.pack()
        
        self.__titre_reserve = Label(self.__frame_reserve_titre, text="Le jeu de Maurice")
        self.__titre_reserve.grid(row=0,column=0)
        
        self.__frame_reserve = Frame()
        self.__frame_reserve.pack()
        
        
        #Ici on crée les boutons de la main du joueur et on affiche sa réserve dessus
        cpt=0
        self.__boutons_main = []
        for i in range(1,5) :
            for j in range(5) :
                if cpt<10:
                    btn = Button(self.__frame_reserve, bg="white", image=self.__img[self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(cpt).str_img()])
                else:
                    btn = Button(self.__frame_reserve, bg="white", image=self.__img["-1--1"])
                self.__boutons_main.append(btn)
                btn.grid(row=i,column=j)
                cpt+=1
        
        #Frame boutton
        self.__frame_boutton = Frame()
        self.__frame_boutton.pack()
        
        self.__titre_boutton = Label(self.__frame_boutton, text="Joueur Maurice")
        self.__titre_boutton.grid(row=0,column=0)
        
        self.__boutton_go = Button(self.__frame_boutton, width=5, height=1, text="Go !", command=self.clique)
        self.__boutton_go.grid(row=0,column=1)
        
        self.__fenetre.mainloop()
        
    
        
    def creer_pioche(self):
        '''Vue -> list(Domino)
        Crée les dominos dans la pioche'''
        pioche = []
        for i in range(0,13):
            for j in range(i,13):
                pioche.append(Domino(i,j))
        return pioche
    
    def creer_reserve(self):
        '''Vue -> list(Domino)
        Pioche 10 dominos de la pioche et les met dans la main du joueur (dans sa réserve)'''
        reserve = []
        for i in range(10):
            reserve.append(self.__jeumexicain.piocher_domino())
        return reserve
    
    def clique(self):
        '''Vue -> Rien
        ajoute d'abord un domino de départ et suit les règles du jeu à chaque clique'''
        #Si la réserve du joueur est vide, on execute la fonction fin_de_partie qui gère les fins de parties
        if(self.__liste_joueur[self.__cptJoueur].len_reserve()==0):
            self.fin_de_partie()
            return
        #Si le domino de départ n'est pas affiché, on cherche le plus grand domino double du joueur (et on l'enlève de sa main), sinon on le fait piocher et on passe au joueur suivant
        self.actualiser_label_reserve()
        if not(self.__jeumexicain.domino_depart_est_choisi()):
            if(self.__liste_joueur[self.__cptJoueur].plus_grand_domino_double() != None):
                #on pose le domino sur le domino de départ
                domino = self.__liste_joueur[self.__cptJoueur].plus_grand_domino_double()
                self.__jeumexicain.placer_domino_depart(domino)
                self.__domino_depart['image'] = self.__img[domino.str_img()]
                #on enlève le domino double de la main du joueur
                reserve = self.__liste_joueur[self.__cptJoueur].reserve()
                del reserve[self.__liste_joueur[self.__cptJoueur].ind_plus_grand_domino_double()]
                #on supprime l'affichage du domino dans la réserve (main du joueur)
                for j in range(self.__liste_joueur[self.__cptJoueur].ind_plus_grand_domino_double(), len(self.__boutons_main)-1):
                    self.__boutons_main[j]['text'] = self.__boutons_main[j+1]['text']
                return
            else:
                self.piocher_domino_reserve()
                self.prochain_joueur()
                return
            return
        #On parcourt la reserve du joueur qui joue
        for i in range(len(self.__liste_joueur[self.__cptJoueur].reserve())):
            #si le joueur n'a pas de domino posé sur son train on regarde quel domino peut être placé après le domino de départ
            if self.__les_cpt[self.__cptJoueur]==0 and self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).peutEtrePlaceApres(self.__jeumexicain.domino_depart()):
                #on permute le domino si il est dans le mauvais sens
                if(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).faceB() == self.__jeumexicain.domino_depart().faceB()):
                    self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).permute()
                self.actualiser_train_reserve(i)
                self.prochain_joueur()
                self.__cpt_fin_partie=0
                return
            #si le joueur a déjà un domino sur son train, on fait pareil sauf qu'on regarde le dernier domino dans le train du joueur
            elif self.__les_cpt[self.__cptJoueur]>=1 and self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).peutEtrePlaceApres(self.__liste_joueur[self.__cptJoueur].dernier_domino_train()):
                #on permute le domino si il est dans le mauvais sens
                if(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).faceB() == self.__liste_joueur[self.__cptJoueur].dernier_domino_train().faceB()):
                    self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).permute()
                self.actualiser_train_reserve(i)
                self.prochain_joueur()
                self.__cpt_fin_partie=0
                return
            #si le jeu mexicain n'a pas de domino posé sur son train on regarde quel domino peut être placé après le domino de départ
            elif self.__cpt_train_mexicain==0 and self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).peutEtrePlaceApres(self.__jeumexicain.domino_depart()):
                #on permute le domino si il est dans le mauvais sens
                if(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).faceB() == self.__jeumexicain.domino_depart().faceB()):
                    self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).permute()
                self.actualiser_mexicain_reserve(i)
                self.prochain_joueur()
                self.__cpt_fin_partie=0
                return
            #si le jeu mexicain a déjà un domino posé sur son train on regarde quel domino peut être placé après sur son train
            elif self.__cpt_train_mexicain>=1 and self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).peutEtrePlaceApres(self.__jeumexicain.dernier_domino_train_mexicain()):
                #on permute le domino si il est dans le mauvais sens
                if(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).faceB() == self.__jeumexicain.dernier_domino_train_mexicain().faceB()):
                    self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).permute()
                self.actualiser_mexicain_reserve(i)
                self.prochain_joueur()
                self.__cpt_fin_partie=0
                return        
        #si on a pas trouvé de domino, on pioche (si elle est pas vide), et on l'ajoute à la main du joueur
        if(self.__jeumexicain.len_pioche()!=0):
            self.piocher_domino_reserve()
            return
        #si la pioche est vide, on passe au prochain joueur tant que tout le monde ne peut plus poser de domino puis on execute la fonction qui gère les fins de parties
        else:
            if(self.__cpt_fin_partie >=5):
                self.fin_de_partie()
                return
            else:
                self.__cpt_fin_partie += 1
                self.prochain_joueur()
                    
    def actualiser_train_reserve(self, i):
        '''Vue, int -> rien
        place le domino d'indice i sur le train du joueur, supprime le domino de la main du joueur'''
        if(self.__les_cpt[self.__cptJoueur]>=5):
            for j in range(0,4):
                self.__les_trains[self.__cptJoueur][j]['image'] = self.__les_trains[self.__cptJoueur][j+1]['image']
            self.__les_cpt[self.__cptJoueur]=4
        #empile le domino sur le train
        self.__liste_joueur[self.__cptJoueur].placer_domino_sur_train(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i))
        #affiche le domino sur le train
        self.__les_trains[self.__cptJoueur][self.__les_cpt[self.__cptJoueur]]['image'] = self.__img[self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).str_img()]
        #supprime le domino de la réserve (main du joueur)
        reserve = self.__liste_joueur[self.__cptJoueur].reserve()
        del reserve[i]
        #supprime l'affichage du domino dans la réserve (main du joueur)
        for j in range(i, len(self.__boutons_main)-1):
            self.__boutons_main[j]['image'] = self.__boutons_main[j+1]['image']
        #on passe au prochain joueur
        self.__les_cpt[self.__cptJoueur] += 1
        
    def actualiser_mexicain_reserve(self, i):
        '''Vue, int -> rien
        place le domino d'indice i sur le train mexicain, supprime le domino de la main du joueur'''
        if(self.__cpt_train_mexicain>=5):
            for j in range(0,4):
                self.__boutons_train_mexicain[j]['image'] = self.__boutons_train_mexicain[j+1]['image']
            self.__cpt_train_mexicain=4
        #empile le domino sur le train
        self.__jeumexicain.placer_domino_sur_train_mexicain(self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i))
        #affiche le domino sur le train
        self.__boutons_train_mexicain[self.__cpt_train_mexicain]['image'] = self.__img[self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(i).str_img()]
        #supprime le domino de la réserve (main du joueur)
        reserve = self.__liste_joueur[self.__cptJoueur].reserve()
        del reserve[i]
        #supprime l'affichage du domino dans la réserve (main du joueur)
        for j in range(i, len(self.__boutons_main)-1):
            self.__boutons_main[j]['image'] = self.__boutons_main[j+1]['image']
        #on passe au prochain joueur
        self.__cpt_train_mexicain += 1
    
    def prochain_joueur(self):
        '''Vue -> rien
        passer au prochain joueur (incrémente le cpt par 1) et donc actualise la réserve de boutons, et le texte'''
        cpt=0
        self.__cptJoueur += 1
        if(self.__cptJoueur==4):
            self.__cptJoueur=0
        for boutons in self.__boutons_main:
            boutons['image'] = self.__img["-1--1"]
        for boutons in self.__boutons_main:
            if(cpt >= self.__liste_joueur[self.__cptJoueur].nombre_de_domino_restant()):
                boutons['image'] = self.__img["-1--1"]
            else:
                boutons['image'] = self.__img[self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(cpt).str_img()]
                cpt+=1
        self.actualiser_label_reserve()
        
    def actualiser_label_reserve(self):
        '''Vue -> rien
        Actualise le label de la reserve selon qui doit jouer'''
        if(self.__cptJoueur==0):
            self.__titre_reserve['text']="Le jeu de Maurice"
            self.__titre_boutton['text']="Joueur Maurice"
        elif(self.__cptJoueur==1):
            self.__titre_reserve['text']="Le jeu d'Albert"
            self.__titre_boutton['text']="Joueur Albert"
        elif(self.__cptJoueur==2):
            self.__titre_reserve['text']="Le jeu de Ginette"
            self.__titre_boutton['text']="Joueur Ginette"
        elif(self.__cptJoueur==3):
            self.__titre_reserve['text']="Le jeu de Mauricette"
            self.__titre_boutton['text']="Joueur Mauricette"
    
    def piocher_domino_reserve(self):
        '''Vue -> rien
        pioche un domino de la réserve et l'ajoute dans la main du joueur (reserve et label)'''
        domino = self.__jeumexicain.piocher_domino()
        self.__liste_joueur[self.__cptJoueur].reserve().append(domino)
        self.__boutons_main[self.__liste_joueur[self.__cptJoueur].nombre_de_domino_restant()-1]['image'] = self.__img[self.__liste_joueur[self.__cptJoueur].i_eme_domino_de_la_reserve(self.__liste_joueur[self.__cptJoueur].nombre_de_domino_restant()-1).str_img()]
        self.prochain_joueur()
        
    def fin_de_partie(self):
        '''Vue -> rien
        Gère les différentes fin de parties'''
        if(self.__liste_joueur[self.__cptJoueur].len_reserve()==0):
            self.__boutton_go["state"] = DISABLED
            frame_gagnant = Frame()
            frame_gagnant.pack()
            
            gagnant = Label(frame_gagnant, text="Le joueur gagnant est " + self.txt_joueur())
            gagnant.grid(row=0,column=0)
            txt = Label(frame_gagnant, text="car le joueur ne possède plus aucun domino")
            txt.grid(row=1,column=0)
            
        elif(self.__jeumexicain.len_pioche()==0):
            self.__boutton_go["state"] = DISABLED
            frame_gagnant = Frame()
            frame_gagnant.pack()
            
            gagnant = Label(frame_gagnant, text="Le joueur gagnant est " + self.compter_valeur_domino()[0])
            gagnant.grid(row=0,column=0)
            txt = Label(frame_gagnant, text="Valeur Maurice : " + str(self.compter_valeur_domino()[1]) + ", valeur Albert : " + str(self.compter_valeur_domino()[2]) + ", valeur Ginette : " + str(self.compter_valeur_domino()[3]) + ", valeur Mauricette : " + str(self.compter_valeur_domino()[4]))
            txt.grid(row=1,column=0)
            
        
        
    def txt_joueur(self):
        '''Vue -> str
        retourne une chaine de caractère avec le nom du joueur'''
        if(self.__cptJoueur==0):
            return "Maurice"
        elif(self.__cptJoueur==1):
            return "Albert"
        elif(self.__cptJoueur==2):
            return "Ginette"
        elif(self.__cptJoueur==3):
            return "Mauricette"
        
    def compter_valeur_domino(self):
        '''Vue -> str
        compte les points de tout les dominos des joueurs et retourne
        la chaine de caractère avec le nom du joueur qui a le moins de points'''
        chaine = ""
        point_maurice = 0
        point_albert = 0
        point_ginette = 0
        point_mauricette = 0
        mini = 0
        joueur = 0
        for domino in self.__liste_joueur[0].reserve():
            point_maurice += domino.faceA()
            point_maurice += domino.faceB()
            mini = point_maurice
            joueur = 0
        for domino in self.__liste_joueur[1].reserve():
            point_albert += domino.faceA()
            point_albert += domino.faceB()
        if mini>point_albert:
            mini = point_albert
            joueur = 1
        for domino in self.__liste_joueur[2].reserve():
            point_ginette += domino.faceA()
            point_ginette += domino.faceB()
        if mini>point_ginette:
            mini = point_ginette
            joueur = 2
        for domino in self.__liste_joueur[3].reserve():
            point_mauricette += domino.faceA()
            point_mauricette += domino.faceB()
        if mini>point_mauricette:
            mini = point_mauricette
            joueur = 3
        self.__cptJoueur = joueur
        return [self.txt_joueur(),point_maurice,point_albert,point_ginette,point_mauricette]


if __name__ == '__main__' :
    mon_appli = Vue()