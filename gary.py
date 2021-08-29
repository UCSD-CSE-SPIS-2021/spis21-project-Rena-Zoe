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

  if gplayer_rect.left < 0:
    gplayer_rect.left = 0
  if gplayer_rect.right > screen_length:
   gplayer_rect.right = screen_length
  if gplayer_rect.bottom > 340:
    gplayer_rect.bottom = 340
  if gplayer_rect.top < 30:
    gplayer_rect.top = 30

def gpoints(screen_length,screen_height, dim_field, screen, player_rect):
  cork_1 = pygame.Rect(50, 40, 15, 20)
  cork1 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork1 = pygame.transform.scale(cork1, (15, 20))
  screen.blit(cork1, cork_1)

  cork_2 = pygame.Rect(85, 40, 15, 20)
  cork2 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork2 = pygame.transform.scale(cork2, (15, 20))
  screen.blit(cork2, cork_2)

  cork_3 = pygame.Rect(120, 40, 15, 20)
  cork3 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork3 = pygame.transform.scale(cork3, (15, 20))
  screen.blit(cork3, cork_3)

  cork_4 = pygame.Rect(155, 40, 15, 20)
  cork4 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork4 = pygame.transform.scale(cork4, (15, 20))
  screen.blit(cork4, cork_4)

  cork_5 = pygame.Rect(190, 40, 15, 20)
  cork5 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork5 = pygame.transform.scale(cork5, (15, 20))
  screen.blit(cork5, cork_5)

  cork_6 = pygame.Rect(190, 90, 15, 20)
  cork6 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork6 = pygame.transform.scale(cork6, (15, 20))
  screen.blit(cork6, cork_6)

  cork_7 = pygame.Rect(155, 90, 15, 20)
  cork7 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork7 = pygame.transform.scale(cork7, (15, 20))
  screen.blit(cork7, cork_7)

  cork_8 = pygame.Rect(120, 90, 15, 20)
  cork8 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork8 = pygame.transform.scale(cork8, (15, 20))
  screen.blit(cork8, cork_8)

  cork_9 = pygame.Rect(85, 90, 15, 20)
  cork9 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork9 = pygame.transform.scale(cork9, (15, 20))
  screen.blit(cork9, cork_9)

  cork_10 = pygame.Rect(50, 90, 15, 20)
  cork10 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork10 = pygame.transform.scale(cork10, (15, 20))
  screen.blit(cork10, cork_10)

  cork_11 = pygame.Rect(15, 90, 15, 20)
  cork11 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork11 = pygame.transform.scale(cork11, (15, 20))
  screen.blit(cork11, cork_11)

  cork_12 = pygame.Rect(15, 130, 15, 20)
  cork12 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork12 = pygame.transform.scale(cork12, (15, 20))
  screen.blit(cork12, cork_12)

  cork_13 = pygame.Rect(70, 130, 15, 20)
  cork13 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork13 = pygame.transform.scale(cork13, (15, 20))
  screen.blit(cork13, cork_13)

  cork_14 = pygame.Rect(130, 130, 15, 20)
  cork14 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork14 = pygame.transform.scale(cork14, (15, 20))
  screen.blit(cork14, cork_14)

  wine_1 = pygame.Rect(72, 170, 10, 30)
  wine1 = pygame.image.load(os.path.join("gary", "wine1.png")).convert_alpha()
  wine1 = pygame.transform.scale(wine1, (10, 30))
  screen.blit(wine1, wine_1)

  cork_15 = pygame.Rect(130, 170, 15, 20)
  cork15 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork15 = pygame.transform.scale(cork15, (15, 20))
  screen.blit(cork15, cork_15)

  wine_2 = pygame.Rect(130, 205, 10, 30)
  wine2 = pygame.image.load(os.path.join("gary", "wine2.png")).convert_alpha()
  wine2 = pygame.transform.scale(wine2, (10, 30))
  screen.blit(wine2, wine_2)

  cork_16 = pygame.Rect(230, 130, 15, 20)
  cork16 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork16 = pygame.transform.scale(cork16, (15, 20))
  screen.blit(cork16, cork_16)

  cork_17 = pygame.Rect(230, 170, 15, 20)
  cork17 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork17 = pygame.transform.scale(cork17, (15, 20))
  screen.blit(cork17, cork_17)

  cork_18 = pygame.Rect(230, 210, 15, 20)
  cork18 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork18 = pygame.transform.scale(cork18, (15, 20))
  screen.blit(cork18, cork_18)

  cork_19 = pygame.Rect(190, 170, 15, 20)
  cork19 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork19 = pygame.transform.scale(cork19, (15, 20))
  screen.blit(cork19, cork_19)

  wine_3 = pygame.Rect(330, 125, 10, 30)
  wine3 = pygame.image.load(os.path.join("gary", "wine2.png")).convert_alpha()
  wine3 = pygame.transform.scale(wine3, (10, 30))
  screen.blit(wine3, wine_3)

  cork_20 = pygame.Rect(330, 170, 15, 20)
  cork20 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork20 = pygame.transform.scale(cork20, (15, 20))
  screen.blit(cork20, cork_20)

  wine_4 = pygame.Rect(288, 185, 10, 30)
  wine4 = pygame.image.load(os.path.join("gary", "wine1.png")).convert_alpha()
  wine4 = pygame.transform.scale(wine4, (10, 30))
  screen.blit(wine4, wine_4)

  cork_21 = pygame.Rect(400, 40, 15, 20)
  cork21 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork21 = pygame.transform.scale(cork21, (15, 20))
  # screen.blit(cork21, cork_21)cork_21 = pygame.Rect(400, 40, 15, 20)
  # cork21 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  # cork21 = pygame.transform.scale(cork21, (15, 20))
  screen.blit(cork21, cork_21)

  cork_22 = pygame.Rect(365, 40, 15, 20)
  cork22 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork22 = pygame.transform.scale(cork22, (15, 20))
  screen.blit(cork22, cork_22)

  cork_23 = pygame.Rect(330, 40, 15, 20)
  cork23 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork23 = pygame.transform.scale(cork23, (15, 20))
  screen.blit(cork23, cork_23)

  cork_24 = pygame.Rect(295, 40, 15, 20)
  cork24 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork24 = pygame.transform.scale(cork24, (15, 20))
  screen.blit(cork24, cork_24)

  cork_25 = pygame.Rect(260, 40, 15, 20)
  cork25 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork25 = pygame.transform.scale(cork25, (15, 20))
  screen.blit(cork25, cork_25)

  cork_26 = pygame.Rect(260, 90, 15, 20)
  cork26 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork26 = pygame.transform.scale(cork26, (15, 20))
  screen.blit(cork26, cork_26)

  cork_27 = pygame.Rect(295, 90, 15, 20)
  cork27 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork27 = pygame.transform.scale(cork27, (15, 20))
  screen.blit(cork27, cork_27)

  cork_28 = pygame.Rect(330, 90, 15, 20)
  cork28 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork28 = pygame.transform.scale(cork28, (15, 20))
  screen.blit(cork28, cork_28)

  cork_29 = pygame.Rect(365, 90, 15, 20)
  cork29 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork29 = pygame.transform.scale(cork29, (15, 20))
  screen.blit(cork29, cork_29)

  cork_30 = pygame.Rect(400, 90, 15, 20)
  cork30 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork30 = pygame.transform.scale(cork30, (15, 20))
  screen.blit(cork30, cork_30)

  cork_31 = pygame.Rect(435, 90, 15, 20)
  cork31 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork31 = pygame.transform.scale(cork31, (15, 20))
  screen.blit(cork31, cork_31)

  cork_32 = pygame.Rect(365, 130, 15, 20)
  cork32 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork32 = pygame.transform.scale(cork32, (15, 20))
  screen.blit(cork32, cork_32)

  cork_33 = pygame.Rect(435, 130, 15, 20)
  cork33 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork33 = pygame.transform.scale(cork33, (15, 20))
  screen.blit(cork33, cork_33)

  cork_34 = pygame.Rect(15, 200, 15, 20)
  cork34 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork34 = pygame.transform.scale(cork34, (15, 20))
  screen.blit(cork34, cork_34)

  cork_35 = pygame.Rect(15, 250, 15, 20)
  cork35 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork35 = pygame.transform.scale(cork35, (15, 20))
  screen.blit(cork35, cork_35)
  
  cork_36 = pygame.Rect(50, 250, 15, 20)
  cork36 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork36 = pygame.transform.scale(cork36, (15, 20))
  screen.blit(cork36, cork_36)

  cork_37 = pygame.Rect(85, 250, 15, 20)
  cork37 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork37 = pygame.transform.scale(cork37, (15, 20))
  screen.blit(cork37, cork_37)

  cork_38 = pygame.Rect(120, 250, 15, 20)
  cork38 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork38 = pygame.transform.scale(cork38, (15, 20))
  screen.blit(cork38, cork_38)

  cork_39 = pygame.Rect(155, 250, 15, 20)
  cork39 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork39 = pygame.transform.scale(cork39, (15, 20))
  screen.blit(cork39, cork_39)

  cork_40 = pygame.Rect(190, 250, 15, 20)
  cork40 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork40 = pygame.transform.scale(cork40, (15, 20))
  screen.blit(cork40, cork_40)

  cork_41 = pygame.Rect(260, 250, 15, 20)
  cork41 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork41 = pygame.transform.scale(cork41, (15, 20))
  screen.blit(cork41, cork_41)

  cork_42 = pygame.Rect(295, 250, 15, 20)
  cork42 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork42 = pygame.transform.scale(cork42, (15, 20))
  screen.blit(cork42, cork_42)

  cork_43 = pygame.Rect(330, 250, 15, 20)
  cork43 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork43 = pygame.transform.scale(cork43, (15, 20))
  screen.blit(cork43, cork_43)

  cork_44 = pygame.Rect(365, 250, 15, 20)
  cork44 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork44 = pygame.transform.scale(cork44, (15, 20))
  screen.blit(cork44, cork_44)

  cork_45 = pygame.Rect(400, 250, 15, 20)
  cork45 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork45 = pygame.transform.scale(cork45, (15, 20))
  screen.blit(cork45, cork_45)

  cork_46 = pygame.Rect(435, 250, 15, 20)
  cork46 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork46 = pygame.transform.scale(cork46, (15, 20))
  screen.blit(cork46, cork_46)

  cork_47 = pygame.Rect(230, 250, 15, 20)
  cork47 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork47 = pygame.transform.scale(cork47, (15, 20))
  screen.blit(cork47, cork_47)

  cork_48 = pygame.Rect(435, 200, 15, 20)
  cork48 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork48 = pygame.transform.scale(cork48, (15, 20))
  screen.blit(cork48, cork_48)

  cork_49 = pygame.Rect(400, 305, 15, 20)
  cork49 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork49 = pygame.transform.scale(cork49, (15, 20))
  screen.blit(cork49, cork_49)

  cork_50 = pygame.Rect(365, 305, 15, 20)
  cork50 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork50 = pygame.transform.scale(cork50, (15, 20))
  screen.blit(cork50, cork_50)

  cork_51 = pygame.Rect(330, 305, 15, 20)
  cork51 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork51 = pygame.transform.scale(cork51, (15, 20))
  screen.blit(cork51, cork_51)

  cork_52 = pygame.Rect(295, 305, 15, 20)
  cork52 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork52 = pygame.transform.scale(cork52, (15, 20))
  screen.blit(cork52, cork_52)

  cork_53 = pygame.Rect(260, 305, 15, 20)
  cork53 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork53 = pygame.transform.scale(cork53, (15, 20))
  screen.blit(cork53, cork_53)

  cork_54 = pygame.Rect(190, 305, 15, 20)
  cork54 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork54 = pygame.transform.scale(cork54, (15, 20))
  screen.blit(cork54, cork_54)

  cork_55 = pygame.Rect(155, 305, 15, 20)
  cork55 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork55 = pygame.transform.scale(cork55, (15, 20))
  screen.blit(cork55, cork_55)

  cork_56 = pygame.Rect(120, 305, 15, 20)
  cork56 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork56 = pygame.transform.scale(cork56, (15, 20))
  screen.blit(cork56, cork_56)

  cork_57 = pygame.Rect(85, 305, 15, 20)
  cork57 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork57 = pygame.transform.scale(cork57, (15, 20))
  screen.blit(cork57, cork_57)

  cork_58 = pygame.Rect(50, 305, 15, 20)
  cork58 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork58 = pygame.transform.scale(cork58, (15, 20))
  screen.blit(cork58, cork_58)

  cork_59 = pygame.Rect(285, 148, 15, 20)
  cork59 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork59 = pygame.transform.scale(cork59, (15, 20))
  screen.blit(cork59, cork_59)

  cork_60 = pygame.Rect(330, 205, 15, 20)
  cork60 = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
  cork60 = pygame.transform.scale(cork60, (15, 20))
  screen.blit(cork60, cork_60)

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