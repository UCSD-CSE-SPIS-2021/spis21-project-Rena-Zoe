import pygame

import os

#Home screen
def homescreen(screen_length,screen_height, dim_field,screen,player_rect):

  #This is where we set the background
  background = pygame.image.load(os.path.join("homepage","home.background.jpg"))

  background = pygame.transform.scale(background, dim_field)

  screen.blit(background, (0,0))

  #This is where the three buttons are
  pygame.font.init()
    #Niema
  niema_rect = pygame.Rect(92, 210, 85, 50)
  pygame.draw.rect(screen, (83,134,150), niema_rect)

  font = pygame.font.Font("./Staatliches-Regular.ttf",20)
  
  niema_x = 111
  niema_y= 215

  niema_list = [" Niema", "(Easy)"]

  show_niema_list = True
  
  start_time = pygame.time.get_ticks()

  if (show_niema_list):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_niema_list = False

  for sentence in niema_list:

    inst = font.render(sentence,True,(255,255,255))

    if (show_niema_list):
      screen.blit(inst,(niema_x, niema_y))
      niema_y += 15

    #Gary
  gary_rect = pygame.Rect(192, 210, 85, 50)
  pygame.draw.rect(screen, (83,134,150), gary_rect)

  font = pygame.font.Font("./Staatliches-Regular.ttf",20)
  
  gary_x = 201
  gary_y= 215

  gary_list = ["     Gary", "(Medium)"]

  show_gary_list = True
  
  start_time = pygame.time.get_ticks()

  if (show_gary_list):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_gary_list = False

  for sentence in gary_list:

    inst = font.render(sentence,True,(255,255,255))

    if (show_gary_list):
      screen.blit(inst,(gary_x, gary_y))
      gary_y += 15
  
    #Curt
  curt_rect = pygame.Rect(292, 210, 85, 50)
  pygame.draw.rect(screen, (83,134,150), curt_rect)
  
  font = pygame.font.Font("./Staatliches-Regular.ttf",20)
  
  curt_x = 310
  curt_y= 215

  curt_list = ["   Curt", "(Hard)"]

  show_curt_list = True
  
  start_time = pygame.time.get_ticks()

  if (show_curt_list):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_curt_list = False

  for sentence in curt_list:

    inst = font.render(sentence,True,(255,255,255))

    if (show_curt_list):
      screen.blit(inst,(curt_x, curt_y))
      curt_y += 15
  
  #Directory button

  direct_rect = pygame.Rect(10, 310, 100, 30)
  pygame.draw.rect(screen, (83,134,150), direct_rect)

  #Directory text
  font = pygame.font.Font("./Staatliches-Regular.ttf",20)

  direct = font.render("Directory",True,(255, 255, 255))

  show_direct = True
  
  start_time = pygame.time.get_ticks()

  if (show_direct):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_direct = False

  if (show_direct):
    screen.blit(direct,(23, 313))
      
#This is our Welcome!

  font = pygame.font.Font("./RampartOne-Regular.ttf",50)

  welcome = font.render("WELCOME!",True,(0,0,0))

  show_welcome = True
  
  start_time = pygame.time.get_ticks()

  if (show_welcome):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_welcome = False

  if (show_welcome):
    screen.blit(welcome,(90, 52))
  
  #This is where our instructions are
  font = pygame.font.Font("./Staatliches-Regular.ttf",18)

  inst_x = 25
  inst_y = 125

  inst_text_list = ["Instructions: Your goal is to eat everything and earn points!","         Press arrow keys to move up, down, left, and right.", "             Small items are 10 pts and large items are 50 pts.","                      Avoid enemies. You have 3 lives. Good luck!"]

  show_inst = True
  
  start_time = pygame.time.get_ticks()

  if (show_inst):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_inst = False

  for sentence in inst_text_list:

    inst = font.render(sentence,True,(0,0,0))

    if (show_inst):
      screen.blit(inst,(inst_x, inst_y))
      inst_y += 16
  
  #Click here text
  font = pygame.font.Font("./Staatliches-Regular.ttf",15)

  click_here = font.render("(Click on a button to choose your professor)",True,(0,0,0))

  show_click_here = True
  
  start_time = pygame.time.get_ticks()

  if (show_click_here):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      click_here = False

  if (show_click_here):
    screen.blit(click_here,(108, 265))
  
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      #print("Josh has a weird symbol.")
      pos = pygame.mouse.get_pos()
      if curt_rect.collidepoint(pos):
        #print("curt needs help")
        return "curt"
      elif gary_rect.collidepoint(pos):
        return "gary"
      elif niema_rect.collidepoint(pos):
        return "niema"
      elif direct_rect.collidepoint(pos):
        return "directory"

  return "home"