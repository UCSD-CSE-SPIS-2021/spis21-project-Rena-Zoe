import pygame

import os

def lose_page(screen_length,screen_height, dim_field, screen, player_rect):

  lose_background = pygame.image.load(os.path.join("lose_win","lose.background.jpg"))

  lose_background = pygame.transform.scale(lose_background, dim_field)

  screen.blit(lose_background, (0,0))

  pygame.font.init()

  font = pygame.font.Font("./RampartOne-Regular.ttf",50)

  lost_title = font.render("You Lose!",True,(0,0,0))

  show_lost_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_lost_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_lost_title = False

  if (show_lost_title):
    screen.blit(lost_title,(115, 90))
  
  font = pygame.font.Font("./Staatliches-Regular.ttf",18)

  lose_x = 20
  lose_y = 160

  lose_text_list = ["                                                    Thanks for playing!", "    And a special thanks to all of our professors and mentors!", "                If you would like to retry or try a different level", "                                      please click the 'Home' button."]

  show_lose = True
  
  start_time = pygame.time.get_ticks()

  if (show_lose):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_lose = False

  for sentence in lose_text_list:

    lose = font.render(sentence,True,(0,0,0))

    if (show_lose):
      screen.blit(lose,(lose_x, lose_y))
      lose_y += 16
  
  #Home
  home_rect = pygame.Rect(200, 235, 85, 50)
  pygame.draw.rect(screen, (150,205,205), home_rect)
  
  font = pygame.font.Font("./RampartOne-Regular.ttf",25)
  
  home = font.render("Home",True,(0,0,0))

  show_home = True
  
  start_time = pygame.time.get_ticks()

  if (show_home):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_home = False

  if (show_home):
    screen.blit(home,(208, 240))

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if home_rect.collidepoint(pos):
        return "home"