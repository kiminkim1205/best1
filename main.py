import pygame
import random

# 초기화
pygame.init()

# 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game - Multi Page")
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.SysFont('malgungothic', 30)
large_font = pygame.font.SysFont('malgungothic', 50)

class Dino:
    def __init__(self):
        self.x = 50
        self.y = 310
        self.y_velocity = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = -15
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.y += self.y_velocity
            self.y_velocity += 0.8  # 중력
            if self.y >= 310:
                self.y = 310
                self.is_jumping = False

    def draw(self):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, 40, 40])

class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = 320
        self.speed = 7

    def update(self):
        self.x -= self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, 20, 30])

def main():
    state = "START"  # START, PLAYING, GAMEOVER
    dino = Dino()
    obstacles = []
    score = 0

    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if state == "START" and event.key == pygame.K_SPACE:
                    state = "PLAYING"
                elif state == "PLAYING" and event.key == pygame.K_SPACE:
                    dino.jump()
                elif state == "GAMEOVER" and event.key == pygame.K_r:
                    # 초기화 후 다시 시작
                    state = "PLAYING"
                    dino = Dino()
                    obstacles = []
                    score = 0

        if state == "START":
            msg = large_font.render("Press SPACE to Start", True, BLACK)
            screen.blit(msg, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 - 50))

        elif state == "PLAYING":
            # 바닥선
            pygame.draw.line(screen, BLACK, (0, 350), (SCREEN_WIDTH, 350), 2)
            
            dino.update()
            dino.draw()

            # 장애물 생성 및 관리
            if random.randint(1, 60) == 1 and (not obstacles or obstacles[-1].x < 500):
                obstacles.append(Obstacle())

            for obs in obstacles[:]:
                obs.update()
                obs.draw()
                
                # 충돌 체크
                dino_rect = pygame.Rect(dino.x, dino.y, 40, 40)
                obs_rect = pygame.Rect(obs.x, obs.y, 20, 30)
                if dino_rect.colliderect(obs_rect):
                    state = "GAMEOVER"

                if obs.x < -20:
                    obstacles.remove(obs)
                    score += 1

            score_txt = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_txt, (700, 20))

        elif state == "GAMEOVER":
            msg = large_font.render("GAME OVER", True, (255, 0, 0))
            restart_msg = font.render("Press 'R' to Restart", True, BLACK)
            screen.blit(msg, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_msg, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

