# PROJET 2 DE LA FORMATION PYTHON : BOOKS TO SCRAPE

## Clonage du repo github

Placez vous dans le dossier où vous souhaitez importer le projet et ouvrez la console, tapez :\

`git clone https://github.com/ThibaultGERARDIN/pythonProjet2.git`

## Création de l'environnement virtuel (venv)

Une fois dans le dossier cloné, vous devez initialiser l'environnement virtuel

### Directement depuis la console :

Sur macOS/Linux :\
`python3 -m venv .venv`
> Vous devrez peut-être run `sudo apt-get install python3-venv` d'abord sur un OS Debian

Sur Windows :\
`python -m venv .venv`
> Vous pouvez aussi utiliser la commande `py -3 -m venv .venv`

### Depuis VsCode :

Ouvrez la palette de commande (Ctrl+Shift+P) et cherchez `Python: Create Environment` puis selectionnez l'option Venv, et choisissez la dernière version de Python pour l'interprete.

## Initialisation du programme

Une fois le dossier cloné et venv créé, il vous faut installer les dépendances nécessaires : BeautifulSoup4 et requests.\
Pour le faire vous pouvez utiliser directement le fichier requirements.txt présent dans le dossier en tapant dans la console : `pip install -r requirements.txt`\
Vous pouvez les installer manuellement via les commandes : `pip install beautifullsoup4` et `pip install requests`

Une fois ces dépendances installées, vous pouvez lancer le programme **main.py** qui va automatiquement extraire les données du site [bookstoscape](http://books.toscrape.com/).\
Le programme va créer un dossier `csv_files` et un dossier `images` dans lesquels seront respectivement stockés les fichiers csv de chaque catégorie de livres, et les images de chaque livre (dans un sous-dossier de chaque catégorie).