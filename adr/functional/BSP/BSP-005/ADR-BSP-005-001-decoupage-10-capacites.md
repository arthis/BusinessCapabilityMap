# ADR-BSP-005-001 — Découpage des 10 capacités L2 "Sinistres & Prestations"

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Gestion Sinistres, Direction Métier
- Tags: BCM, CAP, BSP-005, Sinistres, ProcessFlow

## Contexte

La capacité **BSP.005 "Sinistres & Prestations"** couvre le processus critique de gestion des sinistres et prestations dans une mutuelle. Ce processus doit refléter :
- Le **cycle de vie complet** du sinistre/prestation (de la déclaration à la clôture)
- Les **spécificités mutualistes** (prestations santé/prévoyance, accompagnement sociétaire)
- Les **obligations réglementaires** (délais, traçabilité, médiation)
- Les **enjeux de maîtrise des coûts** et de lutte contre la fraude

## Décision

Découper BSP.005 en **10 capacités L2** suivant le processus métier :

**Processus principal (flux séquentiel) :**
- **DSP.000** - Déclaration du sinistre/prestation (entrée multicanale)
- **OED.000** - Ouverture & Enregistrement du dossier (création, typage)
- **IND.000** - Instruction du dossier (analyse garanties, collecte pièces)
- **ÉDP.000** - Évaluation des dommages/prestations (expertise, estimation)
- **INR.000** - Indemnisation/Règlement (calcul, ordonnancement, paiement)
- **CAD.000** - Clôture & archivage (finalisation, conservation)

**Processus support (transverses) :**
- **PTP.000** - Pilotage des tiers & prestataires (experts, réseaux santé)
- **RES.000** - Recours & subrogation (récupération auprès tiers responsables)
- **DLC.000** - Détection & lutte contre la fraude (scoring, investigations)
- **PRS.000** - Pilotage & reporting (indicateurs, tableaux de bord)

## Justification

**Spécificités mutuelle :**
- **Prestations santé/prévoyance** : évaluation différente des sinistres IARD classiques
- **Réseaux de soins** : gestion spécifique tiers-payant et professionnels santé
- **Accompagnement sociétaire** : dimension d'assistance intégrée au processus
- **Équilibre technique** : impact direct sur performance mutuelle

**Logique processuelle :**
```
DSP → OED → IND → ÉDP → INR → CAD
        ↑     ↑     ↑     ↑
      PTP   DLC   RES   PRS (capacités support)
```

**Obligations réglementaires :**
- **Délais légaux** : chaque étape a des contraintes temporelles
- **Traçabilité** : audit trail complet requis
- **Recours** : obligation de recherche et récupération
- **Reporting** : indicateurs conformité et performance obligatoires

## Alternatives considérées

**Alternative 1 :** Processus simplifié (5-6 capacités) → rejetée (granularité insuffisante)
**Alternative 2 :** Séparation Sinistres/Prestations → rejetée (redondance organisationnelle)
**Alternative 3 :** Fraude dans Support → rejetée (perd spécificité métier sinistres)

## Impacts sur la BCM

- **10 capacités L2** avec flux principaux et supports
- **Interactions fortes :** avec BSP.004 (contrats), BSP.008 (provisions), STE.002 (conformité)
- **Ownership :** majoritairement "Gestion Sinistres/Prestations" + "Antifraude"

## Conséquences

### Positives
- **Visibilité** complète sur processus critique mutuelle
- **Gouvernance** fine des délais et qualité
- **Alignement** avec organisation opérationnelle

### Négatives / Risques
- **Coordination** intensive entre 10 capacités L2
- **Complexité** dans pilotage transverse performance
- **Interface** nombreuses avec autres BSP

## Traçabilité
- Analyse processus sinistres 2025
- Code Assurance - délais légaux
- RFC 010 section "Sinistres & Prestations"