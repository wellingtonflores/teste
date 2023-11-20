from controller.config_init_game_controller import *

#  (parametros)
altura = 650 # ALTURA DA WINDOW
largura = 900  # LARGURA DA WINDOW
col = 15 # LARGURA DA GRID
row = 15 # ALTURA DA GRID
MARGIN = 1 # MARGEM DOS BLOCOS DA GRID
WIDTH = 20 # LARGURA DOS BLOCOS DA DA GRID
HEIGHT = 20 # ALTURA DOS BLOCOS DA DA GRID

config = ConfigInitGameController()
screen = config.screen(largura, altura)
clock = pygame.time.Clock()

def quit_game():
    pygame.display.quit()
# end method quit_game

def wait_players():
    request = RequestConnectionsController()
    accept = AcceptConnectionsController()

    try:
        font = pygame.font.SysFont(None, 30)
        text = font.render('Aguardando Jogador', True, config.background_color('green'))
        screen.blit(text, [largura / 2, altura / 2])
        pygame.display.update()  # Go ahead and update the screen with what we've drawn.

        time.sleep(1.5)
        request.request()
        accept.stop()
        return 'Player 2'
    except:
        try:
            font = pygame.font.SysFont(None, 30)
            text = font.render('Aguardando Jogador', True, config.background_color('green'))
            screen.blit(text, [largura / 2, altura / 2])
            pygame.display.update()  # Go ahead and update the screen with what we've drawn.

            time.sleep(1.5)
            accept.listen()
            return 'Player 1'
        except socket.error as err:
            print(err)
# end method wait_players

def menu_game():
    im_menu = pygame.image.load(
        'images\menu_batalha_naval.png')
    screen.blit(im_menu, [0, 0])
# end method menu_game



def start_menu_game():
    # Variável para controlar o jogo
    done = False
    while not done:
        screen.fill(config.background_color('white'))
        menu_game()
        for event in pygame.event.get():  # User did something
            try:
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    quit_game()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x >= 0 and y >= 48 and x <= 180 and y <= 90:
                        arg0 = wait_players()
                        arg0 = None
                        start_game(arg0)
                    if x >= 0 and y >= 183 and x <= 180 and y <= 225:
                        quit_game()
                        return 0
            except socket.error as err:
                print("erro", err)
        clock.tick(60) # Limit to 60 frames per second
        try:
            pygame.display.update()  # Go ahead and update the screen with what we've drawn.
        except:
            break
# end method start_menu_game

def start_game(arg0):
    grid_ships = config.grid(col, row)
    grid_shots = config.grid(col, row)
    # Variável para controlar o jogo
    done = False
    while not done:
        screen.fill(config.background_color('white'))
        for event in pygame.event.get():  # User did something
            try:
                if event.type == pygame.QUIT:  # If user clicked close
                    quit_game()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    try:
                        try:
                            # set grid_ships
                            ROW = y // (HEIGHT + MARGIN)
                            COL = x // (WIDTH + MARGIN)
                            if COL >= 0 and ROW >= 0:
                                grid_ships[ROW][COL] = 1
                                print([COL, x], [ROW, y])

                        except:
                            # set grid_ships
                            ROW = y // (HEIGHT + MARGIN)
                            COL = (x - (largura - ((MARGIN + WIDTH) * col))) // (WIDTH + MARGIN)
                            if COL >= 0 and ROW >= 0:
                                grid_shots[ROW][COL] = 1
                                print([COL, x], [ROW, y])
                    except:
                        print('except')

                    # print(x, y)
                    if x >= 829 and y >= 620 and x <= 899 and y <= 650:
                        quit_game()
                        return 0
                    if x >= 758 and y >= 620 and x <= 828 and y <= 650:
                        start_menu_game()
                        return 0
            except:
                print("erro")

        draw_grid_ships(grid_ships) # desenha o grid dos navios
        draw_grid_shots(grid_shots) # desenha o grid dos tiros
        giveup_button() # desenha o botão de desistir
        exit_button() # desenha o botão de exit
        status_bar() # desenha a barra de status
        ships_legend() # desenha as legendas dos navios

        # Update screen ever 30 frames per second
        clock.tick(30)  # Limit to 30 frames per second
        try:
            pygame.display.update()  # Go ahead and update the screen with what we've drawn.
        except:
            break
