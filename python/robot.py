import random
import math

class Circle:
    def __init__(self, boundary, x, y, radius, speed):
        self.boundary = (boundary[0] - radius, boundary[1] - radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):

        self.x += int(self.speed * math.cos(self.angle))
        self.y += int(self.speed * math.sin(self.angle))

        # Check for collisions with boundaries
        if self.x - self.radius < 0 or self.x > self.boundary[0] or \
           self.y - self.radius < 0 or self.y > self.boundary[1]:
            # Change direction on collision to any angle between 90 to 270
            self.angle = (self.angle + random.uniform(math.pi, 3 * math.pi / 2)) % (2 * math.pi)
            # if self.angle >= 2 * math.pi:
            #     self.angle %= (2 * math.pi)

    def draw(self):

        circle_position = (self.x, self.y)
        line_ending_postion = (
            int(self.x + self.radius * math.cos(self.angle)),
            int(self.y + self.radius * math.sin(self.angle))
        )

        return (
            circle_position,
            line_ending_postion
        )