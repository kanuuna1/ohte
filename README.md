# Ohjelmistotekniikan harjoitustyö
Tässä ohjelmistotekniikan harjoitustyössä on tarkoitus toteuttaa Mastermind-peli . 
## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuuri](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/changelog.md)
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
### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```