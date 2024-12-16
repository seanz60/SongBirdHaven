import pygame as pg
import math
import constants as c
import random

class GameBird(pg.sprite.Sprite):
	def __init__(self, sprite_sheet):
		pg.sprite.Sprite.__init__(self)
		self.x = random.randint(100, 1500)
		self.y = random.randint(75, 500)
		self.animation_list = self.load_images(sprite_sheet)
		self.frame_index = 0
		self.update_time = pg.time.get_ticks()
		self.speed = random.randint(2, 15)

		#update self
		self.original_image = self.animation_list[self.frame_index]
		self.angle = 0
		self.image = pg.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

	def load_images(self, sprite_sheet):
		size = 50
		animation_list = []
		for x in range(c.ANIMATION_STEPS):
			temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
			animation_list.append(temp_img)
		return animation_list

	def update(self, stage):
		if (stage > 40):
			self.speed = 20
			self.y = 75
		self.move()
		self.play_animation()
		if (self.x <= 0):
			self.x = c.SCREEN_WIDTH
			if (stage < 40):
				self.y = random.randint(75, 500)

	def play_animation(self):
		self.original_image = self.animation_list[self.frame_index]
		if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
			self.update_time = pg.time.get_ticks()
			self.frame_index += 1
			if self.frame_index >= len(self.animation_list):
				self.frame_index = 0

	def draw(self, surface):
		self.image = pg.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		surface.blit(self.image, self.rect)

	def move(self):
		self.x -= self.speed
