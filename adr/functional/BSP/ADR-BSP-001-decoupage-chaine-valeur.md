# ADR-BSP 001 — Découpage des 8 capacités cœur métier mutualiste

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Direction Métier, DSI
- Tags: BCM, CAP, BSP, CoreBusiness, ValueChain

## Contexte

La zone **BUSINESS SERVICE PRODUCTION** couvre le cœur métier d'une mutuelle. Le découpage doit refléter :
- La **chaîne de valeur** spécifique de l'assurance mutualiste
- Les **responsabilités organisationnelles** distinctes
- Les **interactions métier** entre processus
- La **réglementation** sectorielle (Code Mutualité, supervision ACPR)

## Décision

Découper BSP en **8 capacités L1** suivant la chaîne de valeur mutualiste :

**CAP.BSP.001 "Produits & Tarification"** 
- Conception, paramétrage, modèles tarifaires, gouvernance catalogue
- Owner: Marketing Produit / Actuariat

**CAP.BSP.002 "Canaux & Intermédiation"**
- Règles distribution, réseaux, conventions, commissions
- Owner: Distribution

**CAP.BSP.003 "Souscription & Acceptation du Risque"** 
- Analyse, décision, formalisation jusqu'à émission
- Owner: Souscription

**CAP.BSP.004 "Administration des Contrats"**
- Tenue, mouvements, vie du contrat post-émission  
- Owner: Gestion Contrats

**CAP.BSP.005 "Sinistres & Prestations"**
- Déclaration, instruction, indemnisation, accompagnement
- Owner: Gestion Sinistres / Prestations

**CAP.BSP.006 "Interaction & Service Client"**
- Demandes, réclamations, assistance sociétaire
- Owner: Service Client

**CAP.BSP.007 "Cotisations & Recouvrement"**
- Calcul, émission, encaissement, recouvrement
- Owner: Gestion Cotisations

**CAP.BSP.008 "Finance & Actuariat"**
- Performance, provisions, équilibres techniques, prudentiel
- Owner: Finance / Actuariat

## Justification

**Flux de valeur mutualiste :**
```
BSP.001 → BSP.002 → BSP.003 → BSP.004 → BSP.005
   ↓         ↓         ↓         ↑         ↑
BSP.008 ← BSP.007 ← BSP.006 ←──────────────┘
```

**Spécificités organisationnelles :**
- **BSP.007 "Cotisations & Recouvrement"** autonome : enjeu liquidité critique, expertise finance
- **BSP.006 "Interaction & Service Client"** distinct : obligation service sociétaire, expertise relationnelle
- **BSP.008 "Finance & Actuariat"** séparé : vision transverse performance/prudentiel

**Interactions avec STEERING :**
- **STE.001** pilote performance de tous les BSP
- **STE.002** contrôle conformité de tous les BSP (obligations réglementaires)

## Alternatives considérées

**Alternative 1 :** BSP.007 intégré dans BSP.004 → rejetée (enjeu financier dilué)
**Alternative 2 :** BSP.006 fusionné avec Channel → rejetée (perd expertise sociétaire)
**Alternative 3 :** Moins de capacités (5-6) → rejetée (granularité insuffisante pour gouvernance)

## Impacts sur la BCM

- **8 capacités L1** avec ownership claire
- **61 sous-capacités L2** au total
- **Couplages forts** identifiés : BSP.004 ↔ BSP.007, BSP.005 ↔ BSP.006

## Conséquences

### Positives
- Alignement sur chaîne de valeur et organisation mutualiste
- Granularité appropriée pour gouvernance et trajectoires SI
- Clarification des responsabilités métier

### Négatives / Risques  
- Coordination intensive nécessaire entre capacités
- Risque de silos si gouvernance transverse insuffisante

## Traçabilité
- Analyse chaîne de valeur mutualiste 2025
- Cartographie organisationnelle
- RFC 010 "Carto Capacités SI"