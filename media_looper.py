import os
import pygame
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)

usb_path = "/media/pi/USB_NAME/"
media_files = [os.path.join(usb_path, f) for f in os.listdir(usb_path) if os.path.isfile(os.path.join(usb_path, f))]

def play_video(file_path):
    player = OMXPlayer(file_path)
    player.play()
    sleep(player.duration())
    player.quit()

def display_image(file_path):
    img = pygame.image.load(file_path)
    img = pygame.transform.scale(img, (infoObject.current_w, infoObject.current_h))
    screen.blit(img, (0, 0))
    pygame.display.flip()
    sleep(5)  # Adjust the sleep time as needed


while True:
    for media_file in media_files:
        if media_file.lower().endswith(('png', 'jpg', 'jpeg')):
            display_image(media_file)
        elif media_file.lower().endswith(('mp4', 'mkv', 'avi')):
            play_video(media_file)
