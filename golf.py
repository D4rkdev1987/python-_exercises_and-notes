import sys 
import pygame, math, random, time
from pygame.locals import *


("""
Minigolf game made by Ben Nicklaus (marineepo@gmail.com)


How to play:
steer the "golf club" with a pointing device, and shoot with any mouse-button.
The strength of the shot is determined by the distance from the club to the ball,
and is also illustrated by the black line (laser pointer ;))
blue areas are water, if you get your balls (hehe) in it, you'll die.
black areas are borders, where the ball will bounce off from.
brown areas are sand, and your ball will be very slowed down.
The black spot is your goal, the hole.
""")


#global grad
grad = math.pi/180

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
test_img = pygame.Surface((30,30)).convert_alpha()
test_rect = test_img.get_rect()

def mapchecker(levelcount,mode='hole'): #used to check which level we're on
	if levelcount == 1:
		if mode == 'hole': return 500,100
		if mode == 'ball': return 140,170
	elif levelcount == 2:
		if mode == 'hole': return 50,50
		if mode == 'ball': return 300,300
	elif levelcount == 3:
		if mode == 'hole': return 200,100
		if mode == 'ball': return 280,400
	elif levelcount == 4:
		if mode == 'hole': return 500,50
		if mode == 'ball': return 400,400
	elif levelcount == 5:
		if mode == 'hole': return 50,500
		if mode == 'ball': return 100,50
	elif levelcount == 6:
		if mode == 'hole': return 0,0
		if mode == 'ball': return 0,0
	elif levelcount == 0:
		return 250,50 #ball isn't needed here, set in the Ball class. (line 54,55)


class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 400 #start-position of the ball
		self.y = 530 
		self.xdir = 0
		self.ydir = 0
		self.stdfriction = 0.996
		self.friction = self.stdfriction
		self.hardfriction = 0.992 #used on sand and when ball is going slow
		self.speed = 1 #the speed of the ball
		self.circle_ = pygame.draw.circle(screen, (5,78,200), (int(self.x), int(self.y)),7) #the actual ball-"image"
		self.image = pygame.Surface((7,7))
		self.image.blit(self.image, self.circle_)

		self.rect = self.image.get_rect()

	def update(self, vinkel, dy, dx,canshoot):
		self.x += self.xdir #increase x, so the ball moves
		self.y += self.ydir
		self.rect = Rect((self.x,self.y),(self.image.get_width(),self.image.get_height()))
		self.speed = self.speed * self.friction #decrease the speed with the friction
		if canshoot == True:
			self.make_trail(vinkel,dy,dx)

	def make_trail(self,vinkel,dy,dx): #make an "arrow" that points towards the balls goal
		self.coolcirk = pygame.draw.aaline(screen,(20,20,20),(dx+self.x,dy+self.y), (self.x+5,self.y+5))

class Klubba(pygame.sprite.Sprite): #the golf club
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.image = pygame.Surface((8,30)).convert_alpha()
		self.image.fill((106,106,106))
		for n in range(10):
			self.image.set_at((n,10),(240,20,20))
		self.rect = self.image.get_rect()
		self.oldimg = self.image

	def update(self, vinkel):
		self.x = pygame.mouse.get_pos()[0]
		self.y = pygame.mouse.get_pos()[1]
		self.image = pygame.transform.rotate(self.oldimg, vinkel)
		self.rect = Rect((self.x,self.y),(self.image.get_width()-4,self.image.get_height()-20))
		


class Hole(pygame.sprite.Sprite):
	def __init__(self):
		self.x = random.randint(1,700)
		self.y = random.randint(1,500)
		self.rect = pygame.draw.circle(screen, (0,0,0), (200,150), 10)

	def update(self, levelcount):
		self.movement = mapchecker(levelcount) #returns a tuple, x = 0, y = 1
		self.rect = pygame.draw.circle(screen, (0,0,0), (self.movement[0], self.movement[1]), 10)


