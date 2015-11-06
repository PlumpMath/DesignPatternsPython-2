import abc


class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self):
        self.data = {}

    def set_part(self, key, value):
        self.data[key] = value


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


class Engine(metaclass=abc.ABCMeta):
    pass


class Wheel(metaclass=abc.ABCMeta):
    pass


class Door(metaclass=abc.ABCMeta):
    pass


class IBuilder(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def create_vehicle(self):
        pass

    @abc.abstractclassmethod
    def add_wheel(self):
        pass

    @abc.abstractclassmethod
    def add_engine(self):
        pass

    @abc.abstractclassmethod
    def add_doors(self):
        pass

    @abc.abstractclassmethod
    def get_vehicle(self) -> object:
        pass


class BikeBuilder(IBuilder):
    def __init__(self):
        self.bike = None

    def add_doors(self):
        pass

    def add_engine(self):
        self.bike.set_part('engine', Engine())

    def add_wheel(self):
        self.bike.set_part('forward_wheel', Wheel)
        self.bike.set_part('rear_wheel', Wheel)

    def get_vehicle(self):
        return self.bike

    def create_vehicle(self):
        self.bike = Bicycle()


class CarBuilder(IBuilder):
    def __init__(self):
        self.car = None

    def add_doors(self):
        self.car.set_part('door_right', Door())
        self.car.set_part('door_left', Door())
        pass

    def add_engine(self):
        self.car.set_part('engine', Engine())

    def add_wheel(self):
        self.car.set_part('wheel_RF', Wheel)
        self.car.set_part('wheel_LF', Wheel)
        self.car.set_part('wheel_RR', Wheel)
        self.car.set_part('wheel_LR', Wheel)

    def get_vehicle(self):
        return self.car

    def create_vehicle(self):
        self.car = Car()


class Director:
    @staticmethod
    def build(builder: IBuilder):
        builder.create_vehicle()
        builder.add_doors()
        builder.add_engine()
        builder.add_wheel()

        return builder.get_vehicle()


if __name__ == '__main__':
    director = Director()
    bicycle = director.build(BikeBuilder())
    car = director.build(CarBuilder())

    print(bicycle)
    print(car)
