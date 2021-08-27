import pygame

import os

#def loadassets():
 #background = pygame.image.load(os.path.join("curt","curt.background.png"))

#Curt
def curt(screen_length,screen_height, dim_field,screen, player_rect):

  background = pygame.image.load(os.path.join("curt","curt.background.png"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  header_rect = pygame.Rect(0, 0, 465, 30)
  #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (255,239,219), header_rect)

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

  curt_title = font.render("Curt (Hard)",True,(0,0,0))

  show_curt_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_curt_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_curt_title = False

  if (show_curt_title):
    screen.blit(curt_title,(175, 7))

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

  #Curt's Maze: game
  #Player

  player_x = 45
  player_y = 200
  player_width = 35
  player_height = 35
  #player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
  #pygame.draw.rect(screen, (0,0,0), player_rect)
  player = pygame.image.load(os.path.join("curt", "camel.png")).convert()
  player.set_colorkey((0, 0, 0))
  player = pygame.transform.scale(player, (player_width, player_height))
  screen.blit(player, player_rect)

  #Enemies
  #player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
  #pygame.draw.rect(screen, (0,0,0), player_rect)

  #When coding collisions/masking
  #mask_player = pygame.mask.from_surface(player)
  #mask_wall = pygame.mask.from_surface(wall)

  #Walls:
  g_rect1 = pygame.Rect(40, 120, 45, 15)
  pygame.draw.rect(screen, (64, 224,208), g_rect1)
  g_rect2 = pygame.Rect(40, 120, 15, 45)
  pygame.draw.rect(screen, (64, 224,208), g_rect2)
  g_rect3 = pygame.Rect(40, 170, 45, 15)
  pygame.draw.rect(screen, (64, 224, 208), g_rect3)
  g_rect4 = pygame.Rect(90, 120, 15, 115)
  pygame.draw.rect(screen, (64, 224,208), g_rect4)
  g_rect5 = pygame.Rect(40, 240, 65, 15)
  pygame.draw.rect(screen, (64, 224,208), g_rect5)

  g_walls = [g_rect1,g_rect2, g_rect3, g_rect4,g_rect5]

  a_rect1 = pygame.Rect(140, 120, 35, 15)
  pygame.draw.rect(screen, (64, 224, 208), a_rect1)
  a_rect2 = pygame.Rect(180, 120, 15, 55)
  pygame.draw.rect(screen, (64, 224, 208), a_rect2)
  a_rect3 = pygame.Rect(140, 180, 35, 15)
  pygame.draw.rect(screen, (64, 224,208), a_rect3)
  a_rect4 = pygame.Rect(180, 180, 15, 65)
  pygame.draw.rect(screen, (64, 224,208), a_rect4)
  a_rect5 = pygame.Rect(140, 230, 35, 15)
  pygame.draw.rect(screen, (64, 224,208), a_rect5)
  a_rect6 = pygame.Rect(140, 180, 15, 45)
  pygame.draw.rect(screen, (64, 224,208), a_rect6)

  a_walls = [a_rect1, a_rect2, a_rect3, a_rect4, a_rect5, a_rect6]

  m_rect1 = pygame.Rect(230, 120, 15, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect1)
  m_rect2 = pygame.Rect(250, 120, 15, 15)
  pygame.draw.rect(screen, (64, 224,208), m_rect2)
  m_rect3 = pygame.Rect(270, 120, 15, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect3)
  m_rect4 = pygame.Rect(290, 120, 15, 15)
  pygame.draw.rect(screen, (64, 224,208), m_rect4)
  m_rect5 = pygame.Rect(310, 120, 15, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect5)

  m_walls = [m_rect1, m_rect2, m_rect3, m_rect4, m_rect5]

  e_rect1 = pygame.Rect(360, 120, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), e_rect1)
  e_rect2 = pygame.Rect(380, 120, 20, 15)
  pygame.draw.rect(screen, (64, 224,208), e_rect2)
  e_rect3 = pygame.Rect(380, 160, 20, 15)
  pygame.draw.rect(screen, (64, 224,208), e_rect3)
  e_rect4 = pygame.Rect(400, 120, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), e_rect4)
  e_rect5 = pygame.Rect(360, 180, 15, 65)
  pygame.draw.rect(screen, (64, 224,208), e_rect5)
  e_rect6 = pygame.Rect(380, 230, 35, 15)
  pygame.draw.rect(screen, (64, 224,208), e_rect6)

  #e_walls = [e_rect1, e_rect2, e_rect3, e_rect4, e_rect5]

  #Don't want to leave the game area (Boundaries)
  if player_rect.left < 0:
    player_rect.left = 0
  if player_rect.right > screen_length:
   player_rect.right = screen_length
  if player_rect.bottom > 340:
    player_rect.bottom = 340
  if player_rect.top < 30:
    player_rect.top = 30

  #if player_rect.collidelist(g_walls):
    #print("collision!")