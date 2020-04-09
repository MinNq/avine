from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from matplotlib.animation import FuncAnimation

from avine.Transformations import *


def ShowTransformations(data, save_at, gif_length = 1, fps = 30):

    '''
    Show all defined affine transformations applied to
    given data in a gif.

    Parameters:
    - data: array_like. A matrix where each column
    is an augmented data point.
    - save_at: string. The link to where you want to save
    your gif.
    - gif_length (optional): float. Length of the ouput
    gif.
    - fps (optional): int. Frame rate of the output gif.
    '''

    # preprocessing
    Data = augmented(data)
    
    # preparing figure and axes
    fig, axs = plt.subplots(3, 3, figsize = (8,8))
    plt.subplots_adjust(top = 0.8, wspace = 0.3, hspace = 0.4)
    plt.suptitle('Affine Transformations', y = 0.93,
                    size = 'x-large', weight = 'bold')

    lim = max(np.abs(np.max(Data))*.5, 1) + np.abs(np.max(Data))
    margin = .25

    # initializing subplots
    plots = []
    for i in range(9):
        axs[i/3, i%3].set(xlim=(-lim - margin, lim + margin),
                            ylim=(-lim - margin, lim + margin))
        # highlighting x-axis and y-axis
        axs[i/3, i%3].axhline(linewidth = 1, color = 'gray')
        axs[i/3, i%3].axvline(linewidth = 1, color = 'gray')
        plots.append(axs[i/3, i%3].scatter([], [], s = 15,
                        color = 'red', alpha = .5))

    # identity
    plots[0].set_offsets(np.c_[Data[0, :], Data[1, :]])
    axs[0, 0].set_title('Identity')

    # animation function for FuncAnimation
    def animate(frame):

        # a float running from 0 to 1 to track progress
        progress = float(frame)/(fps*gif_length)

        # translation
        update = transformations[1](Data, [progress, progress])
        plots[1].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[0, 1].set_title('Translation')

        # scaling
        scale_factor = progress*(np.array([1.5, 1.2]) - 1) + 1
        update = transformations[2](Data, scale_factor)
        plots[2].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[0, 2].set_title('Scaling')

        # rotation around origin
        update = transformations[3](Data, progress*np.pi/3)
        plots[3].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[1, 0].set_title('Rotation around origin')

        # shearing in x direction
        update = transformations[4](Data, progress*np.pi/3)
        plots[4].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[1, 1].set_title('Shearing in $x$ direction')

        # shearing in y direction
        update = transformations[5](Data, progress*np.pi/3)
        plots[5].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[1, 2].set_title('Shearing in $y$ direction')    

        # reflection through origin
        condition = int(progress*gif_length/float(0.2))%2
        update = transformations[6](Data) if condition else Data
        plots[6].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[2, 0].set_title('Reflection through origin')          

        # reflection through x-axis
        condition = int(progress*gif_length/float(0.2))%2
        update = transformations[7](Data) if condition else Data
        plots[7].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[2, 1].set_title('Reflection through x-axis')  

        # reflection through y-axis
        condition = int(progress*gif_length/float(0.2))%2
        update = transformations[8](Data) if condition else Data
        plots[8].set_offsets(np.c_[update[0, :], update[1, :]])
        axs[2, 2].set_title('Reflection through y-axis')


    anim = FuncAnimation(fig, animate, interval = float(1000)/fps, 
                            frames = fps*gif_length)

    anim.save(save_at, writer = 'imagemagick', dpi = 200)

    print('Your gif is ready! Check it at {}.'.format(save_at))

def ShowSeries(data, transformation_list, save_at, gif_length = 3, fps = 30):

    '''
    Show respectively all given affine transformations 
    applied to given data in a gif.

    Parameters:
    - data: array_like. A matrix where each column
    is an augmented data point.
    - transformation_list: array_like. A list of
    transformations to apply, including
    transformation codes (from 0 to 8) and 
    corresponding parameters in a 2-tuple. If
    there are no parameters, just use an integer.
    - save_at: string. The link to where you want to save
    your gif.
    - gif_length (optional): float. Length of the ouput
    gif.
    - fps (optional): int. Frame rate of the output gif.
    '''

    # preprocessing
    Data = augmented(data)

    # adding an identity to the start
    transformation_list.insert(0, (0,0))

    # standardizing
    transformation_list = standardize(transformation_list)

    # outputs from each component transformation
    to_do = np.array(series(Data, transformation_list))
    
    # preparing figure
    fig = plt.figure(figsize = (5,5))
    plt.subplots_adjust(top = 0.8, wspace = 0.3, hspace = 0.4)
    plt.suptitle('Affine Transformation Series', y = 0.93, weight = 'bold')
    
    # highlighting x-axis and y-axis
    plt.axhline(linewidth = 1, color = 'gray')
    plt.axvline(linewidth = 1, color = 'gray')

    margin = .25
    x_lim = (np.min(to_do[:, 0]) - margin, np.max(to_do[:, 0]) + margin)
    y_lim = (np.min(to_do[:, 1]) - margin, np.max(to_do[:, 1]) + margin)

    # initializing plot
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plot = plt.scatter([], [], s = 25, color = 'red', alpha = .5)

    # checkpoints for turning into the next transformation
    n = len(transformation_list)
    checkpoints = np.arange(0, 1, float(1)/n) + float(1)/n

    # starting with identity
    #plt.scatter(Data[0, :], Data[1, :], s = 25, color = 'blue', alpha = .5)
    plot.set_offsets(np.c_[Data[0, :], Data[1, :]])

    # animation function for FuncAnimation
    def animate(frame):

        # a float running from 0 to 1 to track progress
        progress = float(frame)/(fps*gif_length)

        # looping through checkpoints to catch the right
        # transformation
        for point in range(n):
            if progress < checkpoints[point] and progress + float(1)/n > checkpoints[point]:

                plt.title('Step {}: {}'.format(point, transformation_list[point]))

                unit_progress = n*(progress - checkpoints[point]) + 1

                # translation
                if transformation_list[point][0] == 1:
                    update = transformations[1](to_do[point], [unit_progress, unit_progress])
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])

                # scaling
                elif transformation_list[point][0] == 2:
                    arg = np.array(transformation_list[point][1])
                    scale_factor = unit_progress*(arg - 1) + 1
                    update = transformations[2](to_do[point], scale_factor)
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])

                # rotation around origin
                elif transformation_list[point][0] == 3:
                    arg = transformation_list[point][1]
                    update = transformations[3](to_do[point], unit_progress*arg)
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])

                # shearing in x direction
                elif transformation_list[point][0] == 4:
                    arg = transformation_list[point][1]
                    update = transformations[4](to_do[point], unit_progress*arg)
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])

                # shearing in y direction
                elif transformation_list[point][0] == 5:
                    arg = transformation_list[point][1]
                    update = transformations[5](to_do[point], unit_progress*arg)
                    plot.set_offsets(np.c_[update[0, :], update[1, :]]) 
                
                # reflection through origin
                elif transformation_list[point][0] == 6:
                    update = transformations[6](to_do[point])
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])          

                # reflection through x-axis
                elif transformation_list[point][0] == 7:
                    update = transformations[7](to_do[point])
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])

                # reflection through y-axis
                elif transformation_list[point][0] == 8:
                    update = transformations[8](to_do[point])
                    plot.set_offsets(np.c_[update[0, :], update[1, :]])


    anim = FuncAnimation(fig, animate, interval = float(1000)/fps, 
                            frames = fps*gif_length)

    anim.save(save_at, writer = 'imagemagick', dpi = 200)

    print('Your gif is ready! Check it at {}.'.format(save_at))
