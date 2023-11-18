r=255
g=255
b=255
a=0
s=0
c=0

def setup():
    size(500,400)
    colorMode(HSB)
def draw():
    global r,g,b,a,s,c
    background(22,3,255)
    fill(r,g,b)
    ellipse(200,200,10,10)
    fill(a,s,c)
    ellipse(250,200,10,10)
    noFill()
    ellipse(225,200,100,100)
    r=r-0.5
    g=g-0.5
    b=b-0.5
    a=a+0.5
    s=s+0.5
    c=c+0.5
