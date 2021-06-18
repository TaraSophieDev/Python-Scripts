import cv2
import csv
import os
import colorgram as cg


regular_folder = r"assets\pokemon_sprites\regular"
shiny_folder = r"assets\pokemon_sprites\shiny"


def write_csv(data):
  with open('output\\regular_pokemon_colors.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter='\n')
    writer.writerow(data)
#header = ["pokemon_name", "r1", "g1", "b1", "r2", "g2", "b2", "r3", "g3", "b3", "r4", "g4", "b4", "r5", "g5", "b5" ,"r6", "g6", "b6"]

#colors = cg.extract(r'assets\pokemon_sprites\regular\abra.png', 6)
#print(colors)cle

for r_sprites in os.listdir(regular_folder):
  path = r"assets\pokemon_sprites\regular"
  result = os.path.join(path, r_sprites)
  r_sprite_colors = cg.extract(result, 6)
  print(r_sprite_colors)
  write_csv(r_sprite_colors)

  for index in range(0, len(r_sprite_colors)):
    first_color = r_sprite_colors[index]
    rgb = first_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    #print(r_sprites,"index", index + 1, "r",r, "g", g,"b", b)
    #write_csv(r_sprite_colors)
  #print(r_sprites, r_sprite_colors)


  #print("r" + "'" + regular_folder + r_sprites + "'")

