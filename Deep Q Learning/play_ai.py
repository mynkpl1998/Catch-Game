from __future__ import division, print_function
from keras.models import load_model
import collections
import numpy as np
import os
import wrapped_game
from scipy.misc import imresize
def preprocess_images(images):
	
	if images.shape[0] < 4:
		# single image case
		x_t = images[0]
		x_t = imresize(x_t,(100,100))
		x_t = x_t.astype('float')
		x_t /= 255.0
		s_t = np.stack((x_t,x_t,x_t,x_t),axis=2)
	
	else:
		# 4 images
		xt_list = []
		for i in range(images.shape[0]):
			x_t = imresize(images[i],(100,100))
			x_t = x_t.astype('float')
			x_t /= 255.0
			xt_list.append(x_t)
		s_t = np.stack((xt_list[0],xt_list[1],xt_list[2],xt_list[3]),axis=2)

	s_t = np.expand_dims(s_t,axis=0)
	return s_t

model = load_model('data/AI_MODEL.h5')
num_wins, num_games = 0,0
game = wrapped_game.Stack()

for e in range(1000):
	game.reset()
	# get first state 
	a_0 = 1 # (0 = left, 1 = stay, 2 = right)
	game_over, x_t, r_t = game.mainGame(a_0)
	s_t = preprocess_images(x_t)

	while  not game_over:
	
		q = model.predict(s_t)[0]
		action = np.argmax(q)

		game_over, x_t, r_t = game.mainGame(action)
		s_t = preprocess_images(x_t)

		if r_t == 1:
			num_wins += 1

	num_games +=1

	print("Games : %d | Wins : %d"%(num_games,num_wins))
