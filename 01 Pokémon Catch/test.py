import unittest
from .pokemon import Pokemon


class PokemonTestCase(unittest.TestCase):
    def test_masterball(self):
        pikachu = Pokemon('pikachu', 35)
        self.assertEqual(pikachu.catch_attempt("MASTER_BALL"), True)


    def test_status_pokemon_value(self):
        pikachu = Pokemon('pikachu', 35)
        pikachu.set_status("FROZEN")
        self.assertEqual(pikachu.catch_rate,0.6)


    def test_status_pokemon(self):
        pikachu = Pokemon('pikachu', 35)
        pikachu.set_status("FROZEN")
        self.assertTrue(pikachu.catch_attempt("POKE_BALL"), True)

    def test_status_pokemon2 (self):
        pikachu = Pokemon('pikachu', 35)
        pikachu.set_status("BURNED")
        self.assertTrue(pikachu.catch_attempt("ULTRA_BALL"), True)

    def test_statuspokemon3 (self):
        pikachu = Pokemon('pikachu', 100)
        pikachu.set_status("ASLEEP")
        self.assertTrue(pikachu.catch_attempt("ULTRA_BALL"), True)

    def test_catch_rate_100(self):
        pikachu = Pokemon('pikachu', 100)
        self.assertTrue(pikachu.catch_attempt("POKE_BALL"), True)


    def test_catch_rate_0(self):
        pikachu = Pokemon('pikachu', 0)
        self.assertFalse(pikachu.catch_attempt("POKE_BALL"), False)

    def test_catch_rate_1(self):
        pikachu = Pokemon('pikachu', 2)
        self.assertFalse(pikachu.catch_attempt("POKE_BALL"), False)


if __name__ == "__main__":
    unittest.main()

