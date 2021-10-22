# 01 Pokémon catch test

Write a class named Pokemon that let's you define a name and a catch rate for a Pokémon.

The catch rate is a floating number between 0 and 1 that represents the base probability of a Pokémon to be caught when throwing a Poké Ball at it.

During battle, the Pokémon can be affected by an status condition that changes the probability for being caught.

The Pokemon class must define the following methods:

* `set_status()`: That let's you set an status condition on the Pokémon

* `catch_attempt()`: That returns a boolean telling whether the Pokémon is caught or not, depending on the type of Poké Ball used, the status condition the Pokémon has (if any), and the catch rate of the Pokémon, by applying the following rules:

    1. If a `MASTER_BALL` is used, the Pokémon is caught.

    2. Generate a random number, N, depending on the type of Poké Ball used:
        * For a `POKE_BALL`: 25 to 255
        * For a `GREAT_BALL`: 25 to 200
        * For an `ULTRA_BALL`: 25 to 150

    3. The Pokémon's catch rate is modified if:
        * It is in status `ASLEEP` or `FROZEN` by adding a 25%
        * It is in status `PARALYZED`, `BURNED` or `POISONED` by adding a 10%

    4. Calculate the modified catch rate by dividing 25 by N and adding the result to the Pokémon's base catch rate. Use the modified catch rate as the probability of the Pokémon to be caught.

Write your own unit tests in the provided TestCase for all the possible cases when trying to catch a Pokémon named "Pikachu" that has a catch rate of 35%.

You are only allowed to use `random` and no other library.

## Instructions

1. Fork this repository
2. Get a local copy of your fork
3. Create a new branch
4. Push your work to your fork
5. Send a pull request from your fork's branch to this repo
