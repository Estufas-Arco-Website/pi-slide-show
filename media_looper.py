import os
import pygame
import random
from time import sleep
import subprocess

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)

# Paths
documents_path = "/home/david/Documents/"
media_files = [os.path.join(documents_path, f) for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and f.lower().endswith(('png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov'))]
audio_files = [os.path.join(documents_path, f) for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and f.lower().endswith('mp3')]

# Shuffle audio files
random.shuffle(audio_files)

# Function to play background music
def play_background_music():
    if not pygame.mixer.music.get_busy():
        if audio_files:
            next_song = audio_files.pop()
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
        else:  # Re-shuffle if all songs have been played
            audio_files.extend([os.path.join(documents_path, f) for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and f.lower().endswith('mp3')])
            random.shuffle(audio_files)
            play_background_music()

# Function to display transition effect
def transition_effect():
    for alpha in range(0, 255, 5):
        screen.fill((0, 0, 0))
        overlay = pygame.Surface((infoObject.current_w, infoObject.current_h))
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        sleep(0.01)

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
        # VLC command modified to hide on-screen information and speed up start time
        command = f'cvlc --fullscreen --play-and-exit --no-osd --no-video-title-show "{file_path}"'
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"An error occurred while playing video: {e}")

# Start playing background music
play_background_music()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()

    for media_file in media_files:
        print(f"Accessing file: {media_file}")
        try:
            transition_effect()  # Transition effect
            play_background_music()  # Check and play next song if needed

            if media_file.lower().endswith(('png', 'jpg', 'jpeg')):
                display_image(media_file)
            elif media_file.lower().endswith(('mp4', 'avi', 'mov')):
                play_video(media_file)
        except Exception as e:
            print(f"An error occurred: {e}")
