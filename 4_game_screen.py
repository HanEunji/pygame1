import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # 20을 초과하면 20으로 처리

    # 실제 화면에 grid 형태로 숫자 랜덤 배치
    shuffle_grid(number_count)

# 숫자 섞기 (중요도 별 다섯 개)
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    grid = [[0 for col in range(columns)] for row in range(rows)]   # 5 x 9

    cell_size = 130
    button_size = 110
    screen_letf_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    number = 1 # 시작 숫자 1부터 number_count까지 랜덤 배치
    while number <= number_count:
        row_idx = randrange(0, rows)    # 0~4
        col_idx = randrange(0, columns) # 0~8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] =  number
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_letf_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)


# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)  # 60은 반지름 값, 선 두께 5
    # 그림, 흰색으로 스타트버튼 위치에~

# 게임화면 보여주기
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        pygame.draw.rect(screen, GRAY, rect)

        # 실제 숫자 텍스트
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text, text_rect)


# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)  # 사각형 만들고
start_button.center = (120, screen_height - 120)    # 화면에서 위치 지정

# 색깔
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = [] # 플레이어가 눌러야 하는 버틀들

# 게임 시작 여부
start = False

# setup 함수
setup(1)

# 게임 루프
running = True
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get():    # 발생한 이벤트 종류
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False     # 게임이 실행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:    # 마우스 클릭 발생 시
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 화면 전체를 까맣게
    screen.fill(BLACK)
    
    if start:
        display_game_screen()   # 게임 화면 표시
    else:
        display_start_screen()  # 시작 화면 표시

    # 어딘가 클릭
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()