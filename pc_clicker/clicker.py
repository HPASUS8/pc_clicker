import pygame
import random

def respawn():
    tr.x = random.randint(0, ww - tr.w)
    tr.y = random.randint(0, wh - tr.h)

pygame.init()
pygame.font.init()

pygame.display.set_caption('Кликер')

ww = 350 
wh = 600 
screen_s = (ww, wh)
screen_c = (ww // 2, wh // 2)
screen_t = (ww // 2, 0)

screen = pygame.display.set_mode(screen_s)

fps = 60
cl = pygame.time.Clock()

font = pygame.font.match_font('Comic Sans MS')
f64 = pygame.font.Font(font, 64)
f32 = pygame.font.Font(font, 32)
f20 = pygame.font.Font(font, 20)

init = 2000
finish = init
decrease = 1.002
lastrs = 0

go = False
btr = f20.render('Нажми на любую клавишу!', True, (255, 0, 0))
rr = btr.get_rect()
rr.midtop = screen_c

score = 0

img = pygame.image.load('pc.png')
img = pygame.transform.scale(img, (80, 120))
tr = img.get_rect()

respawn()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if go:
                score = 0
                finish = init
                go = False
                lastrs = pygame.time.get_ticks()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == pygame.BUTTON_LEFT:
                if not go and tr.collidepoint(e.pos):
                    score +=1
                    respawn()
                    lastrs = pygame.time.get_ticks()
                    finish = init / (decrease ** score)
   
    cl.tick(fps)

    screen.fill((255, 208, 202))
    scores = f64.render(str(score), True, (0, 0, 0))
    scorer = scores.get_rect()

    now = pygame.time.get_ticks()
    elap = now - lastrs
    if elap > finish:
        go = True

        scorer.midbottom = screen_c

        screen.blit(btr, rr)
    else:
        h = wh - wh * elap / finish
        timer = pygame.Rect((0 , 0), (ww, h))
        timer.bottomleft = (0, wh)
        pygame.draw.rect(screen, (232, 255, 208), timer)
        screen.blit(img, tr)

        scorer.midtop = screen_t
    screen.blit(scores, scorer)

    pygame.display.flip()
pygame.quit()
