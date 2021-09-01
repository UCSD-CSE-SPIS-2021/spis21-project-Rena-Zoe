import pygame

import os

def secret(screen_length,screen_height, dim_field, screen, mplayer_rect, quote):

  screen.fill((255,182,193))

  #Header
  header_rect = pygame.Rect(0, 0, 470, 30)
  #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (238,162,173), header_rect)

  #Quote Area
  #Header
  header_rect = pygame.Rect(0, 310, 470, 50)
  #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (238,162,173), header_rect)

  pygame.font.init()

  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  direct_title = font.render("Secret Mohan",True,(0,0,0))

  show_direct_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_direct_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_direct_title = False

  if (show_direct_title):
    screen.blit(direct_title,(180, 7))

  home_rect3 = pygame.Rect(420, 5, 40, 20)
  pygame.draw.rect(screen, (205,140,149), home_rect3)

  font = pygame.font.Font("./Staatliches-Regular.ttf",15)
  
  home = font.render("Home",True,(0,0,0))

  show_home = True
  
  start_time = pygame.time.get_ticks()

  if (show_home):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_home = False

  if (show_home):
    screen.blit(home,(426, 5))
  
  #mohan boundaries
  if mplayer_rect.left < 0:
    mplayer_rect.left = 0
  if mplayer_rect.right > screen_length:
    mplayer_rect.right = screen_length
  if mplayer_rect.bottom > 340:
    mplayer_rect.bottom = 340
  if mplayer_rect.top < 30:
    mplayer_rect.top = 30

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if home_rect3.collidepoint(pos):
        return "home"

  font = pygame.font.Font("./Bungee-Regular.ttf",11)

  the_quote = str(quote)

  a_quote = font.render(the_quote,True,(0,0,0))

  show_a_quote = True
  
  start_time = pygame.time.get_ticks()

  if (show_a_quote):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_a_quote = False

  if (show_a_quote):
    screen.blit(a_quote,(10, 320))

  #Gary's quote:
  #"I'm gonna some hot tea!!! - Gary"
  #Michael quote:
  #"Do or do not. There is no try. – Michael"
  #Niema's quote:
  #"I want to thank the students for starting a cult in my name - Niema"
  
  
def m_walls(screen_length,screen_height, dim_field, screen, mplayer_rect, quote):

#mohan walls -- 2025
  #First two
  two_rect1 = pygame.Rect(45, 110, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect1)
  two_rect2 = pygame.Rect(95, 110, 15, 55)
  pygame.draw.rect(screen, (255, 255, 255), two_rect2)
  two_rect3 = pygame.Rect(45, 150, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect3)
  two_rect4 = pygame.Rect(45, 170, 15, 45)
  pygame.draw.rect(screen, (255, 255, 255), two_rect4)
  two_rect5 = pygame.Rect(65, 200, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect5)


  #Zero
  zero_rect1 = pygame.Rect(145, 110, 70, 15)
  pygame.draw.rect(screen, (255, 255, 255), zero_rect1)
  zero_rect2 = pygame.Rect(145, 200, 70, 15)
  pygame.draw.rect(screen, (255, 255, 255), zero_rect2)
  zero_rect3 = pygame.Rect(145, 130, 15, 65)
  pygame.draw.rect(screen, (255, 255, 255), zero_rect3)
  zero_rect4 = pygame.Rect(200, 130, 15, 65)
  pygame.draw.rect(screen, (255, 255, 255), zero_rect4)

  #Second two
  two_rect6 = pygame.Rect(250, 110, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect6)
  two_rect7 = pygame.Rect(300, 110, 15, 55)
  pygame.draw.rect(screen, (255, 255, 255), two_rect7)
  two_rect8 = pygame.Rect(250, 150, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect8)
  two_rect9 = pygame.Rect(250, 170, 15, 45)
  pygame.draw.rect(screen, (255, 255, 255), two_rect9)
  two_rect10 = pygame.Rect(270, 200, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), two_rect10)

  #Five
  five_rect1 = pygame.Rect(370, 110, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), five_rect1)
  five_rect2 = pygame.Rect(350, 110, 15, 55)
  pygame.draw.rect(screen, (255, 255, 255), five_rect2)
  five_rect3 = pygame.Rect(370, 150, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), five_rect3)
  five_rect4 = pygame.Rect(400, 170, 15, 45)
  pygame.draw.rect(screen, (255, 255, 255), five_rect4)
  five_rect5 = pygame.Rect(350, 200, 45, 15)
  pygame.draw.rect(screen, (255, 255, 255), five_rect5)
  
  m_walls = [two_rect1,two_rect2,two_rect3,two_rect4,two_rect5,two_rect6,two_rect7,two_rect8,two_rect9,two_rect10,zero_rect1, zero_rect1, zero_rect1, zero_rect1, five_rect1, five_rect2, five_rect3, five_rect4, five_rect5]