# Apprendre le Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/armand-pierre/Python-pedagogie/master)

Ce répertoire est un ensemble d'algorithmes en Python utilisables pour l'enseignement de la programmation au lycée en France.

## Comment utiliser ce dossier ?

### Jupyter, Basthon et MyBinder

Jupyter est un environnement de programmation très apprécié dans le domaine de la recherche. Il permet en effet de créer des documents mélangeant textes mis en forme, formules de mathématiques et morceaux de codes interactifs, de les exécuter et même de les exporter en fichier PDF.

Pour utiliser les présents fichiers, vous n'avez besoin de rien installer: vous pouvez utiliser MyBinder ou Basthon.

#### Basthon

Basthon est un solution open source française, conçue pour l'enseignement. Vous pouvez charger n'importe quel fichier ici présent avec l'URL `https://notebook.basthon.fr/?from=adresse_url`. Par exemple, https://notebook.basthon.fr/?from=https://github.com/armand-pierre/Python-pedagogie/blob/master/Programmer/Bien%20r%C3%A9diger.ipynb redirige vers le cours "Programmer/Bien rédiger.ipynb" (vous pouvez tout à fait raccourcir ce lien ou le convertir en QRCode).

Basthon est un service ne collectant d'aucune manière des données personnelles, son code est accessible à tous et il est même utilisable hors ligne, je vous le recommande si vous cherchez une manière de publier du code en ligne.

#### MyBinder

MyBinder est une solution open source permettant, avec un navigateur et une connexion Internet, d'utiliser des fichiers Jupyter.

Pour cela, cliquez sur le bouton "launch MyBinder" en haut de page ou ci-dessous.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/armand-pierre/Python-pedagogie/master)

MyBinder garantit le respect des données personnelles, aucune donnée récoltée n'est reliée à vous. MyBinder se réserve seulement le droit de conserver un registre des visites des 30 derniers jours pour éviter une utilisation illégale de leurs services.


### Licence

La licence de ces programmes est la licence GNU GPL v3. Elle vous accorde le droit de l'utiliser à des fins personnelles, de le modifier comme bon vous semble et de le partager librement, à condition que vous-mêmes gardiez ce travail sous la même licence, et puissiez laisser aussi à libre disposition votre travail modifié.

Si vous modifiez ce travail dans votre copie, vous devez expliciter qu'il a été modifié.

### Bibliothèques nécessaires

Je tente au maximum de limiter le nombre de modules Python utilisés, et d'utiliser ceux les plus utiles à l'enseignement de Python et accesibles via Basthon ou MyBinder:
- `matplotlib`, module de création et d'affichages de graphiques divers (nuages de points, histogrammes, camemberts...).
- `numpy`, module de manipulation simple et efficace de grands tableaux de données.
- `scipy`, module comportant de nombreuses fonctions utiles en analyse de données (régressions, transformée de Fourier rapide...)
- des modules de la bibliothèque standarde de Python: math et random.

Beaucoup de codes évitent l'utilisation de modules et de fonctions peut connues ou qui pourraient parasiter l'apprentissage, quitte à avoir des codes moins performants ou concis.