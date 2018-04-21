import pygame, sys
from pygame.locals import *
from CalculatorFunctions import *
#My first Pytgon game
pygame.init()
pygame.display.set_caption('Calculator')
pygame.display.set_icon(pygame.image.load('calculator.xpm'))
FPS = 30
white=(255,255,255)
red=(255,5,0)
clock=pygame.time.Clock()
gameDisplay = pygame.display.set_mode((700,700))
rectpos = (0,0)
font = pygame.font.SysFont(None,40)
equasion = ''
y=0
answer=None
text=font.render(str(answer), False, red)

mouse = pygame.draw.rect(gameDisplay,red,Rect((rectpos),(10,10)))
button1 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
gameDisplay.blit(font.render('1',True,(0,0,200)), (100,200))
    
button2 = pygame.draw.rect(gameDisplay,red,Rect((150,200),(30,30)))
gameDisplay.blit(font.render('2',True,(0,0,200)), (150,200))
    
button3 = pygame.draw.rect(gameDisplay,red,Rect((200,200),(30,30)))
gameDisplay.blit(font.render('3',True,(0,0,200)), (200,200))
    
button4 = pygame.draw.rect(gameDisplay,red,Rect((250,200),(30,30)))
gameDisplay.blit(font.render('4',True,(0,0,200)), (250,200))
    
button5 = pygame.draw.rect(gameDisplay,red,Rect((300,200),(30,30)))
gameDisplay.blit(font.render('5',True,(0,0,200)), (300,200))

button6 = pygame.draw.rect(gameDisplay,red,Rect((350,200),(30,30)))
gameDisplay.blit(font.render('6',True,(0,0,200)), (350,200))

button7 = pygame.draw.rect(gameDisplay,red,Rect((400,200),(30,30)))
gameDisplay.blit(font.render('7',True,(0,0,200)), (400,200))

button8 = pygame.draw.rect(gameDisplay,red,Rect((450,200),(30,30)))
gameDisplay.blit(font.render('8',True,(0,0,200)), (450,200))

button9 = pygame.draw.rect(gameDisplay,red,Rect((500,200),(30,30)))
gameDisplay.blit(font.render('9',True,(0,0,200)), (500,200))

button0 = pygame.draw.rect(gameDisplay,red,Rect((550,250),(30,30)))
gameDisplay.blit(font.render('0',True,(0,0,200)), (550,200))

buttonAdd = pygame.draw.rect(gameDisplay,red,Rect((100,250),(30,30)))
gameDisplay.blit(font.render('+',True,(0,0,200)), (100,250))

buttonSubtract = pygame.draw.rect(gameDisplay,red,Rect((150,250),(30,30)))
gameDisplay.blit(font.render('-',True,(0,0,200)), (150,250))

buttonMultiply = pygame.draw.rect(gameDisplay,red,Rect((200,250),(30,30)))
gameDisplay.blit(font.render('*',True,(0,0,200)), (200,250))

buttonDivide = pygame.draw.rect(gameDisplay,red,Rect((250,250),(30,30)))
gameDisplay.blit(font.render('/',True,(0,0,200)), (250,250))

buttonEquals = pygame.draw.rect(gameDisplay,red,Rect((250,250),(30,30)))
gameDisplay.blit(font.render('=',True,(0,0,200)), (250,250))

buttonClear = pygame.draw.rect(gameDisplay,red,Rect((300,250),(30,30)))
gameDisplay.blit(font.render('C',True,(0,0,200)), (300,250))

buttonDecimal = pygame.draw.rect(gameDisplay,red,Rect((300,250),(30,30)))
gameDisplay.blit(font.render('.',True,(0,0,200)), (300,250))

buttonTan = pygame.draw.rect(gameDisplay,red,Rect((450,250),(30,30)))
gameDisplay.blit(font.render('tan',True,(0,0,200)), (450,250))

