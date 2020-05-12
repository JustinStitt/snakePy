import pygame#<-- used for rendering pipeline (drawing stuff on the screen)
import sys
import random
import time
pygame.init()

size = (500,500)
fillColor = pygame.Color(1,1,1)
snakeColor = pygame.Color(73,16,230)
foodColor = pygame.Color(225,70,50)

window = pygame.display.set_mode(size)
pygame.display.set_caption("SnakePy | Justin Stitt | Score: 0")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",30)

startup = True

class Snake():
    """Slither Slither Slither. I a snake dat what i Do boi"""
    def __init__(self):
        self.startup = True
        self.dir = 1    #0 = up, 1 = right, 2 = down, 3 = left
        self.score = 0
        if startup == True:
            self.pos = [100,100]
        else:
            self.pos = [-100,-100]
        self.speed = 20
        self.size = self.speed
        self.body = []
        self.length = 1
        self.last_pos = [0,0]
        self.gameOver = False

    def on_score(self):
        """Called when the Apple has to pick a new position (on eat)"""
        global startup
        self.score += 1
        pygame.display.set_caption("SnakePy | Justin Stitt | Score: " + str(self.score))
        if startup == False:
            self.add_body_part(1)
        startup = False
    def render(self):

        for x in range(len(self.body)):
            pygame.draw.rect(window,snakeColor,pygame.Rect(self.body[x].pos[0],self.body[x].pos[1],self.size,self.size))

    def move_body(self):
        """Every update, each snake body part is equal to the position of the index below it"""
        for x in range(len(self.body) - 1, 0, -1):# head is always the 0 slot of the body array

            self.body[x].pos[0] = self.body[x-1].last_pos[0]
            self.body[x].pos[1] = self.body[x-1].last_pos[1]

    def update(self):

        for snakes in self.body:
            snakes.last_pos = snakes.pos
        self.checkCollision()
        self.move_body()

        if self.dir == 0:
            self.body[0].pos[1] -= self.speed
        elif self.dir == 1:
            self.body[0].pos[0] += self.speed
        elif self.dir == 2:
            self.body[0].pos[1] += self.speed
        elif self.dir == 3:
            self.body[0].pos[0] -= self.speed

    def checkCollision(self):
        """Checks for various types of collisions that are possible for the snake and its body parts"""
        for x in range(len(self.body)):
            #check for wall collision
            if(  (self.body[x].pos[0] + self.size > size[0]) or (self.body[x].pos[0] < 0) ):
                self.gameOver = True
            elif((self.body[x].pos[1] < 0) or (self.body[x].pos[1] + self.size > size[1]) ):
                self.gameOver = True
            #check for apple collision
            if(self.body[x].pos[0] == apple.pos[0] and self.body[x].pos[1] == apple.pos[1]):
                apple.new_pos()
        for x in range(0,len(self.body) ):
            if x == 0:
                pass
            else:
                if self.body[0].pos == self.body[x].pos:
                    self.gameOver = True
    def add_body_part(self,times):
        for x in range(times):
            self.body.append(Snake())
            self.length += 1
class Apple():
    def __init__(self):
        self.pos = [0,0]
        self.shouldMove = False
        self.size = snake.size
    def new_pos(self):
        self.pos[0] = random.randint(1,(size[0] - 20)/self.size) * 20
        self.pos[1] = random.randint(1,(size[1] - 20)/self.size) * 20
        snake.on_score()
    def render(self):
        pygame.draw.rect(window,foodColor,pygame.Rect(self.pos[0],self.pos[1],self.size,self.size))
snake = Snake()
snake.add_body_part(1)

apple = Apple()
apple.new_pos()
def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dir = 0
            if event.key == pygame.K_RIGHT:
                snake.dir = 1
            if event.key == pygame.K_DOWN:
                snake.dir = 2
            if event.key == pygame.K_LEFT:
                snake.dir = 3

    snake.update()
    if snake.gameOver == True:
        print("Your score was: " + str(snake.score))
        pygame.quit()
        sys.exit()


def render():

    snake.render()
    apple.render()

while True:
    window.fill(fillColor)
    update()
    render()

    #keep last
    pygame.display.flip()
    clock.tick(14)
