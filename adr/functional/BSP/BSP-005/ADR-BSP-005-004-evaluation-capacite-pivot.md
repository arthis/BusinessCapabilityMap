# ADR-BSP-005-004 — Évaluation des dommages en tant que capacité pivot

- Statut: Accepted
- Date: 2026-01-22
- Décideurs: Business Architecture, Gestion Sinistres, Expertise
- Tags: BCM, CAP, BSP-005, ÉDP, Evaluation, Pivot

## Contexte

L'**évaluation des préjudices/dommages** constitue un point critique dans le processus sinistres :
- **Expertise technique** sur dommages (médical, matériel, responsabilité)
- **Décision indemnisation** (quantum, acceptation, refus)
- **Enjeux financiers** majeurs (provisions, réserves, rentabilité)
- **Interface multiple** (clients, professionnels, assureurs, réassureurs)

Cette capacité pourrait être :
- **Intégrée** dans l'instruction (IND)
- **Fusionnée** avec indemnisation (INR)
- **Autonome** avec expertise dédiée

## Décision

Maintenir **CAP.BSP.ÉDP.000 "Évaluation des préjudices/dommages"** comme **capacité pivot autonome** avec :
- **Périmètre :** Expertise, évaluation quantum, décision acceptation/refus
- **Positionnement :** Interface entre instruction (IND) et indemnisation (INR)
- **Ressources :** Experts internes/externes, médecins-conseils, réseaux spécialisés

## Justification

**Spécificités expertise mutuelle :**
- **Solidarité mutualiste** : juste évaluation préjudice = équité entre sociétaires
- **Expertise spécialisée** : santé/prévoyance nécessite compétences médicales
- **Volume/complexité** : masses importantes nécessitent organisation dédiée
- **Enjeux techniques** : impact direct S/P et équilibre mutuelle

**Rôle pivot dans processus :**
- **Input :** dossiers instruits et documentés (IND)
- **Processing :** évaluation technique, avis médical, décision
- **Output :** décision indemnisation + quantum vers (INR)

**Valeur autonomie :**
- **Indépendance** décisionnelle (séparation instruction/évaluation/paiement)
- **Expertise** concentrée et spécialisée
- **Traçabilité** décisions et motivations
- **Performance** dédiée sur enjeu critique

## Alternatives considérées

**Alternative 1 :** Fusion avec IND "Instruction dossier"
→ rejetée (mélange analyse formelle et expertise technique)

**Alternative 2 :** Fusion avec INR "Indemnisation & règlement"
→ rejetée (mélange décision et exécution paiement)

**Alternative 3 :** Externalisation complète expertise
→ rejetée (perte contrôle, cohérence, responsabilité mutualiste)

## Architecture processus résultante

```
DSP → OED → IND → ÉDP → INR → RES
              ↓     ↓     ↓
              PTP → DLC → CAD
```

**ÉDP = point de décision critique** avec :
- **Interfaces amont :** IND (dossiers instruits)
- **Interfaces aval :** INR (décisions indemnisation)
- **Interfaces support :** PTP (experts), DLC (fraude), CAD (contentieux)

## Conséquences

### Organisationnelles
- **Équipe expertise** dédiée (médecins-conseils, experts techniques)
- **Processus** séparation claire instruction/évaluation/paiement
- **Gouvernance** décisionnelle sur acceptation/refus/quantum

### Techniques
- **Outils** spécialisés évaluation (barèmes, référentiels, IA)
- **Interfaçage** avec INR pour transmission décisions
- **Reporting** performance évaluation et justesse provisionnement

### Risques
- **Délai** traitement (étape supplémentaire)
- **Cohérence** décisionnelle (harmonisation pratiques)
- **Interface** complexe avec instruction et indemnisation

## Traçabilité
- Analyse processus sinistres mutuelle
- Benchmark expertise secteur
- RFC 007 "Évaluation des préjudices/dommages"