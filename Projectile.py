import pygame

from Display import Display
from Entity import Entity


class Projectile(Display, Entity):
    Instances = []

    def __init__(self, coord, target, atk, size, speed, pierce, duration, keywords):
        Display.__init__(self, None, coord, size * 25)
        self.movement = pygame.Vector2(target) - self.coord
        self.movement.normalize_ip()
        self.movement *= speed * 200
        self.collided = []

        Entity.__init__(self, [], power=atk, pierce=pierce, duration=duration,
                        speed=speed, size=size, basepierce=pierce, baseduration=duration)

        for keyword in keywords:
            keyword.__init__(self)
        self.keywords = keywords

        Projectile.Instances.append(self)

    def Update(self, dt):
        # mouvement
        self.coord += self.movement * dt
        self.Add("duration", -dt)
        # on vérifie si le projectile ne devrait pas disparaitre
        if self.Get("duration") <= 0:
            Projectile.Instances.remove(self)
        elif self.Get("pierce") <= 0:
            Projectile.Instances.remove(self)
        else:
            for keyword in self.keywords:
                keyword.Update(self, dt)
        super().Update(dt)
