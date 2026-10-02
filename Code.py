import random
import turtle

win = turtle.Screen()
win.title("Maze Runner")
win.bgcolor("black")
win.setup(width=700, height=700)
win.tracer(0)




GRID_SIZE = 24
walls = set()
treasures = []
enemies = []
game_over = False
score = 0



MAP = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP   XXXXXX         XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X  E    XX  XXX        XX",
    "XXXXXX  XX  XXX  E     XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "XT XXX   E    XXXX TXXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X       XXXXXXXXXXXXXXXXX",
    "X              XXXXXXXXXX",
    "XXXXXXXXXXXX  XXXXX T   X",
    "XXXXXXXXXXXX  XXXXX     X",
    "XXX  XXXXXXXX       E   X",
    "XXX                     X",
    "XXX   E      XXXXXXXXXXXX",
    "XXXXXTXXXX   XXXXXXXXXXXX",
    "XXXX  XXXX              X",
    "XX    XXXXX       E     X",
    "XX    XXXXXXXXXXXX   XXXX",
    "XX E  XXXXXXXXXXXX   XXXX",
    "XX    XXXXXXXXXXXX   XXXX",
    "XX  T XXXXXXXXXXXXT  XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]



class Sprite(turtle.Turtle):

    def __init__(self, shape, color, x, y):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.speed(0)
        self.goto(x, y)




class Enemy(Sprite):

    def __init__(self, x, y):
        super().__init__("triangle", "red", x, y)
        self.vx, self.vy = self.random_direction()
        self.move()

    def random_direction(self):
        moves = [(0, GRID_SIZE), (0, -GRID_SIZE), (-GRID_SIZE, 0), (GRID_SIZE, 0)]
        return random.choice(moves)

    def move(self):
        if game_over:
            return

        nx = self.xcor() + self.vx
        ny = self.ycor() + self.vy

        if (nx, ny) not in walls:
            self.goto(nx, ny)
        else:
            self.vx, self.vy = self.random_direction()

      
        win.ontimer(self.move, random.randint(150, 300))



def move_player(dx, dy):
    if game_over:
        return
    nx = player.xcor() + dx
    ny = player.ycor() + dy
    if (nx, ny) not in walls:
        player.goto(nx, ny)


drawer = turtle.Turtle()
drawer.shape("square")
drawer.color("white")
drawer.penup()
drawer.speed(0)
drawer.hideturtle()


player = None



for r, row in enumerate(MAP):
    for c, char in enumerate(row):
        x = -288 + (c * GRID_SIZE)
        y = 288 - (r * GRID_SIZE)

        if char == "X":
            drawer.goto(x, y)
            drawer.stamp()
            walls.add((x, y))
        elif char == "P":
            player = Sprite("square", "blue", x, y)
        elif char == "T":
            treasures.append(Sprite("circle", "gold", x, y))
        elif char == "E":
            enemies.append(Enemy(x, y))





win.listen()
win.onkeypress(lambda: move_player(0, GRID_SIZE), "Up")
win.onkeypress(lambda: move_player(0, -GRID_SIZE), "Down")
win.onkeypress(lambda: move_player(-GRID_SIZE, 0), "Left")
win.onkeypress(lambda: move_player(GRID_SIZE, 0), "Right")






def main_loop():
    global score, game_over

    if game_over:
        return

    
    for t in treasures[:]:
        if player.distance(t) < 12:
            score += 100
            print(f"Score: {score}")
            t.hideturtle()
            t.goto(1000, 1000)
            treasures.remove(t)



 
    for e in enemies:
        if player.distance(e) < 12:
            print("Game Over!")
            game_over = True
            break

    win.update()
    if not game_over:
        win.ontimer(main_loop, 16)



main_loop()
turtle.mainloop()
