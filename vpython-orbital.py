from visual import *
import math

def main():

    window = display(x = 100, y = 0, height = 1800, width = 1800, background = color.black)

    sun = sphere(pos = vector(0,0,0), radius = 24, color = color.yellow, material = materials.rough)
    mercury = sphere(pos = vector(-60,0,0), radius = 3, color = color.gray(0.5), material = materials.rough, make_trail = True, trail_type = "points", interval = 2)
    venus = sphere(pos = vector(-84,0,0), radius = 3.5, color = color.orange, make_trail = True, trail_type = "points", interval = 2.6) 
    earth = sphere(pos = vector (-108, 0, 0), radius = 4.3,  material = materials.earth, make_trail = True, trail_type = "points", interval = 5) 
    moon = sphere(pos = vector(22, 0, 12), radius = 2, color = color.white)
    mars = sphere(pos = vector(-132,0,0), radius = 3.6, color = color.red, material = materials.rough, make_trail = True, trail_type = "points", interval = 6.3)
    jupiter = sphere(pos = vector(-182,0,0), radius = 10, color = color.magenta, material = materials.marble, make_trail = True, trail_type = "points", interval = 10)
    saturnus = sphere(pos = vector(-206,0,0), radius = 8, color = color.orange, material = materials.marble, make_trail = True, trail_type = "points", interval = 8)
    ring = cylinder(pos = vector(-210,0,0), radius = 12, length = 2, axis = (1, 1, 0), color = color.gray(0.5), center = saturnus.pos)
    uranus = sphere(pos = vector(-230,0,0), radius = 5.2, color = color.blue, material = materials.marble, make_trail = True, trail_type = "points", interval = 10)
    neptunus = sphere(pos = vector(-254,0,0), radius = 4.8, color = color.cyan, material = materials.marble, make_trail = True, trail_type = "points", interval = 10)

       
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0

    while true:

        rate(35)
        a = a - ((2*pi)/59)

        x = 60*cos(a)
        z = 60*sin(a)
        
        mercury.pos = (x,0,z)
        mercury.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = mercury.pos)

        b = b - ((2*pi)/225)

        x = 85*cos(b)
        z = 85*sin(b)
        
        venus.pos = (x,0,z)
        venus.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = venus.pos)

        c = c - ((2*pi)/365)
        d = d - ((2*pi)/28)

        x = 108*cos(c)
        z = 108*sin(c)
		
        earth.pos = (x,0,z)
                   
        moon.pos.x = earth.pos.x + 15*cos(d)
        moon.pos.z = earth.pos.z + 15*sin(d)

        earth.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = earth.pos)

        e = e - ((2*pi)/687)

        x = 132*cos(e)
        z = 132*sin(e)
        
        mars.pos = (x,0,z)
        mars.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = mars.pos)

        f = f - ((2*pi)/880)
        
        x = 181*cos(f)
        z = 181*sin(f)
        
        jupiter.pos = (x,0,z)
      
        jupiter.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = jupiter.pos)

        g = g - ((2*pi)/1000)        
        j = j - ((2*pi)/5)

        x = 208*cos(g)
        z = 208*sin(g)
        
        saturnus.pos = (x,0,z)
        ring.pos.x = saturnus.pos.x
        ring.pos.z = saturnus.pos.z
        saturnus.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = saturnus.pos)

        h = h - ((2*pi)/1500)

        x = 230*cos(h)
        z = 230*sin(h)
        
        uranus.pos = (x,0,z)
        uranus.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = uranus.pos)

        i = i - ((2*pi)/2000)

        x = 255*cos(i)
        z = 255*sin(i)
        
        neptunus.pos = (x,0,z)
        neptunus.rotate(angle = (pi/60) ,axis=(-0.15, 1, 0), origin = neptunus.pos)

main()	
