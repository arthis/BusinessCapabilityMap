# ADR-BSP-005-002 — Distinction "Pilotage des tiers & prestataires" capacité autonome

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Gestion Sinistres, Écosystème Santé
- Tags: BCM, CAP, BSP-005, TiersPayant, ReseauxSante, PTP

## Contexte

Dans l'écosystème mutualiste, la gestion des **tiers et prestataires** dans les sinistres/prestations revêt une importance particulière :
- **Réseaux de soins** (professionnels santé, établissements conventionnés)
- **Experts** techniques (automobile, habitation, responsabilité civile)
- **Réparateurs** et prestataires techniques
- **Tiers-payant** et facturation directe

La question s'est posée d'intégrer cette gestion dans les autres capacités du processus ou de la traiter comme support transverse.

## Décision

Créer **CAP.BSP.PTP.000 "Pilotage des tiers & prestataires"** comme capacité L2 autonome avec :
- **Périmètre :** Référencement, conventionnement, pilotage qualité/coûts, facturation
- **Owner :** Gestion Sinistres / Prestations (coordination avec Écosystème)
- **Nature :** Capacité support transverse au processus sinistres

## Justification

**Spécificités mutuelle santé/prévoyance :**
- **Volume critique** : 70-80% des prestations via réseaux de soins
- **Conventionnement spécifique** : tarifs négociés, engagements qualité
- **Tiers-payant généralisé** : facturation directe, pas d'avance frais
- **Enjeu coûts** : maîtrise tarification et volumes via pilotage réseau

**Complexité écosystème :**
- **Multitude acteurs** : médecins, pharmacies, cliniques, laboratoires, opticiens...
- **Réglementations** : conventionnement CPAM, tarifs opposables, dépassements
- **Géographie** : couverture territoriale, proximité, disponibilité
- **Qualité** : accréditations, indicateurs satisfaction, réclamations

**Distinction avec autres capacités BSP.005 :**
- **IND/ÉDP** utilisent le réseau mais ne le pilotent pas
- **INR** effectue les règlements mais ne gère pas les conventions
- **PRS** suit la performance mais ne pilote pas l'écosystème

## Alternatives considérées

**Alternative 1 :** Intégration dans ÉDP "Évaluation dommages/prestations"
→ rejetée (mélange évaluation ponctuelle et pilotage relationnel)

**Alternative 2 :** Rattachement à B2B Exchange (écosystème externe)
→ rejetée (perd spécificité métier sinistres/prestations)

**Alternative 3 :** Support transverse global "Gestion Tiers"
→ rejetée (dilue expertise métier santé/sinistres)

## Impacts sur la BCM

- **Capacité L2 transverse** à toutes les étapes processus sinistres
- **Interactions fortes :** avec ÉDP (expertise), INR (règlements), DLC (fraude réseau)
- **Interface critique** avec B2B Exchange pour échanges techniques

## Conséquences

### Positives
- **Visibilité** sur enjeu stratégique maîtrise coûts santé
- **Expertise** concentrée sur pilotage écosystème
- **Performance** optimisée relations prestataires

### Négatives / Risques
- **Coordination** nécessaire avec toutes étapes processus
- **Interface complexe** avec B2B Exchange (hub technique)
- **Pilotage** qualité/coûts nécessitant gouvernance forte

## Traçabilité
- Analyse écosystème santé 2025
- Enjeux maîtrise coûts prestations
- RFC 010 "Pilotage des tiers & prestataires"