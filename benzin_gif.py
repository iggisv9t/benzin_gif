import numpy as np
import matplotlib.pyplot as plt
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
    if not ('pics' in os.listdir('./')):
        os.system('mkdir pics')

    path = sys.argv[1]

    generate_frames(path)
    os.system('convert pics/*.png -delay 0.001 pics/output.gif')
