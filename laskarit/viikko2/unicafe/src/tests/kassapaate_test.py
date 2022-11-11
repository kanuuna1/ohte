import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullisten_maara_alussa_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_maukkaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullisten_maara_kasvaa_kun_maksu_riittava(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullisen_vaihtoraha_oikein_kun_maksu_riittava(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihto, 10)
    
    def test_edullisten_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_edullisen_vaihtoraha_oikein_kun_maksu_ei_riittava(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihto, 200)

    def test_maukkaiden_maara_kasvaa_kun_maksu_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukkaan_vaihtoraha_oikein_kun_maksu_riittava(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihto, 10)
    
    def test_maukkaiden_maara_ei_kasva_kun_maksu_ei_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_maukkaan_vaihtoraha_oikein_kun_maksu_ei_riittava(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihto, 200)
    
    def test_edullisen_korttiosto_palauttaa_True_kun_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), True)

    def test_edullisen_korttiosto_palauttaa_False_kun_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaan_korttiosto_palauttaa_True_kun_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), True)
    
    def test_maukkaan_korttiosto_palauttaa_False_kun_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
    
    def test_edullisen_korttiosto_veloittaa_summan_kortilta_kun_raha_riittaa(self):
        kortti = Maksukortti(240)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
    
    def test_maukkaan_korttiosto_veloittaa_summan_kortilta_kun_raha_riittaa(self):
        kortti = Maksukortti(400)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
    
    def test_edullisen_korttiosto_kasvattaa_edullisten_maaraa_kun_raha_riittaa(self):
        kortti = Maksukortti(400)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullisen_korttiosto_ei_kasvata_edullisten_maaraa_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaan_korttiosto_kasvattaa_maukkaiden_maaraa_kun_raha_riittaa(self):
        kortti = Maksukortti(400)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukkaan_korttiosto_ei_kasvata_maukkaiden_maaraa_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_edullisen_korttiosto_ei_veloita_summaa_kortilta_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_maukkaan_korttiosto_ei_veloita_summaa_kortilta_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_kassan_rahamaara_ei_muutu_edullisen_korttiostossa(self):
        kortti = Maksukortti(400)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kassan_rahamaara_ei_muutu_maukkaan_korttiostossa(self):
        kortti = Maksukortti(400)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        kortti = Maksukortti(400)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")

    def test_rahaa_ladattaessa_kassan_saldo_muuttuu(self):
        kortti = Maksukortti(400)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)
    
    def test_rahaa_ladattaessa_kassan_saldo_ei_muutu_negatiivisella(self):
        kortti = Maksukortti(400)
        self.kassa.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahaa_ladattaessa_kortin_saldo_ei_muutu_negatiivisella(self):
        kortti = Maksukortti(400)
        self.kassa.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 4.00 euroa")