import pygame

import os

import random

screen_length = 465

screen_height = 350

dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)

num_points = 0

num_lives = 3

quote = "Walk into mentors or professors."

#Draw all the players out here in future
player_x = 218
player_y = 40
player_width = 23
player_height = 23
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
player = pygame.image.load(os.path.join("curt", "camel.png")).convert()
player.set_colorkey((0, 0, 0))
player = pygame.transform.scale(player, (player_width, player_height))
#Hannah
hannah_x = 385
hannah_y = 250
hannah_rect = pygame.Rect(hannah_x, hannah_y, 23, 23)
hannah = pygame.image.load(os.path.join("curt", "hannah.png")).convert()
hannah.set_colorkey((255, 0, 0))
hannah = pygame.transform.scale(hannah, (23, 23))

#Jonny
jonny_x = 150
jonny_y = 145
jonny_rect = pygame.Rect(jonny_x, jonny_y, 23, 23)
jonny = pygame.image.load(os.path.join("curt", "jonny.png")).convert()
jonny.set_colorkey((0, 255, 0))
jonny = pygame.transform.scale(jonny, (25, 25))

#Josh
josh_x = 45
josh_y = 200
josh_rect = pygame.Rect(josh_x, josh_y, 23, 23)
josh = pygame.image.load(os.path.join("curt", "josh.png")).convert_alpha()
josh.set_colorkey((255, 255, 255))
josh = pygame.transform.scale(josh, (23, 23))

#Michael
michael_x = 285
michael_y = 200
michael_rect = pygame.Rect(michael_x, michael_y, 23, 23)
michael = pygame.image.load(os.path.join("curt", "michael.png")).convert()
michael.set_colorkey((0, 0, 0))
michael = pygame.transform.scale(michael, (23, 23))


#Gary player
gplayer_x = 15
gplayer_y = 40
gplayer_rect = pygame.Rect(gplayer_x, gplayer_y, 23, 23)
gplayer = pygame.image.load(os.path.join("gary", "gary.png")).convert()
gplayer.set_colorkey((0, 255, 0))
gplayer = pygame.transform.scale(gplayer, (23, 23))
#Diego
diego_x = 15
diego_y = 305
diego_rect = pygame.Rect(diego_x, diego_y, 23, 23)
diego = pygame.image.load(os.path.join("gary", "diego.png")).convert()
diego.set_colorkey((255, 255, 255))
diego = pygame.transform.scale(diego, (23, 23))
#Alarm clock
aclock_x = 425
aclock_y = 40
aclock_rect = pygame.Rect(aclock_x, aclock_y, 23, 23)
aclock = pygame.image.load(os.path.join("gary", "alarm_clock.png")).convert()
aclock.set_colorkey((0, 0, 0))
aclock = pygame.transform.scale(aclock, (23, 23))
#Akshat
akshat_x = 425
akshat_y = 305
akshat_rect = pygame.Rect(akshat_x, akshat_y, 23, 23)
akshat = pygame.image.load(os.path.join("gary", "akshat.png")).convert()
akshat.set_colorkey((0, 0, 0))
akshat = pygame.transform.scale(akshat, (23, 23))

#Niema
nplayer_x = 215
nplayer_y = 210
nplayer_rect = pygame.Rect(nplayer_x, nplayer_y, 20, 15)
nplayer = pygame.image.load(os.path.join("niema", "honda.png")).convert()
nplayer.set_colorkey((0, 0, 0))
nplayer = pygame.transform.scale(nplayer, (35, 25))
#Younus
younus_x =  70
younus_y = 200
younus_rect = pygame.Rect(younus_x, younus_y, 23, 23)
younus = pygame.image.load(os.path.join("niema", "younus.png")).convert()
younus.set_colorkey((0, 0, 0))
younus = pygame.transform.scale(younus, (23, 23))
#Belt
belt_x = 340
belt_y = 200
belt_rect = pygame.Rect(belt_x, belt_y, 23, 23)
belt = pygame.image.load(os.path.join("niema", "belt.png")).convert()
belt.set_colorkey((0, 0, 0))
belt = pygame.transform.scale(belt, (26, 26))

