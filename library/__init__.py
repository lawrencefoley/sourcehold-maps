import os


class MapFile(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.map = None

    def pack_to_game_folder(self):
        pass

    def unpack_from_game_folder(self):
        pass

    def pack(self):
        pass

    def unpack(self):
        pass

    def unpack_to_folder(self, path):
        pass

    def unpack_to_file_inspection(self):
        self.unpack_to_folder("file_inspection/maps")


MAP_FILE = "Maps"
SAVE_FILE = "Saves"


class Library(object):

    def __init__(self, path="~/Documents/Stronghold Crusader"):
        self.path = os.path.expanduser(path)
        self.maps = os.path.join(self.path, "Maps")
        self.saves = os.path.join(self.path, "Saves")

    def _as_file(self, name):
        return name if not name.endswith(".map") else name + ".map"

    def _as_folder(self, name):
        return name if not name.endswith(".map") else name[-4:]

    def get_from_saves(self, name):
        path = os.path.join(self.saves, self._as_file(name))

    def get_from_maps(self, name):
        pass
