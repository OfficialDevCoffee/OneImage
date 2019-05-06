#ImageHandler.py
from PIL import Image

#이미지 크기 반환 함수
def imageSize(image):
    return image.size

#이미지 코덱 변환
def toJPG(image, imagename, imagecodec):
    return image.save(imagename , imagecodec)

#이미지 thumbnail 변환
def toThumbnail(image, sizeX, sizeY):
    size = (sizeX, sizeY)
    image.thumbnail(size)
    return image

#이미지 픽셀 값 반환
def getPixel(image, x, y):
    return image.getpixel((x, y))

#이미지 픽셀 값 설정
def setPixel(image, x, y, color)
    return image.putpixel((x, y), color)

#이미지 자르기
def cropImage(image, x1, y1, x2, y2):
    return image.crop((x1, y1), (x2, y2))

#이미지 회전
def rotateImage(image, degrees):
    return image.rotate(degress)

#이미지 대칭
def flipImage(image, fliporientation):
    if fliporientation:
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image.transpose(Image.FLIP_TOP_BOTTOM)

#이미지 사이즈 조정
def resizeImage(image, width, height):
    return image.resize((width, height))

#이미지 투명도 조정
def setalphaImage(image, alpha):
    return image.putalpha(alpha)



