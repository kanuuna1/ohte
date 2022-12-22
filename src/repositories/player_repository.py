from database_connection import get_database_connection


def get_player_by_row(row):
    return (row["name"]) if row else None


class PlayerRepository:
    """Pelaajien tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self._connection = connection

    def delete_all(self):
        """Poistaa kaikki pelaajat.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from players")
        self._connection.commit()

    def find_all(self):
        """Hakee kaikki pelaajat.
        Returns:
            Palauttaa listan pelaajien nimimerkkejä merkkijonoina.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from players")
        rows = cursor.fetchall()
        return list(map(get_player_by_row, rows))

    def find_best(self):
        """Palauttaa viisi parasta pelaajaa.
        Returns:
            Palauttaa listan nimiä merkkijonoina.
        """
        cursor = self._connection.cursor()
        cursor.execute("select name from players order by turns limit 5")
        rows = cursor.fetchall()
        return list(map(get_player_by_row, rows))

    def create_player(self, name, turns):
        """Tallentaa pelaajan tietokantaan.
        Args:
            name: Tallennettava pelaajan nimimerkki merkkijonona.
            turns: Pelaajan käyttämät pelikierrokset.
        """
        cursor = self._connection.cursor()
        cursor.execute("insert into players (name, turns) values (?,?)", (name, turns))
        self._connection.commit()

    def find_by_name(self, name):
        """Palauttaa pelaajan nimimerkin perusteella.
        Args:
            name: palautettava nimimerkki.
        Returns:
            Palauttaa nimimerkin merkkijonona, jos nimimerkki on tietokannassa.
            Muussa tapauksessa None.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select name from players where name = ?",
            (name,)
        )
        row = cursor.fetchone()
        return get_player_by_row(row)




player_repository = PlayerRepository(get_database_connection())
