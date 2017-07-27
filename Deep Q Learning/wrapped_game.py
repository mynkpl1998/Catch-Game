import pygame
import random
import collections
import numpy as np
import os

class Stack(object):

	def __init__ (self):

		pygame.init()
		os.environ['SDL_VIDEODRIVER'] = 'dummy'
		self.COLOR_WHITE = (255,255,255)
		self.COLOR_BLACK = (0,0,0)
		self.BLOCK_WIDTH = 98
		self.BLOCK_HEIGHT = 30
		self.GAME_WIDTH = 500
		self.GAME_HEIGHT = 500
		self.BALL_SPEED = 30
	
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

	def returnFrames(self):
		return np.array(list(self.frames))
	
	def reset(self):

		self.BASE_BLOCK_X = 200
		self.BASE_BLOCK_Y = 470
		self.UPPER_BLOCK_X, self.ZONE = self.returnXpos()
		self.UPPER_BLOCK_Y = 20
		self.GAME_OVER = False
		self.REWARD = 0
		self.frames = collections.deque(maxlen=4)
		
		self.screen = pygame.display.set_mode((self.GAME_WIDTH,self.GAME_HEIGHT))
		pygame.display.set_caption('Stack')
		self.clock = pygame.time.Clock()
		self.rect1 = pygame.draw.rect(self.screen,self.COLOR_WHITE,pygame.Rect(self.BASE_BLOCK_X,self.BASE_BLOCK_Y,self.BLOCK_WIDTH,self.BLOCK_HEIGHT))

	def mainGame(self,action):

		pygame.event.pump()
		
		if action == 1: # action = 1 move left
			self.BASE_BLOCK_X -= 100
			if self.BASE_BLOCK_X < 0:
				self.BASE_BLOCK_X = 0
		elif action == 2: # action = 2 move right
			self.BASE_BLOCK_X += 100
			if self.BASE_BLOCK_X > 499:
				self.BASE_BLOCK_X = 400
		else: # action = 0 do nothing
			pass

		self.UPPER_BLOCK_Y += self.BALL_SPEED

		if self.rect1.left == self.ZONE:
			if self.UPPER_BLOCK_Y > 470:
				self.REWARD = 1
				self.GAME_OVER = True
				

		if self.UPPER_BLOCK_Y > self.GAME_WIDTH:
			self.REWARD = -1
			self.GAME_OVER = True

		self.screen.fill(self.COLOR_BLACK)
		self.rect1 = pygame.draw.rect(self.screen,self.COLOR_WHITE,pygame.Rect(self.BASE_BLOCK_X,self.BASE_BLOCK_Y,self.BLOCK_WIDTH,self.BLOCK_HEIGHT))
		self.circle = pygame.draw.circle(self.screen,self.COLOR_WHITE,(self.UPPER_BLOCK_X,self.UPPER_BLOCK_Y),15,0)
		pygame.display.flip()

		self.frames.append(pygame.surfarray.array2d(self.screen))
		self.clock.tick(30)

		return self.GAME_OVER, self.returnFrames(), self.REWARD

if __name__ == "__main__":
	num_wins = 0
	frames = np.array([])
	for i in range(100):
		game = Stack()
		game.reset()
		game_over = False
		while not game_over:
			action = random.randint(0,2)
			game_over, frames, reward = game.mainGame(action)
			if reward == 1:
				num_wins +=1
				print(num_wins)
			#for frame in frames:
			#img = imresize(frame,(80,80))
			#	frame = frame.astype('float')
			#	frame /= 255.0
			#	plt.imshow(frame)
			#	plt.show()
		