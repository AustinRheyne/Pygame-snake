import pygame
from snake import Snake
from cherry import Cherry

pygame.init()
pygame.font.init()

pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((500,500))

player = Snake(screen)
powerUp = Cherry(screen)

pointFont = pygame.font.SysFont("Comic Sans MS", 30)

score = 0

def eventLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.dir = (0,-1)               
            if event.key == pygame.K_s:
                player.dir = (0,1)                
            if event.key == pygame.K_a:
                player.dir = (-1,0)       
            if event.key == pygame.K_d:
                player.dir = (1,0)
        


playGame = True
while playGame:
    pygame.time.Clock().tick(120)

    eventLoop()
    screen.fill((0,0,0))

    player.move_me()
    player.blit_me()
    player.move_body()

    if player.check_loss():
        pygame.quit()

    if powerUp.eat_me(player) == True:
        score += 1
    powerUp.blit_me()

    scoreText = pointFont.render(f'Score: {score}', False, (255,255,255))
    screen.blit(scoreText, (30, 15))

    pygame.display.flip()