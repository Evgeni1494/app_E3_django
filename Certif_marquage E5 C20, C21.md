# E5: Débogage + Monitoring


### C20. Surveiller une application d’intelligence artificielle, en mobilisant des techniques de monitorage et de journalisation, dans le respect des normes de gestion des données personnelles en vigueur, afin d’alimenter la feedback loop* dans une approche MLOps, et de permettre la détection automatique d’incidents.

- La documentation liste les métriques et les seuils et valeurs d’alerte pour chaque métrique à risque.

- La documentation explicite les arguments en faveur des choix techniques pour l’outillage du monitorage de l’application.

- Les outils (collecteurs, journalisation, agrégateurs, filtres, dashboard, etc.) sont installés et opérationnels à minima en environnement local.

- Les règles de journalisation sont intégrées aux sources de l’application, en fonction des métriques à surveiller.

- Les alertes sont configurées et en état de marche, en fonction des seuils préalablement définis.

- La documentation couvre la procédure d’installation et de configuration des dépendances pour l’outillage du monitorage de l’application.

- La documentation est communiquée dans un format qui respecte les recommandations d’accessibilité (par exemple celles de l’association Valentin Haüy ou de Microsoft).

### C21. Résoudre les incidents techniques en apportant les modifications nécessaires au code de l’application et en documentant les solutions pour en garantir le fonctionnement opérationnel.


- La ou les causes du problème sont identifiées correctement.

- Le problème est reproduit en environnement de développement.

- La procédure de débogage du code est documentée depuis l’outil de de suivi.

- La solution documentée explicite chaque étape de la résolution et de son implémentation.

- La solution est versionnée dans le dépôt Git du projet d’application (par exemple avec une merge request).