import random

class Mastermind:
    """Luokka, joka vastaa pelilogiikasta.

    Attributes:
        size: ratkaistavan koodin pituus
        code: ratkaistava koodi
        guess: pelaajan arvaus
        turn: kuvaa, monesko pelivuoro käynnissä
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden peliolion.

        Args:
            size: ratkaistavan koodin pituus
            code: ratkaistava koodi
            guess: pelaajan arvaus
            turn: kuvaa, monesko pelivuoro käynnissä
        """
        self.size = 4
        self.code = []
        self.guess = []
        self.turn = 0
        self.create_code()

    def create_code(self):
        """
        Luo ratkaistavan nelinumeroisen koodin.

        Returns:
            Lista ratkaistavasta numerokoodista.
        """
    
        self.code = random.sample(range(0, 5), self.size)
        return self.code
    
    def compare(self, list1, list2):
        """
        Vertaa kahta listaa peli-idean mukaan.

        Returns:
            Lista, jossa "black" kuvaa oikealla paikalla olevaa oikeaa numeroa ja "white" väärässä paikassa olevaa oikeaa numeroa.
        """

        feedback = []
        list_1 = list1[:]
        list_2 = list2[:]
        for count1, value1 in enumerate(list_1):
            for count2, value2 in enumerate(list_2):
                if count1 == count2 and value1 == value2:
                    feedback.append("black")
                    list_1[count1] = None
                    list_2[count2] = None
                        
        for count1, value1 in enumerate(list_1):
            for count2, value2 in enumerate(list_2):
                if count1 != count2 and value1 == value2 and value1 is not None:
                    feedback.append("white")
                    list_1[count1] = None
                    value1 = None
                    list_2[count2] = None
                    value2 = None
                    continue
              
        return feedback


    def add_guess(self, num):
        """
        Lisää numeron pelaajan arvasta kuvaavaan listaan.

        """
        if num < 0 or num > 6:
            return
        self.guess.append(num)

  




    