# ADR-STE 001 — Séparation "Pilotage d'Entreprise" et "Conformité" 

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Direction Générale, Business Architecture, Conformité
- Tags: BCM, CAP, STE, Zone, Governance, Separation

## Contexte

Dans le contexte mutualiste, le **steering** de l'organisation couvre deux logiques distinctes :
- Le **pilotage stratégique et opérationnel** (performance, transformation, budgets)
- La **conformité réglementaire** (obligations légales, supervision ACPR, contrôles)

Une capacité unique "Gouvernance" masquerait des responsabilités, temporalités et enjeux très différents dans une mutuelle soumise à supervision.

## Décision

Créer deux capacités L1 distinctes dans le zoning STEERING :

**CAP.STE.001 "Pilotage d'Entreprise"**
- Stratégie, performance, transformation, pilotage budgétaire et risques opérationnels
- Owner: Direction Générale
- Logique: *optimisation, décision, agilité*

**CAP.STE.002 "Conformité"**  
- Veille réglementaire, contrôle interne, audits, obligations prudentielles, RGPD
- Owner: Conformité / Risques
- Logique: *obligation, contrôle, justification*

## Justification

**Spécificités mutuelle :**
- **Intensité réglementaire** élevée (Code Mutualité + Solvabilité II + ACPR)
- **Indépendance obligatoire** de la fonction conformité (recommandations ACPR)
- **Temporalités différentes** : pilotage (réactivité) vs conformité (rigueur, traçabilité)
- **Reporting distinct** : interne (performance) vs externe (supervision)

**Interactions identifiées :**
- STE.001 → STE.002 : transmission objectifs conformité, budget conformité
- STE.002 → STE.001 : alertes réglementaires, contraintes à intégrer au pilotage
- STE.002 → BSP.* : contrôles métier, audits opérationnels

## Alternatives considérées

**Alternative 1 :** Capacité unique "Gouvernance" → rejetée (dilue spécificité réglementaire)
**Alternative 2 :** Conformité en Support → rejetée (perd visibilité steering)

## Impacts sur la BCM

- **Deux capacités L1 :** CAP.STE.001, CAP.STE.002
- **Sous-capacités :** 8 L2 pour STE.001, 10 L2 pour STE.002
- **Interactions fortes :** STE.002 contrôle toutes les capacités BSP

## Conséquences

### Positives
- Respect des bonnes pratiques de gouvernance mutualiste
- Indépendance et visibilité de la fonction conformité
- Clarification des responsabilités Direction/Conformité

### Négatives / Risques
- Coordination indispensable entre les deux capacités
- Risque de doublon dans le pilotage des risques

## Traçabilité
- Code de la Mutualité - art. L114-17
- Recommandations ACPR sur gouvernance
- Analyse organisationnelle 2025