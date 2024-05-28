# Importujeme potřebné knihovny
import pygame
import math



# Vytvoření obrazovky
pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('myFont.ttf', 32)
big_font = pygame.font.Font('myFont.ttf', 60)
WIDTH = 896
HEIGHT = 799
screen = pygame.display.set_mode([WIDTH, HEIGHT])



# Definování všech potřebných proměnných
pozadi = []
banners = []
zbrane = []
terce_img = [[], [], []]
terce = {1: [10, 8, 5],
           2: [15, 10, 8], 
           3: [17, 12, 8, 6]} 


level = 0
body = 0
celkem_strel = 0
mode = 0
naboje = 0
ubehly_cas = 0
zbyvajici_cas = 0
pocitadlo = 1
best_cas = 0
best_naboje = 0
best_zbyvajici_cas = 0


shot = False
menu = True
game_over = False
pauza = False
clicked = False
vypsat_hodnoty = False
nove_coords = True


coords1 = [[], [], []]
coords2 = [[], [], []]
coords3 = [[], [], [], []]


# Načtení obrázků
terce_obr = [
    ["obr1.png", "obr1.png", "obr1.png"],
    ["obr2.png", "obr2.png", "obr2.png"],
    ["obr3.png", "obr3.png", "obr3.png", "obr3.png"]
]

pozadi_obr = [
    "pozadi1.png",
    "pozadi2.png",
    "pozadi3.png"
]

zbrane_obr = [
    "gun1.png",
    "gun2.png",
    "gun3.png"
]



#Import obrázků
menu_img = pygame.image.load(f'mainmenu.png')
game_over_img = pygame.image.load(f'gameover.png')
pause_img = pygame.image.load(f'pause.png')



# Tento kod má za následek, že v každém levelu je vždy nové pozadí, zbraň a terče. 
for i in range(1, 4):
    pozadi.append(pygame.image.load(pozadi_obr[i - 1]))
    banners.append(pygame.image.load(f'banner.png'))
    zbrane.append(pygame.transform.scale(pygame.image.load(zbrane_obr[i- 1]), (50, 200)))
    # Pro level 1 a 2.
    if i < 3:
        for j in range(1, 4):
            terce_img[i - 1].append(pygame.transform.scale(
                pygame.image.load(terce_obr[i - 1][j - 1]), (120 - (j * 18), 80 - (j * 12))))
    # Pro level 3.
    else:
        for j in range(1, 5):
            terce_img[i - 1].append(pygame.transform.scale(
                pygame.image.load(terce_obr[i - 1][j - 1]), (120 - (j * 18), 80 - (j * 12))))


# Tento kod má za následek výpis skore, které se ukazuje dole na banneru při každém modu.
def vzhled_score():
    if mode == 0:
        body_text = font.render(f'----------', True, 'black')
        screen.blit(body_text, (320, 660))
        shots_text = font.render(f'Trenink', True, 'black')
        screen.blit(shots_text, (320, 687))
        cas_text = font.render(f'Trenink', True, 'black')
        screen.blit(cas_text, (320, 714))
        mode_text = font.render(f'------------', True, 'black')

    if mode == 1:
        body_text = font.render(f'Body: {body}', True, 'black')
        screen.blit(body_text, (320, 660))
        shots_text = font.render(f'Vystrelene naboje: {celkem_strel}', True, 'black')
        screen.blit(shots_text, (320, 687))
        cas_text = font.render(f'Ubehly cas: {ubehly_cas}', True, 'black')
        screen.blit(cas_text, (320, 714))
        mode_text = font.render(f'Pocet naboju: {naboje}', True, 'black')

    if mode == 2:
        body_text = font.render(f'Body: {body}', True, 'black')
        screen.blit(body_text, (320, 660))
        shots_text = font.render(f'Vystrelene naboje: {celkem_strel}', True, 'black')
        screen.blit(shots_text, (320, 687))
        cas_text = font.render(f'Ubehly cas: {ubehly_cas}', True, 'black')
        screen.blit(cas_text, (320, 714))
        mode_text = font.render(f'Zbyvajici cas: {zbyvajici_cas}', True, 'black')

    if mode == 3:
        body_text = font.render(f'------------', True, 'black')
        screen.blit(body_text, (320, 660))
        shots_text = font.render(f'Vystrelene naboje: {celkem_strel}', True, 'black')
        screen.blit(shots_text, (320, 687))
        cas_text = font.render(f'Ubehly cas: {ubehly_cas}', True, 'black')
        screen.blit(cas_text, (320, 714))
        mode_text = font.render(f'------------', True, 'black')
    screen.blit(mode_text, (320, 741))


