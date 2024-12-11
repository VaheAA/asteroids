# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updatable:
            u.update(dt)
            
        for a in asteroids:
           is_collision_with_player = a.collision(player)       
           if is_collision_with_player:
                print("Game Over!")
                sys.exit()
                
           for s in shots:
               is_collision_hit_by_player = a.collision(s)
               if is_collision_hit_by_player:
                   a.split()
                   s.kill()     
                
        screen.fill('black')
        
        for d in drawable:
            d.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()  