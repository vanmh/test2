from car import Car


def test_car_speed():
    car = Car()
    assert 0 == car.speed

def test_car_speed2():
    car = Car()
    car.accelerate(5)
    car.accelerate(2)
    car.accelerate(8)
    assert 15 == car.speed

def test_car_speed3():
    car = Car()
    car.accelerate(45)
    assert 45 == car.speed
