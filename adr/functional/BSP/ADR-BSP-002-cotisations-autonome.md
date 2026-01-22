# ADR-BSP 002 — "Cotisations & Recouvrement" comme capacité L1 autonome

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Finance, Direction Métier
- Tags: BCM, CAP, BSP, Cotisations, FinancialCriticality

## Contexte

Dans le modèle mutualiste, la gestion des **cotisations** représente :
- Le **flux financier principal** (90%+ des revenus)  
- Un **enjeu de liquidité critique** pour l'équilibre technique
- Des **obligations réglementaires** spécifiques (Code Mutualité)
- Un **couplage structurel** avec l'administration des contrats

La question s'est posée d'intégrer cette capacité dans BSP.004 "Administration des Contrats" ou BSP.008 "Finance & Actuariat".

## Décision

Créer **CAP.BSP.007 "Cotisations & Recouvrement"** comme capacité L1 autonome avec :
- **Périmètre :** Calcul, émission, encaissement, recouvrement des cotisations
- **Owner :** Gestion Cotisations (rattachée Finance)
- **3 sous-capacités L2 :** Calcul/Émission, Encaissement, Recouvrement

## Justification

**Criticité financière :**
- **Impact direct solvabilité :** impayés = risque immédiat sur équilibre technique
- **Volumétrie exceptionnelle :** millions d'appels/an, flux quotidiens
- **Expertise spécifique :** règles complexes collectif/individuel, SEPA, relances

**Spécificités réglementaires :**
- **Code Mutualité :** obligations suspension/résiliation pour impayés
- **Délais impératifs :** procédures de recouvrement encadrées
- **Traçabilité :** audit trail sur décisions impact contrat

**Interactions identifiées avec autres BSP :**
- **BSP.004 → BSP.007 :** mouvements contractuels déclenchent recalcul cotisations
- **BSP.007 → BSP.004 :** impayés déclenchent suspension/résiliation
- **BSP.007 → BSP.008 :** encaissements alimentent performance financière
- **BSP.007 ↔ STE.001 :** pilotage cash-flow et trésorerie

**Interactions avec STEERING :**
- **STE.001** pilote taux recouvrement, délais encaissement (KPI critiques)
- **STE.002** contrôle respect procédures réglementaires recouvrement

## Alternatives considérées

**Alternative 1 :** Intégration dans BSP.004 "Administration Contrats" 
→ rejetée (dilue criticité financière, ownership finance vs contrats)

**Alternative 2 :** Intégration dans BSP.008 "Finance & Actuariat"
→ rejetée (logique opérationnelle vs pilotage, volumétrie vs analyse)

**Alternative 3 :** Capacité Support "Paiements & Encaissements"
→ rejetée (perd spécificité métier mutuelle, impact réglementaire)

## Impacts sur la BCM

- **Capacité L1 autonome :** CAP.BSP.007  
- **Couplage fort** avec BSP.004 (contrats) et BSP.008 (finance)
- **Interactions critiques** avec Support (Comptabilité, B2B Exchange)

## Conséquences

### Positives
- **Visibilité** renforcée sur enjeu financier critique
- **Responsabilité** claire (expertise finance + opérationnel)
- **Gouvernance** adaptée aux volumes et criticité

### Négatives / Risques
- **Coordination intensive** avec Administration Contrats
- **Interface complexe** contrats ↔ cotisations à bien gouverner

## Traçabilité
- Code Mutualité - art. L221-2 (cotisations)
- Analyse criticité financière 2025  
- RFC 010 section "Cotisations & Recouvrement"