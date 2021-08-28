import pygame

import os

def niema(screen_length,screen_height, dim_field, screen):
  
  background = pygame.image.load(os.path.join("niema","niema_background.png"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  header_rect = pygame.Rect(0, 0, 465, 30)
  # #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (152,251,152), header_rect)

  # pygame.font.init()

  # font = pygame.font.Font("./Bungee-Regular.ttf",15)

  # points = font.render("Points:",True,(0,0,0))

  # show_points = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_points):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #     show_points = False

  # if (show_points):
  #   screen.blit(points,(5, 7))
 
  # font = pygame.font.Font("./Bungee-Regular.ttf",15)

  # curt_title = font.render("Curt (Hard)",True,(0,0,0))

  # show_curt_title = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_curt_title):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #     show_curt_title = False

  # if (show_curt_title):
  #   screen.blit(curt_title,(175, 7))

  # font = pygame.font.Font("./Bungee-Regular.ttf",15)
  
  # point_num = "0"

  # point_num_txt = font.render(point_num,True,(0,0,0))

  # show_point_num_txt = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_point_num_txt):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #     show_point_num_txt = False

  # if (show_point_num_txt):
  #   screen.blit(point_num_txt,(80, 7))

  # font = pygame.font.Font("./Bungee-Regular.ttf",15)
  
  # lives_num = "3"

  # lives_num_txt = font.render(lives_num,True,(0,0,0))

  # show_lives_num_txt = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_lives_num_txt):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #     show_lives_num_txt = False

  # if (show_lives_num_txt):
  #   screen.blit(lives_num_txt,(445, 7))

  # font = pygame.font.Font("./Bungee-Regular.ttf",15)

  # lives = font.render("Lives:",True,(0,0,0))

  # show_lives = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_lives):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #     show_lives = False

  # if (show_lives):
  #   screen.blit(lives,(385, 7))



def walls(screen_length,screen_height, dim_field, screen):
  
  #letter s
  s_rect1 = pygame.Rect(76, 120, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect1)
  s_rect2 = pygame.Rect(55, 120, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), s_rect2)
  s_rect3 = pygame.Rect(75, 160, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect3)
  s_rect4 = pygame.Rect(105, 180, 15, 45)
  pygame.draw.rect(screen, (0, 100, 0), s_rect4)
  s_rect5 = pygame.Rect(55, 210, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect5)

  #letter p
  p_rect1 = pygame.Rect(160, 120, 15, 105)
  pygame.draw.rect(screen, (0, 100, 0), p_rect1)
  p_rect2 = pygame.Rect(180, 120, 30, 15)
  pygame.draw.rect(screen, (0, 100, 0), p_rect2)
  p_rect3 = pygame.Rect(180, 160, 30, 15)
  pygame.draw.rect(screen, (0, 100, 0), p_rect3)
  p_rect4 = pygame.Rect(215, 120, 15, 55)
  pygame.draw.rect(screen, (0, 100, 0), p_rect4)

  #letter i
  i_rect1 = pygame.Rect(270, 150, 15, 75)
  pygame.draw.rect(screen, (0, 100, 0), i_rect1)
  i_rect2 = pygame.Rect(270, 120, 15, 15)
  pygame.draw.rect(screen, (0, 100, 0), i_rect2)

  #letter s
  s_rect1 = pygame.Rect(345, 120, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect1)
  s_rect2 = pygame.Rect(325, 120, 15, 55)#-20
  pygame.draw.rect(screen, (0, 100, 0), s_rect2)
  s_rect3 = pygame.Rect(345, 160, 45, 15)
  pygame.draw.rect(screen, (0, 100, 0), s_rect3)
  s_rect4 = pygame.Rect(375, 180, 15, 45)#+30
  pygame.draw.rect(screen, (0, 100, 0), s_rect4)
  s_rect5 = pygame.Rect(325, 210, 45, 15)#-20
  pygame.draw.rect(screen, (0, 100, 0), s_rect5)

  wall_list = [s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, p_rect1, p_rect2, p_rect3, p_rect4, i_rect1, i_rect2, s_rect1, s_rect2, s_rect3, s_rect4, s_rect5]

  return wall_list