# end method start_game

def draw_grid_shots(grid_shots):
    for i in range(row):
        for j in range(col):
            color = config.background_color('black')
            if grid_shots[i][j] == 1:
                color = config.background_color('red')
            pygame.draw.rect(screen, color,
                             [(largura - ((MARGIN + WIDTH) * col) + ((MARGIN + WIDTH) * j)),
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH, HEIGHT])
    pygame.draw.rect(screen, config.background_color('blue'),
                     [(largura - ((MARGIN + WIDTH) * col)),
                      (MARGIN + HEIGHT) * row + MARGIN,
                      (MARGIN + HEIGHT) * col - MARGIN, 50])
    font = pygame.font.SysFont(None, 30)
    text = font.render('SHOTS', True, config.background_color('white'))
    screen.blit(text, [(largura - ((MARGIN + WIDTH) * col)) + 3,
                       (MARGIN + HEIGHT) * row + MARGIN + 15])
# end method draw_grid_shots

def draw_grid_ships(grid_ships):
    for i in range(row):
        for j in range(col):
            color = config.background_color('black')
            if grid_ships[i][j] == 1:
                color = config.background_color('yellow')
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH, HEIGHT])
    pygame.draw.rect(screen, config.background_color('blue'),
                     [MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                      (MARGIN + HEIGHT) * col - MARGIN, 50])
    font = pygame.font.SysFont(None, 30)
    text = font.render('SHIPS', True, config.background_color('white'))
    screen.blit(text, [3, (MARGIN + HEIGHT) * row + MARGIN + 15])
# end method draw_grid_ships

def status_bar():
    pygame.draw.rect(screen, config.background_color('black'), [1, 620, 756, 650])
    font = pygame.font.SysFont(None, 25)
    text = font.render('Status:', True, config.background_color('white'))
    screen.blit(text, [3, 627])
# end method status_bar

def giveup_button():
    pygame.draw.rect(screen, config.background_color('red'), [758, 620, 70, 650])
    font = pygame.font.SysFont(None, 25)
    text = font.render('Give Up', True, config.background_color('white'))
    screen.blit(text, [760, 627])
# end method giveup_button

def exit_button():
    pygame.draw.rect(screen, config.background_color('red'), [829, 620, 70, 650])
    font = pygame.font.SysFont(None, 25)
    text = font.render('Exit', True, config.background_color('white'))
    screen.blit(text, [848, 627])
# end method back_button

def ships_legend():
    font = pygame.font.SysFont(None, 25)
    pygame.draw.rect(screen, config.background_color('black'), [0, 382, 315, 30])
    fragata = font.render('fragata', True, config.background_color('white'))
    screen.blit(fragata, [3, 382])

    pygame.draw.rect(screen, config.background_color('black'), [0, 416, 315, 30])
    corveta = font.render('corveta', True, config.background_color('white'))
    screen.blit(corveta, [3, 416])

    pygame.draw.rect(screen, config.background_color('black'), [0, 450, 315, 30])
    destroier= font.render('destroier', True, config.background_color('white'))
    screen.blit(destroier, [3, 450])

    pygame.draw.rect(screen, config.background_color('black'), [0, 484, 315, 30])
    cruzador = font.render('cruzador', True, config.background_color('white'))
    screen.blit(cruzador, [3, 484])

    pygame.draw.rect(screen, config.background_color('black'), [0, 518, 315, 30])
    submarino = font.render('submarino', True, config.background_color('white'))
    screen.blit(submarino, [3, 518])

    pygame.draw.rect(screen, config.background_color('black'), [0, 552, 315, 30])
    encouracado = font.render('encouracado', True, config.background_color('white'))
    screen.blit(encouracado, [3, 552])

    pygame.draw.rect(screen, config.background_color('black'), [0, 586, 315, 30])
    porta_avioes = font.render('porta_avioes', True, config.background_color('white'))
    screen.blit(porta_avioes, [3, 586])
# end method ships
