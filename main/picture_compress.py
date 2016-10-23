from math import gcd
import os

import numpy as np
import cv2


def pic_compress(filename):
    while filename[0] == '\\' or filename[0] == '/':
        filename = filename[1:]

    TARGET_HEIGHT = 256
    TARGET_WIDTH = 192
    RATIO_HEIGHT = TARGET_HEIGHT // gcd(TARGET_HEIGHT, TARGET_WIDTH)
    RATIO_WIDTH = TARGET_WIDTH // gcd(TARGET_HEIGHT, TARGET_WIDTH)

    raw_img = cv2.imread(filename, cv2.IMREAD_COLOR)

    raw_height = raw_img.shape[0]
    raw_width = raw_img.shape[1]

    if raw_height * RATIO_WIDTH == raw_width * RATIO_HEIGHT:
        extended_height = raw_height
        extended_width = raw_width
    elif raw_height * RATIO_WIDTH > raw_width * RATIO_HEIGHT:
        raw_height = raw_height // RATIO_HEIGHT * RATIO_HEIGHT
        raw_width = raw_width // RATIO_WIDTH * RATIO_WIDTH
        extended_height = raw_height // RATIO_HEIGHT * RATIO_HEIGHT
        extended_width = raw_height // RATIO_HEIGHT * RATIO_WIDTH
    else:
        raw_height = raw_height // RATIO_HEIGHT * RATIO_HEIGHT
        raw_width = raw_width // RATIO_WIDTH * RATIO_WIDTH
        extended_height = raw_width // RATIO_WIDTH * RATIO_HEIGHT
        extended_width = raw_width // RATIO_WIDTH * RATIO_WIDTH

    extended_img = np.zeros((extended_height, extended_width, 4), dtype=np.uint64) + [255, 255, 255, 0]

    start_height = (extended_height - raw_height) // 2
    start_width = (extended_width - raw_width) // 2

    for i in range(raw_height):
        for j in range(raw_width):
            extended_img[start_height + i][start_width + j] = raw_img[i][j][:].tolist() + [255]

    target_img = np.zeros((TARGET_HEIGHT, TARGET_WIDTH, 4), dtype=np.uint64)
    cnt = np.zeros((TARGET_HEIGHT, TARGET_WIDTH), dtype=np.uint64)

    for i in range(extended_height):
        for j in range(extended_width):
            x = i * TARGET_HEIGHT // extended_height
            y = j * TARGET_WIDTH // extended_width

            cnt[x][y] += 1
            target_img[x][y] = target_img[x][y] + extended_img[i][j]

    for i in range(TARGET_HEIGHT):
        for j in range(TARGET_WIDTH):
            if cnt[i][j] > 0:
                target_img[i][j] = target_img[i][j] // cnt[i][j]

    target_filename = os.path.join(os.path.split(filename)[0],
                                   'thumbnail_' + os.path.split(filename)[1].split('.')[0] + '.png')
    cv2.imwrite(target_filename, target_img)
