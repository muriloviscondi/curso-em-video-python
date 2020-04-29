import pygame

pygame.init()
pygame.mixer.music.load('ex021 - Tocando um MP3.mp3')
pygame.mixer.music.play()
pygame.event.wait()