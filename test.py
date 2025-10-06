from drawsvg3D import scene,sphere,camera,point

import math

scene = scene.Scene()

camera = camera.Camera()
camera.projection()

n = 30

objects = []

for i in range(n):
    object = point.Point()
    objects.append(object)

for i in range(n):
    objects[i].center = [1*30*math.cos(i*(2*math.pi/n)),30*math.sin(i*(2*math.pi/n)), 0]
    print(objects[i].center)

for object in objects:
    object.projection(camera)
    scene.objects.append(object)






scene.objects.append(point.Point())




scene.draw()

scene.save()



