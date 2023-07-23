import streamlit as st
import cv2
import numpy as np
import warnings
import json
from paddleocr import PaddleOCR
import time

def testocr(img):
    try:
        ocr = PaddleOCR(use_angle_cls=False, lang="ch", show_log=False) 
        result = ocr.ocr(img, cls=True)
        ret = ''
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                ret += line[-1][0]+'\n'
        print(f'当前ocr识别文本结果:{ret}-{time.time()}')
        return ret
    except Exception as err:
        print(f'testocr异常:{err}')
        return '异常'

upload_file =st.file_uploader("上传", ['png', 'jpg', 'jpeg'])

if upload_file is not None:
    bytes_data = upload_file.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    # ocr识别配料表中
    with st.spinner(f'结果识别中'):
        st.title(f'{testocr(cv2_img)}')
