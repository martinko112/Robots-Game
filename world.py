import pygame
import time
from pygame import mixer
from settings import *
from assets import assets
from player import Player
from sprite_definitions.coin import Coin
from sprite_definitions.lava import Lava
from sprite_definitions.enemy import Enemy

class World():
	def __init__(self, level, screen):
		self.tile_list = []
		self.coins = pygame.sprite.Group()
		self.lava_blocks = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()

		#load images
		self.block = pygame.image.load(assets["block"])
		self.coin = pygame.image.load(assets["coin"])
		self.background_img = pygame.image.load(assets["background"])

		#Setup fonts and colors to display text
		self.black = (0, 0, 0)
		self.white = (255, 255, 255)
		self.font = pygame.font.Font('freesansbold.ttf', 32)
		self.current_time = time.time()
		self.target_time = self.current_time + 3

		self.dead_message = self.font.render(f'Zomrel si! Reštartujem hru...', True, self.black, self.white)
		self.deadMessageRect = self.dead_message.get_rect()
		self.deadMessageRect.center = (screen_width/2, screen_height/2)
		self.game_over = False

		self.victory_message = self.font.render(f'Hurá! Pozbieral si všetky mince!', True, self.black, self.white)
		self.victoryMessageRect = self.victory_message.get_rect()
		self.victoryMessageRect.center = (screen_width/2, screen_height/2)
		self.level_complete = False

		self.screen = screen
		self.level = level

		self.score = 0
		self.lvl_coin_count = 0
		self.world_shift = 0

		mixer.init()

		row_count = 0
		for row in level:
			col_count = 0
			for tile in row:
				if tile == "b":
					img = pygame.transform.scale(self.block, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == "c":
					x = col_count * tile_size
					y = row_count * tile_size
					coin = Coin((x, y), 50)
					self.coins.add(coin)
				if tile == "l":
					x = col_count * tile_size
					y = row_count * tile_size
					lava = Lava((x, y), 50)
					self.lava_blocks.add(lava)
				if tile == "p":
					x = col_count * tile_size
					y = row_count * tile_size
					self.player = Player(x, y, self.screen)
				if tile == "2":
					x = col_count * tile_size
					y = row_count * tile_size
					enemy = Enemy((x+10, y-30), (40, 80), 2)
					self.enemies.add(enemy)
				if tile == "3":
					x = col_count * tile_size
					y = row_count * tile_size
					enemy = Enemy((x+10, y-30), (40, 80), 3)
					self.enemies.add(enemy)
				col_count += 1
			row_count += 1

			self.lvl_coin_count = len(self.coins)
	
	def move_cam(self):
		player = self.player
		player_x = player.rect.centerx
		direction_x = player.dx

		if player_x < (screen_width / 4) and direction_x < 0:
			self.world_shift = 5
			player.speed = 0
		elif player_x > ((screen_width/4) * 3) and direction_x > 0:
			self.world_shift = -5
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 5
	
		for tile in self.tile_list:
			tile[1].x += self.world_shift
	
	def check_coin_collision(self):
		collided_coins = pygame.sprite.spritecollide(self.player,self.coins,True)
		if len(collided_coins) > 0:
			self.score += 1
			pygame.mixer.Channel(0).play(pygame.mixer.Sound(assets["collect_coin"]), maxtime=600)

		self.score_text = self.font.render(f'Pozbierané Mince: {self.score}', True, self.black, self.white)
		self.scoreTextRect = self.score_text.get_rect()
		self.scoreTextRect.center = (160, 20)
	
	def check_lava_collision(self):
		collided_lava_blocks = pygame.sprite.spritecollide(self.player, self.lava_blocks, False)
		if len(collided_lava_blocks) > 0:
			self.dead_restart_game()
	
	def check_enemy_collision(self):
		collided_enemies = pygame.sprite.spritecollide(self.player, self.enemies, False)
		if len(collided_enemies) > 0:
			self.dead_restart_game()
	
	def check_level_complete(self):
		if self.score >= self.lvl_coin_count:
			self.level_complete = True
			self.reset_timer(3)
	
	def dead_restart_game(self):
		self.game_over = True
		self.reset_timer(3)
	
	#resets timer for displaying text
	def reset_timer(self, seconds):
		self.current_time = time.time()
		self.target_time = self.current_time + seconds

	# This method is called every game tick
	def draw(self):
		#diplay world
		self.screen.blit(self.background_img, (0, 0))
		for tile in self.tile_list:
			self.screen.blit(tile[0], tile[1])
		
		#move camera and draw coins, lava and enemies
		self.move_cam()
		self.coins.draw(self.screen)
		self.coins.update(self.world_shift)

		self.lava_blocks.draw(self.screen)
		self.lava_blocks.update(self.world_shift)

		self.enemies.draw(self.screen)
		self.enemies.update(self.world_shift)

		#check if coin collected and display score
		self.check_coin_collision()
		self.screen.blit(self.score_text, self.scoreTextRect)

		# Check for level completion (i.e. all coins collected)
		if self.level_complete == False:
			self.check_level_complete()
		
		if self.level_complete == True:
			if self.current_time < self.target_time:
				self.screen.blit(self.victory_message, self.victoryMessageRect)
				self.current_time = time.time()
			else:
				exit()

		# If player is alive and godmode is off, check for dead
		if god_mode == False and self.game_over == False:
			self.check_lava_collision()
			self.check_enemy_collision()

		# Update player, but hide player when game is over
		if self.game_over == False:
			self.player.update(self)

		# Check if player is dead -> If he is then display text (for 3 seconds)
		if self.game_over == True:
			if self.current_time < self.target_time:
				self.screen.blit(self.dead_message, self.deadMessageRect)
				self.current_time = time.time()
			else:
				self.__init__(self.level, self.screen)




