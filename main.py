import pygame
from Abalone import CreateBoard
from Players import Player

pygame.init()
size = [800, 800]
screen = pygame.display.set_mode(size)

screen.fill((150, 20, 10))

pygame.display.flip()

running = True

board = CreateBoard([e // 2 for e in size], 250)
board.draw_regular_polygon(screen, (250, 100, 50))
board.draw_regular_polygon(screen, (0, 0, 0), 5)
radius, sprites = board.draw_ceil(screen, (250, 159, 122), 2)
coordinates = board.coordinates


p1 = Player()
p1.circles = []
p1.name = "Toto"
p1.color = "white"

p2 = Player() 
p2.circles = []
p2.name = "Hercule"
p2.color = "black"

players = [p1, p2]

play = 0

list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
middle = coordinates[len(list_coo_x)//2]

indice_x = coordinates.index(middle)
indice_y = middle.index(middle[len(middle)//2])
x, y = middle[len(middle)//2]

indice =0

list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
lenX = len(list_coo_x)
lenCo = len(coordinates)
where = lenX//2

selected_circle = []

def get_coordinates(x, y):
    list_coo_x = list(range(5, 9)) + list(range(9, 4, -1))
    print(coordinates[y%len(list_coo_x)][x%list_coo_x[y%len(list_coo_x)]])

while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in sprites if s.collidepoint(pos)]

            if len(clicked_sprites) >= 1:
                coordinate_Circle = clicked_sprites[0].center

                valid = False
                # print([p.circles for p in players if coordinate_Circle in p.circles], coordinate_Circle)
                if not any(p.circles for p in players if coordinate_Circle in p.circles) and len(players[play % 2].circles)<14:
                    players[play % 2].circles.append(coordinate_Circle)
                    pygame.draw.circle(screen, players[play%2].color, coordinate_Circle, radius - 3)
                    valid = True
                play += 1
        # len([p for p in players if len(p.circles)==14]) == len(players)
        if True: 
            
            selector = pygame.draw.circle(screen, (255,255,255), (x, y) , radius, 2)

            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()

                if key[pygame.K_LEFT]:                    
                    indice_x += 1

                if key[pygame.K_RIGHT]:
                    
                    indice_x -= 1

                if key[pygame.K_UP]:
                    
                    indice_y += 1
                
                if key[pygame.K_DOWN]:
                    
                    indice_y -= 1
                    
                
                                
                pygame.draw.circle(screen, (180, 50, 0), (x, y) , radius, 2)
                
                
                x, y = get_coordinates(indice_x, indice_y)
                
                pygame.display.update()

                if key[pygame.K_SPACE]:
                    if (x,y) not in selected_circle:
                        selected_circle.append((x,y))

                print(indice, where)
                
            for circle in selected_circle:
                pygame.draw.circle(screen, (255, 0, 255), circle, radius, 2)

            # print(x, y)

    pygame.display.flip()

pygame.quit()
