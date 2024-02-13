import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)
game_second_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Shooter Game")

FIGHTER_STEP = 0.7
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

ROCKET_STEP = 1
rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = fighter_x + fighter_width / 2 - rocket_width / 2, fighter_y - rocket_height
rocket_was_fired = False

ALIEN_STEP = 0.05
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0

ALIEN_TWO_STEP = 0.05
alien_two_speed = ALIEN_TWO_STEP
alien_two_image = pygame.image.load('images/rayna.png')
alien_two_width, alien_two_height = alien_two_image.get_size()
alien_two_x, alien_two_y = randint(0, screen_width - alien_two_width), 0

ALIEN_THREE_STEP = 0.05
alien_three_speed = ALIEN_THREE_STEP
alien_three_image = pygame.image.load('images/alien.png')
alien_three_width, alien_three_height = alien_three_image.get_size()
alien_three_x, alien_three_y = randint(0, screen_width - alien_three_width), 0

ALIEN_FOUR_STEP = 0.05
alien_four_speed = ALIEN_FOUR_STEP
alien_four_image = pygame.image.load('images/alien.png')
alien_four_width, alien_four_height = alien_four_image.get_size()
alien_four_x, alien_four_y = randint(0, screen_width - alien_four_width), 0

ALIEN_FIVE_STEP = 0.05
alien_five_speed = ALIEN_FIVE_STEP
alien_five_image = pygame.image.load('images/alien.png')
alien_five_width, alien_five_height = alien_five_image.get_size()
alien_five_x, alien_five_y = randint(0, screen_width - alien_five_width), 0

RAYNA_STEP = 0.05
rayna_speed = ALIEN_TWO_STEP
rayna_image = pygame.image.load('images/rayna.png')
rayna_width, rayna_height = rayna_image.get_size()
rayna_x, rayna_y = randint(0, screen_width - rayna_width), 0

DEVIL_STEP = 0.05
devil_speed = DEVIL_STEP
devil_image = pygame.image.load('images/devil.png')
devil_width, devil_height = devil_image.get_size()
devil_x, devil_y = randint(0, screen_width - devil_width), 0

game_is_running = True

game_score = 0

game_second_score = 0

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    alien_y += alien_speed
    alien_two_y += alien_two_speed
    alien_three_y += alien_three_speed
    alien_four_y += alien_four_speed
    alien_five_y += alien_five_speed
    rayna_y += rayna_speed
    devil_y += rayna_speed

    if rocket_was_fired and rocket_y + rocket_height < 5:
        rocket_was_fired = False

    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))
    screen.blit(alien_two_image, (alien_two_x, alien_two_y))
    screen.blit(alien_three_image, (alien_three_x, alien_three_y))
    screen.blit(alien_four_image, (alien_four_x, alien_four_y))
    screen.blit(alien_four_image, (alien_five_x, alien_five_y))
    screen.blit(rayna_image, (rayna_x, rayna_y))
    screen.blit(devil_image, (devil_x, devil_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"Aliens score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    game_second_score_text = game_second_font.render(f"Donald score is: {game_second_score}", True, 'red')
    screen.blit(game_second_score_text, (20, 40))

    pygame.display.update()

    if alien_y + alien_height > screen_height:
        fighter_image = alien_image

    # if alien_two_y + alien_two_height > screen_height:
    #     game_two_is_running = True

    if alien_three_y + alien_three_height > screen_height:
        # game_is_running = False
        fighter_image = alien_image

    if alien_four_y + alien_four_height > screen_height:
        # game_is_running = False
        fighter_image = alien_image

    if alien_five_y + alien_five_height > screen_height:
        # game_is_running = False
        fighter_image = alien_image

    # if rayna_y + rayna_height > screen_height:
    #     game_is_running = True

    if devil_y + devil_height > screen_height:
        game_is_running = False

    if rocket_was_fired and \
            alien_x < rocket_x < alien_x + alien_width - rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocket_was_fired = False
        alien_x, alien_y = randint(0, screen_width - alien_width), 0
        alien_speed += ALIEN_STEP / 2
        game_score += 1

    if rocket_was_fired and \
            alien_two_x < rocket_x < alien_two_x + alien_two_width - rocket_width and \
            alien_two_y < rocket_y < alien_two_y + alien_two_height - rocket_height:
        rocket_was_fired = False
        alien_two_x, alien_two_y = randint(0, screen_width - alien_two_width), 0
        alien_two_speed += ALIEN_TWO_STEP / 2
        game_second_score += 1

    if rocket_was_fired and \
            alien_three_x < rocket_x < alien_three_x + alien_three_width - rocket_width and \
            alien_three_y < rocket_y < alien_three_y + alien_three_height - rocket_height:
        rocket_was_fired = False
        alien_three_x, alien_three_y = randint(0, screen_width - alien_three_width), 0
        alien_three_speed += ALIEN_THREE_STEP / 2
        game_score += 1

    if rocket_was_fired and \
            alien_four_x < rocket_x < alien_four_x + alien_four_width - rocket_width and \
            alien_four_y < rocket_y < alien_four_y + alien_four_height - rocket_height:
        rocket_was_fired = False
        alien_four_x, alien_four_y = randint(0, screen_width - alien_four_width), 0
        alien_four_speed += ALIEN_FOUR_STEP / 2
        game_score += 1

    if rocket_was_fired and \
            alien_five_x < rocket_x < alien_five_x + alien_five_width - rocket_width and \
            alien_five_y < rocket_y < alien_five_y + alien_five_height - rocket_height:
        rocket_was_fired = False
        alien_five_x, alien_five_y = randint(0, screen_width - alien_five_width), 0
        alien_five_speed += ALIEN_FIVE_STEP / 2
        game_score += 1

    if rocket_was_fired and \
            rayna_x < rocket_x < rayna_x + rayna_width - rocket_width and \
            rayna_y < rocket_y < rayna_y + rayna_height - rocket_height:
        rocket_was_fired = False
        rayna_x, rayna_y = randint(0, screen_width - rayna_width), 0
        rayna_speed += RAYNA_STEP / 2
        game_second_score += 1

    if rocket_was_fired and \
            devil_x < rocket_x < devil_x + devil_width - rocket_width and \
            devil_y < rocket_y < devil_y + devil_height - rocket_height:
        rocket_was_fired = False
        devil_x, devil_y = randint(0, screen_width - devil_width), 0
        devil_speed += DEVIL_STEP / 2
        game_second_score += 1

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()