class Maps(pygame.sprite.Sprite):
	def __init__(self):
		self.boxes = []

	def box(self, x, y, width, lenght, mode='default'):
		if mode == 'default': color = (20,0,0)
		elif mode == 'water': color = (50,50,255)
		return pygame.draw.rect(screen, color, Rect((x,y),(width,lenght))),mode

	def circle(self, x, y, radius, mode='sand'):
		return pygame.draw.circle(screen, (194,215,53), (x,y),radius), mode

	def update(self, levelcount): ###define all maps###
		if levelcount == 0:
			self.boxes = []
			self.boxes.append(self.box(100,0,30,600))
			self.boxes.append(self.box(500,0,30,600))
			self.boxes.append(self.box(300,430,220,20))
			self.boxes.append(self.box(300,230,220,20))
			self.boxes.append(self.box(130,330,220,20))

		if levelcount == 1:
			self.boxes = []
			self.boxes.append(self.box(300,400,30,300))
			self.boxes.append(self.box(300,0,30,300))
			self.boxes.append(self.circle(200,300,50))
		if levelcount == 2:
			self.boxes = []
			self.boxes.append(self.box(200,200,90,500,'water'))
			self.boxes.append(self.circle(300,50,55))
			self.boxes.append(self.box(780,0,20,500,'water'))
		if levelcount == 3:
			self.boxes = []
			self.boxes.append(self.box(0,200,400,80,'water'))
			self.boxes.append(self.box(500,200,400,80,'water'))
			self.boxes.append(self.box(485,230,15,40))
			self.boxes.append(self.box(0,180,100,20))
		if levelcount == 4:
			self.boxes = []
			self.boxes.append(self.box(0,200,400,20))
			self.boxes.append(self.box(180,300,600,20))
		if levelcount == 5:
			self.boxes = []
			self.boxes.append(self.box(0,150,400,40,'water'))
			self.boxes.append(self.box(300,300,600,40,'water'))
			self.boxes.append(self.box(0,450,600,40,'water'))
			self.boxes.append(self.circle(160, 480, 50))
		if levelcount == 6:
			self.boxes = []
			self.boxes.append(self.box(0,0,0,0))



