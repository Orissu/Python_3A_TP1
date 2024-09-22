"""
Bastien.Rossiaud
bastien.rossiaud@cpe.fr
19/09/2024
"""

import tp1_functions as f

bis=f.bissextile(1581)
month=f.length_month("mars")

#date=input("veuillez renseigner une date sous le format dd/mm/yyyy : ")
#print(f.verif_date(date))

#revenu=int(input("Veuillez indiquer le montant de vos revenus : "))
#print(f.mes_impots(revenu))

#matrice1=[[1,2],[3,4]]
#matrice2=[[1,3],[2,4]]

#produit=f.multipli_matrices_gene(matrice1,matrice2)

max=0
for i in range(1,1001):
    test=f.temps_de_vol(i)
    if max<test:
        max=test
print(max)

haut=0
for i in range(1,1001):
    var=f.syracuse_max(i)
    if haut<var:
        haut=var
print(haut)