# filename : main.my
"""
Ce programme calcule la suite de Syracuse pour un entier donné,
créer et affiche un graphique de cette suite,
et calcule en parallèle le temps de vol, l'altituude maximale,
et le temps de vol en altitude pour cette suite. 
"""
# imports
from plotly.graph_objects import Scatter, Figure

#### Fonctions secondaires


### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche un graphique des valeurs de la suite de Syracuse.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()

#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        l (list): la suite de Syracuse de source n
    """
    l = []
    l.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        tv (int): le temps de vol
    """
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    tva = 0
    n = l[0]
    if l[1]<l[0]:
        return 1
    for j in range(1, len(l)):
        if l[j] < n:
            return tva+1
        tva += 1
    return tva+1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    n = 0
    for elt in l:
        n = max(n, elt)
    return n


#### Fonction principale


def main():
    """
    Quelques tests de bon fonctionnement.
    """

    # vos appels à la fonction secondaire ici
    val = int(input("Entrez une valeur : "))
    lsyr = syracuse_l(val)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
