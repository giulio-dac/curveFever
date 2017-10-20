# CURVE FEVER
# IMPORTS
import pygame
import random
import math
import time


# INPUTS
number_of_players = int(input("With how many players do you want to play (maximum of 3 players)?: "))

pygame.init()
pygame.font.init()

# CLASSES and FUNCTIONS

class Screen:
    """The window is completely defined in this class"""
    def __init__(self):
        self.width = 1920       #width of the screen
        self.height = 1080      #height of the screen
        self.set_screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.screen_caption = pygame.display.set_caption('Curve Fever')
        self.colour_background = (255, 255, 255)
        self.colour_text = (0, 0, 0)

    def sleep(self, seconds):           #method to pause the animation and freeze the screen
        time.sleep(seconds)

    def print_middle(self, text, size): #method to print some game message in the middle of the screen
        used_font = pygame.font.SysFont('freesansbold.ttf', size)   #importing the needed font
        text_surface = used_font.render(text, True, self.colour_text)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.width / 2), (self.height / 2))
        self.set_screen.blit(text_surface, text_rect)

    def game_start(self):               #method to generate a screen at the beginning which counts down for 3 seconds before the actual game starts

        def wipe(self):  # method to clear the screen
            self.set_screen.fill(self.colour_background)

        def update(self):  # updating the image
            pygame.display.flip()

        self.print_middle("Let's start", 100)
        update(self)
        self.sleep(1)
        wipe(self)

        self.print_middle("3 ....", 75)
        update(self)
        self.sleep(1)
        wipe(self)

        self.print_middle("2 ....", 75)
        update(self)
        self.sleep(1)
        wipe(self)

        self.print_middle("1 ....", 75)
        update(self)
        self.sleep(1)
        wipe(self)

        self.print_middle("GOOOOO", 75)
        update(self)
        self.sleep(1)
        wipe(self)

screen = Screen()
count_down = True
while count_down:                                                               # while loop used for the introduction screen of the game
    screen.game_start()
    count_down = False

class Player:           #the Player class: when instanciated, it generates one of the curves
    """All the usefull information about the player are in this class"""

    def __init__(self, id):
        possible_x_coordinates = [10, screen.width-10, screen.width/2.]         #initial x coordinate of the player
        possible_y_coordinates = [10, 10, screen.height-10]                     #initial y coordinate of the player
        possible_angles = [math.pi/4,3*math.pi/4,-math.pi/2]                    #initial direction of the plaeyer

        self.id = id                                                            #player number
        self.x_coordinate = possible_x_coordinates[self.id]                     #selecting one initial location according to the ID
        self.y_coordinate = possible_y_coordinates[self.id]                     #selecting one initial location according to the ID
        self.speed = 0.5                                                        #curve speed
        self.angle = possible_angles[self.id]                                   #selecting one initial angle according to the ID
        self.thickness = 1
        self.locations = [(self.x_coordinate, self.y_coordinate)]               #list of tuples representing the coordinates
        self.location = (math.floor(self.x_coordinate), math.floor(self.y_coordinate))  #coordinate tuple
        self.color = (random.randint(0, 200), random.randint(0, 200), random.randint(0, 255))
        self.angular_velocity = 0                                               #rate of turn of curve


        self.actual_time = float(pygame.time.get_ticks())/1000.                 #time of animation
        self.time_beginning = float(pygame.time.get_ticks())/1000.              #reference time
        self.not_drawing_list = []                                              #list containing the section of the curves NOT TO be drawn
        self.total_empty_list = []                                              #
        self.number_of_times_in_the_loop = 0                                    #test variable needed further on in the code
    def move(self):                                                             #method to move the curves

        self.actual_time = float(pygame.time.get_ticks()) / 1000.

        self.angle += self.angular_velocity*0.02                                # the direction of the player modified by the users input (angular velocity) multiplied by a smoothening factor (0.02)
        normal_speed_vector = [math.cos(self.angle), math.sin(self.angle)]

        speed_x = normal_speed_vector[0] * self.speed
        speed_y = normal_speed_vector[1] * self.speed

        self.x_coordinate += speed_x
        self.y_coordinate += speed_y
        self.location = (math.floor(self.x_coordinate), math.floor(self.y_coordinate))
        self.locations.append((math.floor(self.x_coordinate), math.floor(self.y_coordinate)))

    def create_hole(self):                                                      #method to generate an empty portion of curve
        self.not_drawing_list.append(self.location)

doquit = False                                                                  # variable that serves for looping. When it turns to be True, the while loop breaks
class Game():                                                                   # class that contains the users control input and the collision function

    def collision(self,i):                                                               #method to detect collision between curves and to check whether one player goes out of the screen
        if players[i].location in positions[:-number_of_players*2] or players[i].x_coordinate>screen.width or players[i].x_coordinate<0 or players[i].y_coordinate>screen.height or players[i].y_coordinate<0:
            players[i].speed = 0

    def game_loop(self,n_players):
        exit_loop = False

        def gamer_1(self):                                                     # defining controls for player 1
            if keys[pygame.K_RIGHT]:
                players[0].angular_velocity =1
            elif keys[pygame.K_LEFT]:
                players[0].angular_velocity = -1
            elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                players[0].angular_velocity = 0

        def gamer_2(self):                                                     # defining controls for player 2
            if keys[pygame.K_a]:
                players[1].angular_velocity = -1
            elif keys[pygame.K_d]:
                players[1].angular_velocity = 1
            elif not keys[pygame.K_a] and not keys[pygame.K_d]:
                players[1].angular_velocity = 0

        def gamer_3(self):                                                     # defining controls for player 3
            if keys[pygame.K_j]:
                players[2].angular_velocity = -1
            elif keys[pygame.K_l]:
                players[2].angular_velocity = 1
            elif not keys[pygame.K_j] and not keys[pygame.K_l]:
                players[2].angular_velocity = 0

        def exit(self):                                                       # function to manually break the loop and exit the game
            quit_loop = False
            if event.type == pygame.QUIT:
                quit_loop = True
            if keys[pygame.K_ESCAPE]:
                quit_loop = True

            nonlocal exit_loop
            exit_loop = quit_loop

        pygame.event.pump()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            exit(self)
            if n_players >=1:
                gamer_1(self)
            if n_players>=2:
                gamer_2(self)
            if n_players==3:
                gamer_3(self)

        global doquit
        doquit = exit_loop