#Secret mohan map players
#Elisa
elisa_x =  70
elisa_y = 200
elisa_rect = pygame.Rect(elisa_x, elisa_y, 32, 32)
elisa = pygame.image.load(os.path.join("secret", "elisa.png")).convert()
elisa.set_colorkey((0, 0, 0))
elisa = pygame.transform.scale(elisa, (32, 32))

#Henry L
henryl_x =  70
henryl_y = 200
henryl_rect = pygame.Rect(henryl_x, henryl_y, 23, 23)
henryl = pygame.image.load(os.path.join("secret", "henryl.png")).convert()
henryl.set_colorkey((0, 0, 0))
henryl = pygame.transform.scale(henryl, (23, 23))

#Henry X
henryx_x =  70
henryx_y = 200
henryx_rect = pygame.Rect(henryx_x, henryx_y, 23, 23)
henryx = pygame.image.load(os.path.join("secret", "henryx.png")).convert()
henryx.set_colorkey((0, 0, 255))
henryx = pygame.transform.scale(henryx, (23, 23))

#Jenelle
jenelle_x =  70
jenelle_y = 200
jenelle_rect = pygame.Rect(jenelle_x, jenelle_y, 23, 23)
jenelle = pygame.image.load(os.path.join("secret", "jenelle.png")).convert()
jenelle.set_colorkey((0, 255, 0))
jenelle = pygame.transform.scale(jenelle, (23, 23))

#Lindsey
lindsey_x =  70
lindsey_y = 200
lindsey_rect = pygame.Rect(lindsey_x, lindsey_y, 23, 23)
lindsey = pygame.image.load(os.path.join("secret", "lindsey.png")).convert()
lindsey.set_colorkey((0, 0, 0))
lindsey = pygame.transform.scale(lindsey, (23, 23))

#Tristin
tristin_x =  70
tristin_y = 200
tristin_rect = pygame.Rect(tristin_x, tristin_y, 23, 23)
tristin = pygame.image.load(os.path.join("secret", "tristin.png")).convert()
tristin.set_colorkey((0, 255, 0))
tristin = pygame.transform.scale(tristin, (23, 23))

#Prothit
prothit_x =  70
prothit_y = 200
prothit_rect = pygame.Rect(prothit_x, prothit_y, 23, 23)
prothit = pygame.image.load(os.path.join("secret", "prothit.png")).convert()
prothit.set_colorkey((0, 0, 255))
prothit = pygame.transform.scale(prothit, (23, 23))
#Nikki
nikki_x =  70
nikki_y = 200
nikki_rect = pygame.Rect(nikki_x, nikki_y, 23, 23)
nikki = pygame.image.load(os.path.join("secret", "nikki.png")).convert()
nikki.set_colorkey((0, 255, 0))
nikki = pygame.transform.scale(nikki, (23, 23))
#Yukati
yukati_x =  70
yukati_y = 200
yukati_rect = pygame.Rect(yukati_x, yukati_y, 23, 23)
yukati = pygame.image.load(os.path.join("secret", "yukati.png")).convert()
yukati.set_colorkey((0, 255, 0))
yukati = pygame.transform.scale(yukati, (23, 23))
#Mohan
mplayer_x =  70
mplayer_y = 200
mplayer_rect = pygame.Rect(mplayer_x, mplayer_y, 23, 23)
mplayer = pygame.image.load(os.path.join("secret", "mohan.png")).convert()
mplayer.set_colorkey((255, 255, 255))
mplayer = pygame.transform.scale(mplayer, (23, 23))
#John
john_x = 285
john_y = 200
john_rect = pygame.Rect(john_x, john_y, 23, 23)
john = pygame.image.load(os.path.join("secret", "john.png")).convert()
john.set_colorkey((0, 255, 0))
john = pygame.transform.scale(john, (23, 23))


#Points
#Star sprites
starsprite = pygame.image.load(os.path.join("curt", "star.png")).convert_alpha()
starsprite = pygame.transform.scale(starsprite, (15, 15))
#Hat sprites
hatsprite = pygame.image.load(os.path.join("curt", "hat.png")).convert_alpha()
hatsprite = pygame.transform.scale(hatsprite, (20, 20))

