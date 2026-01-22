# BCM + ADR Starter Kit

Objectif : rendre explicites et auditables les décisions d’urbanisme implicites dans une Business Capability Map (BCM)
en les formalisant via des ADR (Architecture Decision Records) et en assurant la traçabilité ADR <-> Capability.

## Contenu
- bcm/capabilities.yaml : référentiel canonique des capacités
- adr/ : ADR de cadre (globales) + ADR de contenu (capabilities structurantes / controversées)
- tools/ : validation + génération de vues Mermaid
- views/ : vues générées (BCM, heatmap, traçabilité)

## Quickstart
1) Installer Python 3.11+ (ou 3.10+)
2) `pip install -r tools/requirements.txt`
3) Valider:
   - `python tools/validate_repo.py`
4) Générer les vues:
   - `python tools/generate_views.py`
5) Ouvrir:
   - `views/bcm-l1l2.mmd`
   - `views/adr-traceability.md`

## Gouvernance (recommandée)
- Toute modification de `bcm/capabilities.yaml` et/ou d’ADR passe en PR.
- Les changements structurants (split/merge, règles de niveau, zoning) exigent un ADR.

## Définition rapide
- Capability = "ce que fait l'entreprise" (stable, indépendante du SI et de l'organisation).
- BCM = hiérarchie L1/L2/L3, souvent utilisée en urbanisation pour aligner SI, Data, organisation, investissements.
