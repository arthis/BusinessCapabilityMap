# ADR-BSP-005-003 — "Détection & lutte contre la fraude" spécifique sinistres

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Antifraude, Gestion Sinistres
- Tags: BCM, CAP, BSP-005, Fraude, DLC, SpecificiteMetier

## Contexte

La **lutte contre la fraude** dans une mutuelle présente des enjeux spécifiques :
- **Fraude aux prestations** santé/prévoyance (volumes, montants)
- **Fraude documentaire** (fausses factures, prescriptions détournées)
- **Fraude organisée** (réseaux, complicités professionnels santé)
- **Impact financier** critique sur équilibre technique

La question s'est posée de traiter cette capacité au niveau global (STE.002 Conformité) ou de la spécialiser par domaine métier.

## Décision

Créer **CAP.BSP.DLC.000 "Détection & lutte contre la fraude"** comme capacité L2 spécialisée avec :
- **Périmètre :** Fraude spécifique sinistres/prestations (scoring, investigations, sanctions)
- **Owner :** Antifraude (expertise dédiée sinistres)
- **Positionnement :** Capacité support intégrée au processus BSP.005

## Justification

**Spécificités fraude sinistres/prestations :**
- **Patterns métier** : fraude médicale, surconsommation, détournements réseau
- **Données spécialisées** : historiques consommation, comportements atypiques, géolocalisation
- **Timing critique** : détection précoce dans flux instruction (IND) et évaluation (ÉDP)
- **Expertise** : connaissance fine pratiques médicales, tarifications, réseaux

**Enjeux mutualistes :**
- **Impact solidarité** : fraude = surcoût pour tous les sociétaires
- **Éthique mutualiste** : responsabilité collective de préservation ressources
- **Performance technique** : fraude non maîtrisée = déséquilibre S/P
- **Réputation** : crédibilité système mutualiste

**Intégration processus sinistres :**
- **Scoring temps réel** lors instruction (IND)
- **Alertes expertise** lors évaluation (ÉDP)
- **Blocage paiement** lors indemnisation (INR)
- **Sanctions réseau** via pilotage tiers (PTP)

## Alternatives considérées

**Alternative 1 :** Rattachement à STE.002 "Conformité" (fraude globale)
→ rejetée (perd spécificité métier et réactivité opérationnelle)

**Alternative 2 :** Capacité Support transverse "Antifraude générale"
→ rejetée (dilue expertise sinistres dans autres typologies)

**Alternative 3 :** Intégration dans IND "Instruction dossier"
→ rejetée (mélange instruction normale et suspicion fraude)

## Impacts sur la BCM

- **Capacité L2** intégrée flux processus BSP.005
- **Interactions fortes :** IND (alertes), ÉDP (investigation), INR (blocages), PTP (sanctions)
- **Interface** avec STE.002 pour reporting réglementaire fraude

## Conséquences

### Positives
- **Réactivité** maximale (intégration processus opérationnel)
- **Expertise** spécialisée fraude sinistres/prestations
- **Performance** optimisée détection/traitement

### Négatives / Risques
- **Coordination** avec conformité réglementaire (STE.002)
- **Gouvernance** sanctions et mesures disciplinaires
- **Formation** équipes instruction sur détection fraude

## Traçabilité
- Analyse typologie fraudes mutuelle 2025
- Enjeux performance technique
- RFC 010 "Détection & lutte contre la fraude"