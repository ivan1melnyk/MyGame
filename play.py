import pygame
from enum import Enum
from random import randint

pygame.init()

screen = pygame.display.set_mode((1500, 673))
screen_color = (0, 0, 0)

icon = pygame.image.load('images/console.png').convert_alpha()
background = pygame.image.load('images/background_1.jpg').convert()
heart = pygame.image.load('images/heart/mini_health_heart.png').convert_alpha()
broken_heart = pygame.image.load(
    'images/heart/mini_broken_heart.png').convert_alpha()
text_font = pygame.font.Font('KiwiSoda.ttf', 50)
text_surface = text_font.render('MyGame', False, 'Green')
backgroud_X = 0

clock = pygame.time.Clock()
pygame.display.set_caption("Dendy")
pygame.display.set_icon(icon)


witch = pygame.image.load('images/witches/witch.png').convert_alpha()
witch_list_in_game = []
witch_timer = pygame.USEREVENT + 1
pygame.time.set_timer(witch_timer, randint(2000, 5500))

# Player variables
player_position_X, player_position_Y = 0, 400
player_count = 0
health_level = 5

JUMP_HEIGHT = 120
Y_VELOCITY = JUMP_HEIGHT  # Vertical velocity
GRAVITY = 48  # Gravity force
GROUND_POSITION = player_position_Y
ATTACK = False
DEAD = False
DEAD_ended = False
break_heart = False


