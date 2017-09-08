# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height),0, 32)
    pygame.display.set_caption(ai_settings.screen_caption)
    
    play_button = Button(ai_settings, screen, "Play")
    
    ship = Ship(ai_settings, screen)
    
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    stats = GameStats(ai_settings)
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        # 设置屏幕背景色
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
            play_button)
        
        
run_game()
    
