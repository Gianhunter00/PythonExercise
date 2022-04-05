from math import pi
import pytest
from CircleExercise import Circle


@pytest.fixture
def circle():
    return Circle(radius=5)


def test_circle_init():
    circle = Circle(radius=5)
    assert circle.radius == 5
    assert circle.diameter == 10
    assert circle.area == pi*circle.radius ** 2
    circle_all = Circle.from_diameter(diameter=10)
    assert circle_all.radius == 5
    assert circle_all.diameter == 10
    assert circle_all.area == pi*circle_all.radius ** 2
    
def test_circle_str(circle):
    print(circle)
    assert str(circle) == "CIRCLE PRINT:\nradius: 5\ndiameter: 10\narea: 78.53981633974483\n"
    
def test_circle_add(circle):
    circle_one = circle
    circle_two = circle
    circle_add = circle_one + circle_two
    assert circle_add.radius == 10
    assert circle_add.diameter == 20
    assert circle_add.area == pi*circle_add.radius ** 2
    
def test_circle_eq(circle):
    circle_one = circle
    circle_two = circle
    assert circle_one == circle_two
    
def test_circle_gt(circle):
    circle_one = circle
    circle_two = Circle(radius=10)
    assert circle_two > circle_one
    
def test_circle_sort():
    circle_list = [Circle(radius=24), Circle(radius=15), Circle(radius=43), Circle(radius=27), Circle(radius=21), Circle(radius=30)]
    circle_list.sort()
    assert circle_list[0].radius == 15
    assert circle_list[1].radius == 21
    assert circle_list[2].radius == 24
    assert circle_list[3].radius == 27
    assert circle_list[4].radius == 30
    assert circle_list[5].radius == 43