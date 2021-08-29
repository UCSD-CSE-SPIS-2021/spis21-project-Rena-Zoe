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
  star1 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star1 = pygame.transform.scale(star1, (15, 15))
  screen.blit(star1, star_1)

  star_2 = pygame.Rect(67, 40, 15, 15)
  star2 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star2 = pygame.transform.scale(star2, (15, 15))
  screen.blit(star2, star_2)

  star_3 = pygame.Rect(67, 70, 15, 15)
  star3 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star3 = pygame.transform.scale(star3, (15, 15))
  screen.blit(star3, star_3)

  star_4 = pygame.Rect(67, 95, 15, 15)
  star4 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star4 = pygame.transform.scale(star4, (15, 15))
  screen.blit(star4, star_4)

  star_5 = pygame.Rect(37, 95, 15, 15)
  star5 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star5 = pygame.transform.scale(star5, (15, 15))
  screen.blit(star5, star_5)

  star_6 = pygame.Rect(10, 95, 15, 15)
  star6 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star6 = pygame.transform.scale(star6, (15, 15))
  screen.blit(star6, star_6)

  star_7 = pygame.Rect(10, 122, 15, 15)
  star7 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star7 = pygame.transform.scale(star7, (15, 15))
  screen.blit(star7, star_7)

  star_8 = pygame.Rect(10, 150, 15, 15)
  star8 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star8 = pygame.transform.scale(star8, (15, 15))
  screen.blit(star8, star_8)

  star_9 = pygame.Rect(97, 95, 15, 15)
  star9 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star9 = pygame.transform.scale(star9, (15, 15))
  screen.blit(star9, star_9)

  star_10 = pygame.Rect(127, 95, 15, 15)
  star10 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star10 = pygame.transform.scale(star10, (15, 15))
  screen.blit(star10, star_10)

  star_11 = pygame.Rect(127, 72, 15, 15)
  star11 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star11 = pygame.transform.scale(star11, (15, 15))
  screen.blit(star11, star_11)

  star_12 = pygame.Rect(127, 40, 15, 15)
  star12 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star12 = pygame.transform.scale(star12, (15, 15))
  screen.blit(star12, star_12)

  star_13 = pygame.Rect(157, 40, 15, 15)
  star13 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star13 = pygame.transform.scale(star13, (15, 15))
  screen.blit(star13, star_13)

  star_14 = pygame.Rect(187, 40, 15, 15)
  star14 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star14 = pygame.transform.scale(star14, (15, 15))
  screen.blit(star14, star_14)

  star_90 = pygame.Rect(225, 40, 15, 15)
  star90 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star90 = pygame.transform.scale(star90, (15, 15))
  screen.blit(star90, star_90)

  star_15 = pygame.Rect(157, 95, 15, 15)
  star15 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star15 = pygame.transform.scale(star15, (15, 15))
  screen.blit(star15, star_15)

  star_16 = pygame.Rect(187, 95, 15, 15)
  star16 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star16 = pygame.transform.scale(star16, (15, 15))
  screen.blit(star16, star_16)

  star_17 = pygame.Rect(217, 95, 15, 15)
  star17 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star17 = pygame.transform.scale(star17, (15, 15))
  screen.blit(star17, star_17)

  star_18 = pygame.Rect(247, 95, 15, 15)
  star18 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star18 = pygame.transform.scale(star18, (15, 15))
  screen.blit(star18, star_18)

  star_19 = pygame.Rect(277, 95, 15, 15)
  star19 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star19 = pygame.transform.scale(star19, (15, 15))
  screen.blit(star19, star_19)

  star_20 = pygame.Rect(307, 95, 15, 15)
  star20 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star20 = pygame.transform.scale(star20, (15, 15))
  screen.blit(star20, star_20)

  star_21 = pygame.Rect(337, 95, 15, 15)
  star21 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star21 = pygame.transform.scale(star21, (15, 15))
  screen.blit(star21, star_21)

  star_22 = pygame.Rect(322, 72, 15, 15)
  star22 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star22 = pygame.transform.scale(star22, (15, 15))
  screen.blit(star22, star_22)

  star_23 = pygame.Rect(322, 40, 15, 15)
  star23 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star23 = pygame.transform.scale(star23, (15, 15))
  screen.blit(star23, star_23)

  star_24 = pygame.Rect(292, 40, 15, 15)
  star24 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star24 = pygame.transform.scale(star24, (15, 15))
  screen.blit(star24, star_24)

  star_25 = pygame.Rect(262, 40, 15, 15)
  star25 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star25 = pygame.transform.scale(star25, (15, 15))
  screen.blit(star25, star_25)

  star_26 = pygame.Rect(367, 95, 15, 15)
  star26 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star26 = pygame.transform.scale(star26, (15, 15))
  screen.blit(star26, star_26)

  star_27 = pygame.Rect(397, 95, 15, 15)
  star27 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star27 = pygame.transform.scale(star27, (15, 15))
  screen.blit(star27, star_27)

  star_28 = pygame.Rect(427, 95, 15, 15)
  star28 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star28 = pygame.transform.scale(star28, (15, 15))
  screen.blit(star28, star_28)

  star_29 = pygame.Rect(427, 125, 15, 15)
  star29 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star29 = pygame.transform.scale(star29, (15, 15))
  screen.blit(star29, star_29)

  star_30 = pygame.Rect(427, 150, 15, 15)
  star30 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star30 = pygame.transform.scale(star30, (15, 15))
  screen.blit(star30, star_30)

  star_31 = pygame.Rect(382, 70, 15, 15)
  star31 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star31 = pygame.transform.scale(star31, (15, 15))
  screen.blit(star31, star_31)

  star_32 = pygame.Rect(382, 40, 15, 15)
  star32 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star32 = pygame.transform.scale(star32, (15, 15))
  screen.blit(star32, star_32)

  star_33 = pygame.Rect(412, 40, 15, 15)
  star33 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star33 = pygame.transform.scale(star33, (15, 15))
  screen.blit(star33, star_33)

  star_34 = pygame.Rect(442, 40, 15, 15)
  star34 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star34 = pygame.transform.scale(star34, (15, 15))
  screen.blit(star34, star_34)

  star_35 = pygame.Rect(112, 120, 15, 15)
  star35 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star35 = pygame.transform.scale(star35, (15, 15))
  screen.blit(star35, star_35)

  star_36 = pygame.Rect(112, 145, 15, 15)
  star36 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star36 = pygame.transform.scale(star36, (15, 15))
  screen.blit(star36, star_36)

  star_37 = pygame.Rect(142, 145, 15, 15)
  star37 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star37 = pygame.transform.scale(star37, (15, 15))
  screen.blit(star37, star_37)

  star_38 = pygame.Rect(112, 175, 15, 15)
  star38 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star38 = pygame.transform.scale(star38, (15, 15))
  screen.blit(star38, star_38)

  star_39 = pygame.Rect(112, 205, 15, 15)
  star39 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star39 = pygame.transform.scale(star39, (15, 15))
  screen.blit(star39, star_39)

  star_40 = pygame.Rect(112, 235, 15, 15)
  star40 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star40 = pygame.transform.scale(star40, (15, 15))
  screen.blit(star40, star_40)

  star_41 = pygame.Rect(107, 260, 15, 15)
  star41 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star41 = pygame.transform.scale(star41, (15, 15))
  screen.blit(star41, star_41)

  star_42 = pygame.Rect(202, 115, 15, 15)
  star42 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star42 = pygame.transform.scale(star42, (15, 15))
  screen.blit(star42, star_42)

  star_43 = pygame.Rect(202, 145, 15, 15)
  star43 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star43 = pygame.transform.scale(star43, (15, 15))
  screen.blit(star43, star_43)

  star_44 = pygame.Rect(202, 175, 15, 15)
  star44 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star44 = pygame.transform.scale(star44, (15, 15))
  screen.blit(star44, star_44)

  star_45 = pygame.Rect(202, 205, 15, 15)
  star45 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star45 = pygame.transform.scale(star45, (15, 15))
  screen.blit(star45, star_45)

  star_46 = pygame.Rect(202, 235, 15, 15)
  star46 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star46 = pygame.transform.scale(star46, (15, 15))
  screen.blit(star46, star_46)

  star_47 = pygame.Rect(202, 260, 15, 15)
  star47 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star47 = pygame.transform.scale(star47, (15, 15))
  screen.blit(star47, star_47)

  star_48 = pygame.Rect(335, 115, 15, 15)
  star48 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star48 = pygame.transform.scale(star48, (15, 15))
  screen.blit(star48, star_48)

  star_49 = pygame.Rect(335, 145, 15, 15)
  star49 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star49 = pygame.transform.scale(star49, (15, 15))
  screen.blit(star49, star_49)

  star_50 = pygame.Rect(335, 175, 15, 15)
  star50 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star50 = pygame.transform.scale(star50, (15, 15))
  screen.blit(star50, star_50)

  star_51 = pygame.Rect(335, 205, 15, 15)
  star51 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star51 = pygame.transform.scale(star51, (15, 15))
  screen.blit(star51, star_51)

  star_52 = pygame.Rect(335, 235, 15, 15)
  star52 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star52 = pygame.transform.scale(star52, (15, 15))
  screen.blit(star52, star_52)

  star_53 = pygame.Rect(352, 260, 15, 15)
  star53 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star53 = pygame.transform.scale(star53, (15, 15))
  screen.blit(star53, star_53)

  star_54 = pygame.Rect(10, 200, 15, 15)
  star54 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star54 = pygame.transform.scale(star54, (15, 15))
  screen.blit(star54, star_54)

  star_55 = pygame.Rect(40, 200, 15, 15)
  star55 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star55 = pygame.transform.scale(star55, (15, 15))
  screen.blit(star55, star_55)

  star_56 = pygame.Rect(10, 230, 15, 15)
  star56 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star56 = pygame.transform.scale(star56, (15, 15))
  screen.blit(star56, star_56)

