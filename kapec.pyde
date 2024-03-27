def setup():
    size(700,700)
def draw():
    background(0)
    rect(50,50,30,30)
    # rect(mouseX,mouseY,30,30)
    ellipse(mouseX,mouseY,100,100)
    # if rectRect(20,30,20,20,mouseX,mouseY,30,30):
    if rectEllipse(50,50,30,30,mouseX,mouseY,100):
        fill(0,255,0)
    else:
        fill(255,0,0)
#     if keyPressed == True:
#         rect(random(0,700),random(0,700),20,20)
def rectRect(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x1+w1>=x2) and (x2+w2>=x1) and (y1+h1>=y2) and (y2+h2>=y1):
        return True
    else:
        return False
def rectEllipse(x,y,w,h,x1,y1,diametr):
    testX=x1
    testY=y1
    if x1<x:
        testX=x
    elif x1>x:
        testX=x+w
    if y1<y:
        testY=y
    elif y1>y:
        testY=y+h
    distance=dist(x1,y1,testX,testY)
    if distance<=diametr/2:
        return True
    else:
        return False
    
    
    
    
    
