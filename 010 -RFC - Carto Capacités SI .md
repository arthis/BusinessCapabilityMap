# Macro capabilities

## Steering

### **Pilotage d'Entreprise**

Capacités permettant le pilotage global de l'entreprise

### **Conformité**

Capacités de gestion de la conformité réglementaire, des contrôles internes et du respect des obligations légales.

## Business Service Production

### **Produits & Tarification**

Capacités de définition, paramétrage et évolution des produits d'assurance.

### **Canaux & Intermédiation**

Capacités supportant la vente, les réseaux et les partenaires.

> **Canaux & Intermédiation** correspond au domaine “distribution / vente via réseaux & intermédiaires”, mais **sans empiéter** sur :
> 
> - **Channel** (UX omnicanale, portails, front)
> - **B2B Exchange** (hub d’échanges / API / onboarding technique)
> 
> ici sont décrites les capacités “métier SI” qui permettent d’opérer la distribution (courtiers, partenaires, entreprises, réseaux), ses règles, ses conventions, et son pilotage
> 

### **Souscription & Acceptation du Risque**

Capacités permettant l'analyse, la décision et la formalisation du risque.

> **Souscription & Acceptation du Risque** s’arrête à :
> 
> - décision
> - engagement initial
> - dossier complet prêt à émettre

### **Administration des Contrats**

Capacités assurant la tenue et l'exécution des contrats dans le temps.

> **Administration des Contrats** démarre à :
> 
> - émission
> - prise d’effet
> - vie du contrat

### **Sinistres & Prestations**

Capacités supportant la déclaration, l'instruction et l'indemnisation.

### **Interaction & Service Client**

Capacités de gestion des interactions, demandes et réclamations clients.

### **Cotisations & Recouvrement ( à mettre au niveau macro capabilty ?)**

Capacités de gestion des flux de cotisations, prélèvements et recouvrement des impayés.

- encaissement des cotisations (prélèvement, virement, chèque)
- gestion des rejets et relances
- recouvrement amiable et contentieux

### **Finance & Actuariat**

Capacités financières, comptables et prudentielles.

- provisionnement
- marges techniques
- pricing inputs
- solvabilité / prudentiel

## Support

### **Cybersecurity & Security Operations**

Capacités de protection contre les cybermenaces, gestion des incidents de sécurité et surveillance continue des systèmes d'information. (inclus IAM et access policies)

### **Gestion des Prestataires**

Capacités de sélection, pilotage et suivi des fournisseurs et partenaires externes.

### **Comptabilité & clôture**

Capacités de tenue des comptes, enregistrement des écritures et reporting financier.

- écritures
- clôtures mensuelles/annuelles
- déclaratifs comptables

### **Interopérabilité**

Capacités de transformation et correspondance des données entre systèmes hétérogènes. ( Data Integration, Api Management,…)

### **Gestion documentaire**