# MAIN GAME

game = Game()
players = [Player(x) for x in range(3)]                                       # list with all the instances of the class Player
positions = []                                                                # list that will contain all the positions from all the players in order to check for collision
survivors = number_of_players*[1]                                             # list used for checking which and how many players are still alive in the game
time_beginning = float(pygame.time.get_ticks())/1000.
timing_draw_hole = (3,3.2)                                                    # initial dimensions for the generation of a hole
total_empty_list = []
while doquit==False:                                                          # main loop constantly running and drawing the players on the screen
    screen.set_screen.fill(screen.colour_background)
    game.game_loop(number_of_players)                                         # checking user interactions with the game

    for i in range(number_of_players):                                        # for each player: its position is updated, it is checked for collision and it is drawn on the screen
        players[i].move()
        game.collision(i)
        pygame.draw.lines(screen.set_screen, players[i].color, False, players[i].locations, players[i].thickness)

        time_elapsed = players[i].actual_time - players[i].time_beginning
        if time_elapsed<timing_draw_hole[0]:                                  # for the time before a hole must be drawn
            positions.append(players[i].location)


        elif timing_draw_hole[0]<=time_elapsed <=timing_draw_hole[1]:          # time during which a hole is drawn
            if players[i].number_of_times_in_the_loop == 0:                    # since the pygame drawing function requires 2 points for drawing a line, this provides the first point to do so
                players[i].not_drawing_list.append(players[i].locations[-2])
                players[i].number_of_times_in_the_loop = 1

            players[i].create_hole()
            pygame.draw.lines(screen.set_screen,screen.colour_background,False,players[i].not_drawing_list,players[i].thickness)    # drawing the current hole

        elif time_elapsed >timing_draw_hole[1]:                                 # after the hole being drawn, the coordinates of it are appended to the main hole list
            positions.append(players[i].location)
            players[i].time_beginning = players[i].actual_time
            players[i].total_empty_list.append(players[i].not_drawing_list)
            players[i].not_drawing_list = []
            players[i].number_of_times_in_the_loop = 0
            timing_interval_begin = random.randint(30, 35) / 10.                 # the new dimensions of the hole are redefined, such that the dimensions vary along the game
            timing_interval_end = random.randint(36, 40) / 10.
            timing_draw_hole = (timing_interval_begin, timing_interval_end)

        for empty_spaces in players[i].total_empty_list:                          # for statement for the drawing of all the empty spaces of a player until now
            pygame.draw.lines(screen.set_screen, screen.colour_background, False, empty_spaces, players[i].thickness)


        if players[i].speed == 0:                                                 # checks for dead players and changes the survivors list
            survivors[i] = 0
            if sum(survivors) ==1:                                                 # thare is only one player left, the game is finished
                screen.set_screen.fill((255, 255, 255))
                screen.print_middle("GAME OVER, player " + str(survivors.index(1)+ 1) + " wins", 100)
                pygame.display.flip()
                screen.sleep(3)
                doquit = True
                break

            elif sum(survivors) <= 1:                                               # for solo game in which the player has died
                screen.set_screen.fill((255, 255, 255))
                screen.print_middle("YOU LOST", 100)
                pygame.display.flip()
                screen.sleep(3)
                doquit = True
                break

    pygame.display.flip()


pygame.quit()


# ***With the following code, one can see the trajectories of the players throughout the whole game. It is commented, since we are not supposed to make use of matplotlib***
# import matplotlib.pyplot as plt
# import numpy as np
# coordinates_player_0 = np.asarray(players[0].locations)
# coordinates_player_1 = np.asarray(players[1].locations)
# coordinates_player_2 = np.asarray(players[2].locations)
#
# x_coordinates_player_0 = coordinates_player_0[:,0]
# y_coordinates_player_0 = coordinates_player_0[:,1]
# x_coordinates_player_1 = coordinates_player_1[:,0]
# y_coordinates_player_1 = coordinates_player_1[:,1]
# x_coordinates_player_2 = coordinates_player_2[:,0]
# y_coordinates_player_2 = coordinates_player_2[:,1]
#
#
# plt.plot(x_coordinates_player_1,y_coordinates_player_1,'bx')
# plt.scatter(x_coordinates_player_0,y_coordinates_player_0, facecolor = "None", edgecolors= "r")
# plt.plot(x_coordinates_player_2,y_coordinates_player_2,'gv')
# plt.axes([0,screen.width,0,screen.height])
# plt.grid(True)
# plt.show()