1. Démarrage de Prometheus

Commande pour démarrer Prometheus : sudo systemctl start prometheus

    Ce que fait cette commande : Cette commande démarre le service Prometheus sur votre système. Prometheus est configuré pour scraper les métriques des services que vous avez définis dans son fichier de configuration prometheus.yml.

Commande pour redémarrer Prometheus : sudo systemctl restart prometheus

    Ce que fait cette commande : Cette commande redémarre le service Prometheus. Utilisez-la après avoir modifié le fichier prometheus.yml pour appliquer les changements.

Commande pour vérifier l'état de Prometheus : sudo systemctl status prometheus

    Ce que fait cette commande : Cette commande affiche l'état actuel du service Prometheus, vous permettant de vérifier s'il est en cours d'exécution, arrêté, ou s'il y a des erreurs.

Adresse pour accéder à Prometheus :

    URL par défaut : http://localhost:9090
    Explication : Vous pouvez accéder à l'interface web de Prometheus via cette adresse. Ici, vous pouvez exécuter des requêtes Prometheus, consulter l'état des cibles, et vérifier les alertes.



2. Démarrage de Grafana

Commande pour démarrer Grafana : sudo systemctl start grafana-server

    Ce que fait cette commande : Cette commande démarre le service Grafana. Grafana est l'outil de visualisation utilisé pour afficher les métriques collectées par Prometheus.

Commande pour redémarrer Grafana : sudo systemctl restart grafana-server

    Ce que fait cette commande : Cette commande redémarre le service Grafana. Utilisez-la si vous modifiez la configuration de Grafana ou si vous avez installé de nouveaux plugins.

Commande pour vérifier l'état de Grafana : sudo systemctl status grafana-server

    Ce que fait cette commande : Cette commande vous permet de voir si le service Grafana est en cours d'exécution, et de vérifier s'il y a des erreurs.

Adresse pour accéder à Grafana :

    URL par défaut : http://localhost:3000
    Explication : Vous pouvez accéder à l'interface web de Grafana via cette adresse. Ici, vous pouvez créer des tableaux de bord, configurer des visualisations et des alertes basées sur les données provenant de Prometheus.

3. Arrêt des services

Commande pour arrêter Prometheus : sudo systemctl stop prometheus

    Ce que fait cette commande : 
    Arrête le service Prometheus. Utilisez-la si vous devez arrêter la collecte des métriques temporairement.

Commande pour arrêter Grafana : sudo systemctl stop grafana-server

    Ce que fait cette commande : 
    Arrête le service Grafana. Utile si vous devez arrêter l'accès à l'interface de visualisation temporairement.