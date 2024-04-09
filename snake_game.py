from tkinter import *
import random
import math


WIDTH, HEIGHT = 500, 500
SPEED = 10
LENGHT = 20

RIGHT = (SPEED, 0)
LEFT = (-SPEED, 0)
UP = (0, -SPEED)
DOWN = (0, SPEED)

FOOD_COLOR = '#DC143C'
SNAKE_COLOR = '#66CD00'


class Food:
    def __init__(self):
        self.x = random.randint(30, WIDTH - 30)
        self.y = random.randint(30, HEIGHT - 30)


class Snake:
    def __init__(self):
        self.snake_body = [(random.randint(30, WIDTH - 30),
                            random.randint(30, HEIGHT - 30))]
        self.direction = RIGHT
        self.is_growing = False

    def move(self):
        x_head, y_head = self.snake_body[0]
        x_head_new = x_head + self.direction[0]
        y_head_new = y_head + self.direction[1]
        self.snake_body.insert(0, (x_head_new, y_head_new))
        if not self.is_growing:
            self.snake_body.pop()
        self.is_growing = False

    def turn(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def is_collision(self):
        x_head, y_head = self.snake_body[0]
        return (
            x_head <= 0 or
            x_head >= WIDTH or
            y_head <= 0 or
            y_head >= HEIGHT or
            (x_head, y_head) in self.snake_body[1:]
        )


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.title("Snake Game")
        self.root.geometry("550x600")
        self.root.config(bg="gold")
        img = Image('photo', file='snake.png')
        self.root.call('wm', 'iconphoto', self.root._w, img)
        self.canvas = Canvas(self.root, width=WIDTH,
                             height=HEIGHT, background='black')
        self.canvas.pack(pady=20)
        self.score = 0
        self.score_label = Label(
            self.root, text=f"Score: {self.score}", fg='blue')
        self.score_label.pack()
        self.food = Food()
        self.snake = Snake()
        self.is_game_over = False
        self.root.bind("<Key>", self.on_key_press)

    def on_key_press(self, event):
        key = event.keysym
        if key == 'Right':
            self.snake.turn(RIGHT)
        elif key == 'Left':
            self.snake.turn(LEFT)
        elif key == 'Up':
            self.snake.turn(UP)
        elif key == 'Down':
            self.snake.turn(DOWN)

    def draw_object(self, x, y, color):
        self.canvas.create_rectangle(
            x, y, x+LENGHT, y+LENGHT, fill=color, outline=color)

    def draw_game(self):
        self.canvas.delete(ALL)
        self.draw_object(self.food.x, self.food.y, FOOD_COLOR)  # food
        for x, y in self.snake.snake_body:
            self.draw_object(x, y, SNAKE_COLOR)
        self.score_label.config(text=f"Score: {self.score}")

    def find_distance(self):
        # d=√((x2 – x1)² + (y2 – y1)²).
        p = self.snake.snake_body[0]
        q = self.food.x, self.food.y
        d = math.dist(p, q)
        return d - LENGHT

    def update(self):
        self.snake.move()
        if self.find_distance() <= 0:
            self.score += 1
            self.food = Food()
            self.snake.is_growing = True
        self.draw_game()
        if self.snake.is_collision():
            self.is_game_over = True

        if self.is_game_over:
            self.root.after(100, self.end_game)
        else:
            self.root.after(100, self.update)

    def end_game(self):
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2, fill='red', text="Game Over :(", font=('arial', 50))
        self.root.unbind("<Key>")


game = Game()
game.update()
game.root.mainloop()
