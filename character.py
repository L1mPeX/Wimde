import pygame
import math


class Character:
    def __init__(self, x, y, image):
        self.flip = False
        self.image = image
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
    
    def move(self, dx, dy):
        if dx < 0:
            self.flip = True
        elif dx > 0:
            self.flip = False
        
        if 0 not in (dx, dy):
            dx = dx * math.sqrt(2) / 2
            dy = dy * math.sqrt(2) / 2
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)