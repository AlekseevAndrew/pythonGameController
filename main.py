import gameController
from settings import WIDTH,HEIGHT,NAME

#objects
engine = gameController.gameWindow(WIDTH,HEIGHT,NAME)
amogus = gameController.gameObject(engine,'textures/amogus.png')
isPress=False
butt=None

engine.set_bg_color(0,0,0)
engine.set_icon('textures/icon/64x64.png')
while True:
    for event in engine.get_events():
        if event.type == engine.QUIT:
            print("Game is closed!")
            engine.exit()
        elif event.type == engine.KEYPRESSED:
            isPress=True
            butt=event
        elif event.type == engine.KEYRELEASED:
            isPress=False
    if isPress:
        if engine.get_key(butt,engine.PYGAME.K_a):
                amogus.move(-1,0)
        elif engine.get_key(butt,engine.PYGAME.K_d):
                amogus.move(1,0)
        elif engine.get_key(butt,engine.PYGAME.K_w):
                amogus.move(0,-1)
        elif engine.get_key(butt,engine.PYGAME.K_s):
                amogus.move(0,1)
    engine.tick(amogus)