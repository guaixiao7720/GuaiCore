import pygame

from obj.Obj import Obj


# 未完成
class Music(Obj):
    def __init__(self, game, name, sounds_dict: dict = None, sound: str = None):
        super().__init__(game, name)
        self.__sounds_dict = sounds_dict
        if sound is not None:
            self.__sound: pygame.mixer.Sound = self.__sounds_dict[sound]
        else:
            self.__sound: pygame.mixer.Sound = None

    def run(self):
        pass

    def get_sounds_list(self):
        return self.__sounds_dict

    def load_sounds(self, sounds_dict: dict):
        self.__sounds_dict = sounds_dict

    def add_sounds(self, audio: pygame.mixer.Sound, name: str):
        self.__sounds_dict[name] = audio

    def set_sound(self, name: str):
        self.__sound = self.__sounds_dict[name]
