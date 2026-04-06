class Animal:
    animals: list["Animal"] = []

    def __init__(
            self,
            name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals.append(self)

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(
            self
    ) -> None:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            if self.is_hungry:
                self.is_hungry = False
                return self.appetite
        return 0


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(
            self.name,
            appetite=3,
            is_hungry=is_hungry
        )

    def catch_mouse(self) -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(
            self.name,
            appetite=7,
            is_hungry=is_hungry
        )

    def bring_slippers(self) -> str:
        print("The slippers delivered!")


def feed_animals(animals: list) -> None:
    result = 0
    for animal in animals:
        if animal.is_hungry:
            result += animal.feed()
    return result
