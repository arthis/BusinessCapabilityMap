# ADR-BCM-URBA-0001 — BCM structurée en 3 niveaux (L1/L2/L3)

- Statut: Accepted
- Date: 2026-01-21
- Décideurs: EA / Urbanisation, Business Architecture
- Tags: BCM, Modélisation, Niveaux

## Contexte
La BCM doit servir :
- de langage commun métier/DSI,
- de support à l’urbanisation (alignement applications / data / investissements),
- sans devenir une process map.

Un modèle 2 niveaux manque de granularité pour certains arbitrages (allocation SI, rationalisation, ownership).

## Décision
- La BCM est structurée en 3 niveaux : L1, L2, L3.
- Les vues standards exposées sont L1/L2.
- Le niveau L3 est produit uniquement pour les domaines critiques (High criticality) ou sous transformation.

## Justification
Le 3 niveaux donne l’actionnabilité (L3) sans perdre la lisibilité (L1/L2).

Alternatives :
- 2 niveaux : rejeté (trop macro pour l’urbanisation).
- 4+ niveaux : rejeté (risque de dérive en cartographie de processus).

## Impacts sur la BCM
- Capacités impactées : toutes (règle de construction).
- Vues : générer une vue L1/L2 par défaut.

## Conséquences
### Positives
- Meilleur pilotage de la couverture SI et des investissements.

### Négatives / risques
- Risque de granularité incohérente si L3 non gouverné.

## Traçabilité
- Atelier Urbanisation 2026-01-15
