# Arkkitehtuurikuvaus
## Rakenne
Ohjelman rakenne noudattaa kolmitasoista arkkitehtuuria. Ohjelman pakkausrakenne on seuraavanlainen:
![arkkitehtuuri](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/kuvat/arkkitehtuurikaavio.png)

Pakkauksessa ui on käyttöliittymästä vastaava koodi, pakkauksessa services sovelluslogiikasta ja pakkauksessa repositories tietojen pysyväistalletuksesta vastaava koodi. 

## Käyttöliittymä
Käyttöliittymä sisältää kolme erilaista näkymää: alku-, loppu- ja varsinainen pelinäkymä. Ne on toteutettu omina luokkinaan. Näkymät näytetään UI-luokan avulla. Käyttöliittymää ei tässä vaiheessa ole täysin eristetty sovelluslogiikasta, mikä on selvästi puute. 

## Sovelluslogiikka
Sovelluslogiikasta vastaa luokka Mastermind, joka vastaa pelilogiikasta. Jonkin verran pelin kulkuun liittyvää toimintaa jäi kuitenkin myös käyttöliittymän koodiin, mutta jatkokehittelyssä nämä olisi tarkoitus eriyttää täysin toisistaan. Lisäksi services-luokassa on luokka PlayerService, joka vastaa tietokantaan talletettujen pelaajatietojen käsittelystä.

## Tietojen pysyväistallennus

Pakkauksessa repositories oleva PlayerRepository-luokka vastaa tietojen tallettamisesta. Luokka pyrkii noudattamaan Repository-suunnittelumallia eli on tarvittaessa korvattavissa muilla toteutuksilla. 

### Tiedostot
Sovellus tallettaa pelaajien tiedot tiedostoon, jonka nimi määritellään sovelluksen juuressa olevassa konfiguraatiotiedostossa .env. Tiedot talletetaan SQL-tietokannan tauluun players. Taulu alustetaan initialize_database.py-tiedostossa.

## Päätoiminnallisuudet
Seuraavassa kuvataan joitakin toiminnallisuuksia sekvenssikaavioina. 

### Pelaajan luominen pelaajalistalle
![kaavio](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/kuvat/arkkitehtuuri_create_player.png)
Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan ```PlayerService``` metodia, joka taas kutsuu tietokannasta vastaavaa ```PlayerRepository```-luokan oliota.

### Parhaiden pelaajien listaus
![kaavio](https://github.com/kanuuna1/ohte/blob/master/dokumentaatio/kuvat/arkkitehtuuri_top_players.png)
Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan ```PlayerService``` metodia, joka taas kutsuu tietokannasta vastaavaa ```PlayerRepository```-luokan oliota.

## Ohjelman rakenteeseen jääneet heikkoudet
### Käyttöliittymä
Jonkin verran sovelluslogiikasta vastaavaa koodia jäi käyttöliittymäluokkiin. Lisäksi käyttöliittymän metodeja voisi selkiyttää. 
### Tietojen tallennus
Tietokantaan talletettavista tietueista olisi pitänyt luoda oma luokkansa. Olisi siis voinut olla nykyisten pakkausten lisäksi esim. entities-pakkaus, jonne olisi luotu Player-luokka, ja Player-olioita olisi lisätty tietokantaan. 