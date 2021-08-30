import pygame

import os

#def loadassets():
 #background = pygame.image.load(os.path.join("curt","curt.background.png"))

#Curt
def curt(screen_length,screen_height, dim_field, screen, player_rect, num_points, num_lives):

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
  
  #num_points = 0

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
  if player_rect.left < 0:
    player_rect.left = 0
  if player_rect.right > screen_length:
   player_rect.right = screen_length
  if player_rect.bottom > 340:
    player_rect.bottom = 340
  if player_rect.top < 30:
    player_rect.top = 30

def c10points(screen_length,screen_height, dim_field, screen, player_rect):

  star_1 = pygame.Rect(37, 40, 15, 15)
  starsprite = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  starsprite = pygame.transform.scale(starsprite, (15, 15))
  screen.blit(starsprite, star_1)

  star_2 = pygame.Rect(67, 40, 15, 15)
  

  star_3 = pygame.Rect(67, 70, 15, 15)
 

  star_4 = pygame.Rect(67, 95, 15, 15)
  

  star_5 = pygame.Rect(37, 95, 15, 15)
  

  star_6 = pygame.Rect(10, 95, 15, 15)
  

  star_7 = pygame.Rect(10, 122, 15, 15)
  

  star_8 = pygame.Rect(10, 150, 15, 15)
  

  star_9 = pygame.Rect(97, 95, 15, 15)
  

  star_10 = pygame.Rect(127, 95, 15, 15)
  
  star_11 = pygame.Rect(127, 72, 15, 15)
 

  star_12 = pygame.Rect(127, 40, 15, 15)
  

  star_13 = pygame.Rect(157, 40, 15, 15)
  

  star_14 = pygame.Rect(187, 40, 15, 15)
  

  star_90 = pygame.Rect(225, 40, 15, 15)
  

  star_15 = pygame.Rect(157, 95, 15, 15)
  

  star_16 = pygame.Rect(187, 95, 15, 15)
  

  star_17 = pygame.Rect(217, 95, 15, 15)
  

  star_18 = pygame.Rect(247, 95, 15, 15)
  

  star_19 = pygame.Rect(277, 95, 15, 15)
  

  star_20 = pygame.Rect(307, 95, 15, 15)
  
  
  star_21 = pygame.Rect(337, 95, 15, 15)
  

  star_22 = pygame.Rect(322, 72, 15, 15)
  

  star_23 = pygame.Rect(322, 40, 15, 15)
  

  star_24 = pygame.Rect(292, 40, 15, 15)
  

  star_25 = pygame.Rect(262, 40, 15, 15)
  

  star_26 = pygame.Rect(367, 95, 15, 15)
  

  star_27 = pygame.Rect(397, 95, 15, 15)
  

  star_28 = pygame.Rect(427, 95, 15, 15)
  

  star_29 = pygame.Rect(427, 125, 15, 15)
  

  star_30 = pygame.Rect(427, 150, 15, 15)
  

  star_31 = pygame.Rect(382, 70, 15, 15)
  

  star_32 = pygame.Rect(382, 40, 15, 15)
  

  star_33 = pygame.Rect(412, 40, 15, 15)
  

  star_34 = pygame.Rect(442, 40, 15, 15)
  

  star_35 = pygame.Rect(112, 120, 15, 15)
  

  star_36 = pygame.Rect(112, 145, 15, 15)
  
  star_37 = pygame.Rect(142, 145, 15, 15)

  star_38 = pygame.Rect(112, 175, 15, 15)

  star_39 = pygame.Rect(112, 205, 15, 15)

  star_40 = pygame.Rect(112, 235, 15, 15)

  star_41 = pygame.Rect(107, 260, 15, 15)
  
  star_42 = pygame.Rect(202, 115, 15, 15)

  star_43 = pygame.Rect(202, 145, 15, 15)

  star_44 = pygame.Rect(202, 175, 15, 15)

  star_45 = pygame.Rect(202, 205, 15, 15)
  
  star_46 = pygame.Rect(202, 235, 15, 15)
  
  star_47 = pygame.Rect(202, 260, 15, 15)
  
  star_48 = pygame.Rect(335, 115, 15, 15)
  
  star_49 = pygame.Rect(335, 145, 15, 15)

  star_50 = pygame.Rect(335, 175, 15, 15)
  
  star_51 = pygame.Rect(335, 205, 15, 15)

  star_52 = pygame.Rect(335, 235, 15, 15)

  star_53 = pygame.Rect(352, 260, 15, 15)

  star_54 = pygame.Rect(10, 200, 15, 15)
  
  star_55 = pygame.Rect(40, 200, 15, 15)
  
  star_56 = pygame.Rect(10, 230, 15, 15)

