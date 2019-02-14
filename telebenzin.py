import telepot
from telepot.loop import MessageLoop
import logging
import numpy as np
import time
import cv2
import benzin_gif
import requests
import os

secret_file = '../telegram_token'
with open(secret_file) as fp:
    TOKEN = fp.readline()[:-1]

def handle(msg):
    chat_id = msg['chat']['id']
    try:
        photo = msg['photo']
        print(photo)


        file_path = bot.getFile(photo[-2]['file_id'])['file_path']
        file_link = 'https://api.telegram.org/file/bot' + TOKEN + '/' + file_path
        image = requests.get(file_link).content
        path = 'temp.jpg'
        with open(path, 'wb') as fp:
            fp.write(image)

        benzin_gif.generate_frames(path)
        os.system('convert pics/*.png -delay 0.001 pics/output.gif')
        os.system('ffmpeg -i pics/output.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" pics/video.mp4')

        bot.sendVideo(chat_id, open('pics/video.mp4', 'rb'))
        os.system('rm pics/video.mp4 pics/output.gif')    

    except:
        bot.sendMessage(chat_id, 'Something went wrong.\nDo not try again.')
        print('error')
        print(msg)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
logging.info('Ready')

while 1:
    time.sleep(10)
