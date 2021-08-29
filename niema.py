import pygame

import os

def niema(screen_length,screen_height, dim_field, screen, nplayer_rect, num_points):
  
  background = pygame.image.load(os.path.join("niema","niema_background.png"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  header_rect = pygame.Rect(0, 0, 465, 30)
  # #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (152,251,152), header_rect)

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

  niema_title = font.render("Niema (Easy)",True,(0,0,0))

  show_niema_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_niema_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_niema_title = False

  if (show_niema_title):
    screen.blit(niema_title,(175, 7))

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

  if nplayer_rect.left < 0:
    nplayer_rect.left = 0
  if nplayer_rect.right > screen_length:
   nplayer_rect.right = screen_length
  if nplayer_rect.bottom > 340:
    nplayer_rect.bottom = 340
  if nplayer_rect.top < 30:
    nplayer_rect.top = 30

def n50points(screen_length,screen_height, dim_field, screen, player_rect):
  boba_1 = pygame.Rect(85, 155, 15, 15)
  bobasprite = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
  bobasprite = pygame.transform.scale(bobasprite, (25, 25))
  screen.blit(bobasprite, boba_1)

  boba_2 = pygame.Rect(85, 200, 15, 15)
  boba2 = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
  boba2 = pygame.transform.scale(boba2, (25, 25))
  screen.blit(boba2, boba_2)

  boba_3 = pygame.Rect(350, 155, 15, 15)
  boba3 = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
  boba3 = pygame.transform.scale(boba3, (25, 25))
  screen.blit(boba3, boba_3)

  boba_4 = pygame.Rect(350, 200, 15, 15)
  boba4 = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
  boba4 = pygame.transform.scale(boba4, (25, 25))
  screen.blit(boba4, boba_4)
  
  boba_list = [boba_1, boba_2, boba_3, boba_4]

  return boba_list

def n10points(screen_length,screen_height, dim_field, screen, player_rect):
#Rings and boba = Total of 650 points
  ring_1 = pygame.Rect(15, 40, 15, 15)
  ringsprite = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ringsprite = pygame.transform.scale(ringsprite, (15, 15))
  screen.blit(ringsprite, ring_1)

  ring_2 = pygame.Rect(75, 40, 15, 15)

  ring_3 = pygame.Rect(135, 40, 15, 15)

  ring_4 = pygame.Rect(195, 40, 15, 15)

  ring_5 = pygame.Rect(15, 100, 15, 15)

  ring_6 = pygame.Rect(15, 160, 15, 15)

  ring_7 = pygame.Rect(15, 220, 15, 15)

  ring_8 = pygame.Rect(15, 280, 15, 15)

  ring_9 = pygame.Rect(15, 330, 15, 15)

  ring_10 = pygame.Rect(75, 100, 15, 15)

  ring_44 = pygame.Rect(60, 205, 15, 15)

  ring_45 = pygame.Rect(380, 160, 15, 15)

  ring_13 = pygame.Rect(75, 260, 15, 15)

  ring_14 = pygame.Rect(75, 330, 15, 15)

  ring_15 = pygame.Rect(135, 100, 15, 15)

  ring_16 = pygame.Rect(135, 160, 15, 15)

  ring_17 = pygame.Rect(135, 210, 15, 15)

  ring_18 = pygame.Rect(135, 260, 15, 15)

  ring_19 = pygame.Rect(135, 330, 15, 15)

  ring_20 = pygame.Rect(195, 100, 15, 15)

  ring_22 = pygame.Rect(195, 220, 15, 15)

  ring_23 = pygame.Rect(195, 280, 15, 15)

  ring_24 = pygame.Rect(195, 330, 15, 15)

  ring_21 = pygame.Rect(250, 160, 15, 15)

  ring_25 = pygame.Rect(250, 220, 15, 15)

  ring_26 = pygame.Rect(250, 280, 15, 15)

  ring_27 = pygame.Rect(250, 330, 15, 15)

#These are right of top right pillar
  ring_11 = pygame.Rect(250, 40, 15, 15)

  ring_12 = pygame.Rect(250, 100, 15, 15)

  ring_28 = pygame.Rect(310, 40, 15, 15)

  ring_29 = pygame.Rect(310, 100, 15, 15)

  ring_30 = pygame.Rect(310, 160, 15, 15)

  ring_31 = pygame.Rect(310, 210, 15, 15)

  ring_32 = pygame.Rect(310, 260, 15, 15)

  ring_33 = pygame.Rect(310, 330, 15, 15)

  ring_34 = pygame.Rect(370, 100, 15, 15)

  ring_35 = pygame.Rect(370, 260, 15, 15)

  ring_36 = pygame.Rect(370, 330, 15, 15)

  ring_37 = pygame.Rect(370, 40, 15, 15)

  ring_38 = pygame.Rect(430, 40, 15, 15)

  ring_39 = pygame.Rect(430, 100, 15, 15)

  ring_40 = pygame.Rect(430, 160, 15, 15)

  ring_41 = pygame.Rect(430, 220, 15, 15)


  ring_42 = pygame.Rect(430, 280, 15, 15)


  ring_43 = pygame.Rect(430, 330, 15, 15)

  ring_list = [ring_1, ring_2, ring_3, ring_4, ring_5, ring_6, ring_7, ring_8, ring_9, ring_10, ring_11, ring_12, ring_13, ring_14, ring_15, ring_16, ring_17, ring_18, ring_19, ring_20, ring_21, ring_22, ring_23, ring_24, ring_25, ring_26, ring_27, ring_28, ring_29, ring_30, ring_31, ring_32, ring_33, ring_34, ring_35, ring_36, ring_37, ring_38, ring_39, ring_40, ring_41, ring_42, ring_43, ring_44, ring_45]

  return ring_list
  
def n_walls(screen_length,screen_height, dim_field, screen, nplayer_rect):
  
  #letter s
  s_rect1 = pygame.Rect(80, 140, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect1)
  s_rect2 = pygame.Rect(60, 140, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), s_rect2)
  s_rect3 = pygame.Rect(80, 180, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect3)
  s_rect4 = pygame.Rect(110, 200, 15, 45)
  pygame.draw.rect(screen, (0, 100, 0), s_rect4)
  s_rect5 = pygame.Rect(60, 230, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect5)

  #letter p
  p_rect1 = pygame.Rect(165, 140, 15, 105)
  pygame.draw.rect(screen, (0, 100, 0), p_rect1)
  p_rect2 = pygame.Rect(185, 140, 30, 15)
  pygame.draw.rect(screen, (0, 100, 0), p_rect2)
  p_rect3 = pygame.Rect(185, 180, 30, 15)
  pygame.draw.rect(screen, (0, 100, 0), p_rect3)
  p_rect4 = pygame.Rect(220, 140, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), p_rect4)

  #letter i
  i_rect1 = pygame.Rect(275, 170, 15, 75)
  pygame.draw.rect(screen, (0, 100, 0), i_rect1)
  i_rect2 = pygame.Rect(275, 140, 15, 15)
  pygame.draw.rect(screen, (0, 100, 0), i_rect2)

  #letter s
  s_rect6 = pygame.Rect(350, 140, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect6)
  s_rect7 = pygame.Rect(330, 140, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), s_rect7)
  s_rect8 = pygame.Rect(350, 180, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect8)
  s_rect9 = pygame.Rect(380, 200, 15, 45)
  pygame.draw.rect(screen, (0, 100, 0), s_rect9)
  s_rect10 = pygame.Rect(330, 230, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect10)


  #other walls
  #top left
  wall1 = pygame.Rect(45, 75, 130, 15)
  pygame.draw.rect(screen, (0, 100, 0), wall1)
  #top middle
  wall2 = pygame.Rect(225, 55, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), wall2)
  #top right
  wall3 = pygame.Rect(290, 75, 125, 15)
  pygame.draw.rect(screen, (0, 100, 0), wall3)
  #bottom left
  wall4 = pygame.Rect(45, 285, 130, 15)
  pygame.draw.rect(screen, (0, 100, 0), wall4)
  #bottom middle
  wall5 = pygame.Rect(225, 270, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), wall5)
  #bottom right
  wall6 = pygame.Rect(290, 285, 125, 15)
  pygame.draw.rect(screen, (0, 100, 0), wall6)


  wall_list = [s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, p_rect1, p_rect2, p_rect3, p_rect4, i_rect1, i_rect2, s_rect6, s_rect7, s_rect8, s_rect9, s_rect10, wall1, wall2, wall3, wall4, wall5, wall6] 

  return wall_list