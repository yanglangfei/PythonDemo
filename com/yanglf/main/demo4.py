import sys
import urllib3

import pygame

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
color = (0, 0, 0)
ball = pygame.image.load('../img/ball.jpg')
ballrect = ball.get_rect()
speed = [1, 1]
clock = pygame.time.Clock()  # 设置时钟

while True:  # 死循环确保窗口一直显示
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        ballrect = ballrect.move(speed)
        # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        screen.fill(color)
        screen.blit(ball, ballrect)
        pygame.display.flip()

pygame.quit()