Capacités de stockage, indexation, recherche et archivage des documents. ( inclus l'archivage probatoire)

### **Workflow / BPM / Case Management**

Capacités d'orchestration des processus métier, de gestion des flux de travail et de pilotage des dossiers complexes nécessitant coordination et suivi.

### **Gestion des communications / éditique**

Capacités de composition, génération, diffusion et suivi des communications sortantes (courriers, emails, SMS) et de production documentaire contractuelle.

## Referential

### **Référentiel Personne**

Capacités de gestion centralisée des données d'identité et d'état civil des personnes physiques et morales.

### **Référentiel Adresse**

Capacités de normalisation, validation et géolocalisation des adresses postales.

### **Référentiel Climat**

Capacités de mise à disposition des données météorologiques et climatiques historiques et prévisionnelles.

### **Référentiel Véhicules**

Capacités de gestion des données techniques et administratives des véhicules (marques, modèles, caractéristiques).

### **Référentiel bancaire**

Capacités de gestion des coordonnées bancaires, IBAN, BIC et validation des RIB.

### **Référentiel organisation**

Capacités de gestion de la structure organisationnelle interne (entités, services, hiérarchies).

### **Référentiel Contrat / Police**

Capacités de gestion centralisée des contrats et polices d'assurance, incluant les données de couverture, garanties, et historique contractuel.

### **Référentiel Produit / Garanties / Tarification**

Capacités de gestion centralisée des définitions de produits, garanties, options et règles de tarification.

Produits & Tarification en production, mais un *référentiel* :

- est utilisé par souscription
- par contrats
- par sinistres
- par distribution

Donc il est transversal.

## B2B Exchange

*Capacités permettant de connecter et d’opérer les échanges avec l’écosystème (délégataires, réseaux de soin, partenaires, régulateur, prestataires, data providers), avec traçabilité, sécurité, SLA et standardisation.*

> cette zone devient la **“façade écosystème”**. Elle complète le **Support/Interopérabilité** (qui est plus “interne SI”), en focalisant sur les échanges **avec des tiers** et leurs contraintes (SLA, onboarding, preuve, sécurité, formats)
> 

### **Onboarding  & gouvernance partenaires**

- référencement partenaire, habilitations B2B
- SLA / conventions d’échanges / responsabilités

### **Hub d'échanges partenaires**

- routage des flux B2B
- transformation, enrichissement, orchestration (sans remplacer ton “Interopérabilité”, mais en se focalisant sur *l’écosystème*)

### **API externes & portail partenaire**

- API externes, clés, quotas, portail développeur
- versioning / compatibilité

### **Échanges délégataires**

- délégation sinistres/prestations, cotisations
- contrôles, reporting et réversibilité

### **Échanges santé / tiers payant**

- demandes PEC, factures, remboursements
- échanges NOEMIE (si applicable), flux normalisés

### **Échanges intermédiation**

- devis, souscriptions, avenants
- commissions / suivi portefeuille

### **Échanges financiers**

- banques (SEPA, rejets, mandats)
- paiements / rapprochements (si tu ne crées pas une brique “Paiements & encaissements”)

### **Échanges réglementaires**

- supervision / contrôle (selon obligations)
- dépôts, déclaratifs, preuves d’audit

### **Traçabilité, sécurité des flux**

- journalisation, preuve, horodatage
- contrôle conformité des échanges, chiffrement, signature

## Channel

*Capacités permettant d’exposer des parcours et services aux utilisateurs finaux (adhérents, prospects, entreprises, conseillers, intermédiaires) de façon cohérente, omnicanale et mesurable.*

> ne dupliques pas “Interaction & Service Client” (qui reste production/cœur métier), channel représente   **le “delivery” omnicanal** et la **couche expérience**
> 

### **Expérience omnicanale & parcours**

- cohérence des parcours web/mobile/agence/téléphone
- orchestration front-to-back

### **Portails adhérent & entreprise**

- espace adhérent (contrat, remboursements, attestations)
- espace entreprise (contrats collectifs, populations, reporting)

### **Poste de travail conseiller / front-office**

- poste de travail conseiller
- “assisted selling” (devis, souscription, modification)

### **Acquisition digitale**

- tunnel devis → souscription
- formulaires, simulation, collecte pièces

### **Centre de contact**

- notifications (email/SMS/push)
- campagnes et messages transactionnels (côté expérience)

### **Engagement & notifications**

- CTI (couplage téléphonie-informatique), routage, scripts, base de connaissances
- suivi de la qualité de service

### **Mesure des parcours**

- tracking parcours (conversion, abandon)
- feedback, NPS / CSAT (si utilisé)

<aside>
🗣

- **Channel** = *UX, parcours, exposition* (front)
- **B2B Exchange** = *écosystème, flux externes, SLA, onboarding* (outside-in / inside-out)
- **Interopérabilité (Support)** = *mécanismes transverses d’intégration* (inside-in)
</aside>

## Data & Analytics

### **Gouvernance des données**

- rôles (data owner / steward), politiques
- glossaire / dictionnaire
- gestion du cycle de vie des données

### **Ingestion & alimentation data**

- collecte des données depuis le SI (batch/stream)
- alimentation depuis partenaires (en complément de B2B Exchange)
- orchestration des pipelines

> ⚠️ à distinguer l’ “Interopérabilité” (Support) :
      → **Interopérabilité** = échanges applicatifs “opérationnels” (transactionnels)
      → **Ingestion Data** = alimentation analytique (décorrélée de l’opérationnel)
> 

### **Plateformes de données**

- data lake / warehouse (sans entrer dans la techno)
- gestion des zones (raw/curated/serving)
- archivage data / rétention (si pertinent)

### **BI & reporting**

- reporting réglementaire (si tu veux le rattacher au data)
- tableaux de bord métier (sinistres, prestations, adhésions…)
- self-service BI

### **Analytics avancé & IA**

- scoring fraude, churn, propension
- modèles de prévision (charge sinistres, S/P, consommation santé)
- industrialisation des modèles (MLOps si tu veux, mais tu peux rester “capability”)

### **Partage & accès aux données**

- catalogue de données / data marketplace interne
- API data / extractions contrôlées
- habilitations data (liens avec IAM mais côté “données”)

### **Protection & conformité des données**

- classification, anonymisation/pseudonymisation
- gestion des consentements côté data (lien RGPD)
- contrôle des usages (purpose limitation)

# Capabilities

## **Pilotage d'Entreprise**

### **Définition de la stratégie et des objectifs**

- déclinaison des orientations stratégiques
- objectifs et trajectoires pluriannuelles

### **Pilotage de la performance (KPI / tableaux de bord)**

- indicateurs métier (adhésions, prestations, sinistres)
- suivi qualité de service
- pilotage coûts / productivité

### **Pilotage de l'activité et des opérations**

- suivi charge / capacité
- pilotage de la qualité opérationnelle
- plans d’amélioration continue

### **Contrôle de gestion et pilotage budgétaire**

- construction budgétaire
- suivi du réalisé / forecast
- analyse des écarts

### **Pilotage du portefeuille (offres / garanties / populations)**

- suivi des offres et populations couvertes
- pilotage des segments (individuel / collectif)
- analyses de rentabilité

### **Pilotage du risque global (ERM / risques opérationnels)**

*(hors conformité réglementaire au sens strict, ici on parle surtout pilotage entreprise)*

- cartographie des risques
- suivi des risques opérationnels
- suivi incidents majeurs

### **Pilotage de la transformation**

- gestion de portefeuille projets
- arbitrage, priorisation, suivi bénéfices
- conduite du changement

### **Pilotage de la relation partenaires**

(essentiel en mutuelle : délégataires, opérateurs, réseaux de soin)

- pilotage délégations de gestion
- pilotage prestataires
- performance contractuelle

## Conformité

### **Veille réglementaire et interprétation**

- identification des textes applicables (assurance, mutualité, ACPR…)
- analyse d’impact
- diffusion interne

### **Gestion des obligations prudentielles**

(mutuelle = obligations fortes autour des équilibres et de la supervision)

- exigences de solvabilité (Solvabilité II le cas échéant / cadre applicable)
- exigences de fonds propres
- éléments de justification et documentation

### **Gestion du contrôle interne**

- dispositifs de contrôle
- plan de contrôle interne
- suivi des résultats / anomalies

### **Gestion des audits et inspections**

- audits internes
- audits externes
- préparation et réponses aux inspections (ACPR notamment)

### **Conformité RGPD & protection des données**

- registre des traitements
- gestion des droits (accès, rectification, suppression…)
- analyses d’impact (AIPD/DPIA)
- gouvernance des consentements

### **Conformité lutte contre la fraude & abus**

(important en mutuelle : fraude prestations / fraude documentaire)

- détection et instruction des suspicions
- dispositifs antifraude
- coopération avec partenaires / délégataires

### **Conformité LCB-FT (si applicable)**

Variable selon activités exactes de la mutuelle (produits vie/épargne notamment)

- KYC / connaissance membre
- screening, alerting
- reporting

### **Gestion des politiques, normes et référentiels**

- politiques internes (éthique, sécurité, délégation…)
- référentiels / procédures de conformité
- traçabilité et versioning

### **Gestion des réclamations réglementaires et médiation**

(la réclamation est aussi “Relation Client”, mais l’obligation de dispositif relève souvent conformité)

- suivi des réclamations et obligations de réponse
- reporting conformité
- médiation / litiges

### **GRC SI / conformité sécurité**

(ex : ISO27001, DORA si applicable, contrôles IT…)

- gestion des risques SI et cybersécurité
- conformité des systèmes d'information aux exigences réglementaires
- audits de sécurité et plans de remédiation

## Produits & Tarification

> Bon alignement avec le **Référentiel Produit / Garanties / Tarification** :
> 
> - le référentiel = données “master”
> - Produits & Tarification = règles + gouvernance + cycle de vie

### **Conception et structuration des produits**

- définition des offres (santé / prévoyance / IARD selon cas)
- construction des garanties / options
- règles d’éligibilité (cibles, populations, conditions)

### **Paramétrage des règles produits et garanties**

- règles de couverture (franchises, plafonds, exclusions)
- règles contractuelles (carence, délais, limites)
- versioning produit (évolutions dans le temps)

### **Construction et maintenance des modèles tarifaires**

- modèles de tarification (variables, segmentation, coefficients)
- règles de remises / majorations
- tarification individuel vs collectif

### **Publication et gouvernance du catalogue produit**

- mise à disposition aux canaux / souscription / contrats / sinistres
- gestion des versions en production
- traçabilité, validation, cycle de vie des offres

## **Canaux & Intermédiation**

<aside>
🎯

Disambiguation :

- Lien avec **Channel**
    - Channel = *exposition des parcours*
    - Canaux & Intermédiation = *règles de distribution + réseaux + opérations de vente*
- Lien avec **B2B Exchange**
    - B2B Exchange = *moyen technique d’échange (hub, API, traçabilité)*
    - Canaux & Intermédiation = *contenu métier des échanges (qui, quoi, à quelles conditions)*
- Lien avec **Administration des contrats**
    - Canaux & Intermédiation s’arrête au **commercial**
    - Administration des contrats prend le relais pour la **vie du contrat**
</aside>

### **Gestion des réseaux et intermédiaires**

- référencement des intermédiaires (courtiers, apporteurs, partenaires)
- organisation commerciale / rattachements
- habilitations métier (qui peut vendre quoi)

> ⚠️ Ne pas confondre avec IAM : ici c’est l’habilitation “business”.
> 

### **Gestion des conventions et conditions commerciales**

- conventions de distribution / accords
- conditions tarifaires spécifiques
- gestion des dérogations commerciales

### **Distribution des offres et des règles par canal**

- catalogue vendable par canal
- règles d’éligibilité / contraintes de canal
- gestion des campagnes de mise à dispo des offres

### **Gestion des actes de vente intermédiés**

- suivi des devis / souscriptions via intermédiaire
- traitement des demandes intermédiaires (modifs, résiliations initiées)
- traçabilité des opérations commerciales

> Ici on est sur le “parcours commercial B2B”, pas sur le portail.
> 

### **Commissions, rémunérations et incentives**

- calcul commissions et rétrocessions
- primes / challenges / incentives
- régularisations et litiges commissions

### **Pilotage de la distribution & conformité commerciale**

- pilotage portefeuille par canal / intermédiaire
- suivi performance (conversions, churn, coûts acquisition)
- contrôles distribution (devoir de conseil, commercialisation conforme)

## Souscription & Acceptation du Risque

### **Qualification de la demande**

- recueil du besoin (prospect / entreprise)
- qualification du contexte (individuel / collectif, produit, canal)
- complétude initiale du dossier

### **Évaluation du risque**

- analyse du profil / exposition au risque
- collecte d’informations et pièces
- règles d’éligibilité et contrôles
- questionnaire médical / sélection médicale (si applicable)
- règles d’adhésion collective et d’éligibilité

### **Calcul de tarif & simulation**

- application des règles tarifaires
- simulation multi-scénarios (options / garanties)
- prise en compte des remises / conditions commerciales

> ⚠️ cette capacité consomme le référentiel “Produit / Garanties / Tarification”.
> 

### **Décision de souscription**

- acceptation / refus
- exclusions, surprimes, conditions particulières
- règles d’autorisation / délégation

### **Formalisation de l'engagement**

- constitution du dossier final
- génération des conditions particulières (pré-contractuel)
- validation / consentement / signature (selon cadre)

### **Contrôles & sécurisation de la souscription**

- contrôles de cohérence
- anti-fraude à l’entrée
- contrôles conformité (KYC/LCB-FT si applicable, RGPD consentements)

## Administration des Contrats

### **Émission & mise en vigueur du contrat**

- émission / activation
- prise d’effet
- documents contractuels initiaux

### **Tenue du contrat**

- maintien des données de police
- gestion garanties / options
- historisation des versions

### **Mouvements contractuels (avenants / modifications)**

- changements de couverture
- changements administratifs
- traçabilité des modifications

### **Adhésions & droits (bénéficiaires / populations)**

- affiliation / radiation
- ayants droit / bénéficiaires
- ouverture / fermeture des droits

### **Renouvellement, suspension & résiliation**

- renouvellements
- suspensions
- résiliations / clôture

### **Services contractuels & preuves**

- attestations / justificatifs
- mise à disposition (selfcare / partenaires)
- audit trail / conservation probatoire

## **Sinistres & Prestations**

### **Déclaration du sinistre / de la prestation**

Capacités permettant de capter et qualifier un événement garanti.

- Multicanal (client, intermédiaire, partenaire)
- Qualification initiale
- Rattachement au contrat

### **Ouverture & Enregistrement du dossier**

Capacités assurant la création et la structuration du dossier sinistre.

- Création du dossier
- Typage du sinistre
- Attribution initiale

### **Instruction du dossier**

Capacités de traitement métier du sinistre ou de la prestation.

- Analyse des garanties
- Vérification des droits
- Collecte des pièces
- Décisions intermédiaires

### **Évaluation des dommages / prestations**

Capacités d’estimation financière et technique.

- Évaluation directe
- Gestion des expertises
- Réévaluations

### **Indemnisation / Règlement**

Capacités permettant le paiement ou la prise en charge.

- Calcul des montants
- Ordonnancement des paiements
- Suivi des règlements

### **Pilotage des tiers & prestataires**

Capacités de gestion des intervenants externes.

- Experts
- Réparateurs
- Professionnels de santé
- Réseaux partenaires

### **Recours & subrogation**

Capacités permettant la récupération des sommes auprès de tiers responsables.

- Identification des recours
- Suivi des procédures
- Encaissement des montants

### **Détection & lutte contre la fraude**

Capacités d’identification et de traitement des situations frauduleuses.

- Scoring
- Alertes
- Investigations

### **Clôture & archivage du dossier**

Capacités de finalisation du cycle de vie.

- Clôture administrative
- Archivage
- Traçabilité

### **Pilotage & reporting des sinistres**

Capacités de suivi de l’activité et de la performance.

- Indicateurs
- Tableaux de bord
- Analyse des coûts et délais

### Matrice de correspondance

| Capacité métier (valeur) | Capacité SI ( |
| --- | --- |
| Accueil et prise en charge | Déclaration du sinistre |
| Analyse de la couverture | Ouverture & instruction |
| Instruction du dossier | Instruction du dossier |
| Évaluation de l’impact | Évaluation des dommages |
| Indemnisation ou prise en charge | Indemnisation / règlement |
| Accompagnement de l’assuré | Interaction & service client 
(Macro capacité) |
| Maîtrise des coûts et risques | Fraude & recours |
| Clôture du sinistre | Clôture & archivage |
| — | Pilotage & reporting |

## Finance & Actuariat

### **Pilotage financier & performance économique**

- suivi de la performance (S/P, marge technique, frais de gestion)
- analyse de rentabilité (produits, segments, populations)
- budget, forecasts et atterrissages

### **Actuariat, provisions & équilibres techniques**

- calcul des provisions techniques
- hypothèses actuarielles / modèles
- analyse de la sinistralité / consommation
- contribution aux évolutions tarifaires (inputs pricing)

### **Prudentiel & reporting réglementaire**

- solvabilité / fonds propres (selon cadre applicable)
- reporting prudentiel
- production des états réglementaires et justificatifs

## Interaction & Service Client

Cette structuration permet de couvrir :

- service “standard”
- service “complexe”
- réclamation
- assistance / accompagnement (spécifique mutuelle)

### **Accueil, orientation & qualification des demandes**

- prise en charge multicanale (téléphone, mail, portail, agence)
- qualification / catégorisation des demandes
- orientation vers le bon service (front/back)

### **Traitement des demandes & actes de service**

- exécution des demandes courantes (attestations, modifications simples, informations)
- demandes complexes nécessitant suivi et coordination
- suivi des engagements / délais (SLA)

> Cette capacité s’appuie souvent sur Support : Workflow/BPM/Case Management + GED.
> 

### **Réclamations, litiges & médiation**

- enregistrement et traitement des réclamations
- suivi des litiges
- médiation (selon obligations)

> NB : la gouvernance “obligations réglementaires” est côté Conformité, ici c’est le traitement opérationnel.
> 

### **Assistance & accompagnement sociétaire**

- assistance santé / prévoyance / services associés
- accompagnement du parcours (information proactive)
- coordination avec partenaires (ex : réseaux de soins)

## Cotisations & Recouvrement

Avec ces 3 capacités on couvre :

- le “**billing**” (calcul / émission)
- le “**cash**” (encaissement)
- le “**collection**” (recouvrement)

### **Calcul & émission des cotisations**

- calcul des montants (individuel / collectif)
- prise en compte des évolutions contractuelles (avenants, effectifs, ayants droit)
- émission des appels / échéanciers

### **Encaissement & rapprochement**

- gestion des paiements (prélèvements, virements, chèques, CB selon cas)
- traitement des rejets (SEPA, impayés)
- rapprochement des encaissements et affectation aux contrats

### **Recouvrement & contentieux**

- relances et plans de recouvrement
- gestion des suspensions / résiliations pour non-paiement (en lien avec Administration des contrats)
- traitement des dossiers contentieux et suivi des régularisations

### Interactions clés dans ta BCM

- [ ]  Avec **Administration des Contrats** (Production) 
Pourquoi ? Parce que la cotisation dépend directement de l’état du contrat et de ses mouvements.
- **Entrées vers Cotisations**
    - prise d’effet / émission du contrat
    - avenants (changement garanties/options)
    - adhésions/radiations ayants droit
    - renouvellements / résiliations
- **Sorties vers Administration**
    - suspension pour impayé
    - résiliation pour non-paiement (selon règles)
    - régularisation entraînant remise en vigueur

C’est un couplage structurel : il faut tracer qui déclenche quoi (contrat → cotisation, recouvrement → impacts du contrat).

- [ ]  Avec **Finance & Actuariat** (Production)
Pourquoi ? Car cotisations & Recouvrement alimente la performance technique et la vision prudentielle.
- versements encaissés (réalisé)
- impayés / créances (risque)
- régularisations / annulations
- suivi encours et provisions associées (selon modèle)
- encaissement et impayés ont un impact sur le **ratio de gestion**, la **marge**, et parfois les dispositifs prudentiels.
- [ ]  Avec **Comptabilité & Clôture** (Support)
Pourquoi ?
Car toute cotisation/encaissement produit des écritures et doit être rapproché.
- **Génération / injection des écritures**
    - appels de cotisations
    - encaissements
    - rejets / impayés
    - avoirs / régularisations
- **Rapprochement comptable**
    - lettrage
    - justification des soldes
    - états de clôture

Ici la séparation “Production vs Support” marche bien :

- Cotisation = capacité métier
- Comptabilité = capacité support
- [ ]  Avec **B2B Exchange** (Zone écosystème)
Pourquoi ? Parce que la mutuelle échange avec des tiers : banques, entreprises (collectif), délégataires.
    - **Échanges financiers** (banques)
        - prélèvements SEPA (émission + retours)
        - rejets
        - virements
        - retours d’opération
    - **Entreprises / contrats collectifs**
        - appels de cotisation collectifs
        - intégration des fichiers de paiements / ventilations
        - gestion des écarts
    - **Délégataires**
        - recouvrement délégué ou partagé
        - reporting / contrôle

📌 Astuce d’urbanisation :

- la **décision métier** (ex : impayé > relance > suspension) reste dans Cotisations
- la **mécanique d’échange** reste dans B2B Exchange

- [ ]  Avec **Channel** (Zone parcours) 
Pourquoi ? Car l’expérience adhérent/entreprise inclut paiement, suivi, relances, justificatifs.
- mise à disposition des échéanciers / factures
- paiement en ligne (si présent)
- consultation du statut (à jour / impayé / relance)
- demandes type “relevé de situation”, “attestation de paiement”

Channel est consommateur + point d’action.

Cotisations reste “source of truth”.

- [ ]  Avec **Cybersecurity & Security Operations** (Support)
Pourquoi ?
Encaissement = données sensibles + fraude + exigences de protection.
- contrôle d’accès aux données bancaires (IBAN/RIB)
- traçabilité des actions
- détection d’anomalies (tentatives fraude)
- protection des canaux de paiement
- [ ]  Avec les **Référentiels** (Referential)

Référentiel Contrat/Police

- rattachement des appels à la police
- couverture “à date” / statut contrat

Référentiel bancaire

- IBAN/BIC
- validation RIB
- mandat SEPA (selon choix)

Référentiel Personne / Organisation

- tiers payeur
- entreprise dans les collectifs
- débiteurs multiples

Schéma synthétique (lecture simple)

Tu peux le présenter comme ceci en atelier :

- **Contrats** → déclenche / modifie → **Cotisations**
- **Cotisations** → alimente → **Comptabilité** + **Finance**
- **Cotisations** ↔ échange avec tiers via → **B2B Exchange**
- **Adhérent/Entreprise** ↔ consulte/paye via → **Channel**

# Méthodologie

## Diagram-as-code

### Option A — ArchiMate (standard EA) + outillage

ArchiMate a un **“Capability Map Viewpoint”** dédié (2–3 niveaux + heatmap, etc.). Très aligné “urbanisation”.

> Limite : ArchiMate est surtout “modèle + outil” (pas toujours “as-code” natif), mais certains outils s’intègrent à des exports.
> 

### Option B — Structurizr DSL (diagramme-as-code) via "custom elements"

Structurizr est orienté “model + views” (C4) mais supporte des **éléments custom** et des **custom views** : parfait pour représenter des capacités sous forme de boîtes (L1/L2) et éventuellement des liens.

> versionning dans Git et automatisation
> 

Exemple (Structurizr DSL, style capability map simplifié) :

```
workspace "Capability Map" "Vue urbanisation/fonctionnelle" {
  model {
    l1_sales = element "Ventes" "L1"
    l2_quote = element "Gérer la tarification" "L2"
    l2_order = element "Gérer la commande" "L2"

    l1_sales -> l2_quote "contient"
    l1_sales -> l2_order "contient"
  }

  views {
    custom "capabilities" {
      title "Business Capability Map (extrait)"
      include *
      autoLayout lr
    }
  }
}

```

### Option C — Mermaid / PlantUML / D2 (rapide, lisible, "boîtes imbriquées")

- **Mermaid** (flowchart) : super dans Markdown (GitLab/GitHub, docs).
- **PlantUML** : robuste, beaucoup d’outils.
- **D2** : excellent rendu “box diagrams”, très “diagram-as-code”.

> Pour une capability map “pure”, tu utilises surtout des **groupements/cluster** (L1 contenant L2). Pour une heatmap, tu ajoutes des **styles par classe** (couleur selon maturité, criticité, etc.).
> 

---

### Reco pratique

- **1 fichier “référentiel capacités”** (YAML/JSON/CSV) : id, nom, niveau, parent, description, owner, criticité…
- **1 génération de vues** (Mermaid/D2/Structurizr) :
    - Vue “capability map” (L1/L2)
    - Vue “capabilities ↔ applications”
    - Vue “capabilities ↔ data domains”
- **Heatmaps** : calculées via attributs (maturité, risque, coût) puis rendues en style.

# **🔨  Implementation**

---

<aside>
💡

Many RFCs have an "implementation" section which details how the implementation will work. This section should explain the rough API changes (internal and external), package changes, etc. The goal is to give an idea to reviews about the subsystems that require change and the surface area of those changes.

This knowledge can result in recommendations for alternate approaches that perhaps are idiomatic to the project or result in less packages touched. Or, it may result in the realization that the proposed solution in this RFC is too complex given the problem.

</aside>

# **😣 Abandoned Ideas (Optional)**

---

<aside>
💡

As RFCs evolve, it is common that there are ideas that are abandoned. Rather than simply deleting them from the document, you should try to organize them into sections that make it clear they're abandoned while explaining *why* they were abandoned. 
When sharing your RFC with others or having someone look back on your RFC in the future, it is common to walk the same path and fall into the same pitfalls that we've since matured from. Abandoned ideas are a way to recognize that path and explain the pitfalls and why they were abandoned.

</aside>

# **📊 Recherche**

---

# **🔮 Future considerations**

---

##

- 
- envisager “Cotisations & Recouvrement” comme domaine distinct
- 

## ➕ Briques manquantes importantes

- Paiements & encaissements (ou payment hub)
- Gouvernance Data (si zone Data créée)

Dans Data & Analytics
futures capacités possibles :

### **Qualité & traçabilité (data lineage)**

- contrôles qualité, règles, exceptions
- traçabilité, data lineage
- monitoring des flux et données

### **Modélisation & data products**

- modèles analytiques (faits/dimensions, data products)
- standardisation, enrichissement, dédoublonnage (hors MDM pur)
- référentiels analytiques

**📚 Ressources**

---

# **📅 Chronologie**

---

[POS 2024](https://www.notion.so/POS-2024-2e6861c5d854803c87e1d755ba917da7?pvs=21)