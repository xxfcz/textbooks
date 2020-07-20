from PIL import Image
import glob
import os

# 将文件夹中所有webp图片分别转换为jpg文件
def webp2jpg(img_path):
    for filename in sorted(glob.glob(img_path + r"\*.webp")):  # 读取图片，确保按文件名排序
        im = Image.open(filename)
        if im.mode == "RGB":
            im.load()  # required for png.split()
            #background = Image.new("RGB", im.size, (255, 255, 255))
            #background.paste(im, mask=im.split()[3]) 
            save_name = filename.replace('webp', 'jpg')
            im = im.crop((58, 93, 920, 1320))
            im.save('{}'.format(save_name), 'JPEG')


if __name__ == '__main__':
    webp2jpg(r"E:\xxf\python\ex\images")
