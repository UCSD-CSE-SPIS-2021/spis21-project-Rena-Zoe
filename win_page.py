import pygame

import os

def win_page(screen_length,screen_height, dim_field, screen, player_rect):

  win_background = pygame.image.load(os.path.join("lose_win","win.background.png"))

  win_background = pygame.transform.scale(win_background, dim_field)

  screen.blit(win_background, (0,0))

  pygame.font.init()

  font = pygame.font.Font("./RampartOne-Regular.ttf",50)

  win_title = font.render("You Win!",True,(0,0,0))

  show_win_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_win_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_win_title = False

  if (show_win_title):
    screen.blit(win_title,(125, 70))

  font = pygame.font.Font("./Staatliches-Regular.ttf",18)

  win_x = 20
  win_y = 140

  win_text_list = ["                                                    Thanks for playing!", "    And a special thanks to all of our professors and mentors!", "                If you would like to retry or try a different level", "                                      please click the 'Home' button."]

  show_win = True
  
  start_time = pygame.time.get_ticks()

  if (show_win):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_win = False

  for sentence in win_text_list:

    lose = font.render(sentence,True,(0,0,0))

    if (show_win):
      screen.blit(lose,(win_x, win_y))
      win_y += 16
  
  home_rect = pygame.Rect(200, 215, 85, 50)
  pygame.draw.rect(screen, (255,192,203), home_rect)
  
  font = pygame.font.Font("./RampartOne-Regular.ttf",25)
  
  home = font.render("Home",True,(0,0,0))

  show_home = True
  
  start_time = pygame.time.get_ticks()

  if (show_home):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_home = False

  if (show_home):
    screen.blit(home,(208, 220))

  font = pygame.font.Font("./Staatliches-Regular.ttf",15)

  point = font.render("Niema pts: 650, Gary pts: 800, Curt pts: 1150",True,(0,0,0))

  show_point = True
  
  start_time = pygame.time.get_ticks()

  if (show_point):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_point = False

  if (show_point):
    screen.blit(point,(125, 275))
    
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if home_rect.collidepoint(pos):
        return "home"