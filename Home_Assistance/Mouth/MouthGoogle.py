#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Mouth Google module for Home Assistant '

from MouthBase import MouthBase
from gtts import gTTS
import tempfile
import pygame
import time

__author__ = 'Ed Hsu'


class MouthGoogle(MouthBase):
    def __init__(self):
        pygame.mixer.init()

    def speak(self, words):
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts = gTTS(text=words, lang='zh-TW')
            tts.save("{}.mp3".format(fp.name))
            pygame.mixer.music.load("{}.mp3".format(fp.name))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

if __name__ == '__main__':
    myMouth = MouthGoogle()
    # myMouth.speak('I am so happy.')
    myMouth.speak('你功課寫好了嗎')

