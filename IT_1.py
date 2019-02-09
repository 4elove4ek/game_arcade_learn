import arcade
import random

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 880

CELL_SIZE = 16

SCREEN_COLOR = arcade.color.WHITE

CELL_LINE_COLOR = arcade.color.GRAY_BLUE

COLOR_RED = arcade.color.RED


def draw_cells():
    for i in range(SCREEN_HEIGHT // CELL_SIZE):
        arcade.draw_line(0, i * CELL_SIZE, SCREEN_WIDTH, i * CELL_SIZE, CELL_LINE_COLOR)

    for j in range(SCREEN_WIDTH // CELL_SIZE):

        if j == SCREEN_WIDTH // CELL_SIZE - 4:

            tmp_color = COLOR_RED

            tmp_size = 4



        else:

            tmp_color = CELL_LINE_COLOR

            tmp_size = 1

        arcade.draw_line(j * CELL_SIZE, 0, j * CELL_SIZE, SCREEN_HEIGHT, tmp_color, tmp_size)




arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Title window')

arcade.set_background_color(SCREEN_COLOR)

arcade.start_render()

draw_cells()

arcade.draw_text('Домашняя работа.', CELL_SIZE * 19, CELL_SIZE * 50, arcade.color.BLUE, 20, italic=True)
arcade.draw_text('N 666', CELL_SIZE * 24, CELL_SIZE * 48, arcade.color.BLUE, 20, italic=True)
o = random.randint(7, 15)
for i in range(o):
    a = random.randint(0, 1000)
    b = random.randint(a + 1, a + 1000)
    z = random.randint(1, 2)
    if z == 1:
        arcade.draw_text('{} > {}'.format(a, b), CELL_SIZE * 1, CELL_SIZE * (46 - 2 * i), arcade.color.BLUE, 20, italic=True)
    else:
        arcade.draw_text('{} < {}'.format(b, a), CELL_SIZE * 1, CELL_SIZE * (46 - 2 * i), arcade.color.BLUE, 20, italic=True)
arcade.draw_text('2.', CELL_SIZE * 23, CELL_SIZE * 20, arcade.color.RED, 60, italic=True)
for i in range(o):
    arcade.draw_text('-', CELL_SIZE * 10, CELL_SIZE * (46 - 2 * i), arcade.color.RED, 30, italic=True)

arcade.finish_render()
arcade.run()
