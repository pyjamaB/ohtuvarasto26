import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_suurempi_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(6)
        self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_string_esitys(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")

    def test_negatiivisen_saldon_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisen_saldon_poisto_ei_muuta_saldoa(self):
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarastoVirheellinenAlustus(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-1, -3)

    def test_negatiivinen_tilavuus_on_nolla(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_on_nolla(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarastoLiikaaSaldoa(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(2, 3)

    def test_saldo_ei_isompi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto.saldo, 2)

