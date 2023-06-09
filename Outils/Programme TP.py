"""Guide pour analyse de données d'un TP."""

__author__ = "Armand PIERRE"
__licence__ = "CC BY-NC-SA"

import inspect
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *

# Mesures brutes


# Mesures traitées
x = np.linspace(2, 9, 10) + 0.1*np.random.randn(10)
delta_x = np.full(x.shape, 0.1)
y = 0.5 * x + 0.1*np.random.standard_normal(x.shape)
delta_y = np.full(x.shape, 0.1)

xmin, xmax = np.amin(x), np.amax(x)
ymin, ymax = np.amin(x), np.amax(x)

def func(x, a, b):
    """Fonction modélisant la courbe."""
    return a * x + b # Exemple avec une fonction linéaire

# Cette ligne fait de la magie noire... Elle récupère les noms des paramètres de la fonction !
noms_symboles = tuple(value.name for value in inspect.signature(func).parameters.values())
noms_symboles = noms_symboles[1:]

# Donnez une valeur initiale à chaque symbole -> {"nom": valeur, ...}
estimations_initiales = {"a": 1.2, "b": 0.03}

params_init = np.array([estimations_initiales[nom] for nom in noms_symboles])

parametres_curve, pcov_curve = curve_fit(func, x, y, p0=params_init, sigma=delta_y,absolute_sigma=True)
std_parametres_curve = np.sqrt(np.diag(pcov_curve))
chi_curve = np.sqrt(((func(x,*parametres_curve)-y)**2).sum()) #racine de la somme des résidus au carré
nombre_params= len(parametres_curve)

resultats_curve = [ufloat(parametres_curve[i],std_parametres_curve[i]) for i in range(nombre_params)]

for i in range(nombre_params):
    print(f'{noms_symboles[i]} = {resultats_curve[i]:.2e}')
print(f'Score chi: {chi_curve:.2e}')

# Un bon graphe est un graphe éloquent !
# Donnez un titre, des légendes, les unités des axes...
# C'est simple: si vous oubliez, vous verrez "INSEREZ TITRE" pour vous le rappeler !
titre = "INSEREZ TITRE"
legende_x = "LEGENDE EN X"
legende_y = "LEGENDE EN Y"
texte_func = "y = f(x)" # Ecrivez la formule de func (facultatif)

# Si vous voulez changez le style... Renseignez sur les styles de graphiques Matplotlib !
# Première lettre = couleur
# Deuxième (faucltative): forme
style_points = "bo"
style_courbe = "r"

legende_curve = texte_func + '\n'
for i in range(nombre_params):
    legende_curve+=f'{noms_symboles[i]} = {resultats_curve[i]:.2e}\n'
legende_curve += f'chi= {chi_curve:.2e}'

fig_curve,ax_curve = plt.subplots()
ax_curve.cla()
ax_curve.set_xlabel(legende_x)
ax_curve.set_ylabel(legende_y)
ax_curve.set_title(titre)
ax_curve.errorbar(x,y,yerr=delta_y,xerr=delta_x,fmt=style_points,label='données',capsize=3)

xfit_curve = np.linspace(xmin,xmax)
yfit_curve = func(xfit_curve, *parametres_curve[:]) # le symbole «*» permet de déballer ("unpack") l'array des parametres pour appeler func()
ax_curve.plot(xfit_curve,yfit_curve,style_courbe,label='fit')
ax_curve.text(.9,.1,legende_curve,transform=ax_curve.transAxes,horizontalalignment='right', verticalalignment='bottom')

ax_curve.legend(loc='best')

plt.show()
