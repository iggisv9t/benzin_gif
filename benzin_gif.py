import numpy as np
import cv2
import os
import sys

def save_frame(U, i):
    cv2.imwrite('./pics/frame{:05d}.png'.format(i), U*255)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def generate_frames(path):
    im = cv2.imread(path)
    nframes = 25
    for i in range(nframes):
        shift = 2 * np.pi * (i + 1) / nframes
        U = sigmoid(np.sin(im.astype(np.int32) / (10 + (np.sin(shift) + 3)) + shift))
        save_frame(U, i)

if __name__ == "__main__":
    if not os.path.exists('pics'):
        os.makedirs('pics')

    path = sys.argv[1]

    generate_frames(path)
    os.system('convert pics/*.png -delay 0.001 pics/output.gif')
    os.system('ffmpeg -i pics/output.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" pics/video.mp4')
