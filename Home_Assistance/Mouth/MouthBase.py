#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Mouth Base module for Home Assistant '

from abc import ABCMeta, abstractmethod

__author__ = 'Ed Hsu'


class MouthBase(metaclass=ABCMeta):
    @abstractmethod
    def speak(self, words):
        pass


if __name__ == '__main__':
    pass
