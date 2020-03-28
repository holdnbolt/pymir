import pymir

camera = pymir.camera()
camera.start()

for n in range(10000):
    camera.update()

exit(0)