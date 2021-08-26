import pygame

import os

#Curt
def curt(screen_length,screen_height, dim_field,screen,event):
  
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

  g_rect1 = pygame.Rect(100, 150, 50, 10)
  pygame.draw.rect(screen, (64, 224,208), g_rect1)
  g_rect2 = pygame.Rect(100, 150, 10, 50)
  pygame.draw.rect(screen, (64, 224,208), g_rect2)
  g_rect3 = pygame.Rect(100, 200, 50, 10)
  pygame.draw.rect(screen, (64, 224,208), g_rect3)
  #g_rect4 = pygame.Rect(100, 170,10, 60)
  #pygame.draw.rect(screen, (64, 224,208), g_rect4)
  #g_rect5 = pygame.Rect(100, 200, 20, 30)
  #pygame.draw.rect(screen, (64, 224,208), g_rect5)
  #g_rect6 = pygame.Rect(80, 170, 10, 30)
  #pygame.draw.rect(screen, (64, 224,208), g_rect6)

  #a_rect = pygame.Rect(0, 0, 465, 30)
  #pygame.draw.rect(screen, (255,239,219), a_rect)

  #m_rect = pygame.Rect(0, 0, 465, 30)
  #pygame.draw.rect(screen, (255,239,219), m_rect)

  #e_rect = pygame.Rect(0, 0, 465, 30)
  #pygame.draw.rect(screen, (255,239,219), e_rect)

