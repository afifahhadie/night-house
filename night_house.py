import turtle
import random

window = turtle.Screen()
window.bgcolor("midnight blue")
window.title("My_Picture")

window_width=600
window_height=400
window.setup(width=window_width, height=window_height)

art=turtle.Turtle()
art.shape("arrow")
art.speed(2)

def add_stars(num_dots):
    for _ in range(num_dots):
        x=random.randint(-window_width//2,window_width//2)
        y=random.randint(-200//2,window_height//2)

        art.penup()
        art.goto(x, y)
        art.dot(5, "white")

def draw_filled_square(size):
    art.color("grey10")
    art.begin_fill()
    for _ in range(4):
        art.forward(size)
        art.right(90)
    art.end_fill()

def draw_filled_circle(radius):
    art.color("khaki")
    art.begin_fill()
    art.circle(radius)
    art.end_fill()

def draw_filled_triangle(size):
    art.color("black")
    art.begin_fill()
    for _ in range(3):
        art.forward(size)
        art.left(120)
    art.end_fill()

def draw_filled_rectangle(length, width):
    art.color("dark slate grey")
    art.begin_fill()
    for _ in range(2):
        art.forward(length)
        art.right(90)
        art.forward(width)
        art.right(90)
    art.end_fill()

def draw_window_for_house(size_w):
    art.color("gold")
    art.begin_fill()
    for _ in range(4):
        art.forward(size_w)
        art.right(90)
    art.end_fill()

square_size=100
circle_radius=50
triangle_size=120
rectangle_length=600
rectangle_width=100
size_w=30

num_random_dots=50
add_stars(num_random_dots)

art.penup()
art.goto(0,0)
art.pendown()
draw_filled_square(square_size)

art.penup()
art.goto(0,90)
art.pendown()
draw_filled_circle(circle_radius)

art.penup()
art.goto(-10,0)
art.pendown()
draw_filled_triangle(triangle_size)

art.penup()
art.goto(-300,-100)
art.pendown()
draw_filled_rectangle(rectangle_length, rectangle_width)

art.penup()
art.goto(10,-10)
art.pendown()
draw_window_for_house(size_w)

art.penup()
art.goto(60,-10)
art.pendown()
draw_window_for_house(size_w)

art.penup()
art.goto(10,-50)
art.pendown()
draw_window_for_house(size_w)

art.penup()
art.goto(60,-50)
art.pendown()
draw_window_for_house(size_w)

art.penup()
art.goto(70,-60)

window.exitonclick()