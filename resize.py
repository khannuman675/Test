from PIL import Image
fl=Image.open("download.png")
print(fl.size[0],fl.size[1])
fl=fl.resize(((fl.size[0]//2),(fl.size[1]//2)),Image.ANTIALIAS)
#fl.format=JPG
fl.save("new!_image.jpg",quality=95)
print(fl.size[0],fl.size[1])