import pygame

import os

#def loadassets():
 #background = pygame.image.load(os.path.join("curt","curt.background.png"))

#Curt
def curt(screen_length,screen_height, dim_field, screen, player_rect):

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
  
  #Movement
  if player_rect.left < 0:
    player_rect.left = 0
  if player_rect.right > screen_length:
   player_rect.right = screen_length
  if player_rect.bottom > 340:
    player_rect.bottom = 340
  if player_rect.top < 30:
    player_rect.top = 30

  #When coding collisions/masking
  #mask_player = pygame.mask.from_surface(player)
  #mask_wall = pygame.mask.from_surface(wall)

def walls(screen_length,screen_height, dim_field, screen, player_rect):
  #Walls:
  g_rect1 = pygame.Rect(40, 120, 45, 15)
  pygame.draw.rect(screen, (64, 224,208), g_rect1)
  g_rect2 = pygame.Rect(40, 120, 15, 45)
  pygame.draw.rect(screen, (64, 224,208), g_rect2)
  g_rect3 = pygame.Rect(40, 170, 45, 15)
  pygame.draw.rect(screen, (64, 224, 208), g_rect3)
  g_rect4 = pygame.Rect(90, 120, 15, 105)
  pygame.draw.rect(screen, (64, 224,208), g_rect4)
  g_rect5 = pygame.Rect(40, 230, 65, 15)
  pygame.draw.rect(screen, (64, 224,208), g_rect5)

  #Letter A

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

  #Letter M

  m_rect1 = pygame.Rect(230, 120, 15, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect1)
  m_rect2 = pygame.Rect(250, 120, 15, 15)
  pygame.draw.rect(screen, (64, 224,208), m_rect2)
  m_rect3 = pygame.Rect(272, 120, 10, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect3)
  m_rect4 = pygame.Rect(290, 120, 15, 15)
  pygame.draw.rect(screen, (64, 224,208), m_rect4)
  m_rect5 = pygame.Rect(310, 120, 15, 125)
  pygame.draw.rect(screen, (64, 224,208), m_rect5)

    #Letter E

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

    #Other rectangles
    #corner rectangle (top left)
  wall1 = pygame.Rect(0, 70, 50, 15)
  pygame.draw.rect(screen, (64, 224,208), wall1)
    #corner rectangle (top right)
  wall2 = pygame.Rect(415, 70, 50, 15)
  pygame.draw.rect(screen, (64, 224,208), wall2)
    #corner rectangle (bottom left)
  wall3 = pygame.Rect(0, 295, 50, 15)
  pygame.draw.rect(screen, (64, 224,208), wall3)
    #corner rectangle (bottom right)
  wall4 = pygame.Rect(415, 295, 50, 15)
  pygame.draw.rect(screen, (64, 224,208), wall4)
    #middle top rectangle
  wall5 = pygame.Rect(170, 70, 130, 15)
  pygame.draw.rect(screen, (64, 224,208), wall5)
    #middle bottom rectangle
  wall6 = pygame.Rect(170, 295, 130, 15)
  pygame.draw.rect(screen, (64, 224,208), wall6)
    #top, left of middle rectangle
  wall7 = pygame.Rect(100, 30, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), wall7)
    #top, right of middle rectangle
  wall8 = pygame.Rect(350, 30, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), wall8)
    #bottom, left of middle rectangle
  wall9 = pygame.Rect(100, 295, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), wall9)
    #bottom, right of middle rectangle
  wall10 = pygame.Rect(350, 295, 15, 55)
  pygame.draw.rect(screen, (64, 224,208), wall10)
    #middle of G
  wall11 = pygame.Rect(0, 170, 35, 10)
  pygame.draw.rect(screen, (64, 224,208), wall11)
    #middle of E
  wall12 = pygame.Rect(420, 170, 45, 10)
  pygame.draw.rect(screen, (64, 224,208), wall12)

  curt_walls = [g_rect1,g_rect2, g_rect3, g_rect4,g_rect5, a_rect1, a_rect2, a_rect3, a_rect4, a_rect5, a_rect6, m_rect1, m_rect2, m_rect3, m_rect4, m_rect5, e_rect1, e_rect2, e_rect3, e_rect4, e_rect5, e_rect6, wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall7, wall8, wall9,wall10, wall11, wall12]

  return curt_walls

#def curt_points(screen_length,screen_height, dim_field, screen, player_rect):
  #Make lots of starts and like 4 hats