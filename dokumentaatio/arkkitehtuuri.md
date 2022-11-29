# Arkkitehtuurikuvaus
## Rakenne
```mermaid
classDiagram
    UI <|-- ui
    services <|-- mastermind
    repositories <|-- player_repository

```
Pakkauksessa ui on käyttöliittymästä vastaava koodi, pakkauksessa services sovelluslogiikasta ja pakkauksessa repositories tietojen pysyväistallennuksesta vastaava koodi. 