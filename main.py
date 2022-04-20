import pygame
import pygame.camera
import time

pygame.camera.init()
cam = pygame.camera.Camera('/dev/video0', (640, 480))
cam.start()
img = cam.get_image()
file_name = time.strftime('%d%m-%H%M%S') + '.jpg'
pygame.image.save(img, file_name)
