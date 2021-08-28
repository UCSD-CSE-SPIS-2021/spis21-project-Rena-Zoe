import pygame

import os

def niema(screen_length,screen_height, dim_field, screen, nplayer_rect):
  
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

  ring_1 = pygame.Rect(15, 40, 15, 15)
  ring1 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring1 = pygame.transform.scale(ring1, (15, 15))
  screen.blit(ring1, ring_1)

  ring_2 = pygame.Rect(75, 40, 15, 15)
  ring2 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring2 = pygame.transform.scale(ring2, (15, 15))
  screen.blit(ring2, ring_2)

  ring_3 = pygame.Rect(135, 40, 15, 15)
  ring3 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring3 = pygame.transform.scale(ring3, (15, 15))
  screen.blit(ring3, ring_3)

  ring_4 = pygame.Rect(195, 40, 15, 15)
  ring4 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring4 = pygame.transform.scale(ring4, (15, 15))
  screen.blit(ring4, ring_4)

  ring_5 = pygame.Rect(15, 100, 15, 15)
  ring5 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring5 = pygame.transform.scale(ring5, (15, 15))
  screen.blit(ring5, ring_5)

  ring_6 = pygame.Rect(15, 160, 15, 15)
  ring6 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring6 = pygame.transform.scale(ring6, (15, 15))
  screen.blit(ring6, ring_6)

  ring_7 = pygame.Rect(15, 220, 15, 15)
  ring7 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring7 = pygame.transform.scale(ring7, (15, 15))
  screen.blit(ring7, ring_7)

  ring_8 = pygame.Rect(15, 280, 15, 15)
  ring8 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring8 = pygame.transform.scale(ring8, (15, 15))
  screen.blit(ring8, ring_8)

  ring_9 = pygame.Rect(15, 330, 15, 15)
  ring9 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring9 = pygame.transform.scale(ring9, (15, 15))
  screen.blit(ring9, ring_9)

  ring_10 = pygame.Rect(75, 100, 15, 15)
  ring10 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring10 = pygame.transform.scale(ring10, (15, 15))
  screen.blit(ring10, ring_10)

#Boba here

  boba_1 = pygame.Rect(85, 160, 15, 15)
  boba1 = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
  boba1 = pygame.transform.scale(boba1, (20, 20))
  screen.blit(boba1, boba_1)

  ring_12 = pygame.Rect(85, 210, 15, 15)
  ring12 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring12 = pygame.transform.scale(ring12, (15, 15))
  screen.blit(ring12, ring_12)

#Back to rings

  ring_13 = pygame.Rect(75, 260, 15, 15)
  ring13 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring13 = pygame.transform.scale(ring13, (15, 15))
  screen.blit(ring13, ring_13)

  ring_14 = pygame.Rect(75, 330, 15, 15)
  ring14 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring14 = pygame.transform.scale(ring14, (15, 15))
  screen.blit(ring14, ring_14)

  ring_15 = pygame.Rect(135, 100, 15, 15)
  ring15 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring15 = pygame.transform.scale(ring15, (15, 15))
  screen.blit(ring15, ring_15)

  ring_16 = pygame.Rect(135, 160, 15, 15)
  ring16 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring16 = pygame.transform.scale(ring16, (15, 15))
  screen.blit(ring16, ring_16)

  ring_17 = pygame.Rect(135, 210, 15, 15)
  ring17 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring17 = pygame.transform.scale(ring17, (15, 15))
  screen.blit(ring17, ring_17)

  ring_18 = pygame.Rect(135, 260, 15, 15)
  ring18 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring18 = pygame.transform.scale(ring18, (15, 15))
  screen.blit(ring18, ring_18)

  ring_19 = pygame.Rect(135, 330, 15, 15)
  ring19 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring19 = pygame.transform.scale(ring19, (15, 15))
  screen.blit(ring19, ring_19)

  ring_20 = pygame.Rect(195, 100, 15, 15)
  ring20 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring20 = pygame.transform.scale(ring20, (15, 15))
  screen.blit(ring20, ring_20)

  ring_22 = pygame.Rect(195, 220, 15, 15)
  ring22 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring22 = pygame.transform.scale(ring22, (15, 15))
  screen.blit(ring22, ring_22)

  ring_23 = pygame.Rect(195, 280, 15, 15)
  ring23 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring23 = pygame.transform.scale(ring23, (15, 15))
  screen.blit(ring23, ring_23)

  ring_24 = pygame.Rect(195, 330, 15, 15)
  ring24 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring24 = pygame.transform.scale(ring24, (15, 15))
  screen.blit(ring24, ring_24)

  ring_21 = pygame.Rect(250, 160, 15, 15)
  ring21 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring21 = pygame.transform.scale(ring21, (15, 15))
  screen.blit(ring21, ring_21)

  ring_25 = pygame.Rect(250, 220, 15, 15)
  ring25 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring25 = pygame.transform.scale(ring25, (15, 15))
  screen.blit(ring25, ring_25)

  ring_26 = pygame.Rect(250, 280, 15, 15)
  ring26 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring26 = pygame.transform.scale(ring26, (15, 15))
  screen.blit(ring26, ring_26)

  ring_27 = pygame.Rect(250, 330, 15, 15)
  ring27 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring27 = pygame.transform.scale(ring27, (15, 15))
  screen.blit(ring27, ring_27)

#These are right of top right pillar
  ring_11 = pygame.Rect(85, 160, 15, 15)
  ring11 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring11 = pygame.transform.scale(ring11, (15, 15))
  screen.blit(ring11, ring_11)

  ring_12 = pygame.Rect(85, 210, 15, 15)
  ring12 = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
  ring12 = pygame.transform.scale(ring12, (15, 15))
  screen.blit(ring12, ring_12)

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
  s_rect1 = pygame.Rect(350, 140, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect1)
  s_rect2 = pygame.Rect(330, 140, 15, 55)#-20
  pygame.draw.rect(screen, (0, 100, 0), s_rect2)
  s_rect3 = pygame.Rect(350, 180, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect3)
  s_rect4 = pygame.Rect(380, 200, 15, 45)#+30
  pygame.draw.rect(screen, (0, 100, 0), s_rect4)
  s_rect5 = pygame.Rect(330, 230, 45, 15)#-20
  pygame.draw.rect(screen, (0, 100, 0), s_rect5)

  wall_list = [s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, p_rect1, p_rect2, p_rect3, p_rect4, i_rect1, i_rect2, s_rect1, s_rect2, s_rect3, s_rect4, s_rect5]

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


  wall_list = [s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, p_rect1, p_rect2, p_rect3, p_rect4, i_rect1, i_rect2, s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, wall1, wall2, wall3, wall4, wall5, wall6] 

  return wall_list