#Wine glasses
corksprite = pygame.image.load(os.path.join("gary", "cork.png")).convert_alpha()
corksprite = pygame.transform.scale(corksprite, (15, 20))
#Wine bottles
winesprite = pygame.image.load(os.path.join("gary", "wine1.png")).convert_alpha()
winesprite = pygame.transform.scale(winesprite, (10, 30))
winesprite2 = pygame.image.load(os.path.join("gary", "wine2.png")).convert_alpha()
winesprite2 = pygame.transform.scale(winesprite2, (10, 30))
#Lord of the Rings rings
ringsprite = pygame.image.load(os.path.join("niema", "ring.png")).convert_alpha()
ringsprite = pygame.transform.scale(ringsprite, (15, 15))
#Boba Drinks
bobasprite = pygame.image.load(os.path.join("niema", "boba.png")).convert_alpha()
bobasprite = pygame.transform.scale(bobasprite, (25, 25))


#Classes - Blueprint of an object
  #Object is code representation of a real life thing
#Classes == Factories
  #Class(dog) -> can make lots of dogs on a whim
    #Just call for the dog richard = dog
from time import sleep, time

from home import homescreen
#From the home.py module import homescreen function
from curt import curt, c_walls, c10points, c50points

from gary import gary, g_walls, g10points, g50points

from niema import niema, n_walls, n10points, n50points

from lose_page import lose_page

from win_page import win_page

from directory import directory

from secret import secret, m_walls

clock = pygame.time.Clock()
#This helps the program keep track of time

running = True

FPS = 120

in_home = True

state = "home"

loaded = False

direction = "stop"

#First zero = direction
#Second zero = steps
younus_variable = [0,0]

belt_variable = [0,0]

niema_enemy_variable = [younus_variable,belt_variable]

akshat_variable = [0,0]

diego_variable = [0,0]

clock_variable = [0,0]

gary_enemy_variable = [akshat_variable, diego_variable, clock_variable]

hannah_variable = [0,0]

josh_variable = [0,0]

michael_variable = [0,0]

jonny_variable = [0,0]

curt_enemy_variable = [hannah_variable, josh_variable, michael_variable, jonny_variable]

