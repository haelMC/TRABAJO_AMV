import pygame
import numpy as np
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Optimización de Rutas de Transporte")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configuración de carritos
num_carritos = 5
carritos = []

for _ in range(num_carritos):
    carritos.append({
        'pos': np.array([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]),
        'destino': np.array([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]),
        'speed': random.uniform(1, 3)
    })

# Función para mover carritos hacia su destino
def mover_carritos():
    for carrito in carritos:
        direction = carrito['destino'] - carrito['pos']
        distance = np.linalg.norm(direction)
        
        if distance > 1:  # Si no ha llegado al destino
            direction = direction / distance  # Normalizar la dirección
            carrito['pos'] += (direction * carrito['speed']).astype(int)  # Moverse en la dirección del destino

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mover_carritos()

    # Dibujar carritos y destinos
    for carrito in carritos:
        pygame.draw.circle(screen, BLUE, carrito['pos'].astype(int), 10)  # Carrito
        pygame.draw.circle(screen, RED, carrito['destino'].astype(int), 5)  # Destino

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
