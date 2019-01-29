import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys

def save_frame(U, i):
    fig = plt.figure(figsize=(7, 7))
    plt.imshow(U,
              interpolation=None,
              extent=[-1, 1, -1, 1])
    plt.axis('off')
    plt.savefig('./pics/frame{:05d}.png'.format(i), pad_inches=0)
    plt.close(fig)

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

    print(sys.argv)
    path = sys.argv[1]

    generate_frames(path)

    os.system('convert pics/*.png -delay 0.001 pics/output.gif')
