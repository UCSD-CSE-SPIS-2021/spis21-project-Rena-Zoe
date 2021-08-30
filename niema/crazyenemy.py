    for enemy in niema_enemy:
      enemy_move = random.randint(0, 4)
      enemy_vertical = random.randint(1, 320)
      enemy_horizontal = random.randint(1, 465)
      if enemy_move == 0:
        enemy.move_ip(-(enemy_horizontal), 0)
        if enemy.collidelist(niema_walls) != -1:
          enemy.move_ip(enemy_horizontal,0)
      elif enemy_move == 1:
        enemy.move_ip(enemy_horizontal, 0)
        if enemy.collidelist(niema_walls) != -1:
          enemy.move_ip(-(enemy_horizontal),0)
      elif enemy_move == 2:
        enemy.move_ip(0, -(enemy_vertical))
        if enemy.collidelist(niema_walls) != -1:
          enemy.move_ip(0, enemy_vertical)
      elif enemy_move == 3:
        enemy.move_ip(0, enemy_vertical)
        if enemy.collidelist(niema_walls) != -1:
          enemy.move_ip(0, -(enemy_vertical))