import imagen as ig
import holoviews as hv
from PIL import Image, ImageFilter
from IPython import get_ipython

ipython = get_ipython()
ipython.magic("load_ext holoviews.ipython")
ipython.magic("opts Layout [vertical_spacing=0.0 horizontal_spacing=0.0] Image [show_xaxis=None show_yaxis=None show_frame=False show_title=False padding=0]")

def illusion(pat): 
    h, w = 256, 256
    uni = Image.new('RGB', (h,w))
    for i in range(0, w, bw):
        for j in range(0, h, bh):
            uni.paste(pat, (i, j))
    box = (50, 50, h-50, w-50)
    blur = uni.filter(ImageFilter.BLUR)
    blur = blur.crop(box)
    uni.paste(blur, box)
    return uni

shapes = [ig.Rectangle(), ig.RawRectangle(), ig.Ring(), ig.Disk()]
c = 0
for shape in shapes: 
    for i in range(-0.95, 0.01, 0.95):
        for j in range(-0.95,0.01, 0.95):
            shape.x = i
            shape.y = j

            c += 1
            hv.save(shape[:], 'illusion_image/blur/uniform/{}.png'.format(c));
            pat = Image.open('illusion_image/blur/uniform/{}.png'.format(c))
            pat = pat.resize((16,16))
            pat.save('illusion_image/blur/uniform/{}.png'.format(c))
            ill_0 = illusion(pat)
            ill_0.save('illusion_image/blur/blurred/{}.png'.format(c))

            c += 1
            pat = pat.crop((1,1,15,15))
            pat = pat.resize((16, 16))
            pat.save('illusion_image/blur/uniform/{}.png'.format(c))
            ill_1 = illusion(pat)
            ill_1.save('illusion_image/blur/blurred/{}.png'.format(c))

            c += 1
            pat = pat.resize((100, 100))
            pat = pat.crop((5,5,bh-5,bw-5))
            pat = pat.resize((16, 16))
            pat.save('illusion_image/blur/uniform/{}.png'.format(c))
            ill_2 = illusion(pat)
            ill_2.save('illusion_image/blur/{}.png'.format(c))