# Tato část kodu obstarává všechny vlastnoti ohledně vzhledu zbraně.
def vzhled_zbran():
    # Pozice myši
    mouse_pos = pygame.mouse.get_pos()
    zbran_point = (WIDTH / 2, HEIGHT - 300)
    lasers = ['white', 'black', 'white']
    clicks = pygame.mouse.get_pressed()
    ####################################
    # Výpočet úhlů a rotace zbraně.
    if mouse_pos[0] != zbran_point[0]:
        sklon = (mouse_pos[1] - zbran_point[1]) / (mouse_pos[0] - zbran_point[0])
    else:
        sklon = -100000
    uhel = math.atan(sklon)
    rotation = math.degrees(uhel)
    ###################################
    # Určení vhodné rotace vzhledem k oknu a správné vykreslení zbraně.
    if mouse_pos[0] < WIDTH / 2:
        zbran = pygame.transform.flip(zbrane[level - 1], True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(zbran, 90 - rotation), (WIDTH / 2 - 30, HEIGHT - 350))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
    else:
        zbran = zbrane[level - 1]
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(zbran, 270 - rotation), (WIDTH / 2 - 30, HEIGHT - 350))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)


# Tato část kodu zajištuje přesun objektu zprava do leva, dělá také to, že se vždy na konci objekt přemístí zpátky doprava.
def move_level(coords):
    if level == 1 or level == 2:
        max_hodnota = 3
    else:
        max_hodnota = 4
    for i in range(max_hodnota):
        for j in range(len(coords[i])):
            moje_coords = coords[i][j]
            if moje_coords[0] < -150:
                coords[i][j] = (WIDTH, moje_coords[1])
            else:
                coords[i][j] = (moje_coords[0] - 2 ** i, moje_coords[1])
    return coords


# Tato funkce vytváří kolizní obdélníky pro terče a zároveň je vykresluje na obrazovku. 
def vzhled_level(coords):
    if level == 1 or level == 2:
        terce_rects = [[], [], []]
    else:
        terce_rects = [[], [], [], []]
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            terce_rects[i].append(pygame.rect.Rect((coords[i][j][0] + 20, coords[i][j][1]),
                                                    (60 - i * 12, 60 - i * 12)))
            screen.blit(terce_img[level - 1][i], coords[i][j])
    return terce_rects

# Tato funkce zajišťuje detekci střelby na terče, pokud je terč zasažne, je tento terč odstraněn.
def check_shot(terce, coords):
    global body
    mouse_pos = pygame.mouse.get_pos()
    for i in range(len(terce)):
        for j in range(len(terce[i])):
            if terce[i][j].collidepoint(mouse_pos):
                coords[i].pop(j)
                body += 10 + 10 * (i ** 2)
    return coords


