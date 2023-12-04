from drawbot_skia.drawbot import rect, oval, fill, stroke, strokeWidth, newPage, saveImage, newDrawing

rules = [1, 0, 1, 0, 2, 0, 1, "ёж", 2, 0, 3, 1, "ёжжж"] * 20

w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin

step = (w - margin * 2) / 6
size = step


for rule in rules:
    if rule == 0:
        fill(0/255, 191/255, 255/255)
        stroke(None)
        oval(x, y - step, size, size)
    elif rule == 1:
        fill(70/255, 130/255, 180/255)
        stroke(None)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(0/255, 0/255, 128/255)
        strokeWidth(3)
        oval(x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")

    x += step

    if x >= w - margin:
        x = margin
        y -= step


    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin

saveImage("new.pdf")

###################
#### задание_2 ####
###################

newDrawing()
rules = [1, 3, 2, 0, 2, 3, 1, "ёж"] * 60

w, h = 1050, 742.5
newPage(w, h)

margin = 50
x = margin
y = h - margin

step = (w - margin * 2) / 15
size = step


for rule in rules:
    if rule == 1:
        fill(255/255, 105/255, 180/180)
        stroke(None)
        rect(x, y - step, size, size)
    elif rule == 0:
        fill(199/255, 21/255, 133/255)
        stroke(None)
        oval(x, y - step, size, size)
    elif rule == 2:
        fill(147/255, 112/255, 219/255)
        stroke(None)
        rect(x, y - step, size, size)
    elif rule == 3:
        fill(255/255, 105/255, 180/255)
        stroke(255/255, 20/255, 147/255)
        strokeWidth(3)
        oval(x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")

    x += step

    if x >= w - margin:
        x = margin
        y -= step


    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin

saveImage("smth.pdf")
