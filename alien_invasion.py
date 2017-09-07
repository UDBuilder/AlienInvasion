# -*- coding: utf-8 -*-
import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 设置屏幕背景色
        screen.fill(ai_settings.bg_color)
        
        # 绘制屏幕
        pygame.display.flip()
        
run_game()
    