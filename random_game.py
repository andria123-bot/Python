import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
CIRCLE_RADIUS = 350
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
BALL_RADIUS = 15
MAX_BALLS = 25600  # Limit to prevent system overload
FPS = 60

# Colors
BACKGROUND = (20, 20, 30)
CIRCLE_COLOR = (40, 40, 60)
TEXT_COLOR = (200, 200, 220)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Duplication Game")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont('Arial', 24)

class Ball:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.color = color if color else (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 4)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.alive = True
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        dx = self.x - CIRCLE_CENTER[0]
        dy = self.y - CIRCLE_CENTER[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance + self.radius >= CIRCLE_RADIUS:
            nx = dx / distance
            ny = dy / distance
            
            dot_product = self.vx * nx + self.vy * ny
            self.vx -= 2 * dot_product * nx
            self.vy -= 2 * dot_product * ny
            
            overlap = distance + self.radius - CIRCLE_RADIUS
            self.x -= overlap * nx
            self.y -= overlap * ny
            
            return True  # Ball hit the wall
        return False
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Add a small highlight for 3D effect
        highlight_radius = self.radius // 3
        highlight_pos = (int(self.x - highlight_radius), int(self.y - highlight_radius))
        pygame.draw.circle(screen, (255, 255, 255, 128), highlight_pos, highlight_radius, 1)

def main():
    # Create initial ball at center
    balls = [Ball(CIRCLE_CENTER[0], CIRCLE_CENTER[1])]
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    # Reset the game
                    balls = [Ball(CIRCLE_CENTER[0], CIRCLE_CENTER[1])]
        
        # Update balls
        new_balls = []
        for ball in balls:
            if ball.update() and len(balls) + len(new_balls) < MAX_BALLS:
                # Create a duplicate with slightly different velocity
                duplicate = Ball(ball.x, ball.y, ball.color)
                # Slightly alter the velocity to make them diverge
                duplicate.vx *= random.uniform(0.9, 1.1)
                duplicate.vy *= random.uniform(0.9, 1.1)
                new_balls.append(duplicate)
        
        # Add new balls to the list
        balls.extend(new_balls)
        
        # Draw everything
        screen.fill(BACKGROUND)
        
        # Draw the big circle
        pygame.draw.circle(screen, CIRCLE_COLOR, CIRCLE_CENTER, CIRCLE_RADIUS, 2)
        
        # Draw all balls
        for ball in balls:
            ball.draw()
        
        # Draw UI
        ball_count_text = font.render(f"Balls: {len(balls)}", True, TEXT_COLOR)
        screen.blit(ball_count_text, (20, 20))
        
        instruction_text = font.render("Press R to reset, ESC to quit", True, TEXT_COLOR)
        screen.blit(instruction_text, (WIDTH - instruction_text.get_width() - 20, 20))
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()