from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa mahdolliset tietokantataulut.
    Args:
        connection: tietokantayhteyden Connection-olio
    """
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists players;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()
    cursor.execute('''
        create table players (
            name text primary key,
            turns int
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut."""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)



if __name__ == "__main__":
    initialize_database()
