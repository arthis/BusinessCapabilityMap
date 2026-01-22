# ADR-BCM-URBA-0002 — Une capability = une responsabilité, pas une application

- Statut: Accepted
- Date: 2026-01-21
- Décideurs: EA / Urbanisation, Business Architecture
- Tags: BCM, Urbanisation, Ownership

## Contexte
Lors des cartographies et de la rationalisation, une dérive fréquente est d’assimiler une capability à une application (ex : « CRM = Relation Client »).
Cela crée :
- des recouvrements (plusieurs applications couvrent une même capability),
- des débats stériles “outil vs métier”,
- une incapacité à comparer objectivement des options (build/buy, produit vs plateforme, trajectoire).

## Décision
- Une capability décrit une responsabilité métier stable (le “quoi”), indépendante de la solution.
- Les applications, produits SI et composants techniques sont **mappés** sur les capabilities, mais ne les définissent pas.
- Les libellés de capabilities ne contiennent **aucune** référence à un éditeur, un outil, ou une techno.

## Justification
Cette séparation permet :
- d’éviter les biais technologiques,
- de maintenir un langage commun métier/DSI,
- de piloter une trajectoire (avant/après) sans renommer le métier,
- de mesurer la couverture SI et d’identifier les doublons.

Alternatives :
- Capability = Application : rejeté (trop dépendant du paysage SI, bloque la transformation).
- Capability = Processus : rejeté (dérive en cartographie opérationnelle exhaustive).

## Impacts sur la BCM
- Capacités impactées : toutes (règle de nommage et de périmètre).
- Modèle de cartographie : maintenir une vue séparée « Capability → Applications/Produits » (et non dans la BCM).

## Conséquences
### Positives
- Rationalisation applicative plus objective (couverture, redondances, “gaps”).
- Lisibilité renforcée pour les arbitrages (build/buy, convergence, mutualisation).

### Négatives / risques
- Discipline de gouvernance nécessaire (revues de libellés, contrôle qualité).

## Traçabilité
- Revue Architecture : application de la règle sur les cartographies capability→SI
