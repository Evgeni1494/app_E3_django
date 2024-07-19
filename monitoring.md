Documentation de Monitorage et de Journalisation pour l'Application SoWeChat
1. Introduction

Cette documentation décrit la mise en place du système de monitorage et de journalisation de l'application SoWeChat. L'objectif est de surveiller les performances de l'application, de détecter automatiquement les incidents et d'alimenter la boucle de rétroaction dans une approche MLOps, tout en respectant les normes de gestion des données personnelles en vigueur.
2. Liste des Métriques et Seuils d'Alerte
Métriques

    Nombre de requêtes HTTP (django_http_requests_total):
        Description : Total des requêtes HTTP reçues par l'application.
        Seuil d'alerte : 500 requêtes par minute.

    Temps de réponse HTTP (django_http_request_duration_seconds):
        Description : Durée des requêtes HTTP en secondes.
        Seuil d'alerte : 2 secondes en moyenne sur une période de 5 minutes.

    Erreurs HTTP 500 (django_http_responses_total{status="500"}):
        Description : Nombre de réponses HTTP 500 (erreur serveur).
        Seuil d'alerte : 5 erreurs par minute.

    Utilisation de la mémoire (process_resident_memory_bytes):
        Description : Utilisation de la mémoire par le processus Django.
        Seuil d'alerte : 500 Mo.

    Utilisation du CPU (process_cpu_seconds_total):
        Description : Utilisation du CPU par le processus Django en secondes.
        Seuil d'alerte : 80% d'utilisation moyenne sur une période de 5 minutes.

Seuils d'Alerte

Les seuils d'alerte sont définis pour chaque métrique comme suit :

    Nombre de requêtes HTTP : Alerte si > 500 requêtes par minute.
    Temps de réponse HTTP : Alerte si temps de réponse moyen > 2 secondes sur 5 minutes.
    Erreurs HTTP 500 : Alerte si > 5 erreurs 500 par minute.
    Utilisation de la mémoire : Alerte si utilisation mémoire > 500 Mo.
    Utilisation du CPU : Alerte si utilisation CPU > 80% sur 5 minutes.

3. Arguments pour les Choix Techniques
Prometheus et django-prometheus

    Prometheus : Outil open-source robuste pour la surveillance des applications. Il permet de collecter, agréger et visualiser des métriques en temps réel.
    django-prometheus : Intégration spécifique à Django permettant de collecter des métriques détaillées sur les performances de l'application et l'utilisation des ressources.

Sentry

    Sentry : Outil de surveillance des erreurs et des performances, permettant de capturer et d'alerter sur les exceptions et les problèmes de performance. Sentry offre une intégration facile avec Django et une interface utilisateur riche pour analyser les erreurs.

4. Installation et Configuration des Outils
Installation des Dépendances

Installez les packages nécessaires :

bash

pip install sentry-sdk django-prometheus

Configuration de Prometheus

Ajoutez django-prometheus à INSTALLED_APPS et MIDDLEWARE dans settings.py :

python

INSTALLED_APPS = [
    'django_prometheus',
    # Autres applications...
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    # Autres middlewares...
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

Ajoutez les routes de Prometheus dans urls.py :

python

from django.urls import path, include

urlpatterns = [
    path('metrics/', include('django_prometheus.urls')),
]

Configuration de Sentry

Ajoutez la configuration de Sentry dans settings.py :

python

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",  # Remplacez par votre DSN
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)

Configuration des Logs

Configurez le logging dans settings.py :

python

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

5. Configuration des Alertes
Alertes dans Sentry

    Accéder aux Règles d'Alerte :
        Dans le tableau de bord Sentry, allez dans les paramètres de votre projet.
        Naviguez vers "Alerts" > "Alert Rules".

    Créer une Nouvelle Règle d'Alerte :
        Cliquez sur "Create Alert Rule".
        Configurez les conditions pour lesquelles vous souhaitez recevoir des notifications (par exemple, pour chaque nouvelle erreur, ou pour un certain type d'erreur).

    Configurer les Actions d'Alerte :
        Dans la section "Actions", sélectionnez "Send an email to" et ajoutez les adresses e-mail des destinataires.

Configuration SMTP pour Sentry (Facultatif)

    Accéder aux Paramètres SMTP :
        Dans les paramètres de l'organisation, allez à la section "Mail" ou "SMTP".

    Configurer le Serveur SMTP :
        Entrez les détails de votre serveur SMTP (adresse du serveur, port, utilisateur, mot de passe, etc.).

6. Vérification et Tests
Vérification des Métriques

Accédez à l'URL /metrics pour vérifier que les métriques sont correctement exposées.
Test des Alertes

Provoquez une erreur intentionnelle dans votre application pour vérifier que Sentry envoie des notifications par e-mail.
Test de Performance

Utilisez des outils comme ab (Apache Benchmark) pour générer des requêtes et vérifier que les alertes de performance fonctionnent correctement.