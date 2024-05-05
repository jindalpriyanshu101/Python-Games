import pygame
import random

pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

height = 600
width = 800

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shik Shak Shook')

clock = pygame.time.Clock()

SnakeSize = 10
SnakeSpeed = 15

font_style = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(SnakeSize, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], SnakeSize, SnakeSize]) #sname_block = dimensions of snake

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - SnakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, height - SnakeSize) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! 'C' To Play Again or 'Q' To Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SnakeSize
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SnakeSize
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SnakeSize
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SnakeSize
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        pygame.draw.rect(dis, green, [foodx, foody, SnakeSize, SnakeSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SnakeSize, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - SnakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, height - SnakeSize) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SnakeSpeed) # movement speed

    pygame.quit()
    quit()

gameLoop()