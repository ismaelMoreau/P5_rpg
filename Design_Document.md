Document de design
1. Sommaire
Ce travail est une implémentation d’un environnement pour une I.A. par renforcement inspirer par la bibliothèque de openAi, gym. Cette implémentation est un prototype sous forme de jouet par comparaison à un jeu complet. Son utilité est de tester si l’intelligence artificielle par renforcement est une fonctionnalité possible dans un véritable jeu. Le tout est programmer en python avec un rendu par la bibliothèque P5 elle-même une adaptation de processing. Les graphiques et l’interactivité sont minimaux afin de laisser place au code puisque l’objet, bien que ce soit un travail en programmation d’animation, reste pour moi la possibilité d’y ajouter de l’intelligence artificielle. J’ai fait de mon mieux pour donner une simplicité, une robustesse et une élégance au code pour d’éventuelles modifications afin de mieux tester les possibilités. Le code complet est sur github.

2. Interactivité
Ce jouet propose une temporalité tour par tour. À chaque déplacement du joueur principal par les touches w,a,s,d il y a un pas fait par chaque agent. Ce qui équivaut un tour de boucle de phase d’exploration de l'i.a..
Il y a également un système de rencontre lorsque le joueur principal est sur la même case qu’un autre objet, une fenêtre s’ouvre et différentes options sont disponibles. 
3. Fonctionnalités
3.1 Texte statique
Lorsque survient le panneau de rencontre, du texte est utilisé pour communiquer son sujet.
3.2 Texte dynamique
La fonctionnalité d’attaque dans les rencontres à 75 pourcents de chance d’être efficace dans le cas contraire un cœur sera enlevé et un texte temporaire apparaîtras pour signifier de recommencer.  Si le joueur n’a plus de cœur, le texte de la rencontre changera en indiquant le nouvel état.
3.3 Dessin vectoriel
Tout le graphique est basé sur des images JPEG, mais l’interface utilisateur et le panneau de rencontre ont des rectangles et points vectoriels
3.4 Traitement d’image
J’utilise la notion de transparence sur tous les sprites pour bien définir le contour et donner un rendu plus professionnel.
3.5 Séquence d’images
Les animations sont sous forme de séquences de sprites pour les agents, les npcs et le joueur tous change au moment du déplacement du joueur
3.6 Interface
Les boutons du panneau de rencontre sont un type de contrôle.
3.7 Sections
Il y a un panneau d’interface utilisateur qui communique de l’information au joueur, point de vie et décomptes des monstres restants. Il a aussi le panneau de rencontre pour l’interaction.   
3.8 Clavier
Les déplacements du joueur sont centraux au fonctionnement et sont déterminés par les touches w,a,s,d 
3.9 Souris
La souris permet de cliquer sur son choix sur le panneau de rencontre. Les rectangles des choix seront changés de couleur lorsque la souris passera au-dessus.
3.10 Collection
La carte globale est un fichier .cvs. le tableau a des dimensions déterminer à l’avance. Chaque cellule est le numéro de l’image de la tuile à rendre à l’écran. Seulement les images visibles sont rendues c.-à-d. celles qui sont à l’intérieur des coordonnés centrés sur celles du joueur et l’intérieur des dimensions de la fenêtre.

4. Ressources
Mon inspiration vient de ces projets.
OpenAI. “Gym: A Toolkit for Developing and Comparing Reinforcement Learning Algorithms.” Accessed March 3, 2022. https://gym.openai.com.
Merci au créateur de ce contenu, j’ai adapté plusieurs concepts de leur code.
Clear Code. Creating a Zelda Style Game in Python [with Some Dark Souls Elements], 2022. https://www.youtube.com/watch?v=QU1pPzEGrqw.
RPG - OpenProcessing. Accessed March 3, 2022. https://openprocessing.org/sketch/186988/.
J’ai utilisé Tiled pour la création de la carte
Tiled. “Tiled.” Accessed March 3, 2022. https://www.mapeditor.org/.

5. Présentation
Je suis le seul membre de l’équipe 18 et je suis programmeur web de formation, j’ai travaillé dans une banque et pour une compagnie œuvrant dans le domaine de la cryptomonnaie c’est dernier 4 années. En plus du CASA, je suis une formation en I.A.  Je me passionne pour l’innovation technologique et ce travail en est le reflet.

CONCLUSION
N’ayant jamais fait de code pour un jeu vidéo auparavant j’ai cru que j’aurais le temps de faire bien plus, mais finalement le résultat me satisfait puisque c’est un environnement à modeler et non un jeu complet. J’espère vraiment découvrir si l’intelligence artificielle par renforcement peut devenir une fonctionnalité ludique, du moins être intéressant à intégrer dans un jeu.
