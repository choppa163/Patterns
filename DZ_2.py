"""Выбрал паттерн Builder, потому что тут много компонентов, разные виды пасты, а также я использовал уже этот паттерн
в прошлом задании"""


class Pasta:
    def __init__(self):
        self._type = None
        self._sauce = None
        self._filling = None
        self._toppings = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def sauce(self):
        return self._sauce

    @sauce.setter
    def sauce(self, value):
        self._sauce = value

    @property
    def filling(self):
        return self._filling

    @filling.setter
    def filling(self, value):
        self._filling = value

    @property
    def toppings(self):
        return self._toppings.copy()

    def add_topping(self, topping):
        self._toppings.append(topping)

    def __str__(self):
        return f"Паста: {self._type}, Соус: {self._sauce}, Начинка: {self._filling}, Добавки: {self._toppings}"


class PastaBuilder:
    def __init__(self):
        self._pasta = Pasta()

    @property
    def pasta(self):
        return self._pasta

    @pasta.setter
    def pasta(self, value):
        self._pasta = value

    @property
    def type(self):
        return self._pasta.type

    @type.setter
    def type(self, value):
        self._pasta.type = value

    @property
    def sauce(self):
        return self._pasta.sauce

    @sauce.setter
    def sauce(self, value):
        self._pasta.sauce = value

    @property
    def filling(self):
        return self._pasta.filling

    @filling.setter
    def filling(self, value):
        self._pasta.filling = value

    def add_topping(self, topping):
        self._pasta.add_topping(topping)
        return self

    def build(self):
        return self._pasta


class PastaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_carbonara(self):
        self.builder.type = "Спагетти"
        self.builder.sauce = "Сливочный соус"
        self.builder.filling = "Бекон"
        self.builder.add_topping("Пармезан")
        self.builder.add_topping("Черный перец")
        return self.builder.build()

    def make_bolognese(self):
        self.builder.type = "Тальятелле"
        self.builder.sauce = "Томатный соус"
        self.builder.filling = "Мясной фарш"
        self.builder.add_topping("Базилик")
        return self.builder.build()

    def make_seafood(self):
        self.builder.type = "Лингуине"
        self.builder.sauce = "Чесночно-оливковый соус"
        self.builder.filling = "Креветки и мидии"
        self.builder.add_topping("Петрушка")
        self.builder.add_topping("Лимонный сок")
        return self.builder.build()


if __name__ == "__main__":
    builder = PastaBuilder()
    director = PastaDirector(builder)

    # карбонара
    carbonara = director.make_carbonara()
    print(carbonara)

    # болоньезе
    bolognese = director.make_bolognese()
    print(bolognese)

    # морепродукты
    seafood = director.make_seafood()
    print(seafood)
    print()

    # примеры
    print(f"Тип пасты (Карбонара): {carbonara.type}")
    print(f"Соус (Карбонара): {carbonara.sauce}")
    print(f"Начинка (Карбонара): {carbonara.filling}")
    print(f"Добавки (Карбонара): {carbonara.toppings}")












