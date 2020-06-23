
a=2
#nombre de tailles disponibles
b=10
#taille du client
c=[16,13]
#liste des tailles disponibles
y=[]
#liste vide qui va permettre de stocké les écarts entre la taille demandé par le client et les tailles disponibles
l=len(c)

while l>0:
    for i in c:
        if b>i:
            x=b-i
            y.append(x)
        else:
            x=i-b
            y.append(x)
        l-=1
y.sort()
#commande qui permet de trier la liste des écarts de taille
print(y[0])
#renvoie la valeur ayant l'indice 0 de la liste des écarts de taille. Cela renvoie donc obligatoirement le plus faible écart, car la liste est triée par ordre croissant, l'indice 0 est donc l'écart le plus faible.




