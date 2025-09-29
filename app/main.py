from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        self.on_set_health(health)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def on_set_health(self, health: int) -> None:
        if self.hidden or self not in Animal.alive:
            return

        if health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, beast: Animal) -> None:
        if (isinstance(beast, Carnivore)
                or beast.hidden
                or beast not in Animal.alive):
            return

        beast.health -= 50
        if beast.health <= 0:
            Animal.alive.remove(beast)
