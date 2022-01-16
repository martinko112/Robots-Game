import pygame 
from settings import *
from assets import assets
from world import *
import settings

class Player():
	def __init__(self, x, y, screen):
		self.screen = screen
		
		self.player_img = pygame.image.load(assets["player"])
		self.player_img = pygame.transform.scale(self.player_img, (40, 80))
		self.image = self.player_img

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.width = self.image.get_width()
		self.height = self.image.get_height()

		self.vel_y = 0
		self.speed = settings.speed
		self.gravitation = settings.gravitation
		self.jump_height = settings.jump_height
		self.jumped = False
		self.on_ground = False

		# Variables representing vector by which will player move (DX must be global so that the world.move_cam() can access it)
		self.dx = 0
		self.dy = 0

	def update(self, world):
		#Reset directional vectors every tick
		self.dx = 0
		self.dy = 0

		#get input from keyboard and change class variables
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False and self.on_ground == True:
			self.vel_y = -self.jump_height
			self.jumped = True
		if key[pygame.K_SPACE] == False:
			self.jumped = False
		if key[pygame.K_LEFT]:
			self.dx = -1
		if key[pygame.K_RIGHT]:
			self.dx = 1

		#apply gravitation
		self.vel_y += 1
		if self.vel_y > self.gravitation:
			self.vel_y = self.gravitation
		self.dy += self.vel_y

		#check all collisions with tiles
		self.on_ground = False
		for tile in world.tile_list:
			#check for horizontal collisions
			if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
				self.dx = 0
			#check for vertical collisions
			if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
				#check if jumping (touching ceiling)
				if self.vel_y < 0:
					self.dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				#check if falling (touching ground)
				elif self.vel_y >= 0:
					self.dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.on_ground = True

		#update player location by adding vector (X, Y)
		self.rect.x += self.dx * self.speed
		self.rect.y += self.dy 

        #Restrict player to only be able to go to certain height
		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			self.dy = 0

		#draw player on the screen
		self.screen.blit(self.image, self.rect)