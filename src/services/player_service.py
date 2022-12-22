from repositories.player_repository import (player_repository as default_player_repository)


class NameExistsError(Exception):
    pass

class PlayerService:
    """Talletetuista pelaajatiedoista vastaava luokka."""

    def __init__(self, player_repository=default_player_repository):
        """Luokan konstruktori. Luo uuden pelaajatiedoista vastaavan palvelun.
        Args:
            player_repository:
                Vapaaehtoinen, oletusarvoltaan PlayerRepository-olio, jolla
                on PlayerRepository-luokkaa vastaavat metodit.
        """
        self._player_repository = player_repository

    def create_player(self, name, turns):
        """Luo uuden palaajatietueen.
        Args:
            name: Pelaajan nimimerkkiä kuvaava merkkijono
            turns: Pelaajan käyttämät peliuorot.
        Raises:
            NameExistsError: Virhe,joka tapahtuu, kun nimimerkki on jo käytössä.
        """

        existing_name = self._player_repository.find_by_name(name)
        if existing_name:
            raise NameExistsError
        self._player_repository.create_player(name, turns)

    def top_players(self):
        """Hakee viisi parasta pelaajaa.
        Returns:
            Lista parhaiden pelaajien nimistä merkkijonona.
        """
        return self._player_repository.find_best()

    def find_all(self):
        """Hakee kaikki pelaajat.
        Returns:
            Lista pelaajien nimistä merkkijonona.
        """
        return self._player_repository.find_all()

    def find_by_name(self, name):
        """Hakee pelaajan nimimerkin perusteella.
        Returns:
            Palauttaa nimimerkin merkkijonona, jos nimimerkki on tietokannassa.
            Muussa tapauksessa None.
        """
        return self._player_repository.find_by_name(name)



player_service = PlayerService()
