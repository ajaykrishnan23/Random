import img2pdf
from PIL import Image
import os

def imgs2pdf(imgs_path,file_path):
    file_path[1] = file_path[1]+'.pdf'
    f = open(os.path.join(file_path[0],file_path[1]),"wb")
    imgs_path =[ os.path.join(imgs_path,img) for img in os.listdir(imgs_path) if img.endswith("jpeg")]
    f.write(img2pdf.convert(imgs_path))
    f.close()
    print("succesfully made pdf file")

def main():
    imgs_path = input('Provide absolute path of images')
    file_path = input('Provide absolute path of pdf\'s directory and name of pdf file separated by ,')
    file_path = list(file_path.split(','))
    imgs2pdf(imgs_path,file_path)

main()
