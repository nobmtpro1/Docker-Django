import os
import string
import random
import time
from django.conf import settings


def uploadFile(file, path):
    if file.name:
        randomString = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=10)
        )
        now = int(round(time.time() * 1000))
        fileName, fileExtension = os.path.splitext(file.name)
        newFileName = str(now) + randomString + fileExtension
        fn = os.path.join(str(settings.BASE_DIR) + path, newFileName)
    open(fn, "wb").write(file.file.read())
    return newFileName


def validateFile(file, types, maxSize):
    fileName, fileExtension = os.path.splitext(file.name)
    size = file.size
    print(size)
    if types == "image":
        types = [
            ".apng",
            ".avif",
            ".gif",
            ".jpg",
            ".jpeg",
            ".jfif",
            ".pjpeg",
            ".pjp",
            ".png",
            ".svg",
            ".webp",
        ]
    if fileExtension not in types:
        return "File is not allowed"
    if size > maxSize:
        return "File is too large"
    return False
