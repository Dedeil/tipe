from tkinter import *

class ordinateur(): #Une classe represente une personne/ordinateur
    def __init__(self,K=None,k=None):
        self.__clePublique=K
        self.__clePrivee=k

    def envoyerClePublique(self):
        if self.__clePrivee[0]>=0:
            return self.__clePublique
        else:
            return False

#####################
#Generation des cles#
#####################

    def generationCles(self,p,q,e):
        N=p*q
        indicatriceEulerN=(p-1)*(q-1)#car p et q premier entre eux
        print("Phi(N)="+str(indicatriceEulerN))
        d=self.EuclideEtendu(e,indicatriceEulerN)
        self.__clePublique=(e,N)
        print("K=(e,N)="+str(self.__clePublique))
        self.__clePrivee=(d,N)
        print("k=(d,N)="+str(self.__clePrivee))

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

        #Lettres en nombres
        msgNb=""
        for l in msg:
            msgNb+=correspondance[l]
        print("Message transcrit : "+str(msgNb))
        #Regroupement par groupe de chiffre
        msgTrie=[]
        while len(msgNb)>=len(str(N)):
            if int(msgNb[:len(str(N))])<N:
                msgTrie.append(msgNb[:len(str(N))])
                msgNb=msgNb[len(str(N)):]
            else:
                msgTrie.append(msgNb[:len(str(N))-1])
                msgNb=msgNb[len(str(N))-1:]
        if len(msgNb)>0:
            msgTrie.append(msgNb)

        #Operations sur les nombres
        for loop in range(len(msgTrie)):
            msgTrie[loop]=str((int(msgTrie[loop])**e)%N)
            while len(msgTrie[loop])<3:
                msgTrie[loop]="0"+msgTrie[loop]
        msg=""
        for loop in msgTrie:
            msg+=loop
        return msg

##########################
#Dechiffrement du message#
##########################

    def dechiffrement(self,msg,correspondance):
        d=self.__clePrivee[0]
        N=self.__clePrivee[1]

        #Separation du message en chiffre de moins trois nombre
        msgSep=[]
        while len(msg)>=len(str(N)):
            if int(msg[:len(str(N))])<N:
                msgSep.append(msg[:len(str(N))])
                msg=msg[len(str(N)):]
            else:
                msgSep.append(msg[:len(str(N))-1])
                msg=msg[len(str(N))-1:]
        if len(msg)>0:
            msgSep.append(msg)

        #Transcription des nombres chiffre en nombres traduisible en caracteres
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
                    #print(loop[0])
                j+=1
        return msg

def verifNbPremier(x):
    if x>=2:
        for i in range(2,x//2+1):
            if x%i==0:
                print(str(x)+" n'est pas un nombre premier!\n")
                return False
        return True
    print(str(x)+" est inferieur a 1!\n")
    return False

def verifSontPremier(x,y):
    moitie=min(x,y)//2+1
    for i in range(2,moitie):
        if x%i==0 and y%i==0:
            print(str(x)+" et "+str(y)+" ne sont pas premier entre eux!\n")
            return False
    return True

def demarrer():
    msg=entryVarMsg.get()
    e=entryVarE.get()
    p=entryVarP.get()
    q=entryVarQ.get()
    if verifNbPremier(p) and verifNbPremier(q) and verifSontPremier(e,(p-1)*(q-1)):
        destinataire=ordinateur()

        destinataire.generationCles(p,q,e)
        clePublique=destinataire.envoyerClePublique()

        if clePublique!=False:
            correspondance={"a":"11","b":"12","c":"13","d":"14","e":"15","f":"16","g":"17","h":"18","i":"19","j":"21","k":"22","l":"23","m":"24","n":"25","o":"26","p":"27","q":"28","r":"29","s":"31","t":"32","u":"33","v":"34","w":"35","x":"36","y":"37","z":"38",",":"39","!":"41","'":"42"," ":"43"}

            expediteur=ordinateur()
            hacker=ordinateur()
            
            messageChiffre=expediteur.chiffrement(msg,clePublique,correspondance)
            print("Message chiffre : "+str(messageChiffre))
            msgDechiffre=destinataire.dechiffrement(messageChiffre,correspondance)
            print("Message dechiffre : "+msgDechiffre+"\n")
        else:
            print("d est negatif!\n")

f=Tk()
f.title("Chiffrement/dechiffrement")

global entryVarMsg
global entryVarE
global entryVarP
global entryVarQ
entryVarMsg=StringVar()
entryVarE=IntVar()
entryVarP=IntVar()
entryVarQ=IntVar()
entryVarMsg.set("maths")
entryVarE.set(307)
entryVarP.set(13)
entryVarQ.set(11)

labelMsg=Label(f,text="Entrez votre message:").grid(row=0,column=0)
entryMsg=Entry(f,textvariable=entryVarMsg).grid(row=0,column=1)
labelP=Label(f,text="Entrez p:").grid(row=1,column=0)
entryP=Entry(f,textvariable=entryVarP).grid(row=1,column=1)
labelQ=Label(f,text="Entrez q:").grid(row=2,column=0)
entryQ=Entry(f,textvariable=entryVarQ).grid(row=2,column=1)
labelE=Label(f,text="Entrez e:").grid(row=3,column=0)
entryE=Entry(f,textvariable=entryVarE).grid(row=3,column=1)

startButton=Button(f,text="Demarrer la simulation",command=demarrer).grid(row=4,column=1)
f.mainloop()

#311 307 349
#1013 1061 1011
#5021 1061 1011