def main():
	pygame.init()
	pygame.mouse.set_visible(0)

	#FONT
	pygame.font.init()
	text = pygame.font.SysFont("Times New Roman",20)
	text2 = pygame.font.SysFont("Times New Roman",20)
	
	#variabel inits
	ball = Ball()
	klubba = Klubba()
	hole = Hole()
	maps = Maps()
	canshoot = True
	localhits = 0
	hits = 0
	levelcount = 0
	firstrun = True
	drawhole = True
	gameover = False

	sprite1 = pygame.sprite.RenderPlain((ball))
	sprite2 = pygame.sprite.RenderPlain((klubba))

	while 1:
		klubba.dx = ball.x-klubba.x
		klubba.dy = ball.y-klubba.y

		hypot = math.sqrt(klubba.dx**2 + klubba.dy**2)/50
		vinkel = math.atan2(klubba.dy,klubba.dx) * 180/math.pi
		msg = "hits: %d" % localhits
		msg2 = "level: %d" % levelcount
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_DOWN:
				ball.amount += 0.1
			elif event.type == KEYDOWN and event.key == K_UP:
				ball.amount -= 0.1
			elif event.type == MOUSEBUTTONDOWN and gameover == False:
				if canshoot == True:
					ball.xdir = (math.cos(vinkel * grad) * hypot)
					ball.ydir = (math.sin(vinkel * grad) * hypot)
					canshoot = False
					hits += 1
					localhits += 1
			
		if canshoot == False:
			ball.xdir *= ball.friction
			ball.ydir *= ball.friction

		if (ball.xdir <= 0.3 and ball.xdir >= -0.3) and (ball.ydir <= 0.3 and ball.ydir >= -0.3):
			ball.xdir *= ball.hardfriction
			ball.ydir *= ball.hardfriction
			canshoot = True

		if ball.rect.left <= 0 or ball.rect.right >= width:
			ball.xdir = -ball.xdir
		if ball.rect.top <= 0 or ball.rect.bottom >= height:
			ball.ydir = -ball.ydir

		if ball.rect.colliderect(hole.rect) and (ball.xdir <= 1.9 and ball.xdir >= -1.9) and (ball.ydir <= 1.9 and ball.ydir >= -1.9) and levelcount < 6:
			drawhole = True
			localhits = 0
			levelcount += 1
			ball.x = mapchecker(levelcount,'ball')[0]
			ball.y = mapchecker(levelcount,'ball')[1]
			ball.xdir = 0
			ball.ydir = 0


		for box in maps.boxes:
			if box[1] == 'default':
				if ball.y > box[0].top-3 and ball.y < box[0].top+3 and (ball.x < box[0].right and ball.x > box[0].left):
					ball.ydir = -ball.ydir
				if ball.y > box[0].bottom-3 and ball.y < box[0].bottom+3 and (ball.x < box[0].right and ball.x > box[0].left):
					ball.ydir = -ball.ydir
				if (ball.x > box[0].left-3 and ball.x < box[0].left+3) and ball.y > box[0].top and ball.y < box[0].bottom:
					ball.xdir = -ball.xdir
				if (ball.x > box[0].right-3 and ball.x < box[0].right+3) and ball.y > box[0].top and ball.y < box[0].bottom:
					ball.xdir = -ball.xdir
			elif box[1] == 'water':
				if ball.rect.colliderect(box[0]):
					gameover = True
			elif box[1] == 'sand':
				if ball.rect.colliderect(box[0]):
					ball.friction = 0.9
				else:
					ball.friction = ball.stdfriction

		screen.fill((72,208,58))
		sprite1.update(vinkel,klubba.dy,klubba.dx,canshoot)
		sprite2.update((-vinkel))
		sprite1.draw(screen)
		sprite2.draw(screen)
		maps.update(levelcount)


		if drawhole == True:
			hole.update(levelcount)
		elif firstrun == True:
			hole.update(100,200)

		if gameover == True:
			big = pygame.font.SysFont("Verdana", 50)
			small = pygame.font.SysFont("Verdana",14)
			go_text = big.render("GAME OVER",True,(0,0,0))
			hit_univ = "all hits: %d" % hits
			hit_local = "hits on this map: %d" % localhits
			hits_univ = small.render(hit_univ, True,(0,0,0))
			hits_local = small.render(hit_local, True,(0,0,0))
			screen.blit(go_text, (width/2, height/2))
			screen.blit(hits_univ, (width/2, (height/2)+100))
			screen.blit(hits_local, (width/2, (height/2)+120))
			ball.xdir = 0
			ball.ydir = 0

		if levelcount == 6:
			big = pygame.font.SysFont("Verdana", 50)
			small = pygame.font.SysFont("Verdana",14)
			go_text = big.render("Congratulations!",True,(0,0,0))
			screen.blit(go_text, (width/2, height/2))
			hit_univ = "all hits: %d" % hits
			hits_univ = small.render(hit_univ, True,(0,0,0))
			screen.blit(hits_univ, (width/2, (height/2)+100))

		s = text.render(msg, True, (0,0,0))
		screen.blit(s, (10,10))
		s2 = text2.render(msg2, True, (0,0,0))
		screen.blit(s2, (10,30))

		ball.rect = pygame.draw.circle(screen, (5,78,200), (int(ball.x+5), int(ball.y+5)),7) #hack to get the ball to blit over the sand

		pygame.display.flip()
		pygame.time.Clock().tick(230)
		if levelcount > 0:
			firstrun = False

if __name__ == '__main__': main()