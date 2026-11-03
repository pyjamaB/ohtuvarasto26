"""Moduuli testeille"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testiluokka tiedostolle varasto.py"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa, luoko konstruktori tyhjän varaston"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa, onko varaston tilavuus oikein"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa, lisätäänkö saldo oikein"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa, pieneneekö varaston tila"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa, otetaanko oikea määrä"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa, lisääntyykö varaston tila"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_suurempi_kuin_on_tilaa(self):
        """Testaa, onko varaston saldo oikein, kun lisätään yli varaston tilan"""
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_liikaa(self):
        """Testaa, onko varaston saldo oikein, kun otetaan liikaa"""
        self.varasto.lisaa_varastoon(6)
        self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_string_esitys(self):
        """Testaa, onko str-esitys oikein"""
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")

    def test_negatiivisen_saldon_lisays_ei_muuta_saldoa(self):
        """Testaa, että negatiivisen saldon lisäys toimii oikein"""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisen_saldon_poisto_ei_muuta_saldoa(self):
        """Testaa, että negatiivisen saldon poisto toimii oikein"""
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarastoVirheellinenAlustus(unittest.TestCase):
    """Testiluokka tiedostolle varasto.py"""
    def setUp(self):
        self.varasto = Varasto(-1, -3)

    def test_negatiivinen_tilavuus_on_nolla(self):
        """Testaa, että negatiivisen tilan alustus on nolla"""
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_on_nolla(self):
        """Testaa, että negatiivisen saldon alustus on nolla"""
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarastoLiikaaSaldoa(unittest.TestCase):
    """Testiluokka tiedostolle varasto.py"""
    def setUp(self):
        self.varasto = Varasto(2, 3)

    def test_saldo_ei_isompi_kuin_tilavuus(self):
        """Testaa, ettei saldo ole isompi kuin tilavuus"""
        self.assertAlmostEqual(self.varasto.saldo, 2)