def draw_buttom(rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    text_start_again = text_font.render(text, False, text_color)
    screen.blit(text_start_again, (690, 325))


# Player animations
stay = [pygame.image.load('images/IDLE/IDLE_1.png').convert_alpha(),
        pygame.image.load('images/IDLE/IDLE_2.png').convert_alpha(),
        pygame.image.load('images/IDLE/IDLE_3.png').convert_alpha(),
        pygame.image.load('images/IDLE/IDLE_4.png').convert_alpha(),]

jump = [pygame.image.load('images/run/run_1.png').convert_alpha(),
        pygame.image.load('images/run/run_2.png').convert_alpha(),
        pygame.image.load('images/run/run_3.png').convert_alpha(),
        pygame.image.load('images/run/run_4.png').convert_alpha(),
        pygame.image.load('images/run/run_5.png').convert_alpha(),
        pygame.image.load('images/run/run_6.png').convert_alpha(),
        pygame.image.load('images/run/run_7.png').convert_alpha(),]

walk = [pygame.image.load('images/walk/walk_1.png').convert_alpha(),
        pygame.image.load('images/walk/walk_2.png').convert_alpha(),
        pygame.image.load('images/walk/walk_3.png').convert_alpha(),
        pygame.image.load('images/walk/walk_4.png').convert_alpha(),
        pygame.image.load('images/walk/walk_5.png').convert_alpha(),
        pygame.image.load('images/walk/walk_6.png').convert_alpha(),
        pygame.image.load('images/walk/walk_7.png').convert_alpha(),
        pygame.image.load('images/walk/walk_8.png').convert_alpha(),]

attack = [pygame.image.load('images/attack/attack_1.png').convert_alpha(),
          pygame.image.load('images/attack/attack_2.png').convert_alpha(),
          pygame.image.load('images/attack/attack_3.png').convert_alpha(),
          pygame.image.load('images/attack/attack_4.png').convert_alpha(),
          pygame.image.load('images/attack/attack_5.png').convert_alpha(),
          pygame.image.load('images/attack/attack_6.png').convert_alpha(),]

jump_attack = [pygame.image.load('images/jump_attack/jump_attack_1.png').convert_alpha(),
               pygame.image.load(
                   'images/jump_attack/jump_attack_2.png').convert_alpha(),
               pygame.image.load(
                   'images/jump_attack/jump_attack_3.png').convert_alpha(),
               pygame.image.load(
                   'images/jump_attack/jump_attack_4.png').convert_alpha(),
               pygame.image.load(
                   'images/jump_attack/jump_attack_5.png').convert_alpha(),
               pygame.image.load(
                   'images/jump_attack/jump_attack_6.png').convert_alpha(),
               pygame.image.load('images/jump_attack/jump_attack_6.png').convert_alpha(),]

attack_2 = [pygame.image.load(
    f'images/attack_2/attack_2.{i}.png').convert_alpha() for i in range(1, 7)]

hurt = [pygame.image.load('images/hurt/hurt_1.png').convert_alpha(),
        pygame.image.load('images/hurt/hurt_2.png').convert_alpha(),]

dead = [pygame.image.load(
    f'images/dead/dead_{i}.png').convert_alpha() for i in range(1, 7)]


class Movement(Enum):
    STAY = 1
    JUMP = 2
    WALK = 3
    ATTACK = 4
    JUMP_ATTACK = 5
    ATTACK_2 = 6
    HURT = 7
    DAED = 8


MOVEMENT = Movement(1)
Previous_movement = Movement(3)

running = True
while running:
    mouse_pos = pygame.Rect(pygame.mouse.get_pos() + (5, 5))
    mouse_clicked = False

    player_rect = walk[0].get_rect(
        topleft=(player_position_X, player_position_Y))
    player_attack_rect = walk[0].get_rect(
        topleft=(player_position_X+150, player_position_Y))

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == witch_timer:
            witch_list_in_game.append(witch.get_rect(
                topleft=(1200, randint(300, 450))))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

        elif event.type == pygame.KEYDOWN:
            player_count = 0
            if event.key == pygame.K_s:
                Previous_movement = Movement(3)
                MOVEMENT = Movement(1)
                # print('CHANGE STATE TO STAY')
            elif event.key == pygame.K_w:
                Previous_movement = MOVEMENT
                MOVEMENT = Movement(2)
                # print('CHANGE STATE TO JUMP')
            elif event.key == pygame.K_d:
                Previous_movement = Movement(1)
                MOVEMENT = Movement(3)
                # print('CHANGE STATE TO WALK')
            elif event.key == pygame.K_a:
                Previous_movement = MOVEMENT
                MOVEMENT = Movement(4)
                ATTACK = True
                # print('CHANGE STATE TO ATTACK')
            elif event.key == pygame.K_q:
                Previous_movement = MOVEMENT
                MOVEMENT = Movement(5)
                ATTACK = True
                # print('CHANGE STATE TO JUMP_ATTACK')
            elif event.key == pygame.K_z:
                Previous_movement = MOVEMENT
                MOVEMENT = Movement(6)
                ATTACK = True
                # print('CHANGE STATE TO ATTACK_2')
            elif event.key == pygame.K_SPACE:
                MOVEMENT, Previous_movement = Previous_movement, MOVEMENT

    keys_pressed = pygame.key.get_pressed()

    # Do logical updates here.
    # ...
    screen.blit(background, (backgroud_X, 0))
    screen.blit(background, (1340+backgroud_X, 0))
    for seg in range(1, health_level+1):
        screen.blit(heart, (25*seg, 0))
    screen.blit(text_surface, (500, 0))

    if witch_list_in_game:
        for el in witch_list_in_game:
            witch_rect = witch.get_rect(topleft=(el.x, el.y))
            screen.blit(witch, el)
            el.x -= 25

            if player_attack_rect.colliderect(witch_rect) and ATTACK:
                witch_list_in_game.remove(el)
            elif player_rect.colliderect(witch_rect):
                health_level -= 1
                Previous_movement = MOVEMENT
                MOVEMENT = Movement(7)
                break_heart = True
                witch_list_in_game.remove(el)

    if break_heart:
        screen.blit(broken_heart, ((health_level+1)*25, 0))
    break_heart = False

    match MOVEMENT.value:
        case 1:
            screen.blit(stay[player_count],
                        (player_position_X, player_position_Y))
            if player_count == 3:
                player_count = 0
            else:
                player_count += 1
        case 2:
            player_count += 1
            player_position_Y -= Y_VELOCITY
            Y_VELOCITY -= GRAVITY
            if player_count == 6:
                print('CHANGE STATE')
                player_position_Y = GROUND_POSITION
                player_count = 0
                MOVEMENT = Previous_movement
                Y_VELOCITY = JUMP_HEIGHT
            screen.blit(jump[player_count],
                        (player_position_X, player_position_Y))
        case 3:
            screen.blit(walk[player_count],
                        (player_position_X, player_position_Y))
            if player_count == 7:
                player_count = 0
            else:
                player_count += 1
        case 4:
            screen.blit(attack[player_count],
                        (player_position_X, player_position_Y))
            if player_count == 5:
                player_count = 0
                MOVEMENT = Previous_movement
                ATTACK = False
            else:
                player_count += 1
        case 5:
            player_count += 1
            player_position_Y -= Y_VELOCITY
            Y_VELOCITY -= GRAVITY
            if player_count == 6:
                # print('CHANGE STATE')
                ATTACK = False
                player_position_Y = GROUND_POSITION
                player_count = 0
                MOVEMENT = Previous_movement
                Y_VELOCITY = JUMP_HEIGHT
            screen.blit(jump_attack[player_count],
                        (player_position_X, player_position_Y))
        case 6:
            screen.blit(attack_2[player_count],
                        (player_position_X, player_position_Y))
            if player_count == 5:
                player_count = 0
                ATTACK = False
                MOVEMENT = Previous_movement
            else:
                player_count += 1
        case 7:
            if player_count >= 1:
                player_count = 0
                screen.blit(hurt[1], (player_position_X, player_position_Y))
                MOVEMENT = Previous_movement
            else:
                screen.blit(hurt[0], (player_position_X, player_position_Y))
                player_count += 1
        case 8:
            screen.blit(dead[player_count],
                        (player_position_X, player_position_Y))
            if player_count == 5:
                player_count = 0
                DEAD = True
                DEAD_ended = True
                MOVEMENT = Movement(1)
                Previous_movement = Movement(3)
            else:
                player_count += 1

    # print(f'JUMP_COUNT: {player_count}, POSITION Y: {player_position_Y}, VELOCITY: {Y_VELOCITY}, GRAVITY: {GRAVITY}, MOVEMENT: {MOVEMENT.value}')

    # Update game objects
    if MOVEMENT.value != 1 and MOVEMENT.value != 4:
        backgroud_X -= 5
    if backgroud_X == -1340:
        backgroud_X = 0

    if health_level == 0 and not DEAD:
        player_count = 0
        DEAD = True
        MOVEMENT = Movement(8)
    if DEAD and DEAD_ended:
        pygame.draw.rect(screen, 'Red', pygame.Rect(0, 0, 1500, 673))
        pygame.draw.rect(screen, 'Yellow', pygame.Rect(0, 0, 1500, 673), 15)
        text_loser = text_font.render('GAME OVER', False, 'Yellow')
        screen.blit(text_loser, (700, 200))
        buttom = pygame.Rect(650, 300, 300, 100)
        draw_buttom(buttom, 'Yellow', 'Start Again', 'Red')
        if mouse_clicked and buttom.colliderect(mouse_pos):
            health_level = 6
            DEAD = False
            DEAD_ended = False
            witch_list_in_game = []

    pygame.display.update()
    clock.tick(10)  # Increased FPS for smoother physics
