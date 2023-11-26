from drawbot_skia.drawbot import fill, rect, stroke, strokeWidth, saveImage

y = 15
x = 15
step = 20
for i in range(49):
    for j in range(49):
        fill(106/255, 90/255, 205/255)
        stroke(186/255, 85/255,211/255)
        strokeWidth(1)
        rect(x, y, 10, 10)
        y = y + step
    y = 15
    x = x + step

saveImage("task_2.pdf")
