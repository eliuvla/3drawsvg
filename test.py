from drawsvg3D import scene,sphere



scene = scene.Scene()

scene.objects.append(sphere.Sphere())

scene.draw()

scene.save()



