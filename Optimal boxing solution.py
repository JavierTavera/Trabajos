GlowScript 3.1 VPython

l = []

l.append(int(input())) #x
l.append(int(input())) #y
l.append(int(input())) #z

#l1 = int(input())
#l2 = int(input())
#l3 = int(input())

B1 = 5
B2 = 6
B3 = 4

definx = definy = definz = 0

maxi = 0

for i in range(3):
    x = int(l[0 + i]/B1)
    y = int(l[(1 + i)%3]/B2)
    z = int(l[(2 + i)%3]/B3)
    if x*y*z > maxi:
        maxi = x*y*z
        definx = l[0 + i]
        definy = l[(1 + i)%3]
        definz = l[(2 + i)%3]
    

container1 = box(pos=vector(0,0,-definy*int(definy/B2)/2), opacity=0.3, opacity=0.3, length=B1, height=B2, width=0.1, color=color.cyan)
container1 = box(pos=vector(0,-definz*int(definz/B3)/2,1), opacity=0.3, opacity=0.3, length=B2, height=0.1, width=B3, color=color.cyan)

box1=box(pos=vector(0,0,0), length=definx, height=definz, width=definy, color=color.white)
#box2=box(pos=vector(-1,-1.01,0), length=3, height=1, width=1, color=color.white)

scene.caption = """The maximum number of boxes within the container have to be positioned in this way"""
