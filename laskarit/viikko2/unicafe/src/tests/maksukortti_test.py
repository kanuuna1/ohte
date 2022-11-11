import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_latauksen_jalkeen_saldo_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    
    def test_saldo_vahenee_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_saldo_ei_muutu_kun_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")  

    def test_otto_palauttaa_True_kun_rahaa_on(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)

    def test_otto_palauttaa_False_kun_rahaa_ei_ole(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
