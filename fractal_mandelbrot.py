import time

import pygame
from numba import njit
from pygame import gfxdraw

SIZE = 600


def draw_pixel(screen, x, y, color):
    gfxdraw.pixel(screen, x, y, color)


@njit(fastmath=True)
def mandelbrot(user_view, scale, num_of_iterations):
    for y in range(-SIZE // 2 + user_view[1], SIZE // 2 + user_view[1]):
        for x in range(-SIZE // 2 + user_view[0], SIZE // 2 + user_view[0]):
            a = x / scale
            b = y / scale
            c = complex(a, b)
            z = complex(0)
            n = 0
            for n in range(num_of_iterations):
                z = z ** 5 + c
                if abs(z) > 100:
                    break
            color = n * 2.55
            yield x + SIZE//2 - user_view[0], y + SIZE//2 - user_view[1], (color, color, color)


def main():
    x, y = 0, 0
    scale = 150
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    now_mandelbrot = mandelbrot((x, y), scale, 100)
    for iterator in now_mandelbrot:
        draw_pixel(screen, iterator[0], iterator[1], iterator[2])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x0, y0 = pygame.mouse.get_pos()

                x = x0
                y = y0
                scale *= 2

                now_mandelbrot = mandelbrot((x, y), scale, 100)
                for iterator in now_mandelbrot:
                    draw_pixel(screen, iterator[0], iterator[1], iterator[2])
        pygame.display.update()


if __name__ == "__main__":
    main()

