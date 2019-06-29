from database.access.api import Api
from database import tables


class SoundApi(Api):
    def __init__(self, bind):
        super().__init__(bind)

    def add_sound_file(self, uuid, name):
        sound = tables.Sound()
        sound.resource = tables.Resource(uuid=uuid, name=name, type=ResourceType.sound)
        self.insert(sound)
        return sound

    def get_sound_file(self, uuid):
        return self.select(tables.Sound, tables.Sound.uuid == uuid).first()

    def get_sound_files(self):
        return self.select(tables.Sound)

    def remove_sound_file(self, uuid):
        sound = self.get_sound_file(uuid)
        if sound is None:
            return False
        self.delete(sound.resource)
        return True

    def remove_sound_files(self, uuids=[]):
        for uuid in uuids:
            if not self.remove_sound_file(uuid):
                return False
        return True