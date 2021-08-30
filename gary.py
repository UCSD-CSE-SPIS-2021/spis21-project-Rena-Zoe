import pygame

import os

def gary(screen_length,screen_height, dim_field, screen, gplayer_rect, num_points, num_lives):
  
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
  
  point_num = str(num_points)

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
  
  lives_num = str(num_lives)

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

  #Boundaries
  if gplayer_rect.left < 0:
    gplayer_rect.left = 0
  if gplayer_rect.right > screen_length:
   gplayer_rect.right = screen_length
  if gplayer_rect.bottom > 340:
    gplayer_rect.bottom = 340
  if gplayer_rect.top < 30:
    gplayer_rect.top = 30

def g50points(screen_length,screen_height, dim_field, screen, player_rect):
  wine_1 = pygame.Rect(72, 170, 10, 30)
  winesprite = pygame.image.load(os.path.join("gary", "wine1.png")).convert_alpha()
  winesprite = pygame.transform.scale(winesprite, (10, 30))
  screen.blit(winesprite, wine_1)

  wine_2 = pygame.Rect(130, 205, 10, 30)
  winesprite2 = pygame.image.load(os.path.join("gary", "wine2.png")).convert_alpha()
  winesprite2 = pygame.transform.scale(winesprite2, (10, 30))
  screen.blit(winesprite2, wine_2)

  wine_3 = pygame.Rect(330, 125, 10, 30)

  wine_4 = pygame.Rect(288, 185, 10, 30)

  wine_list = [wine_1, wine_2, wine_3, wine_4]

  return wine_list

def g10points(screen_length,screen_height, dim_field, screen, player_rect):
  cork_1 = pygame.Rect(50, 40, 15, 20)
  corksprite = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  corksprite = pygame.transform.scale(corksprite, (15, 20))
  screen.blit(corksprite, cork_1)

  cork_2 = pygame.Rect(85, 40, 15, 20)

  cork_3 = pygame.Rect(120, 40, 15, 20)
  
  cork_4 = pygame.Rect(155, 40, 15, 20)
  
  cork_5 = pygame.Rect(190, 40, 15, 20)
  
  cork_6 = pygame.Rect(190, 90, 15, 20)
  
  cork_7 = pygame.Rect(155, 90, 15, 20)
  
  cork_8 = pygame.Rect(120, 90, 15, 20)
  
  cork_9 = pygame.Rect(85, 90, 15, 20)
  
  cork_10 = pygame.Rect(50, 90, 15, 20)
  
  cork_11 = pygame.Rect(15, 90, 15, 20)
  
  cork_12 = pygame.Rect(15, 130, 15, 20)
  
  cork_13 = pygame.Rect(70, 130, 15, 20)
  
  cork_14 = pygame.Rect(130, 130, 15, 20)
  
  cork_15 = pygame.Rect(130, 170, 15, 20)
  
  cork_16 = pygame.Rect(230, 130, 15, 20)

  cork_17 = pygame.Rect(230, 170, 15, 20)

  cork_18 = pygame.Rect(230, 210, 15, 20)
  
  cork_19 = pygame.Rect(190, 170, 15, 20)
  
  cork_20 = pygame.Rect(330, 170, 15, 20)
  
  cork_21 = pygame.Rect(400, 40, 15, 20)
  # screen.blit(cork21, cork_21)cork_21 = pygame.Rect(400, 40, 15, 20)
  # cork21 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  # cork21 = pygame.transform.scale(cork21, (15, 20))

  cork_22 = pygame.Rect(365, 40, 15, 20)
  
  cork_23 = pygame.Rect(330, 40, 15, 20)
  
  cork_24 = pygame.Rect(295, 40, 15, 20)
  
  cork_25 = pygame.Rect(260, 40, 15, 20)
  
  cork_26 = pygame.Rect(260, 90, 15, 20)
  
  cork_27 = pygame.Rect(295, 90, 15, 20)
  
  cork_28 = pygame.Rect(330, 90, 15, 20)
  
  cork_29 = pygame.Rect(365, 90, 15, 20)
  
  cork_30 = pygame.Rect(400, 90, 15, 20)
  
  cork_31 = pygame.Rect(435, 90, 15, 20)
  
  cork_32 = pygame.Rect(365, 130, 15, 20)
  
  cork_33 = pygame.Rect(435, 130, 15, 20)
  
  cork_34 = pygame.Rect(15, 200, 15, 20)
  
  cork_35 = pygame.Rect(15, 250, 15, 20)
  
  cork_36 = pygame.Rect(50, 250, 15, 20)
  
  cork_37 = pygame.Rect(85, 250, 15, 20)
  
  cork_38 = pygame.Rect(120, 250, 15, 20)
  
  cork_39 = pygame.Rect(155, 250, 15, 20)
  
  cork_40 = pygame.Rect(190, 250, 15, 20)
  
  cork_41 = pygame.Rect(260, 250, 15, 20)
  
  cork_42 = pygame.Rect(295, 250, 15, 20)
  
  cork_43 = pygame.Rect(330, 250, 15, 20)
  
  cork_44 = pygame.Rect(365, 250, 15, 20)

  cork_45 = pygame.Rect(400, 250, 15, 20)

  cork_46 = pygame.Rect(435, 250, 15, 20)

  cork_47 = pygame.Rect(230, 250, 15, 20)

  cork_48 = pygame.Rect(435, 200, 15, 20)

  cork_49 = pygame.Rect(400, 305, 15, 20)

  cork_50 = pygame.Rect(365, 305, 15, 20)

  cork_51 = pygame.Rect(330, 305, 15, 20)
  
  cork_52 = pygame.Rect(295, 305, 15, 20)

  cork_53 = pygame.Rect(260, 305, 15, 20)

  cork_54 = pygame.Rect(190, 305, 15, 20)

  cork_55 = pygame.Rect(155, 305, 15, 20)

  cork_56 = pygame.Rect(120, 305, 15, 20)

  cork_57 = pygame.Rect(85, 305, 15, 20)

  cork_58 = pygame.Rect(50, 305, 15, 20)

  cork_59 = pygame.Rect(285, 148, 15, 20)

  cork_60 = pygame.Rect(330, 205, 15, 20)

  cork_list = [cork_1, cork_2, cork_3, cork_4, cork_5, cork_6, cork_7, cork_8, cork_9, cork_10, cork_11, cork_12, cork_13, cork_14, cork_15, cork_16, cork_17, cork_18, cork_19, cork_20, cork_21, cork_22, cork_23, cork_24, cork_25, cork_26, cork_27, cork_28, cork_29, cork_30, cork_31, cork_32, cork_33, cork_34, cork_35, cork_36, cork_37, cork_38, cork_39, cork_40, cork_41, cork_42, cork_43, cork_44, cork_45, cork_46, cork_47, cork_48, cork_49, cork_50, cork_51, cork_52, cork_53, cork_54, cork_55, cork_56, cork_57, cork_58, cork_59, cork_60]

  return cork_list

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