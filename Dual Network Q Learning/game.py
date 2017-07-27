import pygame
import random
import sys
class Stack(object):

	def __init__ (self):

		pygame.init()
		self.COLOR_WHITE = (255,255,255)
		self.COLOR_BLACK = (0,0,0)
		self.BLOCK_WIDTH = 98
		self.BLOCK_HEIGHT = 30
		self.GAME_WIDTH = 500
		self.GAME_HEIGHT = 500
		self.BALL_SPEED = 20

	def returnXpos(self):
		number = random.randint(0,4)
		if number == 0:
			return 47, 0
		elif number == 1:
			return 147,100
		elif number == 2:
			return 247,200
		elif number == 3:
			return 347,300
		else:
			return 447,400

	def reset(self):

		self.BASE_BLOCK_X = 200
		self.BASE_BLOCK_Y = 470
		self.UPPER_BLOCK_X, self.ZONE = self.returnXpos()
		self.UPPER_BLOCK_Y = 20
		self.GAME_OVER = False
		self.REWARD = 0

		self.screen = pygame.display.set_mode((self.GAME_WIDTH,self.GAME_HEIGHT))
		pygame.display.set_caption('Stack')
		self.clock = pygame.time.Clock()
		self.rect1 = pygame.draw.rect(self.screen,self.COLOR_WHITE,pygame.Rect(self.BASE_BLOCK_X,self.BASE_BLOCK_Y,self.BLOCK_WIDTH,self.BLOCK_HEIGHT))

	def mainGame(self):

		pygame.event.pump()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.BASE_BLOCK_X -= 100
					if self.BASE_BLOCK_X < 0:
						self.BASE_BLOCK_X = 0
				elif event.key == pygame.K_RIGHT:
					self.BASE_BLOCK_X += 100
					if self.BASE_BLOCK_X > 499:
						self.BASE_BLOCK_X = 400

		self.UPPER_BLOCK_Y += self.BALL_SPEED

		if self.rect1.left == self.ZONE:
			if self.UPPER_BLOCK_Y > 470:
				self.REWARD = 1
				self.GAME_OVER = True
		if self.UPPER_BLOCK_Y > self.GAME_WIDTH:
			self.REWARD = -1
			self.GAME_OVER = True

		print("Reward : %d"%(self.REWARD))
		self.screen.fill(self.COLOR_BLACK)
		self.rect1 = pygame.draw.rect(self.screen,self.COLOR_WHITE,pygame.Rect(self.BASE_BLOCK_X,self.BASE_BLOCK_Y,self.BLOCK_WIDTH,self.BLOCK_HEIGHT))
		self.circle = pygame.draw.circle(self.screen,self.COLOR_WHITE,(self.UPPER_BLOCK_X,self.UPPER_BLOCK_Y),15,0)
		pygame.display.flip()
		self.clock.tick(30)

		return self.GAME_OVER

if __name__ == "__main__":
	game = Stack()
	game.reset()
	game_over = False
	while not game_over:
		game_over = game.mainGame()