buttonCos = pygame.draw.rect(gameDisplay,red,Rect((500,250),(30,30)))
gameDisplay.blit(font.render('cos',True,(0,0,200)), (500,250))

buttonSin = pygame.draw.rect(gameDisplay,red,Rect((550,250),(30,30)))
gameDisplay.blit(font.render('sin',True,(0,0,200)), (550,250))

buttonLeftBracket = pygame.draw.rect(gameDisplay,red,Rect((600,250),(30,30)))
gameDisplay.blit(font.render('(',True,(0,0,200)), (600,250))

buttonRightBracket = pygame.draw.rect(gameDisplay,red,Rect((650,250),(30,30)))
gameDisplay.blit(font.render(')',True,(0,0,200)), (650,250))

buttonSqrttt = pygame.draw.rect(gameDisplay,red,Rect((650,250),(30,30)))
gameDisplay.blit(font.render('sqrt',True,(0,0,200)), (100,300))

while True:
    try:
        pygame.display.set_caption('Calculator')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                rectpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse.colliderect(button1):
                    equasion = equasion + '1'
                if mouse.colliderect(button2):
                    equasion = equasion + '2'
                if mouse.colliderect(button3):
                    equasion = equasion + '3'
                if mouse.colliderect(button4):
                    equasion = equasion + '4'
                if mouse.colliderect(button5):
                    equasion = equasion + '5'
                if mouse.colliderect(button6):
                    equasion = equasion + '6'
                if mouse.colliderect(button7):
                    equasion = equasion + '7'
                if mouse.colliderect(button8):
                    equasion = equasion + '8'
                if mouse.colliderect(button9):
                    equasion = equasion + '9'
                if mouse.colliderect(button0):
                    equasion = equasion + '0'
                if mouse.colliderect(buttonAdd):
                    equasion = equasion + '+'
                if mouse.colliderect(buttonSubtract):
                    equasion = equasion + '-'
                if mouse.colliderect(buttonMultiply):
                    equasion = equasion + '*'
                if mouse.colliderect(buttonDivide):
                    equasion = equasion + '/'
                if mouse.colliderect(buttonDecimal):
                    equasion = equasion + '.'
                if mouse.colliderect(buttonTan):
                    equasion = equasion + 'tan('
                if mouse.colliderect(buttonCos):
                    equasion = equasion + 'cos('
                if mouse.colliderect(buttonSin):
                    equasion = equasion + 'sin('
                if mouse.colliderect(buttonLeftBracket):
                    equasion = equasion + '('
                if mouse.colliderect(buttonRightBracket):
                    equasion = equasion + ')'
                if mouse.colliderect(buttonSqrttt):
                    equasion = equasion + 'sqrt('
                if mouse.colliderect(buttonEquals):
                    if equasion[0] != '+' or equasion[0] != '-' or equasion[0] != '*' or equasion[0] != '/':
                        answer = eval(equasion)
                        text = font.render('='+str(answer), False, red)
                        gameDisplay.blit(text, (0,40))
                    else:
                        answer = '=Error'
                if mouse.colliderect(buttonClear):
                    equasion = ''
                    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        gameDisplay.fill(white)
        mouse = pygame.draw.rect(gameDisplay,red,Rect((rectpos),(10,10)))
        
        button1 = pygame.draw.rect(gameDisplay,red,Rect((100,200),(30,30)))
        gameDisplay.blit(font.render('1',True,(0,0,200)), (100,200))
        
        button2 = pygame.draw.rect(gameDisplay,red,Rect((150,200),(30,30)))
        gameDisplay.blit(font.render('2',True,(0,0,200)), (150,200))
        
        button3 = pygame.draw.rect(gameDisplay,red,Rect((200,200),(30,30)))
        gameDisplay.blit(font.render('3',True,(0,0,200)), (200,200))
        
        button4 = pygame.draw.rect(gameDisplay,red,Rect((250,200),(30,30)))
        gameDisplay.blit(font.render('4',True,(0,0,200)), (250,200))
        
        button5 = pygame.draw.rect(gameDisplay,red,Rect((300,200),(30,30)))
        gameDisplay.blit(font.render('5',True,(0,0,200)), (300,200))

        button6 = pygame.draw.rect(gameDisplay,red,Rect((350,200),(30,30)))
        gameDisplay.blit(font.render('6',True,(0,0,200)), (350,200))

        button7 = pygame.draw.rect(gameDisplay,red,Rect((400,200),(30,30)))
        gameDisplay.blit(font.render('7',True,(0,0,200)), (400,200))
        
        button8 = pygame.draw.rect(gameDisplay,red,Rect((450,200),(30,30)))
        gameDisplay.blit(font.render('8',True,(0,0,200)), (450,200))
        
        button9 = pygame.draw.rect(gameDisplay,red,Rect((500,200),(30,30)))
        gameDisplay.blit(font.render('9',True,(0,0,200)), (500,200))
        
        button0 = pygame.draw.rect(gameDisplay,red,Rect((550,200),(30,30)))
        gameDisplay.blit(font.render('0',True,(0,0,200)), (550,200))

        buttonAdd = pygame.draw.rect(gameDisplay,red,Rect((100,250),(30,30)))
        gameDisplay.blit(font.render('+',True,(0,0,200)), (100,250))

        buttonSubtract = pygame.draw.rect(gameDisplay,red,Rect((150,250),(30,30)))
        gameDisplay.blit(font.render('-',True,(0,0,200)), (150,250))

        buttonMultiply = pygame.draw.rect(gameDisplay,red,Rect((200,250),(30,30)))
        gameDisplay.blit(font.render('*',True,(0,0,200)), (200,250))

        buttonDivide = pygame.draw.rect(gameDisplay,red,Rect((250,250),(30,30)))
        gameDisplay.blit(font.render('/',True,(0,0,200)), (250,250))

        buttonEquals = pygame.draw.rect(gameDisplay,red,Rect((300,250),(30,30)))
        gameDisplay.blit(font.render('=',True,(0,0,200)), (300,250))

        buttonClear = pygame.draw.rect(gameDisplay,red,Rect((350,250),(30,30)))
        gameDisplay.blit(font.render('C',True,(0,0,200)), (350,250))

        buttonDecimal = pygame.draw.rect(gameDisplay,red,Rect((400,250),(30,30)))
        gameDisplay.blit(font.render('.',True,(0,0,200)), (400,250))

        buttonTan = pygame.draw.rect(gameDisplay,red,Rect((450,250),(30,30)))
        gameDisplay.blit(font.render('tan',True,(0,0,200)), (450,250))

        buttonCos = pygame.draw.rect(gameDisplay,red,Rect((500,250),(30,30)))
        gameDisplay.blit(font.render('cos',True,(0,0,200)), (500,250))

        buttonSin = pygame.draw.rect(gameDisplay,red,Rect((550,250),(30,30)))
        gameDisplay.blit(font.render('sin',True,(0,0,200)), (550,250))

        buttonLeftBracket = pygame.draw.rect(gameDisplay,red,Rect((600,250),(30,30)))
        gameDisplay.blit(font.render('(',True,(0,0,200)), (600,250))

        buttonRightBracket = pygame.draw.rect(gameDisplay,red,Rect((650,250),(30,30)))
        gameDisplay.blit(font.render(')',True,(0,0,200)), (650,250))

        buttonSqrttt = pygame.draw.rect(gameDisplay,red,Rect((100,300),(30,30)))
        gameDisplay.blit(font.render('sqrt',True,(0,0,200)), (100,300))

        gameDisplay.blit(font.render(equasion,True,red), (250,y))
        gameDisplay.blit(text, (250,40))
                         
        clock.tick(FPS)
        pygame.display.update()
    except SyntaxError:
        answer = 'ERROR'
    
