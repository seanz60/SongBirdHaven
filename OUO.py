import pygame as pg
import constants as c
import time
from bird import Bird
from button import Button
from game_bird import GameBird
from bread import Bread
from ending_bird import EndBird

#initialize game
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption(":)")

#game variables
stage = 0
click_for_next = False
black_stop = False
last_click = 0
cont = True;
back_bird_made = False
make_game_bird = 30
book_found = False
bird_touched = False
birdy_birdy = False
bread_dropped = False
orphanage_time = False
ended = False

#load images
door = pg.image.load('door.png').convert_alpha()
skateboard = pg.image.load('skateboard.png').convert_alpha()
entrance_left = pg.image.load('entrance_left.png').convert_alpha()
entrance_right = pg.image.load('entrance_right.png').convert_alpha()
flying_bird_sheet = pg.image.load('flying_bird_sprite_sheet.png').convert_alpha()
guide = pg.image.load('guide.png').convert_alpha()
sad_face = pg.image.load('sad_face.png').convert_alpha()
park_left = pg.image.load('park_left.png').convert_alpha()
park_right =pg.image.load('park_right.png').convert_alpha()
bread_image = pg.image.load('bread.png').convert_alpha()
town_image_one = pg.image.load('town1.png').convert_alpha()
town_image_two = pg.image.load('town2.png').convert_alpha()
orphanage = pg.image.load('orphanage.png').convert_alpha()
right_arrow = pg.image.load('right.png').convert_alpha()
left_arrow = pg.image.load('left.png').convert_alpha()
book = pg.image.load('book.png').convert_alpha()
back_john = pg.image.load('back_john.png').convert_alpha()
front_john = pg.image.load('front_john.png').convert_alpha()
face_john = pg.image.load('john_face.png').convert_alpha()
big_bird = pg.image.load('dad_bird.png').convert_alpha()
small_bird = pg.image.load('son_bird.png').convert_alpha()

#buttons
lost_skateboard = pg.image.load('skateboard_button.png').convert_alpha()

#load fonts for displaying text
text_font = pg.font.SysFont("Consolas", 24, bold = True)
large_font = pg.font.SysFont("Consolas", 36)

#function for drawing text on screen
def draw_text(text, font, text_col, x , y):
	if (click_for_next == False or stage == 0):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))

def create_bird():
	new_bird = GameBird(flying_bird_sheet)
	bird_group.add(new_bird)

def create_bread():
	new_bread = Bread(bread_image, 700, 650)
	bread_group.add(new_bread)

def create_endbird(sheet, x, y, dad):
	new_ebird = EndBird(sheet, x, y, dad)
	ebird_group.add(new_ebird)


#create button
skateboard_button = Button(1340, 700, lost_skateboard)
bread_button = Button(650, 650, bread_image)
right_button = Button(1350, 325, right_arrow)
left_button = Button(50, 325, left_arrow)
book_button = Button(800, 500, book)
john_button = Button(700, 500, back_john)

#create groups
bird_group = pg.sprite.Group()
bread_group = pg.sprite.Group()
ebird_group = pg.sprite.Group()

