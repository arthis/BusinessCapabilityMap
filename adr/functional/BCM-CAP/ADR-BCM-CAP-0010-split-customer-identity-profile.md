# ADR-BCM-CAP-0010 — Séparer “Gérer l’identité client” et “Gérer le profil client”

- Statut: Accepted
- Date: 2026-01-21
- Décideurs: Business Architecture, Digital, Sécurité
- Tags: BCM, CAP, Split, Customer

## Contexte
Dans les ateliers, la capacité “Gérer le client” recouvrait :
- identité (authentification, identifiants),
- profil (données CRM, préférences, consentements).

Cette fusion masque des décisions d’urbanisation : responsabilités, produits SI et trajectoires distincts.

## Décision
Créer deux capacités L2 distinctes :
- CAP.CUST.010 “Gérer l’identité client” (zoning CHANNELS, owner Digital/Sécurité)
- CAP.CUST.020 “Gérer le profil client” (zoning BUSINESS SERVICE PRODUCTION, owner CRM)

## Justification
- Identité = problématiques IAM/CIAM + sécurité + cycle de vie différent.
- Profil = information business + CRM/CDP + gouvernance data différente.

Alternative : une capacité unique “Gérer le client” rejetée (non actionnable pour l’urbanisation).

## Impacts sur la BCM
- Capacités impactées : CAP.CUST.010, CAP.CUST.020
- Parent : CAP.CUST.000
- Zoning : CHANNELS vs BUSINESS SERVICE PRODUCTION
- Mapping SI : CIAM/IAM vs CRM/CDP (à formaliser via ADR-BCM-MAP-xxxx si besoin)

## Conséquences
### Positives
- Clarifie ownership, trajectoires et responsabilités.
### Négatives / risques
- Besoin d’une décision de “mastership” et synchronisation (future ADR).

## Traçabilité
- Atelier Customer 2026-01-10
