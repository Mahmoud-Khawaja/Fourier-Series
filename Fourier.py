import pygame
import numpy as np

# visualizing square wave with Fourier Series
# singal switching between +1 and -1 
# f(x) = 4/pi*summation((1/n)sin(n*pi*x/L)) n = 1,3,5 -> inf


# set up
width = 1200
height = 600
radius = 100
time = 0
fps = 60
x_cir = width/2 - 400
y_cir = height/2
wave = [] # saving the wave pattern
N = 1
n = 1

# colors 
white = (255,255,255)
black = (0,0,0)
red = (170,35,35)
blue = (35,128,170)


# configurations
pygame.display.set_caption("Fourier")
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(fps)
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    x = x_cir
    y = y_cir
    
    for i in range(n):

        prev_x,prev_y=x,y
        N = i*2+1 # values of n = {1,3,5,7,....2n+1}
        
        #(4/pi*n)sin(n*pi*x/L)
        radius = int(100*(4/(N*np.pi)))
        x += int(radius*np.cos(N*time))
        y += int(radius*np.sin(N*time))
        
        pygame.draw.circle(window,white,(prev_x,prev_y),radius,2)
        pygame.draw.line(window,blue,(prev_x,prev_y),(x,y),2)
        pygame.draw.circle(window,red,(x,y),5)
    
    wave.insert(0,y)
    if len(wave)>=width:
         wave.pop()

    pygame.draw.line(window,white,(x,y),(x_cir+350,wave[0]),3)

    for i in range(len(wave)):
        pygame.draw.circle(window,white,(i+x_cir+350,wave[i]),1)

    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP] and n < 400:
        n+=1
        pygame.time.delay(50)
    if key[pygame.K_DOWN] and n > 1:
        n-=1
        pygame.time.delay(50)


    time+=.02
    print(n)
    pygame.display.update()


pygame.quit()
