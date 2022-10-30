def setup():
    size(800, 800)
    noStroke()
    fill(0)
    background(0, 0, 102)
    
def draw(): 
    noStroke()
    fill(128, 128, 128)
    ellipse(400, 800, 1600, 500)
    rectMode(CENTER)
    fill(51, 51, 255)
    rect(600, 600, 20, 100)
    fill(0, 153, 0)
    ellipse(600, 550, 60, 70)
    fill(255, 255, 153)
    ellipse(585, 550, 16, 32)
    ellipse(615, 550, 16, 32)
    noStroke() 
    fill(255, 255, 204)
    ellipse(200, 100, 7, 7)
    ellipse(250, 150, 9, 9)
    ellipse(300, 200, 10, 10)
    ellipse(350, 175, 8, 8)
    ellipse(400, 190, 10, 10)
    ellipse(450, 300, 7, 7)
    ellipse(600, 350, 7, 7) 
    ellipse(200, 210, 8, 8)
    ellipse(50, 220, 8, 8)
    ellipse(60, 305, 9, 9)
    ellipse(90, 400, 8, 8)
    ellipse(500, 100, 9, 9)
    ellipse(600, 400, 7, 7)
    ellipse(750, 300, 9, 9)
    ellipse(730, 500, 8, 8)
    ellipse(720, 100, 8, 8)
    fill(51, 51, 255)
    rectMode(CENTER)
    rect(520, 520, 20, 100)
    fill(0, 153, 0)
    ellipse(520, 470, 60, 70)
    fill(255, 255, 153)
    ellipse(505, 470, 16, 32)
    ellipse(535, 470, 16, 32) 
    fill(96, 96, 96)
    ellipse(400, 600, 100, 10)
    ellipse(200, 700, 100, 10)
    ellipse(350, 640, 80, 7)
    ellipse(750, 600, 90, 8)
    ellipse(300, 560, 100, 10)
    ellipse(200, 600, 100, 8)
    ellipse(580, 700, 90, 8)
    ellipse(700, 780, 90, 8)
    ellipse(100, 780, 90, 7)
    ellipse(400, 760, 80, 9)
    fill(153, 51, 255)


w, h = 800, 800

pfc = (255, 255, 255)
w, h = 800, 800

pfc = (204, 102, 0)
olc = (153, 0, 76)
bgc = (0, 0, 102)

pw = 7
rw = 7

def draw_planet(position, ps):
    pushMatrix()
    
    # translate(position[0], position[1])
    starting_height = random(ps/4, ps/2)
    starting_width = random(ps*1.2, ps*2)
    rotate(random(2*PI))
    
    
    # Add colored circle
    fill(pfc[0], pfc[1], pfc[2])
    strokeWeight(pw)
    circle(0, 0, ps)
    
    # Settings for the rings
    noFill()
    strokeWeight(rw)
    for i in range(int(random(4, 12))):
        ellipse(0, 0, starting_height + i * 10, starting_width + i * 30)
    
    # Cover up part of the rings
    strokeWeight(pw)
    fill(pfc[0], pfc[1], pfc[2])
    arc(0, 0, ps, ps, 1.5*PI, 2.5*PI);
    
    popMatrix()

def setup():
    size(w, h)
    pixelDensity(2)
    frameRate(2)
    
    translate(w/2, h/2)
    
    stroke(olc[0], olc[1], olc[2])
    
    background(bgc[0], bgc[1], bgc[2])

    draw_planet((w/2, h/2), random(100, 400))

    



    
    

     

    
    

    
