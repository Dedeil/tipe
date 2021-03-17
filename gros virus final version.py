class ordinateur(): #Une classe représente une personne/ordinateur
    def __init__(self,K=None,k=None):
        self.__clePublique=K
        self.__clePrivee=k

    def envoyerClePublique(self):
        return self.__clePublique

#####################
#Génération des clés#
#####################

    def generationCles(self,p,q,e):
        N=p*q
        indicatriceEulerN=(p-1)*(q-1)#car p et q premier entre eux
        d=self.EuclideEtendu(e,indicatriceEulerN)
        self.__clePublique=(e,N)
        self.__clePrivee=(d,N)

    def EuclideEtendu(self,a,b):
        r,r1,u,u1,v,v1=a,b,1,0,0,1
        while r1!=0:
            q=r//r1
            r,r1,u,u1,v,v1=r1,r-(q*r1),u1,u-(q*u1),v1,v-(q*v1)
        return u

########################
#Chiffrement du message#
########################

    def chiffrement(self,msg,clePublique,correspondance):
        e=clePublique[0]
        N=clePublique[1]
        print(msg)

        #Lettres en nombres
        msgNb=""
        for l in msg:
            msgNb+=correspondance[l]
        #Regroupement par groupe de chiffre
        msgTrie=[]
        while len(msgNb)>=3:
            if int(msgNb[:3])<N:
                msgTrie.append(msgNb[:3])
                msgNb=msgNb[3:]
            else:
                msgTrie.append(msgNb[:2])
                msgNb=msgNb[2:]
        if len(msgNb)>0:
            msgTrie.append(msgNb)

        #Opérations sur les nombres
        for loop in range(len(msgTrie)):
            msgTrie[loop]=str((int(msgTrie[loop])**e)%N)
            while len(msgTrie[loop])<3:
                msgTrie[loop]="0"+msgTrie[loop]
        msg=""
        for loop in msgTrie:
            msg+=loop
        return msg

##########################
#Déchiffrement du message#
##########################

    def dechiffrement(self,msg,correspondance):
        d=self.__clePrivee[0]
        N=self.__clePrivee[1]

        #Séparation du message en chiffre de moins trois nombre
        msgSep=[]
        for i in range(0,len(msg),3):
            msgSep.append(msg[i:i+3])
            while len(msgSep[-1])>1:
                if msgSep[-1][0]=="0":
                    msgSep[-1]=msgSep[-1][1:]
                else:
                    break

        #Transcription des nombres chiffré en nombres traduisible en caractères
        msgNb=""
        for i in range(len(msgSep)):
            tmp=str(int(msgSep[i])**d%N)
            msgNb+=tmp
            
        #Transcription nombres-lettres
        lettresDico=list(correspondance.keys())
        msg=""
        for i in range(0,len(msgNb),2):
            j,verif=0,True
            while verif:
                loop = list(correspondance.items())[j]
                if msgNb[i:i+2]==loop[1]:
                    msg+=loop[0]
                    verif=False
                j+=1
        return msg

correspondance={"a":"11","b":"12","c":"13","d":"14","e":"15","f":"16","g":"17","h":"18","i":"19","j":"21","k":"22","l":"23","m":"24","n":"25","o":"26","p":"27","q":"28","r":"29","s":"31","t":"32","u":"33","v":"34","w":"35","x":"36","y":"37","z":"38",",":"39","!":"41","'":"42"," ":"43"}
expediteur=ordinateur()
destinataire=ordinateur()
hacker=ordinateur()

destinataire.generationCles(307,3,7)
clePublique=destinataire.envoyerClePublique()
messageChiffre=expediteur.chiffrement("that truly is a polish moment",clePublique,correspondance)
print(messageChiffre)
msgDechiffre=destinataire.dechiffrement(messageChiffre,correspondance)
print(msgDechiffre)
