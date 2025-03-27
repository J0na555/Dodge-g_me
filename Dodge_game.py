import pygame
import random

pygame.init()

screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dodge Game")
clock = pygame.time.Clock()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#blocks setup
object_width = 30
object_height = 30
fall_speed = 3
object_color = blue

#player setup
player_width = 60
player_height = 20
player_speed = 6
player_color = red
player = pygame.Rect((screen_width - player_width) // 2, screen_height - player_height - 10, player_width, player_height)

falling_objects = []

running = True
game_over = False

#game loop
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        #mov't
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  or keys[pygame.K_a] and player.left >= 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.right <= screen_width:
            player.x += player_speed

        # randomly spawning objects
        if random.randint(1, 30) == 1:
            x_pos = random.randint(0, screen_width)
            falling_objects.append(pygame.Rect(x_pos, 0, object_width, object_height))

        #falling objects
        for obj in falling_objects:
            obj.y += fall_speed
        
        #removing objects off screen 
        falling_objects = [obj for obj in falling_objects if obj.y <= screen_height]

        #speeding overtime
        fall_speed += 0.005

        #drawing object
        for obj in falling_objects:
            pygame.draw.rect(screen, object_color, obj)

        #drawing player
        pygame.draw.rect(screen, player_color, player)

        #collision detection
        for obj in falling_objects:
            if player.colliderect(obj):
                game_over = True
                break

    else:
        #gameover screen
        font = pygame.font.SysFont(None, 60)
        game_over_text = font.render("Game Over", True, red)
        screen.blit(game_over_text, ((screen_width - game_over_text.get_width()) // 2, screen_height // 2 - 30 ))

    pygame.display.update()
    clock.tick(60)    
pygame.quit()

       


