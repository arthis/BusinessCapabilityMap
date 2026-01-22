# ADR-BCM-URBA-0003 — Décider au bon niveau (L1/L2/L3)

- Statut: Accepted
- Date: 2026-01-21
- Décideurs: EA / Urbanisation, Business Architecture
- Tags: BCM, Gouvernance, Décisions

## Contexte
Sans règle explicite de “niveau de décision”, les arbitrages se font :
- trop macro (au L1) : décisions floues, non actionnables,
- trop fin (au L3) : micro-optimisation, discussions interminables, instabilité du modèle.

Cela impacte directement :
- la priorisation des roadmaps,
- la rationalisation applicative,
- la définition des services et contrats d’intégration.

## Décision
- **L1** sert au cadrage stratégique, à la communication et au pilotage “valeur”.
- **L2** sert aux arbitrages d’urbanisation : ownership, rationalisation, budgets, priorisation, trajectoires.
- **L3** sert au design actionnable : services métiers, contrats (API/événements), règles détaillées, tests de couverture.

## Justification
- L2 est suffisamment stable pour organiser responsabilités, investissements et transformation.
- L3 donne l’actionnabilité (interfaces, règles, invariants) sans saturer le pilotage.
- L1 permet de garder une vue lisible et durable.

Alternatives :
- Décider tout au L1 : rejeté (insuffisant pour l’urbanisation).
- Décider tout au L3 : rejeté (instable, trop coûteux, favorise la dérive “process map”).

## Impacts sur la BCM
- Roadmaps : structurées par capabilities **L2**.
- Backlogs de transformation : détaillés en **L3** uniquement sur les domaines critiques / en transformation.
- Revues d’architecture : décisions de découpage au **L2**, décisions de contrats/intégration au **L3**.

## Conséquences
### Positives
- Arbitrages plus rapides et comparables.
- Réduction des débats de granularité.
- Meilleure cohérence des contrats d’intégration (API/événements) avec le modèle.

### Négatives / risques
- Nécessite une discipline de gouvernance (templates d’ateliers, règles de modélisation).

## Traçabilité
- Guide d’urbanisation BCM v1 — section “Niveaux de décision”
