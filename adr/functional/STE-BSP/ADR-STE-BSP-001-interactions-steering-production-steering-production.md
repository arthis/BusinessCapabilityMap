# ADR-STE-BSP 001-Interactions Steering ↔ Business Service Production

- Statut: Accepted  
- Date: 2026-01-22
- Décideurs: Business Architecture, Direction Générale, Direction Métier
- Tags: BCM, CAP, STE, BSP, Interactions, Governance

## Contexte

Les capacités **STEERING** (pilotage et conformité) et **BUSINESS SERVICE PRODUCTION** (cœur métier) ne sont pas indépendantes. Dans une mutuelle, leurs interactions sont :
- **Structurelles** : pilotage performance, contrôles conformité
- **Réglementaires** : supervision ACPR, reporting obligatoire  
- **Opérationnelles** : arbitrages, transformations, budgets

Il est crucial de documenter ces interactions pour éviter les silos et assurer la cohérence.

## Décision

Formaliser les **interactions bidirectionnelles** entre zones STEERING et BSP :

### STE.001 "Pilotage d'Entreprise" → Tous les BSP
**Nature :** Pilotage performance et transformation
- **Objectifs stratégiques** déclinés par capacité BSP
- **Budgets** et allocation ressources par domaine métier
- **KPI** et tableaux de bord de performance opérationnelle
- **Arbitrages** transformation et priorisation projets

### STE.002 "Conformité" → Tous les BSP  
**Nature :** Contrôles réglementaires transverses
- **Obligations légales** à respecter par capacité métier
- **Contrôles internes** et audits opérationnels  
- **Réclamations réglementaires** remontées par BSP.006
- **Conformité produits** (BSP.001), sinistres (BSP.005), etc.

### Tous les BSP → STE.001 "Pilotage d'Entreprise"
**Nature :** Reporting performance et demandes d'arbitrage
- **Performance réalisée** vs objectifs (revenus, coûts, qualité)
- **Risques opérationnels** et incidents majeurs
- **Demandes budgétaires** et investissements
- **Propositions d'évolution** métier et organisation

### Tous les BSP → STE.002 "Conformité"  
**Nature :** Alertes et justifications réglementaires
- **Incidents conformité** et non-conformités détectées
- **Évolutions réglementaires** nécessitant adaptation métier
- **Éléments justificatifs** pour audits et inspections
- **Réclamations clients** à traiter (délais, médiation)

## Justification

**Spécificités mutualiste :**
- **Supervision ACPR** nécessite traçabilité bout-en-bout
- **Équilibre technique** piloté conjointement (STE.001 + BSP.008)  
- **Service sociétaire** contrôlé réglementairement (STE.002 + BSP.006)
- **Délégations** métier sous contrôle gouvernance (STE.001 + STE.002)

**Enjeux d'urbanisation :**
- **Cohérence** des systèmes de pilotage et reporting
- **Évitement** redondance dans collecte indicateurs
- **Intégration** des outils de conformité dans processus métier

## Impacts sur la BCM

### Gouvernance
- **Comité BCM** avec représentation STEERING + BSP
- **Propriétaires** des interactions clairement identifiés
- **SLA internes** sur reporting et contrôles

### Systèmes d'Information  
- **Datawarehouse** alimenté par toutes les capacités BSP
- **Outils conformité** intégrés aux processus métier
- **Tableau de bord** unifié Direction Générale

### Organisation
- **Correspondants conformité** dans chaque domaine BSP
- **Rituels** pilotage performance transverses  
- **Formation** réglementaire pour équipes métier

## Conséquences

### Positives
- **Vision globale** cohérente pilotage + métier
- **Efficacité** des contrôles et reporting
- **Réactivité** face aux évolutions réglementaires

### Négatives / Risques
- **Complexité** coordination entre 10 capacités L1
- **Charge** reporting si mal optimisée
- **Risque** bureaucratie si gouvernance trop lourde

## Traçabilité
- Recommandations ACPR gouvernance
- Analyse flux décisionnel 2025
- RFC 010 interactions STE ↔ BSP