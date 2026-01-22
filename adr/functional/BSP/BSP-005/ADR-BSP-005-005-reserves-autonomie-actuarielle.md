# ADR-BSP-005-005 — Séparation "Constitution des réserves" du processus indemnisation

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Actuariat, Gestion Sinistres, Finance
- Tags: BCM, CAP, BSP-005, RES, Reserves, Actuariat

## Contexte

La **constitution des réserves** dans une mutuelle présente des enjeux spécifiques :
- **Obligation réglementaire** : provisionnement Solvabilité II
- **Équilibre technique** : impact direct S/P et solvabilité
- **Expertise actuarielle** : méthodes statistiques, triangles développement
- **Temporalité différente** : réserves ≠ paiements immédiats

La question s'est posée d'intégrer cette activité :
- Dans **INR "Indemnisation & règlement"** (même domaine sinistres)
- Dans **CAP.SUP.ACT.000 "Actuariat"** (expertise technique)
- En capacité **autonome L2**

## Décision

Maintenir **CAP.BSP.RES.000 "Constitution des réserves"** comme capacité L2 autonome avec :
- **Périmètre :** Provisionnement sinistres, évaluation coût ultime, reporting prudentiel
- **Rattachement :** BSP.005 (cohérence domaine sinistres/prestations)
- **Expertise :** Actuariat sinistres + connaissance métier mutuelle

## Justification

**Spécificités réserves mutuelle :**
- **Mutualisation risque** : réserves = garantie solidarité future
- **Équilibre technique** : sur-provisionnement = excédent distribué, sous-provisionnement = déficit sociétaires
- **Réglementaire** : Best Estimate + Risk Margin spécifiques mutuelles
- **Transparence** : information sociétaires sur évolution engagements

**Autonomie technique justifiée :**
- **Expertise actuarielle** spécialisée (statistiques, modèles)
- **Temporalité propre** : cycles évaluation trimestriels/annuels
- **Données massives** : historiques, triangles, cadences règlement
- **Responsabilité** : engagement prudentiel et réglementaire

**Cohérence avec BSP.005 :**
- **Domaine métier** : sinistres/prestations (même risques)
- **Données partagées** : historiques indemnisation
- **Interface naturelle** : évaluation (ÉDP) → indemnisation (INR) → provisionnement (RES)

## Alternatives considérées

**Alternative 1 :** Intégration dans INR "Indemnisation"
→ rejetée (mélange opérationnel quotidien et expertise technique cyclique)

**Alternative 2 :** Rattachement à SUP.ACT "Actuariat"
→ rejetée (perd proximité données/processus sinistres)

**Alternative 3 :** Fusion avec CAD "Contentieux & recours"
→ rejetée (logiques métier différentes)

## Architecture processus intégrée

```
Flux opérationnel sinistres :
DSP → OED → IND → ÉDP → INR
                    ↓     ↓
Flux support spécialisé :  
                   RES ← données historiques
                    ↓
              Reporting prudentiel
```

**RES** collecte données de tous les processus sinistres pour :
- **Provisionnement** dossiers en cours
- **Évaluation** coût ultime par garantie/année
- **IBNR** estimation sinistres non déclarés
- **Reporting** Solvabilité II

## Conséquences

### Organisationnelles
- **Équipe actuariat sinistres** (profil dual : actuariat + métier mutuelle)
- **Gouvernance** : comité de provisionnement trimestriel
- **Responsabilité** : engagement prudentiel société et autorités

### Techniques
- **Outils actuariels** : logiciels triangulation, réserves
- **Interface** avec comptabilité (provisions)
- **Reporting** : états prudentiels, information sociétaires

### Financières
- **Impact bilan** : évolution réserves = variation capitaux propres
- **Solvabilité** : ratio couverture = fonction qualité provisionnement
- **Distribution** : excédent provisionnement = ristourne potentielle

## Pilotage de la capacité

### KPI
- **Boni/Mali** développement réserves N-1, N-2
- **Ratio** provisions/primes par garantie
- **Délai** production reporting trimestriel

### Risques
- **Sous-provisionnement** : impact solvabilité
- **Sur-provisionnement** : excédent non redistribué
- **Modèle** inadéquat : erreur systématique

## Traçabilité
- Réglementation Solvabilité II mutuelles
- Analyse coût ultime historique
- RFC 009 "Constitution des réserves"