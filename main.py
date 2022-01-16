import pygame
from pygame import mixer
from world import World
from settings import *
from assets import assets
from game_map import level1_map

#Initialise game clock, game screen and create World Instance
pygame.init()
mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(window_name)

# Load game music, set volume and play
mixer.music.load(assets["bg_music"])
mixer.music.set_volume(0.5)
mixer.music.play()

world = World(level1_map, screen)

run = True
while run:

	clock.tick(fps)

    #draws world and implements all game logic in here!!!
	world.draw()

    #quit game upon clicking X
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()