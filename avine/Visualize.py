import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from matplotlib.animation import FuncAnimation
from avine.Transformations import * 


'''
ShowTransformations(data, gif_length = 1, fps = 60)

> create a gif with all defined affine transformations 
applied to given data

data: array_like. Coordinates in 2-d Cartesian space.
gif_length: int or float. Length of ouput gif in second. 
fps: int. Frame rate of output gif.
'''

def ShowTransformations(data, gif_length = 1, fps = 60):

	# creating a figure and a bunch of subplots
	fig = plt.figure(figsize = (8, 8))
	plt.subplots_adjust(top = 0.8, wspace = 0.3, hspace = 0.4)
	plt.suptitle('Affine Transformations', y = 0.93,
					size = 'x-large', weight = 'bold')

	axs = [] # a list of axes
	artists = [] # a list of artists
	for subplot_id in range(9):
		axs.append(plt.subplot(3, 3, subplot_id + 1))
		artists.append(axs[subplot_id].scatter([], []))

	# titles for the subplots
	titles = ['No change']
	titles.append('Translate')
	titles.append('Scale about origin',)
	titles.append('Rotate about origin')
	titles.append('Shear in $x$ direction')
	titles.append('Shear in $y$ direction')
	titles.append('Reflect about origin')
	titles.append('Reflect about $x$-axis')
	titles.append('Reflect about $y$-axis')

	# preprocessing
	augmented_data = [augmented(vector) for vector in data]

	distances = [np.dot(vector[:2].T, vector[:2]) for vector in augmented_data]
	lim = np.max(distances) + max(.5*np.max(distances), 1.5)

	# clearing all axes and reseting their appearance
	def reset():
		for subplot_id in range(1, 9):

			axs[subplot_id].cla()

			axs[subplot_id].set_title(titles[subplot_id])
			axs[subplot_id].set_xlim(-lim, lim)
			axs[subplot_id].set_ylim(-lim, lim)
			axs[subplot_id].grid(True)

			# highlighting x-axis and y-axis
			axs[subplot_id].axhline(linewidth = 1, color = 'gray')
			axs[subplot_id].axvline(linewidth = 1, color = 'gray')

	# identity
	for subplot_id in range(0, 1):	

		axs[subplot_id].set_title(titles[subplot_id])
		axs[subplot_id].set_xlim(-lim, lim)
		axs[subplot_id].set_ylim(-lim, lim)
		axs[subplot_id].grid(True)

		# highlighting x-axis and y-axis
		axs[subplot_id].axhline(linewidth = 1, color = 'gray')
		axs[subplot_id].axvline(linewidth = 1, color = 'gray')

		to_show = np.array([func_list[subplot_id](vector) 
							for vector in augmented_data])
		axs[subplot_id].scatter(to_show[:, 0], to_show[:, 1], 
								color = 'red', s = 20, alpha = 0.5)

	# initialization function for FuncAnimation
	def init():
		artists.set_data([], [])
		return artists,

	# animation function for FuncAnimation
	def animate(frame):

		progress = float(frame)/(fps*gif_length)

		if frame:
			print('Progress: {}%'.format(progress*90), flush = True)

		reset()

		# translation and scaling
		for subplot_id in range(1, 3):
			
			to_show = np.array([func_list[subplot_id](vector, [progress*(-.5), progress*1.5]) 
								for vector in augmented_data])
			axs[subplot_id].scatter(to_show[:, 0], to_show[:, 1],
									color = 'red', s = 20, alpha = 0.5)

		# rotation and shearing
		for subplot_id in range(3, 6):
			
			to_show = np.array([func_list[subplot_id](vector, progress*np.pi/3) 
								for vector in augmented_data])
			axs[subplot_id].scatter(to_show[:, 0], to_show[:, 1],
									color = 'red', s = 20, alpha = 0.5)

		# reflection
		for subplot_id in range(6, 9):

			if int(progress*10)%2:
				to_show = np.array([func_list[subplot_id](vector) 
								for vector in augmented_data])
			else:
				to_show = np.array([vector for vector in augmented_data])

			axs[subplot_id].scatter(to_show[:, 0], to_show[:, 1],
									color = 'red', s = 20, alpha = 0.5)


		return artists

	# making animation with FuncAnimation
	anim = FuncAnimation(fig, animate, frames = int(fps*gif_length),
						interval = float(1000)/fps, blit = True)

	# saving the animation into a gif with ImageMagick
	anim.save('~/affine_transformations.gif', writer='imagemagick', dpi = 200)

	print('Done! Check your gif!', flush = True)
