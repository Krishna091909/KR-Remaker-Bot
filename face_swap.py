import cv2
import numpy as np
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(file_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID, 'caption': '🧠 Face swapped image from Remaker Flask bot'}
        requests.post(url, files=files, data=data)

def swap_faces(src_path, tgt_path):
    src_img = cv2.imread(src_path)
    tgt_img = cv2.imread(tgt_path)
    
    src_img = cv2.resize(src_img, (300, 300))
    tgt_img = cv2.resize(tgt_img, (300, 300))

    h, w, _ = src_img.shape
    center = (w // 2, h // 2)
    mask = 255 * np.ones(src_img.shape, src_img.dtype)

    output = cv2.seamlessClone(src_img, tgt_img, mask, center, cv2.NORMAL_CLONE)
    result_path = "static/uploads/result.jpg"
    cv2.imwrite(result_path, output)

    send_to_telegram(result_path)
    return result_path
