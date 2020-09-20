
'''Em ubuntu nao consigo fazer funcionar o pygame'''
import pygame

import os

pygame.mixer.init()
pygame.init()

if os.path.exists('the_skye_boat_song.mp3'):

    pygame.mixer.music.load('the_skye_boat_song.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(40)
    parar = input('Digite algo para parar...')

else:
    print('nao achou o arquivo :/ ')