while running:

  clock.tick(FPS)

  if state == "home":
    #Want some way to keep track of what page you are in -> dont want to be in the menu anymore if don't need it

    #Curt's point lists
    star_list = c10points(screen_length,screen_height, dim_field, screen, player_rect)

    hat_list = c50points(screen_length,screen_height, dim_field, screen, player_rect)

    #Gary's point lists
    cork_list = g10points(screen_length,screen_height, dim_field, screen, player_rect)

    wine_list = g50points(screen_length,screen_height, dim_field, screen, player_rect)

    #Niema's point lists
    ring_list = n10points(screen_length,screen_height, dim_field, screen, player_rect)

    boba_list = n50points(screen_length,screen_height, dim_field, screen, player_rect)

    #Niema's enemy list
    niema_enemy = [younus_rect, belt_rect]

    #Gary's enemy list
    gary_enemy = [diego_rect, aclock_rect, akshat_rect]

    #Curt's enemy list
    curt_enemy = [hannah_rect, michael_rect, jonny_rect, josh_rect]

    num_points = 0

    num_lives = 3

    #Curt's starting point:
    player_rect.left = player_x
    player_rect.top = player_y
    #Hannah's starting point:
    hannah_rect.left = hannah_x
    hannah_rect.top = hannah_y
    #Jonny's starting point:
    jonny_rect.left = jonny_x
    jonny_rect.top = jonny_y
    #Michael's starting point:
    michael_rect.left = michael_x
    michael_rect.top = michael_y
    #Josh's starting point:
    josh_rect.left = josh_x
    josh_rect.top = josh_y
    #Gary's starting point:
    gplayer_rect.left = gplayer_x
    gplayer_rect.top = gplayer_y
    #Diego's starting point:
    diego_rect.left = diego_x
    diego_rect.top = diego_y
    #Akshat's starting point:
    akshat_rect.left = akshat_x
    akshat_rect.top = akshat_y
    #Clock's starting point:
    aclock_rect.left = aclock_x
    aclock_rect.top = aclock_y
    #Niema's starting point:
    nplayer_rect.left = nplayer_x
    nplayer_rect.top = nplayer_y
    #Younus' starting point:
    younus_rect.left = younus_x
    younus_rect.top = younus_y
    #Belt's starting point:
    belt_rect.left = belt_x
    belt_rect.top = belt_y
    direction = "none"

    #Counter before player death
    counter = 0

    page = homescreen(screen_length,screen_height, dim_field, screen, player_rect)
    
    state = page

  elif page == "curt":
    #Calling Curt's screen
    curt(screen_length,screen_height, dim_field, screen, player_rect, num_points, num_lives)
    #Calling Curt's walls
    curt_walls = c_walls(screen_length,screen_height, dim_field, screen, player_rect)

    #Curt's sprites
    bye_star = player_rect.collidelist(star_list)
    if bye_star != -1:
      star_list.remove(star_list[bye_star])
      num_points += 10
    for star in star_list:
      screen.blit(starsprite, star)
    bye_hat = player_rect.collidelist(hat_list)
    if bye_hat != -1:
      hat_list.remove(hat_list[bye_hat])
      num_points += 50
    for hat in hat_list:
      screen.blit(hatsprite, hat)
    if num_points == 1150:
      page = "win"

    bye_lives = player_rect.collidelist(curt_enemy)
    if bye_lives != -1 and counter < 1:
      num_lives -= 1
      counter = 100
      if num_lives == 1:
        player_rect.left = player_x
        player_rect.top = player_y
      if num_lives == 2:
        player_rect.left = player_x
        player_rect.top = player_y
    elif counter > 0:
      counter -= 1
    if num_lives == 0:
      page = "lose"
      
    screen.blit(player, player_rect)
    screen.blit(hannah, hannah_rect)
    screen.blit(jonny, jonny_rect)
    screen.blit(josh, josh_rect)
    screen.blit(michael, michael_rect)
      #Draw the player here to continuously draw it as its moving over the frames
    #Curt's player's movement
    if direction == "left":
      player_rect.move_ip(-2, 0)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(2,0)
    elif direction == "right":
      player_rect.move_ip(2, 0)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(-2,0)
    elif direction == "up":
      player_rect.move_ip(0, -2)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(0, 2)
    elif direction == "down":
      player_rect.move_ip(0, 2)
      if player_rect.collidelist(curt_walls) != -1:
        player_rect.move_ip(0, -2)
    else:
      pass
      
    #Curt Enemy movement
    for enemy in range(len(curt_enemy_variable)):
      curt_enemy_variable[enemy][0] #Direction
      curt_enemy_variable[enemy][1] #Steps/Distance
      
      if curt_enemy_variable[enemy][1] <= 0:
        curt_enemy_variable[enemy][0] = random.randint(0, 3)
        curt_enemy_variable[enemy][1] = 120
      if curt_enemy_variable[enemy][0] == 0:
        curt_enemy[enemy].move_ip(-2,0) #Left
        curt_enemy_variable[enemy][1] -= 2
        if curt_enemy[enemy].collidelist(curt_walls) > -1:
          curt_enemy[enemy].move_ip(2,0)
          curt_enemy_variable[enemy][0] = random.randint(0, 3)
          curt_enemy_variable[enemy][1] = 60
      elif curt_enemy_variable[enemy][0] == 1:
        curt_enemy[enemy].move_ip(2,0) #Right
        curt_enemy_variable[enemy][1] -= 2
        if curt_enemy[enemy].collidelist(curt_walls) > -1:
          curt_enemy[enemy].move_ip(-2,0)
          curt_enemy_variable[enemy][0] = random.randint(0, 3)
          curt_enemy_variable[enemy][1] = 60
      elif curt_enemy_variable[enemy][0] == 2:
        curt_enemy[enemy].move_ip(0,-2) #Up
        curt_enemy_variable[enemy][1] -= 2
        if curt_enemy[enemy].collidelist(curt_walls) > -1:
          curt_enemy[enemy].move_ip(0,2)
          curt_enemy_variable[enemy][0] = random.randint(0, 3)
          curt_enemy_variable[enemy][1] = 60
      elif curt_enemy_variable[enemy][0] == 3:
        curt_enemy[enemy].move_ip(0,2) #Down
        curt_enemy_variable[enemy][1] -= 2
        if curt_enemy[enemy].collidelist(curt_walls) > -1:
          curt_enemy[enemy].move_ip(0,-2)
          curt_enemy_variable[enemy][0] = random.randint(0, 3)
          curt_enemy_variable[enemy][1] = 60
          
      #Curt enemy boundaries
      if curt_enemy[enemy].left < 0:
        curt_enemy[enemy].left = 0
      if curt_enemy[enemy].right > screen_length:
        curt_enemy[enemy].right = screen_length
      if curt_enemy[enemy].bottom > 340:
        curt_enemy[enemy].bottom = 340
      if curt_enemy[enemy].top < 30:
        curt_enemy[enemy].top = 30
        
  elif page == "gary":
    #Gary's screen is called
    gary(screen_length,screen_height, dim_field, screen, gplayer_rect, num_points, num_lives)
    
    #Walls get set up
    gary_walls = g_walls(screen_length,screen_height, dim_field, screen, gplayer_rect)

    #Gary's points
    bye_cork = gplayer_rect.collidelist(cork_list)
    if bye_cork != -1:
      cork_list.remove(cork_list[bye_cork])
      num_points += 10
    for cork in cork_list:
      screen.blit(corksprite, cork)
    bye_wine = gplayer_rect.collidelist(wine_list)
    if bye_wine != -1:
      wine_list.remove(wine_list[bye_wine])
      num_points += 50
    for wine in wine_list:
      screen.blit(winesprite, wine)
    bye_wine2 = gplayer_rect.collidelist(wine_list)
    if bye_wine2 != -1:
      wine_list.remove(wine_list[bye_wine2])
      num_points += 50
    for wine in wine_list:
      screen.blit(winesprite2, wine)
    if num_points == 800:
      page = "win"

    #Gary's lives
    bye_lives = gplayer_rect.collidelist(gary_enemy)
    if bye_lives != -1 and counter < 1:
      num_lives -= 1
      counter = 100
      if num_lives == 1:
        gplayer_rect.left = gplayer_x
        gplayer_rect.top = gplayer_y
      if num_lives == 2:
        gplayer_rect.left = gplayer_x
        gplayer_rect.top = gplayer_y
    elif counter > 0:
      counter -= 1
    if num_lives == 0:
      page = "lose"

    #Blitting all of Gary's sprites
    screen.blit(gplayer, gplayer_rect)
    screen.blit(diego, diego_rect)
    screen.blit(aclock, aclock_rect)
    screen.blit(akshat, akshat_rect)

    #Gary's movement
    if direction == "left":
      gplayer_rect.move_ip(-1, 0)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(1,0)
    elif direction == "right":
      gplayer_rect.move_ip(1, 0)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(-1,0)
    elif direction == "up":
      gplayer_rect.move_ip(0, -1)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(0, 1)
    elif direction == "down":
      gplayer_rect.move_ip(0,1)
      if gplayer_rect.collidelist(gary_walls) != -1:
        gplayer_rect.move_ip(0, -1)
    else:
      pass

    #Gary Enemy movement
    for enemy in range(len(gary_enemy_variable)):
      gary_enemy_variable[enemy][0] #Direction
      gary_enemy_variable[enemy][1] #Steps/Distance
      
      if gary_enemy_variable[enemy][1] <= 0:
        gary_enemy_variable[enemy][0] = random.randint(0, 3)
        gary_enemy_variable[enemy][1] = 60
      if gary_enemy_variable[enemy][0] == 0:
        gary_enemy[enemy].move_ip(-1,0) #Left
        gary_enemy_variable[enemy][1] -= 2
        if gary_enemy[enemy].collidelist(gary_walls) > -1:
          gary_enemy[enemy].move_ip(1,0)
          gary_enemy_variable[enemy][0] = random.randint(0, 3)
          gary_enemy_variable[enemy][1] = 60
      elif gary_enemy_variable[enemy][0] == 1:
        gary_enemy[enemy].move_ip(1,0) #Right
        gary_enemy_variable[enemy][1] -= 2
        if gary_enemy[enemy].collidelist(gary_walls) > -1:
          gary_enemy[enemy].move_ip(-1,0)
          gary_enemy_variable[enemy][0] = random.randint(0, 3)
          gary_enemy_variable[enemy][1] = 60
      elif gary_enemy_variable[enemy][0] == 2:
        gary_enemy[enemy].move_ip(0,-1) #Up
        gary_enemy_variable[enemy][1] -= 2
        if gary_enemy[enemy].collidelist(gary_walls) > -1:
          gary_enemy[enemy].move_ip(0,1)
          gary_enemy_variable[enemy][0] = random.randint(0, 3)
          gary_enemy_variable[enemy][1] = 60
      elif gary_enemy_variable[enemy][0] == 3:
        gary_enemy[enemy].move_ip(0,1) #Down
        gary_enemy_variable[enemy][1] -= 2
        if gary_enemy[enemy].collidelist(gary_walls) > -1:
          gary_enemy[enemy].move_ip(0,-1)
          gary_enemy_variable[enemy][0] = random.randint(0, 3)
          gary_enemy_variable[enemy][1] = 60

      #Gary enemy boundaries, Shift tab makes it unindent
      if gary_enemy[enemy].left < 0:
        gary_enemy[enemy].left = 0
      if gary_enemy[enemy].right > screen_length:
        gary_enemy[enemy].right = screen_length
      if gary_enemy[enemy].bottom > 340:
        gary_enemy[enemy].bottom = 340
      if gary_enemy[enemy].top < 30:
        gary_enemy[enemy].top = 30

  elif page == "niema":
    #Calling Niema's screen
    niema(screen_length,screen_height, dim_field, screen, nplayer_rect, num_points, num_lives)
    
    #Calling Niema's walls
    niema_walls = n_walls(screen_length,screen_height, dim_field, screen, player_rect)

    #Niema's points
    bye_ring = nplayer_rect.collidelist(ring_list)
    if bye_ring != -1:
      ring_list.remove(ring_list[bye_ring])
      num_points += 10
    for ring in ring_list:
      screen.blit(ringsprite, ring)
    bye_boba = nplayer_rect.collidelist(boba_list)
    if bye_boba != -1:
      boba_list.remove(boba_list[bye_boba])
      num_points += 50
    for boba in boba_list:
      screen.blit(bobasprite, boba)
    if num_points == 650:
      # Pauses at 640 points, but we want them to see how many points they earned
      # started = time()
      # sleep(5)
      # ended = time()
      page = "win"
    
    #Niema's number of lives
    bye_lives = nplayer_rect.collidelist(niema_enemy)
    #Neima's enemies are Younus and a belt
    if bye_lives != -1 and counter < 1:
      # niema_enemy.remove(niema_enemy[bye_lives])
      num_lives -= 1
      counter = 100
      if num_lives == 1:
        nplayer_rect.left = nplayer_x
        nplayer_rect.top = nplayer_y
      if num_lives == 2:
        nplayer_rect.left = nplayer_x
        nplayer_rect.top = nplayer_y
    elif counter > 0:
      counter -= 1
    if num_lives == 0:
      page = "lose"
    
    #Niema's sprites
    screen.blit(nplayer, nplayer_rect)
    screen.blit(younus, younus_rect)
    screen.blit(belt, belt_rect)
    
    #Niema's movement
    if direction == "left":
      nplayer_rect.move_ip(-2, 0)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(2,0)
    elif direction == "right":
      nplayer_rect.move_ip(2, 0)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(-2,0)
    elif direction == "up":
      nplayer_rect.move_ip(0, -2)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(0, 2)
    elif direction == "down":
      nplayer_rect.move_ip(0, 2)
      if nplayer_rect.collidelist(niema_walls) != -1:
        nplayer_rect.move_ip(0, -2)
    else:
      pass

    # print(len(niema_enemy_variable[0]))
    #Niema Enemy movement
    for enemy in range(len(niema_enemy_variable)):
      niema_enemy_variable[enemy][0] #Direction
      niema_enemy_variable[enemy][1] #Steps/Distance
      
      if niema_enemy_variable[enemy][1] <= 0:
        niema_enemy_variable[enemy][0] = random.randint(0, 3)
        niema_enemy_variable[enemy][1] = 60
      if niema_enemy_variable[enemy][0] == 0:
        niema_enemy[enemy].move_ip(-2,0) #Left
        niema_enemy_variable[enemy][1] -= 2
        if niema_enemy[enemy].collidelist(niema_walls) > -1:
          niema_enemy[enemy].move_ip(2,0)
          niema_enemy_variable[enemy][0] = random.randint(0, 3)
          niema_enemy_variable[enemy][1] = 60
      elif niema_enemy_variable[enemy][0] == 1:
        niema_enemy[enemy].move_ip(2,0) #Right
        niema_enemy_variable[enemy][1] -= 2
        if niema_enemy[enemy].collidelist(niema_walls) > -1:
          niema_enemy[enemy].move_ip(-2,0)
          niema_enemy_variable[enemy][0] = random.randint(0, 3)
          niema_enemy_variable[enemy][1] = 60
      elif niema_enemy_variable[enemy][0] == 2:
        niema_enemy[enemy].move_ip(0,-2) #Up
        niema_enemy_variable[enemy][1] -= 2
        if niema_enemy[enemy].collidelist(niema_walls) > -1:
          niema_enemy[enemy].move_ip(0,2)
          niema_enemy_variable[enemy][0] = random.randint(0, 3)
          niema_enemy_variable[enemy][1] = 60
      elif niema_enemy_variable[enemy][0] == 3:
        niema_enemy[enemy].move_ip(0,2) #Down
        niema_enemy_variable[enemy][1] -= 2
        if niema_enemy[enemy].collidelist(niema_walls) > -1:
          niema_enemy[enemy].move_ip(0,-2)
          niema_enemy_variable[enemy][0] = random.randint(0, 3)
          niema_enemy_variable[enemy][1] = 60

      #Niema enemy boundaries, Shift tab makes it unindent
      if niema_enemy[enemy].left < 0:
        niema_enemy[enemy].left = 0
      if niema_enemy[enemy].right > screen_length:
        niema_enemy[enemy].right = screen_length
      if niema_enemy[enemy].bottom > 340:
        niema_enemy[enemy].bottom = 340
      if niema_enemy[enemy].top < 30:
        niema_enemy[enemy].top = 30

  elif page == "directory":
    state = directory(screen_length, screen_height, dim_field, screen)
    if state == "secret":
     page = state
    #Curt's starting point:
    player_rect.left = 115
    player_rect.top = 55
    #Hannah's starting point:
    hannah_rect.left = 115
    hannah_rect.top = 85
    #Jonny's starting point:
    jonny_rect.left = 115
    jonny_rect.top = 115
    #Michael's starting point:
    michael_rect.left = 115
    michael_rect.top = 175
    #Josh's starting point:
    josh_rect.left = 115
    josh_rect.top = 145
    #Gary's starting point:
    gplayer_rect.left = 265
    gplayer_rect.top = 55
    #Diego's starting point:
    diego_rect.left = 265
    diego_rect.top = 85
    #Akshat's starting point:
    akshat_rect.left = 265
    akshat_rect.top = 115
    #John
    john_rect.left = 265
    john_rect.top = 145
    #Younus' starting point:
    younus_rect.left = 265
    younus_rect.top = 175
    #Elisa
    elisa_rect.left = 260
    elisa_rect.top = 205
    #Henry L
    henryl_rect.left = 265
    henryl_rect.top = 237
    #Jenelle
    jenelle_rect.left = 115
    jenelle_rect.top = 205
    #Lindsey
    lindsey_rect.left = 115
    lindsey_rect.top = 235
    #Niema's starting point:
    nplayer_rect.left = 415
    nplayer_rect.top = 55
    #MohanMohan
    mplayer_rect.left = 415
    mplayer_rect.top = 85
    #Tristin
    tristin_rect.left = 415
    tristin_rect.top = 115
    #Prothit
    prothit_rect.left = 415
    prothit_rect.top = 145
    #Henry X
    henryx_rect.left = 415
    henryx_rect.top = 175
    #Nikki
    nikki_rect.left = 415
    nikki_rect.top = 205
    #Yukati
    yukati_rect.left = 415
    yukati_rect.top = 235
    #Blitting
    screen.blit(player, player_rect)
    screen.blit(hannah, hannah_rect)
    screen.blit(jonny, jonny_rect)
    screen.blit(josh, josh_rect)
    screen.blit(michael, michael_rect)
    screen.blit(gplayer, gplayer_rect)
    screen.blit(diego, diego_rect)
    screen.blit(akshat, akshat_rect)
    screen.blit(nplayer, nplayer_rect)
    screen.blit(younus, younus_rect)
    screen.blit(elisa, elisa_rect)
    screen.blit(henryl, henryl_rect)
    screen.blit(henryx, henryx_rect)
    screen.blit(jenelle, jenelle_rect)
    screen.blit(lindsey, lindsey_rect)
    screen.blit(tristin, tristin_rect)
    screen.blit(prothit, prothit_rect)
    screen.blit(nikki, nikki_rect)
    screen.blit(yukati, yukati_rect)
    screen.blit(mplayer, mplayer_rect)
    screen.blit(john, john_rect)

    #Need to figure out if possible to update x and y coordinates for rectangle
  elif page == "secret":
    state = secret(screen_length,screen_height, dim_field, screen,mplayer_rect)
    #Mohan's walls
    m_walls(screen_length,screen_height, dim_field, screen,mplayer_rect)
    #Curt's starting point:
    player_rect.left = 115
    player_rect.top = 55
    #Hannah's starting point:
    hannah_rect.left = 115
    hannah_rect.top = 85
    #Jonny's starting point:
    jonny_rect.left = 115
    jonny_rect.top = 115
    #Michael's starting point:
    michael_rect.left = 115
    michael_rect.top = 175
    #Josh's starting point:
    josh_rect.left = 115
    josh_rect.top = 145
    #Gary's starting point:
    gplayer_rect.left = 265
    gplayer_rect.top = 55
    #Diego's starting point:
    diego_rect.left = 265
    diego_rect.top = 85
    #Akshat's starting point:
    akshat_rect.left = 265
    akshat_rect.top = 115
    #John
    john_rect.left = 265
    john_rect.top = 145
    #Younus' starting point:
    younus_rect.left = 265
    younus_rect.top = 175
    #Elisa
    elisa_rect.left = 260
    elisa_rect.top = 205
    #Henry L
    henryl_rect.left = 265
    henryl_rect.top = 237
    #Jenelle
    jenelle_rect.left = 115
    jenelle_rect.top = 205
    #Lindsey
    lindsey_rect.left = 115
    lindsey_rect.top = 235
    #Niema's starting point:
    nplayer_rect.left = 415
    nplayer_rect.top = 55
    #Mohan
    mplayer_rect.left = 415
    mplayer_rect.top = 85
    #Tristin
    tristin_rect.left = 415
    tristin_rect.top = 115
    #Prothit
    prothit_rect.left = 415
    prothit_rect.top = 145
    #Henry X
    henryx_rect.left = 415
    henryx_rect.top = 175
    #Nikki
    nikki_rect.left = 415
    nikki_rect.top = 205
    #Yukati
    yukati_rect.left = 415
    yukati_rect.top = 235
    #Blitting
    screen.blit(player, player_rect)
    screen.blit(hannah, hannah_rect)
    screen.blit(jonny, jonny_rect)
    screen.blit(josh, josh_rect)
    screen.blit(michael, michael_rect)
    screen.blit(gplayer, gplayer_rect)
    screen.blit(diego, diego_rect)
    screen.blit(akshat, akshat_rect)
    screen.blit(nplayer, nplayer_rect)
    screen.blit(younus, younus_rect)
    screen.blit(elisa, elisa_rect)
    screen.blit(henryl, henryl_rect)
    screen.blit(henryx, henryx_rect)
    screen.blit(jenelle, jenelle_rect)
    screen.blit(lindsey, lindsey_rect)
    screen.blit(tristin, tristin_rect)
    screen.blit(prothit, prothit_rect)
    screen.blit(nikki, nikki_rect)
    screen.blit(yukati, yukati_rect)
    screen.blit(mplayer, mplayer_rect)
    screen.blit(john, john_rect)

  elif page == "win":
  #win/lose page is called
    state = win_page(screen_length,screen_height, dim_field, screen, player_rect)

  elif page == "lose":
    state = lose_page(screen_length,screen_height, dim_field, screen, player_rect)

    #It's not calling the functions again/reseting the lives and the points

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN: 

      if event.key == pygame.K_q:

        running = False

      #Directions, help know what left, right, up and down is, used earlier in loop
      if event.key == pygame.K_LEFT:
        direction = "left"
      if event.key == pygame.K_RIGHT:
        direction = "right"
      if event.key == pygame.K_UP:
        direction = "up"
      if event.key == pygame.K_DOWN:
        direction = "down"

  pygame.display.update()