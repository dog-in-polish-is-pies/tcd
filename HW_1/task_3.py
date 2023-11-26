from drawbot_skia.drawbot import rect, fill, oval, stroke, strokeWidth, saveImage

rect(150, 150, 700, 700)

x = 150
y = 150
for x in range(40):
    for y in range(40):
        fill(x/12, 0, 1)
        rect(52*x, 52*y, 15, 15)


for x in range(20):
    for y in range(20):
        fill(0, x/10, 1)
        oval(50*x, 50*y, 20, 20)

fill(None)
stroke(255/255, 255/255, 255/255)
strokeWidth(101)
rect(150, 150, 700, 700)

saveImage('task_3.pdf')
