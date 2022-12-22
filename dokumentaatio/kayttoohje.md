# Käyttöohje
Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Konfigurointi
Tallennukseen käytettävien tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa .env-tiedostossa. Tiedostot luodaan automaattisesti data-hakemistoon, jos niitä ei vielä siellä ole. Tiedosto on seuraavassa muodossa:
```
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä asenna riippuvuudet komennolla:
```
poetry install
```
Sitten suorita alustustoimenpiteet komennolla:
```
poetry run invoke build
```
Nyt ohjelman voi käynnistää komennolla:
```
poetry run invoke start
```
Sovellus avautuu tervetulonäkymään, josta pelin voi aloittaa painamalla Aloita peli -painiketta.
Seuraavaksi siirrytään pelinäkymään, jossa pelaaja valitsee ruudun alaosassa olevia palloja klikkaamalla haluamansa värin, ja kyseisenvärinne pallo piirtyy pelilautanäkymään. Kun neljä väriä on klikattu, viereen ilmestyy palaute, jossa musta pallo kuvaa oikeaa väriä oikealla paikalla ja valkoinen oikeaa väriä väärällä paikalla. Sitten pelaajan seuraava vuoro alkaa ja se sujuu kuten edellinen. Peli jatkuu, kunnes pelaaja arvaa koodin oikein tai kun pelivuorot on käytetty loppuun. Lopuksi kysytään pelaajan nimimerkkiä, ja sitten näytetään top 5 -pelaajat.