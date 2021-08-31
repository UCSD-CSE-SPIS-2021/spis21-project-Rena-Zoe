import pygame

import os

def secret(screen_length,screen_height, dim_field, screen, mplayer_rect):

  screen.fill((255,182,193))

  header_rect = pygame.Rect(0, 0, 470, 30)
  #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (238,162,173), header_rect)

  pygame.font.init()

  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  direct_title = font.render("Secret Mohan",True,(0,0,0))

  show_direct_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_direct_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_direct_title = False

  if (show_direct_title):
    screen.blit(direct_title,(180, 7))

  home_rect3 = pygame.Rect(420, 5, 40, 20)
  pygame.draw.rect(screen, (205,140,149), home_rect3)

  font = pygame.font.Font("./Staatliches-Regular.ttf",15)
  
  home = font.render("Home",True,(0,0,0))

  show_home = True
  
  start_time = pygame.time.get_ticks()

  if (show_home):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_home = False

  if (show_home):
    screen.blit(home,(426, 5))