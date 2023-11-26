# Class: Information Systems 2023/2
# Students: João Castro, Juliana Ballin, Caio Jorge, Caio Pereira
# Year: 2023

import pygame
import time
import os
import random

# Initialize Pygame (Inicializa o Pygame)
pygame.init()

# Define colors (Define as cores)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Maximum score (Pontuação máxima)
SCORE_MAX = 3

# Set the screen size and create a Pygame display (Define o tamanho da tela e cria a janela do Pygame)
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2023-11-28")

# Initialize clocks for various time measurements (Inicializa relógios para diferentes medidas de tempo)
initial_clock = time.time()
final_clock = time.time()

uper_wall_final_clock = time.time()
uper_wall_initial_clock = time.time()

lower_wall_final_clock = time.time()
lower_wall_initial_clock = time.time()

# Hit counter (Contador de colisões)
hit_counter = 0

# Create text objects for score, victory, and restart messages (Cria objetos de texto para pontuação, vitória e mensagens de reinício)
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text (Texto de Vitória)
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# restart text (Texto de jogar novamente)
restart_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
restart_text = restart_font .render('PRESSIONE "R" PARA REINICIAR', True, COLOR_WHITE, COLOR_BLACK)
restart_text_rect = score_text.get_rect()
restart_text_rect.center = (500, 500)

# Load sound effects and music (Carrega efeitos sonoros e música)
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# Music list (Lista de músicas)
music_list = ['assets/musica1.mp3', 'assets/musica2.mp3', 'assets/musica3.mp3', 'assets/musica4.mp3']
current_song = 0

# Music starting (Inicia a música)
pygame.mixer.music.load(music_list[current_song])
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# Player 1 (Jogador 1)
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# Player 2 - robot (Jogador 2 - robô)
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300

# Ball (Bola)
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# Score (Pontuação)
score_1 = 0
score_2 = 0

# Game over (Fim de jogo)
game_over = False

# Difficulty (Dificuldade)
difficult = 0

# Game loop (Loop principal do jogo)
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    # Music skip (Pular música)
    if not pygame.mixer.music.get_busy():
        current_song = (current_song + 1) % len(music_list)
        pygame.mixer.music.load(music_list[current_song])
        pygame.mixer.music.play()

    # Keystroke events (Eventos de teclas pressionadas)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True

            # Restart the game if 'R' is pressed when it's over (Reinicia o jogo se 'R' for pressionado quando acabar)
            if game_over:
                if event.key == pygame.K_r:
                    player_1_y = 300
                    player_2_y = 300
                    ball_x = 640
                    ball_y = 360
                    ball_dx = 5
                    ball_dy = 5
                    score_1 = 0
                    score_2 = 0
                    difficult = 0
                    game_over = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # Checking the victory condition (Verificando a condição de vitória)
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # Clear screen (Limpa a tela)
        screen.fill(COLOR_BLACK)

        # Ball collision with the wall (Colisão da bola com a parede)
        if ball_y > 700:
            uper_wall_final_clock = time.time()
            if 0.001 < uper_wall_final_clock - uper_wall_initial_clock:
                print(uper_wall_final_clock - uper_wall_initial_clock)
                ball_dy *= -1
                bounce_sound_effect.play()
                uper_wall_initial_clock = time.time()
                print('colidi em baixo')
        elif ball_y <= 0:
            lower_wall_final_clock = time.time()
            if 0.001 < lower_wall_final_clock - lower_wall_initial_clock:
                print(lower_wall_final_clock - lower_wall_initial_clock)
                ball_dy *= -1
                bounce_sound_effect.play()
                lower_wall_initial_clock = time.time()
                print('colidi em cima')

        # Ball collision with the player 1's paddle (Colisão da bola com a raquete do jogador 1)
        if ball_x < 100:
            if player_1_y < ball_y + 25:
                if player_1_y + 150 > ball_y:
                    final_clock = time.time()
                    if 0.1 < final_clock - initial_clock:
                        if ball_x > 50:
                            initial_clock = time.time()
                            ball_dx *= -1
                            ball_dy = random.uniform(-7, 7)
                            if abs(ball_dy) < 3:
                                ball_dy = 3 if ball_dy > 0 else -3
                            difficult += random.randint( (int(-1 * (abs(1* ball_dx))/2)), int(abs(1 * ball_dx)))
                            bounce_sound_effect.play()
                            hit_counter += 1
                            if ball_x < 80:
                                ball_dy *= -1

        # Ball collision with the player 2's paddle4 (Colisão da bola com a raquete do jogador 2)
        if ball_x > 1160:
            if player_2_y < ball_y + 25:
                if player_2_y + 150 > ball_y:
                    ball_dx *= -1
                    ball_dy = random.uniform(-7, 7)
                    if abs(ball_dy) < 3:
                        ball_dy = 3 if ball_dy > 0 else -3
                    bounce_sound_effect.play()
                    hit_counter += 1

        # Scoring points (Marcar pontos)
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dy *= -0.6
            ball_dx *= -0.6
            score_2 += 1
            difficult = 0
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dy *= -0.6
            ball_dx *= -0.6
            score_1 += 1
            difficult = 0
            scoring_sound_effect.play()

        # Ball movement (Movimento da bola)
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # Increase speed (Aumentar velocidade)
        if hit_counter >= 3:
            ball_dx *= 1.2
            ball_dy *= 1.2
            hit_counter = 0

        # Player 1 up movement (Movimento para cima do jogador 1)
        if player_1_move_up:
            player_1_y -= 10
        else:
            player_1_y += 0

        # Player 1 down movement (Movimento para baixo do jogador 1)
        if player_1_move_down:
            player_1_y += 10
        else:
            player_1_y += 0

        # Player 1 collides with upper wall (Colisão do jogador 1 com a parede superior)
        if player_1_y <= 0:
            player_1_y = 0

        # Player 1 collides with lower wall (Colisão do jogador 1 com a parede inferior)
        elif player_1_y >= 570:
            player_1_y = 570

        # Player 2 "Artificial Intelligence" (Jogador 2 "Inteligência Artificial")
        player_2_y = ball_y + difficult
        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # Update score HUD (Atualiza o HUD de pontuação)
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # Drawing objects on the screen (Desenha objetos na tela)
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        game_over = True
        # Drawing victory (Desenha a mensagem de vitória)
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)
        screen.blit(restart_text, restart_text_rect)

    # Update screen (Atualiza a tela)
    pygame.display.flip()
    game_clock.tick(60)

# Quit Pygame (Encerra o Pygame)
pygame.quit()