# Tato část kodu má na starost vzhled hlavního menu.
def vzhled_menu():
    global game_over, pauza, mode, level, menu, ubehly_cas, celkem_strel, body, naboje
    global zbyvajici_cas, best_naboje, best_zbyvajici_cas, best_cas, vypsat_hodnoty, clicked, nove_coords
    game_over = False
    pauza = False
    screen.blit(menu_img, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()


    # Vytvýří zony, kde se zaregistruje kliknutí.
    training_tlacitko = pygame.rect.Rect((190, 538), (260, 100))
    #training_tlacitko = pygame.draw.rect(screen, "green", [190, 538, 260, 100], 3)

    screen.blit(font.render(f'{best_naboje}', True, 'black'), (700, 587))
    naboje_tlacitko = pygame.rect.Rect((495, 538), (260, 100))
    #naboje_tlacitko = pygame.draw.rect(screen, "green", [495, 538, 260, 100], 3)

    screen.blit(font.render(f'{best_zbyvajici_cas}', True, 'black'), (400, 726))
    zbyvajici_cas_tlacitko = pygame.rect.Rect((190, 675), (260, 100))
    #zbyvajici_cas_tlacitko = pygame.draw.rect(screen, "green", [190, 675, 260, 100], 3)

    screen.blit(font.render(f'{best_cas}', True, 'black'), (700, 728))
    best_cas_tlacitko = pygame.rect.Rect((495, 675), (260, 100))
    #best_cas_tlacitko = pygame.draw.rect(screen, "green", [495, 675, 260, 100], 3)

    reset_tlacitko = pygame.rect.Rect((340, 400), (260, 100))
    #reset_tlacitko = pygame.draw.rect(screen, "green", [340, 400, 260, 100], 3)


    ################################


    # Tyto podmínky tvoři tlačítka, podle toho na jaký se klikne, takový mod se spustí.
    # not clicked mi provádí, aby hra zaregistrovala pouze první kliknutí na tlačítko 
    if training_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 0
        level = 1
        menu = False
        ubehly_cas = 0
        celkem_strel = 0
        body = 0
        clicked = True
        nove_coords = True

    if naboje_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 1
        level = 1
        menu = False
        ubehly_cas = 0
        naboje = 99
        celkem_strel = 0
        body = 0
        clicked = True
        nove_coords = True

    if zbyvajici_cas_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 2
        level = 1
        menu = False
        zbyvajici_cas = 45
        ubehly_cas = 0
        celkem_strel = 0
        body = 0
        clicked = True
        nove_coords = True

    if best_cas_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 3
        level = 1
        menu = False
        ubehly_cas = 0
        celkem_strel = 0
        body = 0
        clicked = True
        nove_coords = True
    
    if reset_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        best_cas = 0
        best_naboje = 0
        best_zbyvajici_cas = 0
        clicked = True
        vypsat_hodnoty = True


# Funkce zajištujicí konec hry.
# Pokud uživatel stiskne návrat do menu, uvidí zde své skore.
# Pokud uživatel klidne na exit, hra se vypne.
def vzhled_game_over():
    global clicked, level, pauza, game_over, menu, body, celkem_strel, ubehly_cas, zbyvajici_cas
    if mode == 3:
        display_score = ubehly_cas
    else:
        display_score = body
    screen.blit(game_over_img, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    exit_tlacitko = pygame.rect.Rect((170, 661), (260, 100))
    menu_tlacitko = pygame.rect.Rect((475, 661), (260, 100))
    screen.blit(big_font.render(f'{display_score}', True, 'white'), (650, 580))
    if menu_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        clicked = True
        level = 0
        pauza = False
        game_over = False
        menu = True
        body = 0
        celkem_strel = 0
        ubehly_cas = 0
        zbyvajici_cas = 0
    if exit_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        global run
        run = False


# Vzhled pro tlačítko pauzy.
def vzhled_pauza():
    global level, pauza, menu, body, celkem_strel, ubehly_cas, zbyvajici_cas, clicked, nove_coords
    screen.blit(pause_img, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    pokracovat_tlacitko = pygame.rect.Rect((170, 661), (260, 100))
    menu_tlacitko = pygame.rect.Rect((475, 661), (260, 100))
    if pokracovat_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level = pokracovat_level
        pauza = False
        clicked = True
    if menu_tlacitko.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level = 0
        pauza = False
        menu = True
        body = 0
        celkem_strel = 0
        ubehly_cas = 0
        zbyvajici_cas = 0
        clicked = True
        nove_coords = True

# Kod pro celkový chod hry
run = True
while run:
    timer.tick(fps)
    if level != 0:
        if pocitadlo < 60:
            pocitadlo += 1
        else:
            pocitadlo = 1
            ubehly_cas += 1
            if mode == 2:
                zbyvajici_cas -= 1

    #Tato část aktualizuje souřadnice cílů. Má na starost, že se vždy po spuštění nového levelu souřadnice resetují.
    if nove_coords:
        coords1 = [[], [], []]
        coords2 = [[], [], []]
        coords3 = [[], [], [], []]
        for i in range(3):
            my_list = terce[1]
            for j in range(my_list[i]):
                coords1[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
        for i in range(3):
            my_list = terce[2]
            for j in range(my_list[i]):
                coords2[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
        for i in range(4):
            my_list = terce[3]
            for j in range(my_list[i]):
                coords3[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 100) + 30 * (j % 2)))
        nove_coords = False

    # Tento blok kodu řídí zobrazení herního prostředí v závislosti na aktuálním levelu a herním stavu.
    screen.fill('black')
    screen.blit(pozadi[level - 1], (0, 0))
    screen.blit(banners[level - 1], (0, HEIGHT - 200))
    if menu:
        level = 0
        vzhled_menu()
    if game_over:
        level = 0
        vzhled_game_over()
    if pauza:
        level = 0
        vzhled_pauza()

    if level == 1:
        terce_boxes = vzhled_level(coords1)
        coords1 = move_level(coords1)
        if shot:
            coords1 = check_shot(terce_boxes, coords1)
            shot = False
    elif level == 2:
        terce_boxes = vzhled_level(coords2)
        coords2 = move_level(coords2)
        if shot:
            coords2 = check_shot(terce_boxes, coords2)
            shot = False
    elif level == 3:
        terce_boxes = vzhled_level(coords3)
        coords3 = move_level(coords3)
        if shot:
            coords3 = check_shot(terce_boxes, coords3)
            shot = False
    if level > 0:
        vzhled_zbran()
        vzhled_score()

    # Závěrečná část kodu je určena pro hlavní herní smyčku hry.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if (0 < mouse_position[0] < WIDTH) and (0 < mouse_position[1] < HEIGHT - 200):
                shot = True
                celkem_strel += 1
                if mode == 1:
                    naboje -= 1
            if (670 < mouse_position[0] < 860) and (660 < mouse_position[1] < 715):
                pokracovat_level = level
                pauza = True
                clicked = True
            if (670 < mouse_position[0] < 860) and (715 < mouse_position[1] < 760):
                menu = True
                clicked = True
                nove_coords = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked:
            clicked = False

    if level > 0:
        if terce_boxes == [[], [], []] and level < 3:
            level += 1
        if (level == 3 and terce_boxes == [[], [], [], []]) or (mode == 1 and naboje == 0) or (
                mode == 2 and zbyvajici_cas == 0):
            nove_coords = True

            if mode == 1:
                if body > best_naboje:
                    best_naboje = body
                    vypsat_hodnoty = True

            if mode == 2:
                if body > best_zbyvajici_cas:
                    best_zbyvajici_cas = body
                    vypsat_hodnoty = True

            if mode == 3:
                if level == 3:
                    best_cas = ubehly_cas
                    vypsat_hodnoty = True
                    
            game_over = True
    pygame.display.flip()
pygame.quit()