#This one is weird and where josh spawns
  star_57 = pygame.Rect(70, 200, 15, 15)

  star_58 = pygame.Rect(10, 260, 15, 15)

  star_59 = pygame.Rect(40, 260, 15, 15)

  star_60 = pygame.Rect(70, 260, 15, 15)

  star_61 = pygame.Rect(142, 260, 15, 15)

  star_62 = pygame.Rect(172, 260, 15, 15)

  star_63 = pygame.Rect(232, 260, 15, 15)

  star_64 = pygame.Rect(262, 260, 15, 15)

  star_65 = pygame.Rect(292, 260, 15, 15)

  star_66 = pygame.Rect(322, 260, 15, 15)

  star_67 = pygame.Rect(382, 260, 15, 15)

  star_68 = pygame.Rect(412, 260, 15, 15)

  star_69 = pygame.Rect(442, 260, 15, 15)

  star_70 = pygame.Rect(427, 230, 15, 15)

  star_71 = pygame.Rect(427, 200, 15, 15)

  star_72 = pygame.Rect(397, 200, 15, 15)

  star_73 = pygame.Rect(250, 175, 15, 15)

  star_74 = pygame.Rect(250, 205, 15, 15)

  star_75 = pygame.Rect(250, 235, 15, 15)

  star_76 = pygame.Rect(287, 145, 15, 15)

  star_77 = pygame.Rect(287, 175, 15, 15)

  star_78 = pygame.Rect(287, 205, 15, 15)

  star_91 = pygame.Rect(287, 235, 15, 15)

  star_79 = pygame.Rect(70, 290, 15, 15)

  star_92 = pygame.Rect(70, 320, 15, 15)

  star_81 = pygame.Rect(40, 320, 15, 15)

  star_82 = pygame.Rect(10, 320, 15, 15)

  star_93 = pygame.Rect(130, 290, 15, 15)

  star_80 = pygame.Rect(130, 320, 15, 15)

  star_94 = pygame.Rect(160, 320, 15, 15)

  star_95 = pygame.Rect(190, 320, 15, 15)

  star_83 = pygame.Rect(250, 320, 15, 15)

  star_84 = pygame.Rect(280, 320, 15, 15)

  star_85 = pygame.Rect(310, 320, 15, 15)

  star_86 = pygame.Rect(310, 290, 15, 15)

  star_87 = pygame.Rect(380, 290, 15, 15)

  star_88 = pygame.Rect(380, 320, 15, 15)

  star_89 = pygame.Rect(410, 320, 15, 15)

  star_list = [star_1, star_2, star_3, star_4, star_5, star_6, star_7, star_8, star_9, star_10, star_11,star_12,star_13,star_14,star_15,star_16,star_17,star_18,star_19,star_20, star_21, star_22, star_23, star_24, star_25, star_26, star_27, star_28, star_29, star_30, star_31, star_32, star_33, star_34, star_35, star_36, star_37, star_38, star_39, star_40, star_41, star_42, star_43, star_44, star_45, star_46, star_47, star_48, star_49, star_50, star_51, star_52, star_53, star_54, star_55, star_56, star_57, star_58, star_59, star_60, star_61, star_62, star_63, star_64, star_65, star_66, star_67, star_68, star_69, star_70, star_71, star_72, star_73, star_74, star_75, star_76, star_77, star_78, star_79, star_80, star_81, star_82, star_83, star_84, star_85, star_86, star_87, star_88, star_89, star_90, star_91, star_92, star_93, star_94, star_95]
  #print(len(star_list))
  return star_list


def c50points(screen_length,screen_height, dim_field, screen, player_rect):
  hat_1 = pygame.Rect(2, 40, 15, 15)
  hatsprite = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hatsprite = pygame.transform.scale(hatsprite, (20, 20))
  screen.blit(hatsprite, hat_1)

  hat_2 = pygame.Rect(247, 145, 15, 15)
  hat2 = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hat2 = pygame.transform.scale(hat2, (20, 20))
  screen.blit(hat2, hat_2)

  hat_3 = pygame.Rect(218, 320, 15, 15)
  hat3 = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hat3 = pygame.transform.scale(hat3, (20, 20))
  screen.blit(hat3, hat_3)

  hat_4 = pygame.Rect(440, 320, 15, 15)
  hat4 = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hat4 = pygame.transform.scale(hat4, (20, 20))
  screen.blit(hat4, hat_4)

  hat_list = [hat_1, hat_2, hat_3, hat_4]

  return hat_list


def c_walls(screen_length,screen_height, dim_field, screen, player_rect):
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