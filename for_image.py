import PIL
from PIL import Image
from django.utils.timezone import now


def give_name(name, string):
    folders = ['blog', 'banner', 'feedback', 'specialist']
    ext = name.rsplit('.', 1)

    n = name.split('/')[0]
    print(name)
    print(n)
    if n in folders:
        name = name.split('_', 1)[-1]

        return string + '_' + name

    name = str(now()).rsplit('.', 1)[0]
    new_name = "{}_{}.{}".format(string, name, ext[-1]).replace(' ', '_').replace(':', '')

    return new_name


def resize_image(ob, size1, size2):
    path1 = ob.photo.path
    path2 = ob.photo_small.path

    img1 = Image.open(ob.photo)
    img2 = Image.open(ob.photo)

    width1, height1 = img1.size
    percent1 = size1 / width1
    height1 = int(height1 * percent1)

    width2, height2 = img2.size
    percent2 = size2 / width2
    height2 = int(height2 * percent2)
    img1 = img1.resize((size1, height1), PIL.Image.ANTIALIAS)
    img2 = img2.resize((size2, height2), PIL.Image.ANTIALIAS)
    img1.save(path1)
    img2.save(path2)
