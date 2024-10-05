from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Error, not found picture")

        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + ".jpg"
        rotated.save(new_filename)
    
    def do_croped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + ".jpg"
        cropped.save(new_filename)

myIm = ImageEditor("original.jpg")
myIm.open()

myIm.do_left()
myIm.do_croped()

for im in myIm.changed:
    im.show()