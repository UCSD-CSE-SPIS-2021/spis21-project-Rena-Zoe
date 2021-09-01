
import pygame

import os

def directory(screen_length,screen_height, dim_field, screen):

  screen.fill((191,239,255))

  header_rect = pygame.Rect(0, 0, 470, 30)
  #pos x, pos y, width, length
  
  pygame.draw.rect(screen, (188,210,238), header_rect)

  pygame.font.init()

  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  direct_title = font.render("Directory",True,(0,0,0))

  show_direct_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_direct_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_direct_title = False

  if (show_direct_title):
    screen.blit(direct_title,(180, 7))

  #Curt
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  curt_title2 = font.render("Curt:",True,(0,0,0))

  show_curt_title2 = True
  
  start_time = pygame.time.get_ticks()

  if (show_curt_title2):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_curt_title2 = False

  if (show_curt_title2):
    screen.blit(curt_title2,(10, 60))

  #Hannah
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  hannah_title = font.render("Hannah:",True,(0,0,0))

  show_hannah_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_hannah_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_hannah_title = False

  if (show_hannah_title):
    screen.blit(hannah_title,(10, 90))

  #Jonny
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  jonny_title = font.render("Jonny:",True,(0,0,0))

  show_jonny_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_jonny_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_jonny_title = False

  if (show_jonny_title):
    screen.blit(jonny_title,(10, 120))

  #Josh
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  josh_title = font.render("Josh:",True,(0,0,0))

  show_josh_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_josh_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_josh_title = False

  if (show_josh_title):
    screen.blit(josh_title,(10, 150))

  #Michael
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  michael_title = font.render("Michael:",True,(0,0,0))

  show_michael_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_michael_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_michael_title = False

  if (show_michael_title):
    screen.blit(michael_title,(10, 180))


  #Gary player
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  gary_title2 = font.render("Gary:",True,(0,0,0))

  show_gary_title2 = True
  
  start_time = pygame.time.get_ticks()

  if (show_gary_title2):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_gary_title2 = False

  if (show_gary_title2):
    screen.blit(gary_title2,(170, 60))


  #Diego
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  diego_title = font.render("Diego:",True,(0,0,0))

  show_diego_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_diego_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_diego_title = False

  if (show_diego_title):
    screen.blit(diego_title,(170, 90))

  #Akshat
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  akshat_title = font.render("Akshat:",True,(0,0,0))

  show_akshat_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_akshat_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_akshat_title = False

  if (show_akshat_title):
    screen.blit(akshat_title,(170, 120))
  #John
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  john_title = font.render("John:",True,(0,0,0))

  show_john_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_john_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_john_title = False

  if (show_john_title):
    screen.blit(john_title,(170, 150))

  #Niema
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  niema_title2 = font.render("Niema:",True,(0,0,0))

  show_niema_title2 = True
  
  start_time = pygame.time.get_ticks()

  if (show_niema_title2):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_niema_title2 = False

  if (show_niema_title2):
    screen.blit(niema_title2,(320, 60))


  #Younus
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  younus_title = font.render("Younus:",True,(0,0,0))

  show_younus_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_younus_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_younus_title = False

  if (show_younus_title):
    screen.blit(younus_title,(170, 180))
  
  #Jenelle
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  jenelle_title = font.render("Jenelle:",True,(0,0,0))

  show_jenelle_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_jenelle_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_jenelle_title = False

  if (show_jenelle_title):
    screen.blit(jenelle_title,(10, 210))
  
  #Elisa
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  elisa_title = font.render("Elisa:",True,(0,0,0))

  show_elisa_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_elisa_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_elisa_title = False

  if (show_elisa_title):
    screen.blit(elisa_title,(170, 210))
  
  #Lindsey
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  lindsey_title = font.render("Lindsey:",True,(0,0,0))

  show_lindsey_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_lindsey_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_lindsey_title = False

  if (show_lindsey_title):
    screen.blit(lindsey_title,(10, 240))
  
  #Henryl
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  henryl_title = font.render("Henry L:",True,(0,0,0))

  show_henryl_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_henryl_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_henryl_title = False

  if (show_henryl_title):
    screen.blit(henryl_title,(170, 240))
  
  #tristin
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  tristin_title = font.render("Tristin:",True,(0,0,0))

  show_tristin_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_tristin_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_tristin_title = False

  if (show_tristin_title):
    screen.blit(tristin_title,(320, 120))

  #henry x
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  henryx_title = font.render("Henry X:",True,(0,0,0))

  show_henryx_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_henryx_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_henryx_title = False

  if (show_henryx_title):
    screen.blit(henryx_title,(320, 180))

  #Nikki
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  nikki_title = font.render("Nikki:",True,(0,0,0))

  show_nikki_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_nikki_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_nikki_title = False

  if (show_nikki_title):
    screen.blit(nikki_title,(320, 210))

  #Prothit
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  prothit_title = font.render("Prothit:",True,(0,0,0))

  show_prothit_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_prothit_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_prothit_title = False

  if (show_prothit_title):
    screen.blit(prothit_title,(320, 150))

  #mohan
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  mohan_title = font.render("Mohan:",True,(0,0,0))

  show_mohan_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_mohan_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_mohan_title = False

  if (show_mohan_title):
    screen.blit(mohan_title,(320, 90))
  
  #Yukati
  font = pygame.font.Font("./Bungee-Regular.ttf",15)

  yukati_title = font.render("Yukati:",True,(0,0,0))

  show_yukati_title = True
  
  start_time = pygame.time.get_ticks()

  if (show_yukati_title):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_yukati_title = False

  if (show_yukati_title):
    screen.blit(yukati_title,(320, 240))

  #exit button --> returns to home screen
  
  home_rect2 = pygame.Rect(420, 5, 40, 20)
  pygame.draw.rect(screen, (141,182,205), home_rect2)

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
  
  #secret mohan level button

  mohan_button = pygame.Rect(170, 280, 120, 40)
  pygame.draw.rect(screen, (188,210,238), mohan_button)
 
  pygame.font.init()

  font = pygame.font.Font("./RampartOne-Regular.ttf",20)

  clickme = font.render("Click Me!",True,(0,0,0))

  show_clickme = True
  
  start_time = pygame.time.get_ticks()

  if (show_clickme):
    
    now_time = pygame.time.get_ticks()
    if (now_time - start_time > 500):
      show_clickme = False

  if (show_clickme):
    screen.blit(clickme,(180, 280))


  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if home_rect2.collidepoint(pos):
        return "home"
      if mohan_button.collidepoint(pos):
        # page = "secret"
        # print("Clicking")
        return "secret"
