import os
import pygame
from time import sleep
import subprocess

# Initialize Pygame
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)

# Path to your media file
documents_path = "/home/david/Documents/"
media_files = [os.path.join(documents_path, f) for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and f.lower().endswith(('png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov'))]

# Function to display image
def display_image(file_path):
    try:
        img = pygame.image.load(file_path)
        img_ratio = img.get_width() / img.get_height()
        screen_ratio = infoObject.current_w / infoObject.current_h

        if img_ratio > screen_ratio:
            scaled_width = infoObject.current_w
            scaled_height = scaled_width / img_ratio
        else:
            scaled_height = infoObject.current_h
            scaled_width = scaled_height * img_ratio

        img = pygame.transform.scale(img, (int(scaled_width), int(scaled_height)))
        x = int((infoObject.current_w - scaled_width) / 2)  # Center horizontally
        y = int((infoObject.current_h - scaled_height) / 2)  # Center vertically

        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(img, (x, y))
        pygame.display.update()
        sleep(5)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"An error occurred while displaying image: {e}")

# Function to play video
def play_video(file_path):
    try:
        command = f'omxplayer --win "0 0 {infoObject.current_w} {infoObject.current_h}" "{file_path}"'
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"An error occurred while playing video: {e}")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()

    for media_file in media_files:
        print(f"Accessing file: {media_file}")
        try:
            if media_file.lower().endswith(('png', 'jpg', 'jpeg')):
                display_image(media_file)
            elif media_file.lower().endswith(('mp4', 'avi', 'mov')):
                play_video(media_file)
        except Exception as e:
            print(f"An error occurred: {e}")
