import cv2, os, json, argparse, sys
import numpy as np
from PIL import Image

def vis_gif(images, filename, fps=30):
    for i in range(len(images)):
        img = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
        images[i] = Image.fromarray(img)
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=int(1000 / fps), loop=0)

def vis_mp4(images, filename, fps=30):
    video = cv2.VideoWriter(filename, 0x7634706d, fps, (images[0].shape[1],images[0].shape[0]))
    for image in images:
        video.write(image)
    video.release()

H, W = 244, 244

images = [None for i in range(H)]

for i in range(len(images)):
    im = np.zeros((H, W, 3))
    im[i, ...] = 255
    images[i] = (im).astype(np.uint8)

vis_mp4(images, filename='out.mp4', fps=30)
vis_gif(images, filename='out.gif', fps=30)


