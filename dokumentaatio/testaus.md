# Testausdokumentti
Ohjelmaa on testattu niin automatisoiduin yksikkö- ja integraatiotestein unittestilla kuin manuaalisesti järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Sovelluslogiikasta vastaavaa ```Mastermind```-luokkaa testataan TestMastermind-testiluokalla.
### Repositorio-luokat
Reposiotorio-luokkaa ```PlayerRepository``` testataan ainoastaan testeissä käytössäolevilla tiedostoilla. Tiedostojen nimet on konfiguroitu .env.test-tiedostoon. ```PlayerRepository```-luokkaa testataan TestPlayerRepository-testiluokalla.
### Testauskattavuus
Käyttöliittymää lukuunottamttta testauksen haarautumakattavuus on 