#This one is weird and where josh spawns
  star_57 = pygame.Rect(70, 200, 15, 15)
  star57 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star57 = pygame.transform.scale(star57, (15, 15))
  screen.blit(star57, star_57)

  star_58 = pygame.Rect(10, 260, 15, 15)
  star58 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star58 = pygame.transform.scale(star58, (15, 15))
  screen.blit(star58, star_58)

  star_59 = pygame.Rect(40, 260, 15, 15)
  star59 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star59 = pygame.transform.scale(star59, (15, 15))
  screen.blit(star59, star_59)

  star_60 = pygame.Rect(70, 260, 15, 15)
  star60 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star60 = pygame.transform.scale(star60, (15, 15))
  screen.blit(star60, star_60)

  star_61 = pygame.Rect(142, 260, 15, 15)
  star61 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star61 = pygame.transform.scale(star61, (15, 15))
  screen.blit(star61, star_61)

  star_62 = pygame.Rect(172, 260, 15, 15)
  star62 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star62 = pygame.transform.scale(star62, (15, 15))
  screen.blit(star62, star_62)

  star_63 = pygame.Rect(232, 260, 15, 15)
  star63 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star63 = pygame.transform.scale(star63, (15, 15))
  screen.blit(star63, star_63)

  star_64 = pygame.Rect(262, 260, 15, 15)
  star64 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star64 = pygame.transform.scale(star64, (15, 15))
  screen.blit(star64, star_64)

  star_65 = pygame.Rect(292, 260, 15, 15)
  star65 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star65 = pygame.transform.scale(star65, (15, 15))
  screen.blit(star65, star_65)

  star_66 = pygame.Rect(322, 260, 15, 15)
  star66 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star66 = pygame.transform.scale(star66, (15, 15))
  screen.blit(star66, star_66)

  star_67 = pygame.Rect(382, 260, 15, 15)
  star67 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star67 = pygame.transform.scale(star67, (15, 15))
  screen.blit(star67, star_67)

  star_68 = pygame.Rect(412, 260, 15, 15)
  star68 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star68 = pygame.transform.scale(star68, (15, 15))
  screen.blit(star68, star_68)

  star_69 = pygame.Rect(442, 260, 15, 15)
  star69 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star69 = pygame.transform.scale(star69, (15, 15))
  screen.blit(star69, star_69)

  star_70 = pygame.Rect(427, 230, 15, 15)
  star70 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star70 = pygame.transform.scale(star70, (15, 15))
  screen.blit(star70, star_70)

  star_71 = pygame.Rect(427, 200, 15, 15)
  star71 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star71 = pygame.transform.scale(star71, (15, 15))
  screen.blit(star71, star_71)

  star_72 = pygame.Rect(397, 200, 15, 15)
  star72 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star72 = pygame.transform.scale(star72, (15, 15))
  screen.blit(star72, star_72)

  hat_2 = pygame.Rect(247, 145, 15, 15)
  hat2 = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hat2 = pygame.transform.scale(hat2, (20, 20))
  screen.blit(hat2, hat_2)

  star_73 = pygame.Rect(250, 175, 15, 15)
  star73 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star73 = pygame.transform.scale(star73, (15, 15))
  screen.blit(star73, star_73)

  star_74 = pygame.Rect(250, 205, 15, 15)
  star74 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star74 = pygame.transform.scale(star74, (15, 15))
  screen.blit(star74, star_74)

  star_75 = pygame.Rect(250, 235, 15, 15)
  star75 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star75 = pygame.transform.scale(star75, (15, 15))
  screen.blit(star75, star_75)

  star_76 = pygame.Rect(287, 145, 15, 15)
  star76 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star76 = pygame.transform.scale(star76, (15, 15))
  screen.blit(star76, star_76)

  star_77 = pygame.Rect(287, 175, 15, 15)
  star77 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star77 = pygame.transform.scale(star77, (15, 15))
  screen.blit(star77, star_77)

  star_78 = pygame.Rect(287, 205, 15, 15)
  star78 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star78 = pygame.transform.scale(star78, (15, 15))
  screen.blit(star78, star_78)

  star_78 = pygame.Rect(287, 235, 15, 15)
  star78 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star78 = pygame.transform.scale(star78, (15, 15))
  screen.blit(star78, star_78)

  star_79 = pygame.Rect(70, 290, 15, 15)
  star79 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star79 = pygame.transform.scale(star79, (15, 15))
  screen.blit(star79, star_79)

  star_80 = pygame.Rect(70, 320, 15, 15)
  star80 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star80 = pygame.transform.scale(star80, (15, 15))
  screen.blit(star80, star_80)

  star_81 = pygame.Rect(40, 320, 15, 15)
  star81 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star81 = pygame.transform.scale(star81, (15, 15))
  screen.blit(star81, star_81)

  star_82 = pygame.Rect(10, 320, 15, 15)
  star82 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star82 = pygame.transform.scale(star82, (15, 15))
  screen.blit(star82, star_82)

  star_79 = pygame.Rect(130, 290, 15, 15)
  star79 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star79 = pygame.transform.scale(star79, (15, 15))
  screen.blit(star79, star_79)

  star_80 = pygame.Rect(130, 320, 15, 15)
  star80 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star80 = pygame.transform.scale(star80, (15, 15))
  screen.blit(star80, star_80)

  star_81 = pygame.Rect(160, 320, 15, 15)
  star81 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star81 = pygame.transform.scale(star81, (15, 15))
  screen.blit(star81, star_81)

  star_82 = pygame.Rect(190, 320, 15, 15)
  star82 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star82 = pygame.transform.scale(star82, (15, 15))
  screen.blit(star82, star_82)

  star_83 = pygame.Rect(250, 320, 15, 15)
  star83 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star83 = pygame.transform.scale(star83, (15, 15))
  screen.blit(star83, star_83)

  star_84 = pygame.Rect(280, 320, 15, 15)
  star84 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star84 = pygame.transform.scale(star84, (15, 15))
  screen.blit(star84, star_84)

  star_85 = pygame.Rect(310, 320, 15, 15)
  star85 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star85 = pygame.transform.scale(star85, (15, 15))
  screen.blit(star85, star_85)

  star_86 = pygame.Rect(310, 290, 15, 15)
  star86 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star86 = pygame.transform.scale(star86, (15, 15))
  screen.blit(star86, star_86)

  star_87 = pygame.Rect(380, 290, 15, 15)
  star87 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star87 = pygame.transform.scale(star87, (15, 15))
  screen.blit(star87, star_87)

  star_88 = pygame.Rect(380, 320, 15, 15)
  star88 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star88 = pygame.transform.scale(star88, (15, 15))
  screen.blit(star88, star_88)

  star_89 = pygame.Rect(410, 320, 15, 15)
  star89 = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
  star89 = pygame.transform.scale(star89, (15, 15))
  screen.blit(star89, star_89)


def c50points(screen_length,screen_height, dim_field, screen, player_rect):
  hat_1 = pygame.Rect(2, 40, 15, 15)
  hat1 = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
  hat1 = pygame.transform.scale(hat1, (20, 20))
  screen.blit(hat1, hat_1)

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