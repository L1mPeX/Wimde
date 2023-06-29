import pygame
import math


class Character():
    def __init__(self, x, y, animation_list):
        self.flip = False
        self.running = False
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
    
    def move(self, dx, dy):
        self.running = False
        if 0 != dx or 0 != dy:
            self.running = True
        if dx < 0:
            self.flip = True
        elif dx > 0:
            self.flip = False
        
        if 0 not in (dx, dy):
            dx = dx * math.sqrt(2) / 2
            dy = dy * math.sqrt(2) / 2
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        if self.running == True:
            self.update_action(1)
        else:
            self.update_action(0)
        animation_cooldown = 70
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index = (self.frame_index + 1) % 4
            print(self.frame_index)
            self.update_time = pygame.time.get_ticks()

    def update_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)