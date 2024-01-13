# Atividade 009: Atividade 009: Animação com PyGame (trabalho individual)
# Nome: Juliana Ballin Lima 
# Matrícula: 2315310011

import pygame
import sys
import os
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sonic Animation")

# Cores
white = (255, 255, 255)

# Caminhos das imagens
base_path = os.path.join("C:\\Users\\JuhBa\\Documents\\GitHub\\atividade009\\animacao-sonic")

image_path = os.path.join(base_path, "imagens", "sonic.png")
background_path = os.path.join(base_path, "background.png")
walk_frames = [os.path.join(base_path, "imagens", f"sonic_walk_{i}.png") for i in range(3)]
run_frames = [os.path.join(base_path, "imagens", f"sonic_run_{i}.png") for i in range(3)]
jump_path = os.path.join(base_path, "imagens", "sonic_jump.png")

# Carrega as imagens
sonic_image = pygame.image.load(image_path)
background = pygame.image.load(background_path)
walk_frames = [pygame.image.load(path) for path in walk_frames]
run_frames = [pygame.image.load(path) for path in run_frames]
jump_frame = pygame.image.load(jump_path)

# Personagem Sonic
sonic_rect = sonic_image.get_rect()
sonic_rect.topleft = (100, height - sonic_rect.height - 140)  # Posiciona 140 pixels acima da parte inferior

# Variáveis de movimento
move_left = False
move_right = False
is_jumping = False
jump_count = 10

# Configurações de animação
clock = pygame.time.Clock()
animation_speed = 15  # Aumente a velocidade de animação
current_frame = 0

# Direção do Sonic
facing_left = False

# Velocidade de movimento
speed = 5

# Tempo de tecla pressionada para ativar corrida
press_duration_for_run = 3  # 3 segundos
start_time = time.time()

# Velocidade de corrida
run_speed = 60

# Loop principal
while True:
    pygame.event.pump()  # Processa eventos

    screen.blit(background, (0, 0))  # Renderiza o fundo

    keys = pygame.key.get_pressed()

    # Calcula a duração da tecla pressionada
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        if not move_left and not move_right:
            start_time = time.time()
        elapsed_time = time.time() - start_time
        if elapsed_time > press_duration_for_run:
            speed = run_speed  # Aumenta a velocidade para 60 se a tecla for mantida pressionada por mais de 3 segundos

    if keys[pygame.K_LEFT]:
        sonic_rect.x -= speed
        facing_left = True
        current_frame += 1
    if keys[pygame.K_RIGHT]:
        sonic_rect.x += speed
        facing_left = False
        current_frame += 1

    # Atualizações de pulo
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            sonic_rect.y -= int((jump_count ** 2) * 0.5 * neg)
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Limita o sonic à tela
    if sonic_rect.left < 0:
        sonic_rect.left = 0
        facing_left = False
    if sonic_rect.right > width:
        sonic_rect.right = width
        facing_left = True

    # Animação
    if current_frame >= animation_speed:
        current_frame = 0
    walk_animation = current_frame // (animation_speed // len(walk_frames))
    run_animation = current_frame // (animation_speed // len(run_frames))

    # Renderiza o personagem
    if is_jumping:
        # Virar sonic_jump para a esquerda se estiver se movendo para a esquerda
        jump_frame_render = pygame.transform.flip(jump_frame, facing_left, False)
        screen.blit(jump_frame_render, sonic_rect.topleft)
    elif facing_left:
        if walk_animation < len(walk_frames):
            screen.blit(pygame.transform.flip(walk_frames[walk_animation], True, False), sonic_rect.topleft)
    elif keys[pygame.K_LEFT]:
        if walk_animation < len(walk_frames):
            screen.blit(walk_frames[walk_animation], sonic_rect.topleft)
    elif keys[pygame.K_RIGHT]:
        if run_animation < len(run_frames):
            screen.blit(run_frames[run_animation], sonic_rect.topleft)
        else:
            screen.blit(sonic_image, sonic_rect.topleft)
    else:
        screen.blit(sonic_image, sonic_rect.topleft)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True

    # Atualizações da tela
    pygame.display.flip()
    clock.tick(30)  # FPS
