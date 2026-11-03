"""Moduuli Varasto-luokalle"""

class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0
        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Funktio tarkastaa tilan määrän"""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Funktio lisää varastoon"""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Funktio ottaa varastosta"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
