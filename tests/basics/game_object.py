import pymir

camera = pymir.camera()
camera.start()
obj = pymir.gobject()
camera.attach_object(obj)

for n in range(10):
    camera.update()