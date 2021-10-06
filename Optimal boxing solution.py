GlowScript 3.1 VPython

l = []

l.append(int(input())) #x
l.append(int(input())) #y
l.append(int(input())) #z

B1 = 5
B2 = 6
B3 = 4

spacing = 0.01

definx = definy = definz = 0

maxi = 0

for i in range(3):
    x = int(B1/(l[0 + i] + spacing))
    y = int(B2/l[(1 + i)%3] + spacing)
    z = int(B3/l[(2 + i)%3] + spacing)
    if x*y*z > maxi:
        maxi = x*y*z
        definx = l[0 + i]
        definy = l[(1 + i)%3]
        definz = l[(2 + i)%3]
        x1 = x
        y1 = y
        z1 = z
    

container1 = box(pos=vector(0,0,-B2/2 - 0.1), opacity=0.3, opacity=0.3, length=B1, height=B3, width=0.1, color=color.cyan)
container2 = box(pos=vector(0,-B3/2 - 0.1,0), opacity=0.3, opacity=0.3, length=B1, height=0.1, width=B2, color=color.cyan)
container2 = box(pos=vector(-B1/2 - 0.1,0,0), opacity=0.3, opacity=0.3, length=0.1, height=B3, width=B2, color=color.cyan)

for i in range(x1):
    for j in range(y1):
        for k in range(z1):
            box1=box(pos=vector(-B1/2 + definx/2 + i*(definx + spacing),-B3/2 + definz/2 + k*(definx + spacing),-B2/2 + definy/2 + j*(definy + spacing)), length=definx, height=definz, width=definy, color=color.white)
#box2=box(pos=vector(-1,-1.01,0), length=3, height=1, width=1, color=color.white)

scene.caption = """The maximum number of boxes that can fit in the container are:  """ + str(maxi) + """\nThe position of the cointainer ahs to have these dimentions: x: ... """ + str(definx)
