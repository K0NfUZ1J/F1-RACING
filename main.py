from pygame import *
win = display.set_mode((700, 500))
display.set_caption("F1 RACING")
display.set_icon(image.load('pngwing1.com.png'))
background = transform.scale(image.load('фон.jpg'), (700, 500))

x3,y3= 130, 290
x2,y2 = 100, 300
x1, y1 = 150, 280
sprite1 = transform.scale(image.load('pngwing.com.png'), (100, 100))
sprite2 = transform.scale(image.load('pngwing.com (1).png'), (100, 100))
sprite3 = transform.scale(image.load('pngwing.com (2).png'), (100, 100))
speed = 5

run = True
clock = time.Clock()
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            print("Автор: Бондаренко Єгор")
            run = False
    win.blit(background, (0,0))
    win.blit(sprite1,(x1, y1))
    win.blit(sprite2, (x2, y2))
    win.blit(sprite3, (x3, y3))


    keys_pressed = key.get_pressed()

    if keys_pressed[K_w] and y1 > 0:
        y1 -= speed
    if keys_pressed[K_s] and y1 < 400:
        y1 += speed
    if keys_pressed[K_a] and x1 > 0:
        x1 -= speed
    if keys_pressed[K_d] and x1 < 600:
        x1 += speed

    if keys_pressed[K_UP] and y2 > 0:
        y2 -= speed
    if keys_pressed[K_DOWN] and y2 < 400:
        y2 += speed
    if keys_pressed[K_LEFT] and x2 > 0:
        x2 -= speed
    if keys_pressed[K_RIGHT] and x2 < 600:
        x2 += speed

    if keys_pressed[K_u] and y3 > 0:
        y3 -= speed
    if keys_pressed[K_j] and y3 < 400:
        y3 += speed
    if keys_pressed[K_h] and x3 > 0:
        x3 -= speed
    if keys_pressed[K_k] and x3 < 600:
        x3 += speed

    display.update()
    clock.tick(FPS)