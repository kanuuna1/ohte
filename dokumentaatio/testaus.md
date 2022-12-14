# Testausdokumentti
Ohjelmaa on testattu niin automatisoiduin yksikkö- ja integraatiotestein unittestilla kuin manuaalisesti järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Sovelluslogiikasta vastaavaa ```Mastermind```-luokkaa testataan TestMastermind-testiluokalla. 
```PlayerService```-luokkaa testataan TestPlayerService-luokalla. ```PlayerService```-olio alustetaan siten, että sille annetaan riippuvuuksiksi repositorio-olio, joka tallentaa tietoa muistiin pysyväistalletuksen asemesta. Tätä varten testiin on luotu luokka ```FakePlayerRepository```.

### Repositorio-luokat
Reposiotorio-luokkaa ```PlayerRepository``` testataan vain testeissä käytössä olevilla tiedostoilla. Tiedostojen nimet on konfiguroitu .env.test-tiedostoon. ```PlayerRepository```-luokkaa testataan TestPlayerRepository-testiluokalla.

### Testauskattavuus
Käyttöliittymää lukuunottamttta testauksen haarautumakattavuus on 94 %:
![testikattavuusraportti](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/kuvat/coverage.png)
Myös tiedostot build.py- ja initialize_database.py jätettiin testikattavuuden ulkopuolelle.

## Järjestelmätestaus
Sovellusta on testattu vain Linux-ympäristössä.

### Toiminnallisuudet

Määrittelydokumentissa luetellut toiminnallisuudet on käyty läpi. Kaikkien toiminnallisuuksien yhteydessä on syötekentät yritetty täyttää myös virheellisillä arvoilla kuten tyhjillä.

## Sovellukseen jääneet laatuongelmat
Sovelluksen loppunäkymä ei toimi kunnolla. 