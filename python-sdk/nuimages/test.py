from nuimages import NuImages

nuim = NuImages(verbose=True, lazy=True)

#print(nuim.category[0])
#print(nuim.object_ann[0])

nuim.explorer.render_image(nuim.image[0]['token'])