#game loop
run = True
while run:

	clock.tick(c.FPS)
	###########################################################
	# UPDATING SECT
	###########################################################

	bird_group.update(stage)
	bread_group.update(bird_group)
	ebird_group.update(ebird_group)

	###########################################################
	# DRAWING SECT
	###########################################################
	screen.fill("black")
	#print(stage)


	if (stage == 0):
		click_for_next = True
		draw_text("CLICK TO START", large_font, "white", 600, 350)
	
	if (stage == 1):
		draw_text("Please Dad", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 2):
		draw_text("Let's move to Songbird Haven", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 3):
		draw_text("Songbird Haven is perfect", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 4):
		draw_text("Songbird Haven is paradise", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 5):
		draw_text("ABSOLUTELY NOT", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 6):
		if (pg.time.get_ticks() - last_click > 4000):
			click_for_next = True
		else:
			screen.blit(door, (575, 150))

	if (stage == 7):
		if (pg.time.get_ticks() - last_click > 4000):
			click_for_next = True
		else:
			screen.blit(skateboard, (375, 150))

	if (stage == 8):
		if (pg.time.get_ticks() - last_click > 4000):
			stage = stage + 1
			last_click = pg.time.get_ticks()
		
	if (stage == 9):
		draw_text("Johnathan?", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 10):
		draw_text("I must find him...", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 11 or stage == 12):
		screen.blit(entrance_left, (0,0))
		screen.blit(entrance_right, (750, 0))
		if (back_bird_made == False):
			back_bird_made = True
			back_bird = Bird(flying_bird_sheet, 1500, 50)
		back_bird.update()
		back_bird.draw(screen)
		if (pg.time.get_ticks() - last_click > 1500 and stage == 11):
			click_for_next = True

	if (stage == 12):
		screen.blit(guide, (800, 275))
		if (pg.time.get_ticks() - last_click > 1500):
			click_for_next = True

	if (stage == 13):
		draw_text("Hello Stranger!", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 14):
		draw_text("Are you here to stay?", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 15):
		draw_text("No, I am looking for my son", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 16):
		if (pg.time.get_ticks() - last_click < 500):
			screen.blit(sad_face, (300, 0))
		if (pg.time.get_ticks() - last_click > 500):
			draw_text("Well that's a shame", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2500):
			click_for_next = True 

	if (stage == 17):
		draw_text("I will help you look", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 18):
		draw_text("But please consider staying", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 19):
		draw_text("Songbird Haven is perfect", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True

	if (stage == 20):
		draw_text("Songbird Haven is paradise", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			click_for_next = True
	
	if (stage == 21):
		screen.blit(park_left, (0,0))
		screen.blit(park_right, (600, 0))
		if skateboard_button.draw(screen) and stage == 24:
			stage = stage + 1
		if (pg.time.get_ticks() - last_click > 3000):
			click_for_next = True

	if (stage == 22):
		draw_text("This is our park", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 23):
		draw_text("Do you see your son?", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 24):
		screen.blit(park_left, (0,0))
		screen.blit(park_right, (600, 0))
		if skateboard_button.draw(screen) and stage == 24:
			stage = stage + 1
			last_click = pg.time.get_ticks()

	if (stage == 25):
		draw_text("John's skateboard...", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 26):
		draw_text("He was here!", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 27):
		draw_text("That means he is safe", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True 

	if (stage == 28):
		draw_text("No it doesn't", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 29):
		draw_text("Not until I find him", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 30):
		if (pg.time.get_ticks() - last_click < 500):
			screen.blit(sad_face, (300, 0))
		if (pg.time.get_ticks() - last_click > 500):
			draw_text("The bird feeding man is missing", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2500):
			click_for_next = True 

	if (stage == 31):
		draw_text("Please feed the birds first", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 32):
		draw_text("I will lead you to the houses after", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 33):
		screen.blit(park_left, (0,0))
		screen.blit(park_right, (600, 0))
		for bird in bird_group:
			bird.draw(screen)
		for bread in bread_group:
			bread.draw(screen)
		if (make_game_bird > 0):
			create_bird()
			make_game_bird -= 1
		if skateboard_button.draw(screen) and stage == 24:
			stage = stage + 1
			last_click = pg.time.get_ticks()
		if bread_button.draw(screen) and (pg.time.get_ticks() - last_click > 1000):
			create_bread()
			last_click = pg.time.get_ticks()
		if len(bird_group.sprites()) == 0:
			stage += 1
			bird_group.empty()
			bread_group.empty()
			last_click = pg.time.get_ticks()

	if (stage == 34):
		draw_text("Great job!", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 35):
		draw_text("Now isn't Songbird Haven just fun?", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 36):
		draw_text("Enough talking", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 37):
		draw_text("Take me to the houses", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 38):
		screen.blit(town_image_one, (0, 0))
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 39):
		draw_text("Isn't the view nice?", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 40):
		draw_text("Shut up", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 41):
		screen.blit(town_image_one, (0, 0))
		for bird in bird_group:
			bird.draw(screen)
		for bread in bread_group:
			bread.draw(screen)
		if (book_found and bird_touched == False and birdy_birdy == False):
			create_bird()
			birdy_birdy = True
		if (bird_touched):
			if (bread_dropped == False):
				if (bread_button.draw(screen)):
					bread_dropped = True
					create_bread()
					last_click = pg.time.get_ticks()
		if (len(bird_group.sprites()) == 0):
			if (birdy_birdy):
				bird_touched = True
			if (right_button.draw(screen) and pg.time.get_ticks() - last_click > 1500):
				stage += 1
				last_click = pg.time.get_ticks()
		if (pg.time.get_ticks() - last_click > 250 and bread_dropped and orphanage_time == False):
			stage = 47

	if (stage == 42):
		screen.blit(town_image_two, (0, 0))
		if (book_button.draw(screen) and pg.time.get_ticks() - last_click > 1000 and book_found == False):
			last_click = pg.time.get_ticks()
			stage += 2
		if (len(bird_group.sprites()) == 0):
			if (left_button.draw(screen) and pg.time.get_ticks() - last_click > 1500):
				stage -= 1
				last_click = pg.time.get_ticks()

	if (stage == 43):
		if (pg.time.get_ticks() - last_click < 500):
			screen.blit(sad_face, (300, 0))
		if (pg.time.get_ticks() - last_click > 500):
			draw_text("No one is allowed into the Orphanage", large_font, "white", 350, 350)
		if (pg.time.get_ticks() - last_click > 2500):
			stage -= 1
			last_click = pg.time.get_ticks()

	if (stage == 44):
		draw_text("That's Johnathan's diary", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 45):
		draw_text("This guy isn't helping me", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 46):
		draw_text("I must shake him off", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 3000):
			book_found = True
			stage = 42

	if (stage == 47):
		draw_text("The Bread!", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 48):
		draw_text("You stay right here", large_font, "white", 600, 350)
		if (pg.time.get_ticks() - last_click > 2500):
			stage = 41
			orphanage_time = True
			last_click = pg.time.get_ticks()

	if (stage == 49):
		screen.blit(orphanage, (0,0))
		if (john_button.draw(screen) and pg.time.get_ticks() - last_click > 2500):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 50):
		draw_text("Johnathan?", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			click_for_next = True

	if (stage == 51):
		if (pg.time.get_ticks() - last_click < 1000):
			draw_text("They tormented me", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 2000):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 52):
		if (pg.time.get_ticks() - last_click < 950):
			draw_text("I was alone", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1900):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 53):
		if (pg.time.get_ticks() - last_click < 900):
			draw_text("But I at least had you", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1800):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 54):
		if (pg.time.get_ticks() - last_click < 850):
			draw_text("But I thought wrong", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1700):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 55):
		if (pg.time.get_ticks() - last_click < 800):
			draw_text("Nobody listened", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1600):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 56):
		if (pg.time.get_ticks() - last_click < 750):
			draw_text("You didn't listen", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1500):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 57):
		if (pg.time.get_ticks() - last_click < 700):
			draw_text("Johnathan...", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1400):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 58):
		if (pg.time.get_ticks() - last_click < 650):
			draw_text("We will work this out okay?", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1300):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 59):
		if (pg.time.get_ticks() - last_click < 600):
			draw_text("Let's go back home first", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 1200):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 60):
		if (pg.time.get_ticks() - last_click < 550):
			draw_text("But I am home", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1100):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 61):
		if (pg.time.get_ticks() - last_click < 500):
			draw_text("We are home", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 1000):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 62):
		if (pg.time.get_ticks() - last_click < 450):
			draw_text("Don't leave Dad", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 900):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 63):
		if (pg.time.get_ticks() - last_click < 400):
			draw_text("We are home", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 800):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 64):
		if (pg.time.get_ticks() - last_click < 350):
			draw_text("This is home", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 700):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 65):
		if (pg.time.get_ticks() - last_click < 300):
			draw_text("This is paradise", large_font, "yellow", 600, 350)
		if (pg.time.get_ticks() - last_click > 600):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 66):
		if (pg.time.get_ticks() - last_click < 2000):
			draw_text("JOHNATHAN STOP IT", large_font, "blue", 600, 350)
		if (pg.time.get_ticks() - last_click > 2500):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 67):
		if (pg.time.get_ticks() - last_click < 2000):
			screen.blit(orphanage, (0,0))
			if (john_button.draw(screen) and stage == 11214121):
				last_click = pg.time.get_ticks()
		if (pg.time.get_ticks() - last_click > 2000):
			screen.blit(orphanage, (0,0))
			screen.blit(front_john,(700, 500))
		if (pg.time.get_ticks() - last_click > 2500):
			last_click = pg.time.get_ticks()
			stage += 1
	
	if (stage == 68):
		if (pg.time.get_ticks() - last_click < 2000):
			draw_text("Songbird Haven is perfect", large_font, "red", 600, 350)
		if (pg.time.get_ticks() - last_click > 3500):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 69):
		if (pg.time.get_ticks() - last_click < 2000):
			draw_text("Songbird Haven is paradise", large_font, "red", 600, 350)
		if (pg.time.get_ticks() - last_click > 3500):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 70):
		if (pg.time.get_ticks() - last_click < 5000):
			screen.blit(face_john, (300, 100))
		if (pg.time.get_ticks() - last_click > 10000):
			last_click = pg.time.get_ticks()
			stage += 1

	if (stage == 71):
		screen.fill("black")
		for ebird in ebird_group:
			ebird.draw(screen)
		if (ended == False):
			create_endbird(big_bird, 500, 250, True)
			create_endbird(small_bird, 1000, 450, False)
			ended = True

	#event handler
	for event in pg.event.get():
		#quit program
		if event.type == pg.QUIT:
			run = False
		#mouse click
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			mouse_pos = pg.mouse.get_pos()
			if (click_for_next):
				stage = stage + 1
				click_for_next = False
				last_click = pg.time.get_ticks()
			if (stage == 41):
				for bird in bird_group:
					if (abs(bird.x - mouse_pos[0]) < 50 and abs(bird.y - mouse_pos[1]) < 50):
						bird.kill()
			if (stage == 42 and mouse_pos[0] > 700 and mouse_pos[0] < 1400 and mouse_pos[1] > 0 and mouse_pos[1] < 400 and pg.time.get_ticks() - last_click > 1000):
				if (orphanage_time):
					stage = 49
				else:
					stage = stage + 1
					last_click = pg.time.get_ticks()
	#update display
	pg.display.flip()

pg.quit()

