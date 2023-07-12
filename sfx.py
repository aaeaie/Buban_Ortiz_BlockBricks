import pygame

class Sfx:
    def __init__(self):
        self.click_sound = pygame.mixer.Sound("Sounds/click.ogg")
        self.exit_sound = pygame.mixer.Sound("Sounds/exit.ogg")
        self.mode_sound = pygame.mixer.Sound("Sounds/setmode.ogg")

    def click(self):
        self.click_sound.set_volume(0.2)
        self.click_sound.play()

    def bye(self):
        self.exit_sound.set_volume(0.5)
        self.exit_sound.play()
    
    def set_mode(self):
        self.mode_sound.set_volume(0.3)
        self.mode_sound.play()