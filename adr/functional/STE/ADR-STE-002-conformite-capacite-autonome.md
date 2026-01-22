# ADR-STE 002 — "Conformité" comme capacité L1 distincte du "Pilotage"

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Direction Générale, Conformité, Risk Management
- Tags: BCM, CAP, Conformité, Governance, Separation

## Contexte

Dans le secteur mutualiste, la conformité présente des enjeux réglementaires majeurs :
- **Supervision ACPR** spécifique aux organismes d'assurance
- **Code de la Mutualité** avec obligations particulières
- **Solvabilité II** (selon taille et activités)
- **Réglementations transverses** (RGPD, LCB-FT, DORA)

La question s'est posée d'intégrer la conformité dans une capacité plus large "Gouvernance & Pilotage".

## Décision

Maintenir **CAP.STE.002 "Conformité"** comme capacité L1 autonome :
- **Périmètre :** Veille réglementaire, contrôle interne, audits, obligations prudentielles, RGPD
- **Owner :** Conformité / Risques  
- **Zoning :** STEERING
- **Distinction claire** avec CAP.STE.001 "Pilotage d'Entreprise"

## Justification

**Spécificités secteur mutualiste :**
- **Intensité réglementaire** : mutuelle = statut particulier avec obligations spécifiques
- **Supervision dédiée** : reporting ACPR, inspections, justifications prudentielles
- **Responsabilité personnelle** des dirigeants en cas de manquement
- **Expertise juridique** nécessaire (veille, interprétation, mise en œuvre)

**Disambiguation avec "Pilotage" :**
- **Conformité** = *obligations légales, contrôles, reporting externe imposé*
- **Pilotage** = *performance, stratégie, objectifs internes, optimisation*

**Enjeux organisationnels :**
- **Indépendance** de la fonction conformité (recommandations régulateur)
- **Reporting direct** à la Direction Générale / Conseil d'Administration
- **Expertise spécialisée** distincte du contrôle de gestion

## Alternatives considérées

**Alternative 1 :** Intégration dans "Pilotage d'Entreprise" → rejetée (dilue spécificité réglementaire)
**Alternative 2 :** Capacité "Gouvernance & Contrôle" globale → rejetée (mélange enjeux internes/externes)
**Alternative 3 :** Rattachement à "Support" → rejetée (perd visibilité steering)

## Impacts sur la BCM

- **Capacité maintenue :** CAP.STE.002
- **10 sous-capacités L2 :** Veille réglementaire, Prudentiel, Contrôle interne, Audits, RGPD, etc.
- **Interactions fortes :** avec toutes les capacités métier (contrôles transverses)

## Conséquences

### Positives
- Visibilité et gouvernance renforcées sur les enjeux réglementaires
- Alignement avec l'organisation type des mutuelles
- Facilite le reporting et les audits ACPR

### Négatives / Risques
- Coordination nécessaire avec "Pilotage" pour éviter la redondance
- Risque de cloisonnement si gouvernance insuffisante

## Traçabilité
- Code de la Mutualité - art. L114-17 (fonction conformité)
- Recommandations ACPR sur gouvernance
- RFC 010 section "Conformité"