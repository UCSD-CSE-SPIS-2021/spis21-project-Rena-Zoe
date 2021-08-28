import pygame

import os

def gary(screen_length,screen_height, dim_field, screen, gplayer_rect):
  
  background = pygame.image.load(os.path.join("gary","gary_background.png"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  header_rect = pygame.Rect(0, 0, 465, 30)
  # # #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (255, 174, 185), header_rect)

  pygame.font.init()

  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  points = font.render("Points:",True,(0,0,0))

  show_points = True
  
  start_time = pygame.time.get_ticks()

  if (show_points):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_points = False

  if (show_points):
    screen.blit(points,(5, 7))
 
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  gary_title = font.render("Gary (Medium)",True,(0,0,0))

  show_gary_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_gary_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
     show_gary_title = False

  if (show_gary_title):
    screen.blit(gary_title,(175, 7))

  font = pygame.font.Font("./Bungee-Regular.ttf",15)
  
  point_num = "0"

  point_num_txt = font.render(point_num,True,(0,0,0))

  show_point_num_txt = True
  
  start_time = pygame.time.get_ticks()

  if (show_point_num_txt):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_point_num_txt = False

  if (show_point_num_txt):
    screen.blit(point_num_txt,(80, 7))

  font = pygame.font.Font("./Bungee-Regular.ttf",15)
  
  lives_num = "3"

  lives_num_txt = font.render(lives_num,True,(0,0,0))

  show_lives_num_txt = True
  
  start_time = pygame.time.get_ticks()

  if (show_lives_num_txt):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
     show_lives_num_txt = False

  if (show_lives_num_txt):
    screen.blit(lives_num_txt,(445, 7))

  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  lives = font.render("Lives:",True,(0,0,0))

  show_lives = True
  
  start_time = pygame.time.get_ticks()

  if (show_lives):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
     show_lives = False

  if (show_lives):
    screen.blit(lives,(385, 7))
  



def g_walls(screen_length,screen_height, dim_field, screen, gplayer_rect):
  
  #letter u
  
  u_rect1 = pygame.Rect(40, 130, 15, 80)
  pygame.draw.rect(screen, (205, 129, 98), u_rect1)
  u_rect2 = pygame.Rect(45, 215, 65, 15)
  pygame.draw.rect(screen, (205, 129, 98), u_rect2)
  u_rect3 = pygame.Rect(105, 130, 15, 80)
  pygame.draw.rect(screen, (205, 129, 98), u_rect3)
  
  #letter c
  c_rect1 = pygame.Rect(155, 130, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), c_rect1)
  c_rect2 = pygame.Rect(155, 150, 15, 60)
  pygame.draw.rect(screen, (205, 129, 98), c_rect2)
  c_rect3 = pygame.Rect(155, 215, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), c_rect3)
  c_rect4 = pygame.Rect(205, 130, 15, 25)
  pygame.draw.rect(screen, (205, 129, 98), c_rect4)
  c_rect5 = pygame.Rect(205, 205, 15, 25)
  pygame.draw.rect(screen, (205, 129, 98), c_rect5)

  #letter s

  s_rect1 = pygame.Rect(275, 130, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect1)
  s_rect2 = pygame.Rect(255, 130, 15, 55)
  pygame.draw.rect(screen, (205, 129, 98), s_rect2)
  s_rect3 = pygame.Rect(275, 170, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect3)
  s_rect4 = pygame.Rect(305, 190, 15, 40)
  pygame.draw.rect(screen, (205, 129, 98), s_rect4)
  s_rect5 = pygame.Rect(255, 215, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect5)

  #letter d
  d_rect1 = pygame.Rect(355, 170, 15, 60)
  pygame.draw.rect(screen, (200, 129, 98), d_rect1)
  d_rect2 = pygame.Rect(375, 170, 30, 15)
  pygame.draw.rect(screen, (205, 129, 98), d_rect2)
  d_rect3 = pygame.Rect(375, 215, 30, 15)
  pygame.draw.rect(screen, (205, 129, 98), d_rect3)
  d_rect4 = pygame.Rect(410, 130, 15, 100)
  pygame.draw.rect(screen, (205, 129, 98), d_rect4)

  #Top left
  wall1 = pygame.Rect(0, 70, 100, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall1)
  #Top middle
  wall2 = pygame.Rect(232, 30, 15, 65)
  pygame.draw.rect(screen, (205, 129, 98), wall2)
  #Top right
  wall3 = pygame.Rect(365, 70, 100, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall3)
  #middle left
  wall4 = pygame.Rect(0, 175, 35, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall4)
  #middle right
  wall5 = pygame.Rect(430, 175, 35, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall5)
  #bottom left
  wall6 = pygame.Rect(0, 280, 100, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall6)
  #bottom middle
  wall7 = pygame.Rect(232, 280, 15, 100)
  pygame.draw.rect(screen, (205, 129, 98), wall7)
  #bottom right
  wall8 = pygame.Rect(365, 280, 100, 15)
  pygame.draw.rect(screen, (205, 129, 98), wall8)

  wall_list = [u_rect1, u_rect2, u_rect3, c_rect1, c_rect2, c_rect3, c_rect4, c_rect5, s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, d_rect1, d_rect2, d_rect3, d_rect4, wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]

  return wall_list