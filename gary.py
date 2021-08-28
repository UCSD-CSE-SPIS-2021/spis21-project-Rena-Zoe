import pygame

import os

def gary(screen_length,screen_height, dim_field, screen):
  
  background = pygame.image.load(os.path.join("gary","gary_background.png"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  header_rect = pygame.Rect(0, 0, 465, 30)
  # # #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (255, 174, 185), header_rect)

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
  #    show_curt_title = False

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
  #    show_lives_num_txt = False

  # if (show_lives_num_txt):
  #   screen.blit(lives_num_txt,(445, 7))

  # font = pygame.font.Font("./Bungee-Regular.ttf",15)

  # lives = font.render("Lives:",True,(0,0,0))

  # show_lives = True
  
  # start_time = pygame.time.get_ticks()

  # if (show_lives):
    
  #   now_time = pygame.time.get_ticks()
  #   if (now_time - start_time > 500):
  #    show_lives = False

  # if (show_lives):
  #   screen.blit(lives,(385, 7))



def walls(screen_length,screen_height, dim_field, screen):
  
  #letter u
  
  u_rect1 = pygame.Rect(45, 120, 15, 80)
  pygame.draw.rect(screen, (205, 129, 98), u_rect1)
  u_rect2 = pygame.Rect(50, 205, 65, 15)
  pygame.draw.rect(screen, (205, 129, 98), u_rect2)
  u_rect3 = pygame.Rect(110, 120, 15, 80)
  pygame.draw.rect(screen, (205, 129, 98), u_rect3)
  
  #letter c
  c_rect1 = pygame.Rect(160, 120, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), c_rect1)
  c_rect2 = pygame.Rect(160, 140, 15, 60)
  pygame.draw.rect(screen, (205, 129, 98), c_rect2)
  c_rect3 = pygame.Rect(160, 205, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), c_rect3)
  c_rect4 = pygame.Rect(210, 120, 15, 25)
  pygame.draw.rect(screen, (205, 129, 98), c_rect4)
  c_rect5 = pygame.Rect(210, 195, 15, 25)
  pygame.draw.rect(screen, (205, 129, 98), c_rect5)

  #letter s

  s_rect1 = pygame.Rect(280, 120, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect1)
  s_rect2 = pygame.Rect(260, 120, 15, 55)
  pygame.draw.rect(screen, (205, 129, 98), s_rect2)
  s_rect3 = pygame.Rect(280, 160, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect3)
  s_rect4 = pygame.Rect(310, 180, 15, 45)
  pygame.draw.rect(screen, (205, 129, 98), s_rect4)
  s_rect5 = pygame.Rect(260, 210, 45, 15)
  pygame.draw.rect(screen, (205, 129, 98), s_rect5)

  #letter d
  d_rect1 = pygame.Rect(360, 160, 15, 65)
  pygame.draw.rect(screen, (205, 129, 98), d_rect1)
  d_rect2 = pygame.Rect(380, 160, 30, 15)
  pygame.draw.rect(screen, (205, 129, 98), d_rect2)
  d_rect3 = pygame.Rect(380, 210, 30, 15)
  pygame.draw.rect(screen, (205, 129, 98), d_rect3)
  d_rect4 = pygame.Rect(415, 120, 15, 105)
  pygame.draw.rect(screen, (205, 129, 98), d_rect4)

  wall_list = [u_rect1, u_rect2, u_rect3, c_rect1, c_rect2, c_rect3, c_rect4, c_rect5, s_rect1, s_rect2, s_rect3, s_rect4, s_rect5, d_rect1, d_rect2, d_rect3, d_rect4]

  return wall_list