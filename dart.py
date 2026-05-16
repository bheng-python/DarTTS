#various imports
import pygame
import math
#first loads up pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#might make bigger but just sets up the display and how big it is
clock = pygame.time.Clock()#sets up the clock code
pygame.display.set_caption("Show Text")#these lines of code are for setting up the font
font = pygame.font.SysFont("Arial", 24)#this is for the specfic font and font size for the game
#image setup
dart_orig = pygame.image.load("dart2.png").convert_alpha()#this code loads the darts
dart_orig = pygame.transform.scale(dart_orig, (75, 75))#this code scales the dart properly
dart_orig = pygame.transform.rotate(dart_orig, 180)#this code rotates the dart so it faces the right direction when its still
dart_orig.set_colorkey((210,211,213))#I had to use something online to find the specific rgb value for the background to get rid of it
#backgrund
background = pygame.image.load("background4.jpg").convert_alpha()#this is for loading your basic background where the enemies will be
background = pygame.transform.scale(background, (800,448))this code is for scaling it to the correct width, I had to use a little math so it would still look ok
ground = pygame.image.load("ground.jpg").convert_alpha()#This is just for loading the ground in which you fire on
ground = pygame.transform.scale(ground, (800,457))#this code is for scaling it to the correct width, I had to use a little math so it would still look ok
#enemies
#each of these 3 lines of code are for various descriptons of items.
blue_flame_boss = pygame.image.load("blue_flame_boss.png").convert_alpha()#being able to convert alpha Im pretty sure allows you to use color key or it only worked if i added it
blue_flame_boss = pygame.transform.scale(blue_flame_boss, (100,100))#i wanted to scale this up at a higher level then the others as I figured I needed a mini boss or a enemy that was higher
blue_flame_boss.set_colorkey((255,255,255))#this code is just to get rid of the background
pumpkin = pygame.image.load("pumpkin.png").convert_alpha()# same thing with the other convert alpha is good
pumpkin = pygame.transform.scale(pumpkin, (75, 75))#I wanted to use 75 75 for normal enemies as it looks mostly sized correctly
pumpkin.set_colorkey((255,255,255))#this code is just to get rid of the background
robot = pygame.image.load("robot.png").convert_alpha()# same thing with the other convert alpha is good
robot = pygame.transform.scale(robot, (75,75))#I wanted to use 75 75 for normal enemies as it looks mostly sized correctly
robot.set_colorkey((255,255,255))#this code is just to get rid of the background
eyeball = pygame.image.load("eyeball.png").convert_alpha()# same thing with the other convert alpha is good
eyeball = pygame.transform.scale(eyeball, (75,75))#I wanted to use 75 75 for normal enemies as it looks mostly sized correctly
eyeball.set_colorkey((255,255,255))#this code is just to get rid of the background
tree = pygame.image.load("tree.png").convert_alpha()# same thing with the other convert alpha is good
tree = pygame.transform.scale(tree, (75,75))#I wanted to use 75 75 for normal enemies as it looks mostly sized correctly
tree.set_colorkey((255,255,255))#this code is just to get rid of the background
#varraibles
money = 0#i wanted to add a money function to the shop
mode = "Normal"#change these between easy normal and hard for different diifculties will add a button later
enemy_health_mult = 1#this is for setting up difficulties
damage_mult = 1#this is also for setting difficulties
debug_mode = True#this is a booleg with flips between true and false to shop hitboxes or not
health = 100# this line of code was for showing your health
score = None#this I might change from score to kills but I do not know
main_game = False#so this is to change what your seeing and to pause either the shop or the main game, change to true and you see the main game, change to false and you dont
shop = True#so this is to change what your seeing and to pause either the shop or the main game,change to true and you see the shop, change to false and you dont
damageable = 0#this is so if you hit the target you cant get repeated damage as the darts hitbox still interacts for a few seconds
dart_pos = [150, 450]#this is for the darts position along the game board
dart_vel = [0, 0]#this is for the current speed and direction for the dart
is_flying = False#this dectects if its flying such as when you release you mouse after you press down and drag
drag_start = None#None is nil which means theres no object in its memoery and it will still not give a error code
MAX_DRAG = 150  #this is how big you can drag the circle, change if you want it to go faster or slower
GRAVITY = 0.4 #change this to higher if you wont your dart to go down faster and lower if you want it to go more straight, also the downforce added each frame
running = True#first sets running to true
#colors
x1=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it#these three are for items, might change too two or one deppending on gamemode
x2=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it
x3=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it
x4=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it#this is for the dart selection
x5=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it, these two are for the buy and reroll buttons, Buy button
x6=0#i wanted a varaible to add onto the shop buttons so if your hovering over them they turn brigther, might have overcomplicated it, reroll button
while running:#this just runs it all
    if main_game:#This is for wether your in the shop or main game
        if mode == "Easy":#dectets if mode is easier then runs next 3 lines
            GRAVITY = 0.3#makes the dart get less affected by gravity
            enemy_health_mult = 0.7#sets enemy health to 70%
            damage_mult = 1.5#makes your damage higher too
        if mode == "Normal":#this is the normal game
            GRAVITY = 0.5#sets gravity to 50%
            enemy_health_mult = 1#sets health to normal
            damage_mult = 1#sets damage to normal
        if mode == "Hard":#this is for hard mode
            GRAVITY = 0.7#makes it harder to throw
            damage_mult = 0.6#makes you do less damage
            enemy_health_mult = 1.3#makes enemies stronger
        screen.fill((0, 0, 0))#fills the screen so the past images dont intefere with the game
        screen.blit(background, (0, -90))#this blits or shows the background on screen and we putting it first because we want everything layered on top
        screen.blit(ground, (0, 298))#this is for throwwing same thing as the previous we want everything layered on top but its also covering some of the background on purpose to hide ugly parts of the background
        mouse_pos = pygame.mouse.get_pos()#allows for mouse movements
        for event in pygame.event.get():#gets various different events
            if event.type == pygame.QUIT:#dectects if you press the x button and quits the game
                running = False#quits the game
            if event.type == pygame.MOUSEBUTTONDOWN:#this dectects if the mouse is down and then runs the following code
                drag_start = event.pos#this sets the darts position to where you orgginaly pressed down with your mouse
                x, y = event.pos#because event.pos is a tuple you cant use ussal methods for declaring it so you have to remove the tuple part by setting it to two varabiles which i put as x and y
                if y < 300:#this dectets if you go out of range and sets it back in range for throwing for y axis
                    y = 305#this actaully sets it to 305
                if x > 250:#same thing as last two lines but for the x axis, before the other lines so it runs smoothly and porperly
                    x = 235#actaully sets it to proper ammount
                drag_start = (x,y)#sets where you first clicked down to drag start used for later lines
                dart_pos = list(drag_start)#this adds the darts position to the list
                is_flying = False#this sets is_flying to false because you havent released yet
            if event.type == pygame.MOUSEBUTTONUP and drag_start:#this dectects if the mouse is up
                # Calculate total distance dragged
                dx = event.pos[0] - drag_start[0]#cacluatles the distince between when you first clicked whcih is dragstart and when you release which is event.pos for x
                dy = event.pos[1] - drag_start[1]#cacluatles the distince between when you first clicked whcih is dragstart and when you release which is event.pos for y
                dist = math.hypot(dx, dy)#this caculates the length of the diagonal between the start point of x,y and the end point of x,y ysing pythagoreon theorem

                # If dragged too far, shrink the vector to MAX_DRAG, this is for limiting how far you can drag
                if dist > MAX_DRAG: #This checks if its dragged to far
                    scale = MAX_DRAG / dist
                    dx *= scale#this multiplies the dx by the scale
                    dy *= scale#this multiplies the dy by the scale

                dart_vel = [dx * 0.15, dy * 0.15]#this gets the darts initally speed based on how far you draged
                is_flying = True#this changes is flying to true so it can print the dart, turns on pyhsics ofr the dart
                drag_start = None#resets the drag_start to None so it can be replayed
            if event.type == pygame.KEYDOWN:#this code is used for various key events
                if event.key == pygame.K_e:#this is for debug mode, wont be on for players
                    if debug_mode == True:#if debug is true sets it to false
                        debug_mode = False#actually sets it to false
                    elif debug_mode == False:#if its false sets it to true, used for single button changing
                        debug_mode = True#acutally sets it to true
                if event.key == pygame.K_h:#used for debugging sets health to 100
                    health = 100#sets the health to 100
                    print("health:",health)#shows health to double check and provide a break in the command bar
                if event.key == pygame.K_r:#changes between the shop and the main game
                    if main_game == True:#same code used previosuly for the debug mode but for main game
                        main_game = False#it first sets main game to false
                        shop = True#then it sets shop to true
                    elif shop == True:#switches them up for one button comands
                        shop = False#first sets shop to false so it dosent run anymore
                        main_game = True#then it loads many game
        #the code is used for physics
        if is_flying:#detects if you released the mouse then runs the darts gravity code
            dart_vel[1] += GRAVITY#adds the darts velicoty to gravity so it progresbily goes further down
            dart_pos[0] += dart_vel[0]#adds the darts x so it goes right
            dart_pos[1] += dart_vel[1]#adds the previous gravity code so it always goes down, thinking of making a upside down gamemode like moon gravity or smth
            if dart_pos[1] < 300:#detects if the dart hits the ceiling and first sets the darts y back down to 300
                dart_pos[1] = 300#sets it to 300
                if dart_vel[1] < 0:# then it provides a high gravity
                    dart_vel[1] *= -0.2# right here so it bounces off
            angle = -math.degrees(math.atan2(dart_vel[1], dart_vel[0]))#this code is for showing what angle to print the dart, copied this from yt ngl

        else:#if its not flying then keeps it level
            angle = 0 #if its not throwing its angle will be 0 so it will be flat, may change in future so it will follow the mouse

        #this code draws the launch area and the line
        if drag_start: #this checks if yur mouse is down and draws a circle around where you initally clicked down to limit how far you can drag
            # Draw a circle showing the max drag limit
            pygame.draw.circle(screen, (100, 100, 100), drag_start, MAX_DRAG, 2) #this draws a circle where you clicked down with a diamter of MAX_DRAG and this can change with variables


            dx = mouse_pos[0] - drag_start[0]#cacluates how many pixels moved between when you first clicked and when you released/dragged for the x axis
            dy = mouse_pos[1] - drag_start[1]#this caclualtes how many pixeks you moved when you first clikced and when you dragged for the y axis
            dist = math.hypot(dx, dy)#this finds the straight line distince between the dx and dy

            line_end = mouse_pos#it sets the line end to mouses position so it can draw a straight line
            if dist > MAX_DRAG:#checks if the distince of the line you dragged is greater then the set amount and resets it back to its nearest point along the circle
                line_end = (drag_start[0] + dx * MAX_DRAG / dist, #this makes sure the line stops perfectly at 100 pixels because of dx * max_drag / dist such as if you dragged 200 to the ight it would be 200 * 100/200 which would = 100
                            drag_start[1] + dy * MAX_DRAG / dist) #this the same thing as the previous line but for the y axis, used a little yt to get this code cuz lwk kinda hard,

            pygame.draw.line(screen, (255, 255, 255), drag_start, line_end, 2)#this draws a line from where you iniitally pressed down and the line end math
        #draws the dart
        rotated_dart = pygame.transform.rotate(dart_orig, angle)#this draws the dart and changes its rotation as it goes along its trijcetory.
        rect = rotated_dart.get_rect(center=dart_pos)#this sets the center of the dart as its rotation point so not errors occur and make it look nicer
        screen.blit(rotated_dart, rect)#this finnaly blits the dart for each tick
        #code for wakks
        if debug_mode:
            middle_wall = pygame.draw.line(screen, (0, 255, 0), (0,300), (800,300), 5)#theses are lines for the horzinatl axis so it can have more info on the top and not just be a dart playing game cuz thats boring
            bottom_wall = pygame.draw.line(screen, (0, 255, 0), (0, 597.5), (800, 597.5), 5)#this is for drawing varioys debug walls so I can better code UI
            #code for the box you can fire in
            #pygame.draw.line(screen, (0, 255, 0), (0,450), (250, 450), 5)#this is for the horzantal line for inventory.
            small_wall_left = pygame.draw.line(screen, (0, 255, 0), (2.5, 300), (2.5,600), 5)#for the left most wall, not needed ngl
            small_wall_right = pygame.draw.line(screen, (0, 255, 0), (797.5, 300), (797.5,600), 5)#for the right most wall also probley not needed
        #enemys
        #scoring debug wall_score# i had to make them very small so the dart couldnt hit two targets at once
        high_rect = pygame.Rect(790, 325, 10, 30)#this is for the best target, and first creating the sprite, idk why i put it here and not on top
        pygame.draw.rect(screen, (100,100,255), high_rect)#this draws the spirte and at a specific color which i chose as a light blue
        medium_rect = pygame.Rect(790, 425, 10, 30)#this is for the medium target, and first creating the sprite, idk why i put it here and not on top
        pygame.draw.rect(screen, (100,255,100), medium_rect)#this draws the spirte and at a specific color which i chose as a light green
        low_rect = pygame.Rect(790, 525, 10, 30)#this is for the worse target, and first creating the sprite, idk why i put it here and not on top, kinda just a target you will always hit if you miss
        pygame.draw.rect(screen, (255,100,100), low_rect)#decided on light red for this target
        #enemy health
        enemy_health_display = pygame.Rect(565, 215, 220, 60)#this is for drawing the box for the enemies health
        pygame.draw.rect(screen, (128, 128, 128), enemy_health_display)#this is for blitting it to screen
        enemy_health = pygame.Rect(575, 225, health*2, 40)#this multiples health by 2 so you can see a moving green health bar, acutally supposed to be down here because it constantly changes kidna
        pygame.draw.rect(screen, (0, 255, 0), enemy_health)#this is used for bltting it
        text = font.render("health: "+str(health), True, (0,0,0))#this is for rendering the health so you can see it as a number, used for the players pov
        small_wall_middle = pygame.draw.line(screen, (0, 50, 255), (250,295), (250,600), 5)#these are lines for a box so you can only fire the dart from a certain area.
        screen.blit(text, (575, 225))#blits the text
        if damageable > 6:#dectects if it can be damaged
            if rect.colliderect(high_rect):#if its colliding with the best target runs folling code
                health -= 50#subtracts 50 health
                print("health:", health)#prints health to console so I can debug
                damageable = 0#sets damage back down to 0 so you dont do like inf damage
            elif rect.colliderect(medium_rect):#if its colliding with the ok target runs folling code
                health -= 30#subtracts 30 health
                print("health:", health)#prints health to console so I can debug
                damageable = 0#sets damage back down to 0 so you dont do like inf damage
            elif rect.colliderect(low_rect):#if its colliding with the terrible target runs folling code
                health -= 10#subtracts 10 health kinda useless lwk but might add a like boss where you have to do exact damage or it gains health, or all enemies, interrestng
                print("health:", health)#prints health to console so I can debug
                damageable = 0#sets damage back down to 0 so you dont do like inf damage
        if health <= 0:#dectects if you health is 0 or higher
            print("you lose")#for me dubugging
            print("your score is:", score)#also for me debugging
            health = 100#sets health back to 100
        damageable += 0.1#constanlty adds 0.1 to damagable so you can hit targets again
    if shop:#dectets if shop is running then runs follwoing coed
        mouse_rect = pygame.mouse.get_pos()#allows for mouse movements
        mouse_rect = pygame.Rect((mouse_rect), 10, 10)#creates a 10 pixel by 10 pixel hit box for mouse
        screen.fill((0, 0, 0))#screen fills so there are no blurring
        for event in pygame.event.get():#gets various events, could have used outside of if shop or main menu
            if event.type == pygame.QUIT:#decects if you quit game, might add a quit anniamation
                running = False#sets the game to stop running all code
            if event.type == pygame.KEYDOWN:#dectets if your pressing down on a key
                if event.key == pygame.K_m:#for debugging it
                    money = 1000#sets money to a high ammount
                if event.key == pygame.K_r:#changes between the shop and the main game
                    if main_game == True:#same code used previosuly for the debug mode but for main game
                        main_game = False#it first sets main game to false
                        shop = True#then it sets shop to true
                    elif shop == True:#switches them up for one button comands
                        shop = False#first sets shop to false so it dosent run anymore
                        main_game = True#then it loads many game
                if event.key == pygame.K_UP:#this is for debuging to colors for the buttons
                    x1 += 15#sets all buttons to a higher color contrast
                    x2 += 15#sets all buttons to a higher color contrast
                    x3 += 15#sets all buttons to a higher color contrast
                    x4 += 15#sets all buttons to a higher color contrast
                if event.key == pygame.K_DOWN:#resets button color
                    x1 = 0#sets it back to 0
                    x2 = 0#sets it back to 0
                    x3 = 0#sets it back to 0
                    x4 = 0#sets it back to 0
                if event.key == pygame.K_LEFT:#wanted a different code for buying and selling buttons
                    x5 += 15#sets all buttons to a higher color contrast
                    x6 += 15#sets all buttons to a higher color contrast
                if event.key == pygame.K_RIGHT:#resets the colors
                    x5 = 0#sets it back to 0
                    x6 = 0#sets it back to 0
        if x1 or x2 or x3 or x4 >= 45:#stops it from breaking cuz you cant have colors over 255
            x1 = 45#sets it back down to 45, absoulte limit
            x2 = 45#sets it back down to 45, absoulte limit
            x3 = 45#sets it back down to 45, absoulte limit
            x4 = 45#sets it back down to 45, absoulte limit
        if mouse_rect.colliderect(shop_box_1):# dectrects if your mouse is colliding with the shop
            x1 = 45#sets the colors to 45
        shop_box = pygame.Rect(25, 25, 750, 550)#creates shop box outer backgroudnd
        pygame.draw.rect(screen, (48, 31, 30), shop_box)#for drawing it
        shop_box_small = pygame.Rect(50, 50, 700, 500)#craetes shop box inner background
        pygame.draw.rect(screen, (88, 57, 39), shop_box_small)#draws it
        shop_box_1 = pygame.Rect(100,75,150,150)#these for lines are for creating the different shop boxes, shop box 1, different items also differet rarites, higher number higher rariates
        shop_box_2 = pygame.Rect(325,75,150,150)#medium rarity
        shop_box_3 = pygame.Rect(550, 75,150,150)#best item
        shop_dart = pygame.Rect(200, 275,400,200)#this box is for showing different darts, wanted it to be slightly bigger
        pygame.draw.rect(screen, (193+x1, 196+x1, 199+x1), shop_box_1)#this code is for drawing it and adds the previous code for making it lighter
        pygame.draw.rect(screen, (193+x2, 196+x2, 199+x2), shop_box_2)#this code is for drawing it and adds the previous code for making it lighter
        pygame.draw.rect(screen, (193+x3, 196+x3, 199+x3), shop_box_3)#this code is for drawing it and adds the previous code for making it lighter
        pygame.draw.rect(screen, (193+x4, 196+x4, 199+x4), shop_dart)#this code is for drawing it and adds the previous code for making it lighter
        shop_buy = pygame.Rect(75, 250, 100, 50)#this sets up the shop buying code
        shop_reroll = pygame.Rect(625, 250, 100, 50)#this sets up the shop rerolling code
        pygame.draw.rect(screen, (194-x5, 24, 7), shop_buy)#draws it and allows for making it darker when mouse is over
        pygame.draw.rect(screen, (255-x6, 215-x6, 0), shop_reroll)#same thing as previous
        text_Reroll = font.render(("Reroll"), True, (0,0,0))#creates text for user
        screen.blit(text_Reroll, (650, 260))#draws text
        text_Buy = font.render(("Buy"), True, (0,0,0))#same thing as previous 2
        screen.blit(text_Buy, (110, 260))#same thing as previous 3
    pygame.display.flip()#shows the info on the screen
    clock.tick(60)#the tick rate

pygame.quit()#this finnaly quits the game after running is set the false, may make a end scene could be cool
