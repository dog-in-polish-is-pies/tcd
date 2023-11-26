from drawbot_skia.drawbot import oval, fill, saveImage

y = 45 
step = 200

for i in range(5):
    fill(1, 0, 5)
    oval(200, y, 100, 100)
    y = y + step

saveImage("task_1.pdf")
