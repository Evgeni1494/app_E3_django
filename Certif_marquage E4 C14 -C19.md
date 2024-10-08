 # E4: “Développer une app”

### C14. Analyser le besoin d’application d’un commanditaire intégrant un service d'intelligence artificielle, en rédigeant les spécifications fonctionnelles et en le modélisant, dans le respect des standards d’utilisabilité et d’accessibilité, afin d’établir avec précision les objectifs de développement correspondant au besoin et à la faisabilité technique.


- La modélisation des données respecte un formalisme : Merise, entités-relations, etc.

- La modélisation des parcours utilisateurs respecte un formalisme : schéma fonctionnel, wireframes, etc.

- Chaque spécification fonctionnelle couvre le contexte, les scénarios d’utilisation et les critères de validation.

- Les objectifs d’accessibilités sont directement intégrés aux critères d’acceptation des user stories.

- Les objectifs d’accessibilité sont formulés en s’appuyant sur un des standards d'accessibilité : WCAG, RG2AA, etc.

### C15. Concevoir le cadre technique d’une application intégrant un service d’intelligence artificielle, à partir de l'analyse du besoin, en spécifiant l’architecture technique et applicative et en préconisant les outils et méthodes de développement, pour permettre le développement du projet.



- Les spécifications techniques rédigées couvrent l’architecture de l’application, ses dépendances et son environnement d’exécution (langage de programmation, framework, outils, etc).

- Les éventuels services (PaaS, SaaS, etc) et prestataires ayant une démarche éco-responsable sont favorisés lors des choix techniques.

- Les flux de données impliqués dans l’application sont représentés par un diagramme de flux de données.

- La preuve de concept est accessible et fonctionnelle en environnement de pré-production.

- La conclusion à l’issue de la preuve de concept donne un avis précis permettant une prise de décision sur la poursuite du projet.


### C16. Coordonner la réalisation technique d’une application d’intelligence artificielle en s’intégrant dans une conduite agile de projet et un contexte MLOps et en facilitant les temps de collaboration dans le but d’atteindre les objectifs de production et de qualité.

- Les cycles, les étapes de chaque cycle, les rôles, les rituels et les outils de la méthode agile appliquée sont respectés dans sa mise en place et tout au long du projet.

- Les outils de pilotage (tableau kanban, burndown chart, backlog, etc.) sont disponibles dans les conditions prévues par la méthode appliquée.

- Les objectifs et les modalités des rituels sont partagés à toutes les parties prenantes et rappeler si besoin.

- Les éléments de pilotage sont rendus accessibles à toutes les parties du projet et ce tout au long du projet, en accord avec les recommandations de la méthode de gestion de projet appliquée.

### C17. Développer les composants techniques et les interfaces d’une application en utilisant les outils et langages de programmation adaptés et en respectant les spécifications fonctionnelles et techniques, les standards et normes d’accessibilité, de sécurité et de gestion des données en vigueur dans le but de répondre aux besoins fonctionnels identifiés.


- L’environnement de développement installé respecte les spécifications techniques du projet.

- Les interfaces sont intégrées et respectent les maquettes.

- Les comportements des composants d’interface (validation formulaire, animations, etc.) et la navigation respectent les spécifications fonctionnelles.

- Les composants métier sont développés et fonctionnent comme prévu par les spécifications techniques et fonctionnelles.

- La gestion des droits d’accès à l’application ou à certains espaces de l’application est développée et respecte les spécifications fonctionnelles.

- Les flux de données sont intégrés dans le respect des spécifications techniques et fonctionnelles.

- Les développements sont réalisés dans le respect des bonnes pratiques d’éco-conception d’une application (Les recommandations d’éco-index ou Green IT par exemple)

- Les préconisations du top 10 d’OWASP sont implémentées dans l’application quand nécessaire.

- Des tests d’intégration ou unitaires couvrent au moins les composants métier et la gestion des accès.

- Les sources sont versionnées et accessibles depuis un dépôt Git distant.

- La documentation technique couvre l’installation de l’environnement de développement, l’architecture applicative, les dépendances, l’exécution des tests.

- La documentation est communiquée dans un format qui respecte les recommandations d’accessibilité (par exemple celles de l’association Valentin Haüy ou de Microsoft).


### C18. Automatiser les phases de tests du code source lors du versionnement des sources à l’aide d’un outil d’intégration continue* de manière à garantir la qualité technique des réalisations.

- La documentation pour l’utilisation de la chaîne couvre les outils, toutes les étapes, les tâches et tous les déclencheurs de la chaîne.

- Un outil de configuration et d'exécution d’une chaîne d’intégration continue est sélectionné de façon cohérente avec l’environnement technique du projet.

- La chaîne intègre toutes les étapes nécessaires et préalables à l'exécution des tests de l’application (build, configurations...).

- La chaîne exécute les tests de l’application disponibles lors de son déclenchement.

- Les configuration sont versionnées avec les sources du projet d’application, sur un dépôt Git distant.

- La documentation de la chaîne d’intégration continue couvre la procédure d’installation, de configuration et de test de la chaîne.

- La documentation est communiquée dans un format qui respecte les recommandations d’accessibilité (par exemple celles de l’association Valentin Haüy ou de Microsoft).


### C19. Créer un processus de livraison continue d’une application en s’appuyant sur une chaîne d’intégration continue et en paramétrant les outils d’automatisation et les environnements de test afin de permettre une restitution optimale de l’application.

- La documentation pour l’utilisation de la chaîne couvre toutes les étapes de la chaîne, les tâches et tous les déclencheurs disponibles.

- Le ou les fichiers de configuration de la chaîne sont correctement reconnus et exécutés par le système.

- La ou les étapes de packaging (compilation, minification, build de containers, etc.) de l’application sont intégrées à la chaîne et s'exécutent sans erreur.

- L’étape de livraison (pull request par exemple) est intégrée et exécutée une fois la ou les étapes de packaging validées.

- Les sources de la chaîne sont versionnées et accessibles depuis le dépôt Git distant du projet d’application.

- La documentation de la chaîne de livraison continue couvre la procédure d’installation, de configuration et de test de la chaîne.

- La documentation est communiquée dans un format qui respecte les recommandations d’accessibilité (par exemple celles de l’association Valentin Haüy ou de Microsoft).