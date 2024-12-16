import pygame as pg
import math
import constants as c
import random

class EndBird(pg.sprite.Sprite):
	def __init__(self, sprite_sheet, x, y, dad):
		pg.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.animation_list = self.load_images(sprite_sheet, dad)
		self.frame_index = 0
		self.update_time = pg.time.get_ticks()
		self.speed = random.randint(2, 15)

		#update self
		self.original_image = self.animation_list[self.frame_index]
		self.angle = 0
		self.image = pg.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		self.delay = random.randint(100, 5000)

	def load_images(self, sprite_sheet, dad):
		size = 125
		if (dad):
			size = 250
		animation_list = []
		for x in range(3):
			temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
			animation_list.append(temp_img)
		if (dad):
			temp_img = animation_list[0]
			animation_list[0] = animation_list[2]
			animation_list[2] = temp_img
		return animation_list

	def update(self, stage):
		self.play_animation()

	def play_animation(self):
		self.original_image = self.animation_list[self.frame_index]
		if (pg.time.get_ticks() - self.update_time > self.delay or self.frame_index > 0):
			if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
				self.update_time = pg.time.get_ticks()
				self.frame_index += 1
				if self.frame_index >= len(self.animation_list):
					self.frame_index = 0
					self.delay = random.randint(100, 5000)

	def draw(self, surface):
		self.image = pg.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		surface.blit(self.image, self.rect)


