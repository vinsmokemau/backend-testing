import random
class Pokemon:

    def __init__(self, name_pokemon, catch_rate):
        self.name_pokemon = name_pokemon
        if (catch_rate >= 100):
            self.catch_rate = 1
        else:
            self.catch_rate = (catch_rate / 100)

    def set_status(self, status):
        status = status.upper()
        if status in ['ASLEEP', 'FROZEN']:
            self.catch_rate += 0.25
        elif status in ['PARALYZED', 'BURNED', 'POISONED']:
            self.catch_rate += 0.10
        else:
            self.catch_rate += 0.00

    def catch_attempt(self, pokeball):

        if self.catch_rate==0:
            return False

        if pokeball == 'MASTER_BALL':
            return True
        elif pokeball == 'POKE_BALL':
            random_number = random.randint(25, 255)
            probabilidad = (25 / random_number) + self.catch_rate
            # print(probabilidad)
            #BOOLEAN BASED ON PROBABILITY
            return random.random() < probabilidad

        elif pokeball == 'GREAT_BALL':
            random_number = random.randint(25, 200)
            probabilidad = (25 / random_number) + self.catch_rate
            # print(probabilidad)
            return random.random() < probabilidad

        elif pokeball == 'ULTRA_BALL':
            random_number = random.randint(25, 150)
            probabilidad = (25 / random_number) + self.catch_rate
            # print(probabilidad)
            return random.random() < probabilidad

        else:
            return False

