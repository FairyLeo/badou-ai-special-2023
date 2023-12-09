#均值哈希
def  hash_mean(img):
    h, w = img.shape[:2]
    # 计算均值哈希值
    m = np.mean(img)
    print(m)
    # 计算哈希值
    d = []
    for i in range(h):
        for j in range(w):
            if img[i, j] > m:
                d.append(1)
            else:
                d.append(0)
    return d

#插值哈希
def hash_pil(img):
    img = img.resize((8, 8), Image.ANTIALIAS)
    # 灰度化
    img = img.convert('L')
    # 二值化
    img = img.point(lambda i: 0 if i < 100 else 255, '1')
    # 计算哈希值
    d = []
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == 0:
                d.append(1)
            else:
                d.append(0)
    return d

#差值哈希
def hash_difference(img):
    h, w = img.shape[:2]
    # 计算差值哈希值
    l = []
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # 灰度差值
            g = abs(np.mean(img[i - 1, j - 1]) - np.mean(img[i + 1, j + 1]))
            l.append(g)
    return l
