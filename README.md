# Ohjelmistotekniikan harjoitustyö
Tässä ohjelmistotekniikan harjoitustyössä on tarkoitus toteuttaa [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game))-peli. Pelissä on tarkoitus arvata ohjelman arpoma nelivärinen kooodi. Ohjelma antaa palautetta arvauksista. Peli päättyy, kun pelaaja arvaa rivin oikein tai kun 10 vuoroa on käytetty. 
## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuuri](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/changelog.md)
- [Testausdokumentti](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/testaus.md)
- [Käyttöohje](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/kayttoohje.md)

## Asennus
1. Asenna riippuvuudet komennolla:
```
poetry install
```
2. Suorita alustustoimenpiteet komennolla:
```
poetry run invoke build
```
3. Käynnistä sovellus komennolla:
```
poetry run invoke start
```
## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```
poetry run invoke start
```
### Testaus
Testit suoritetaan komennolla:
```
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin voi generoida komennolla:
```
poetry run invoke coverage-report
```
Raportti muodostuu htmlcov-hakemistoon.
### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```