from pickletools import read_stringnl_noescape
from sre_constants import ANY


def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    param list i: Inimeste järjend
    param list p: Palgate järjend
    param int n: Inimeste arv
    rtype: list, list
    """
    if n>0:
        for j in range(n):
            nimi=(input("Nimi: ")).capitalize() 
            palk=int(input("Palk: ")) 
            i.append(nimi) 
            p.append(palk)
    return i,p  
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    param list i: Inimeste järjend
    param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j]) 
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimi=input("Keda kustutada ära(nimi): ") 
    for j in range(0,len(i)-1):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p

def kellel_on_suurim_palk(i:list,p:list):
    """Funktsioon leiab kõige suurim palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimed=[] #tühi list
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed 
    
    
def kellel_on_väiksem_palk(i:list,p:list):
    """Funktsioon leiab kõige väiksem palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimed=[] #tühi list
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed 

def sorteeritud_palgad(i:list,p:list): 
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """

    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p

 
