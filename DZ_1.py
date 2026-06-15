# продукт
class RepairResult:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return "\n".join(self.parts)

# интерфейс строителя
class Builder:
    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_putty(self):
        pass

    def plaster_walls(self):
        pass

    def prime_wall(self):
        pass

    def paint_wall(self):
        pass

    def get_result(self):
        pass

# строители
class Tiler(Builder):
    def __init__(self):
        self.result = RepairResult()

    def prepare_floor(self):
        self.result.add("Подготовка пола выполнена")

    def lay_tiles(self):
        self.result.add("Укладка плитки выполнена")

    def get_result(self):
        return self.result

# отделочник
class Finisher(Builder):
    def __init__(self):
        self.result = RepairResult()

    def apply_putty(self):
        self.result.add("Шпаклевка нанесена")

    def plaster_walls(self):
        self.result.add("Стены оштукатурены")

    def get_result(self):
        return self.result

# маляр
class Painter(Builder):
    def __init__(self):
        self.result = RepairResult()

    def prime_wall(self):
        self.result.add("Стена загрунтована")

    def paint_wall(self):
        self.result.add("Стена покрашена")

    def get_result(self):
        return self.result

# директор
class Director:
    def __init__(self, builder):
        self.builder = builder

    def make_floors(self):
        self.builder.prepare_floor()
        self.builder.lay_tiles()

    def level_walls(self):
        self.builder.apply_putty()
        self.builder.plaster_walls()

    def paint_walls(self):
        self.builder.prime_wall()
        self.builder.paint_wall()

    def turnkey_works(self):
        self.builder.prepare_floor()
        self.builder.lay_tiles()
        self.builder.apply_putty()
        self.builder.plaster_walls()
        self.builder.prime_wall()
        self.builder.paint_wall()

# примеры
if __name__ == '__main__':
    print("Плиточник делает полы:")
    tiler = Tiler()
    director = Director(tiler)
    director.make_floors()
    print(tiler.get_result().list_parts())
    print()

    print("Отделочник выравнивает стены:")
    finisher = Finisher()
    director = Director(finisher)
    director.level_walls()
    print(finisher.get_result().list_parts())
    print()

    print("Маляр красит стены:")
    painter = Painter()
    director = Director(painter)
    director.paint_walls()
    print(painter.get_result().list_parts())


