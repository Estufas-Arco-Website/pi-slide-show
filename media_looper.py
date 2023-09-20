import os
import pygame
from time import sleep

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)

documents_path = "/home/pi/Documents/"
media_files = [os.path.join(documents_path, f) for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and f.lower().endswith(('png', 'jpg', 'jpeg'))]

# Check if media_files list is empty and print a message if it is
if not media_files:
    print(f"No image files found in the directory: {documents_path}")
else:
    print(f"Found {len(media_files)} media files in the directory: {documents_path}")

def display_image(file_path):
    try:
        img = pygame.image.load(file_path)
        img = pygame.transform.scale(img, (infoObject.current_w, infoObject.current_h))
        screen.blit(img, (0, 0))
        pygame.display.update()
        sleep(5)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"An error occurred while displaying image: {e}")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()

    for media_file in media_files:
        print(f"Accessing file: {media_file}")
        try:
            display_image(media_file)
        except Exception as e:
            print(f"An error occurred: {e}")
