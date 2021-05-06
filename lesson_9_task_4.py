class Car:
    speed = 60
    color = 'gray'
    name = 'Nissan'
    is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, command):
        print(f'машина поврнула {command}')

    def show_speed(self):
        print(f'текущая скорость = {self.speed}')


class TownCar(Car):
    name = 'Toyota'

    def show_speed(self, speed=60):
        self.speed = speed
        if speed <= 60:
            print(f'текущая скорость = {self.speed}')
        else:
            print('превышение скорости')


class SportCar(Car):
    name = 'BMW'
    color = 'red'


class WorkCar(Car):
    name = 'Renault'

    def show_speed(self, speed=40):
        self.speed = speed
        if speed <= 40:
            print(f'текущая скорость = {self.speed}')
        else:
            print('превышение скорости')


class PoliceCar(Car):
    is_police = True


print("Car")
some_car = Car()
print(some_car.name)
some_car.go()
some_car.turn('налево')
some_car.stop()
some_car.show_speed()
some_car.speed = 98
some_car.show_speed()
print()
print("TownCar")
city_car = TownCar()
print(city_car.name)
print(city_car.color)
city_car.go()
city_car.turn('направо')
city_car.show_speed(60)
city_car.show_speed(61)
print(city_car.is_police)
print()
print("WorkCar")
job_car = WorkCar()
print(job_car.name)
job_car.show_speed(50)
job_car.show_speed(40)
print()
print("SportCar")
sport = SportCar()
print(sport.color)
print(sport.name)
sport.go()
sport.show_speed()
sport.speed = 120
sport.show_speed()
print()
print("PoliceCar")
police = PoliceCar()
print(police.name)
print(police.color)
print(police.is_police)
