import pygame as pg
import constants as c
import math

class Bread(pg.sprite.Sprite):
	def __init__(self, image, x, y):
		pg.sprite.Sprite.__init__(self)
		self.image = image
		self.x = x
		self.y = y 
		self.speed = 6
		self.angle = 0
		self.image = pg.transform.rotate(self.image, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

	def update(self, bird_group):
		self.move()
		if (self.y > c.SCREEN_HEIGHT):
			self.kill()
		for bird in bird_group:
			if (abs(bird.x - self.x) < 50 and abs(bird.y - self.y) < 50):
				bird.kill()
				self.kill()

	def move(self):
		self.y -= 10

	def draw(self, surface):
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		surface.blit(self.image, self.rect)
