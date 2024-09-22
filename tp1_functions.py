"""
@Bastien.Rossiaud
bastien.rossiaud@cpe.fr
19/09/2024
to do :retaffer matrices et hanoi et finir le tp(tricolore etc)
"""

def bissextile(year):
    """vérifie si une année est bissextile ou non.
    in : entier symbolisant une année à vérifier
    out : un booléen
    """
    if year >= 1582 :    #vérif si l'année est supérieure à 1582
        if year % 10 != 0 and year % 4 == 0 :  #vérif de la validité d'une année bissextile
            return True
    return False

def length_month(month):
    """fonction qui donne le nombre de jours d'un mois après 
    avoir vérifié la validité des paramètres.
    in : string symbolisant un des douzes Mois sans majuscules
     en français et avec les accents
    out : integer (nombre de jours)
    """
    lst_months= ["janvier","février","mars","avril",
    "mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    int_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month in lst_months:   #vérif de la saisie du paramètre
        for i in range(len(lst_months)) :
            if lst_months[i] == month :     #on trouve quel mois month est
                return int_months[i]        #on renvoie le nombre de jours associé a la liste des mois
    return False


def verif_date(date):
    """ fonction qui vérifie si une date est valide ou non.
    in : une date de type string sous la forme "dd/mm/yyyy"
    out : Booléen
    """
    dico_months={"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31} #dico associant mois/nombre de jours
    lst_date = date.split("/")                #sépare les jours les mois et les années de la date donnée
    if int(lst_date[2]) >= 1582 :              #tests pour verif la date
        if 1 <= int(lst_date[1]) <= 12 :
            if int(lst_date[0]) <= dico_months[lst_date[1]] :     #comparaison entre la date et le dico
                return True
    return False

def mes_impots(revenu):
    """fonction qui calcule le montant de l'impôt sur le revenu d'une personne seule
    in : le revenu d'une personne sous la forme d'un entier
    out : un entier impôt
    """
    impot=0
    if revenu<=10225:
        return impot
    elif 10226<=revenu<=26070:
        reste=revenu-10226
        impot=reste*0.11
        return impot
    elif 26071<=revenu<=74545:
        reste = revenu-26071
        impot=reste*0.3+26070*0.11
        return impot
    elif 74546<=revenu<=160336:
        reste=revenu-74546
        impot=reste*0.41+74545*0.3
        return impot
    else:
        reste=revenu-160336
        impot=reste*0.45+160336*0.41
        return impot
    
def mes_impots_generique(revenu,plafonds,taux):
    """fonction qui calcule le montant de l'impôt sur le revenu d'une personne seule
    in : le revenu d'une personne sous la forme d'un entier avec deux listes : les plafonds et les taux
    out : un entier impôt
    """
    impot = 0
    for i,nombre in enumerate(plafonds):
        if revenu > 10225 and revenu <= nombre:
            reste = revenu-plafonds[i-1] + 1
            impot = reste * taux[i] + (plafonds[i-1]+1) * taux[i-1]
        elif revenu <= 10225 : 
            return impot
        else : 
            reste = revenu-plafonds[i]
            impot = reste * taux[i] + (plafonds[i-1]+1) * taux[i-1]
    
def multipli_matrices_gene(matrice1,matrice2):
    """ fonction affichant le résultat de la multiplication
    de deux matrices carrées.
    in : matrice1 et matrice2 deux matrices carrées(lst de lst)
    out : une seule matrice produit des deux (lst de lst)
    """
    m = len(matrice1)
    n = len(matrice2)
    res = [[]*n]
    for i in range(m):
        for j in range(n):
            res[i][j] = matrice1[i][j] * matrice2[j][i] 
            print(res[i][j])  
    return res

def hanoi(n,source=1,destination=2,aide=3):
    """fonction qui recre le jeu de la tour de hanoi
    in : n le nombre de palets
    source destination et aide des string
    """
    if n == 1:
        n = 2
    #pour récursif trois lignes : appel a hanoi un print et un appel a hanoi

def syracuse(n,suite=[]):
    """fonction qui affiche la suite de Syracuse
    in : un entier n et une liste vide
    out: la suite de syracuse sous forme de liste"""
    if n == 1:
        return suite
    elif n % 2 == 0 : 
        suite.append(n)
        return syracuse(int(n//2),suite)
    elif n % 2 != 0 :
        suite.append(n)
        return syracuse(n*3+1,suite)

    
def syracuse_max(n,max=0):
    """fonction qui retourne le max de la suite de Syracuse
    in : un entier n et un max qui vaut 0
    out : un entier max"""
    if n == 1:
        return max
    elif n % 2 == 0 :
        if max < n :
            max = n
        return syracuse_max(int(n//2),max)
    elif n % 2 != 0 :
        if max < n :
            max = n
        return syracuse_max(n*3+1,max)
    
    
def temps_de_vol(n):
    """fonction qui calcule le temps de vol d'un nombre n de Syracuse
    in : un entier n 
    out : le temps de vol sous forme d'un entier"""
    if n == 1 :
        return 0
    elif n % 2 == 0 :
        return 1 + temps_de_vol(int(n//2))
    elif n % 2 != 0 :
        return 1+temps_de_vol(n*3+1)
    
def tricolore(n):
    """fonction qui permet"""

