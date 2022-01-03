import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True
while running:
    # 이벤트 루프
    for event in pygame.event.get():    # 발생한 이벤트 종류
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False     # 게임이 실행중이 아님
# 게임 종료
pygame.quit()