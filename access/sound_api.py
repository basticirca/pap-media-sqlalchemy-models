from database.access.api import Api
from database import tables
from database.tables.resource import ResourceType


class SoundApi(Api):
    def __init__(self, bind):
        super().__init__(bind)

    def add_sound(self, uuid, name):
        sound = tables.Sound()
        sound.resource = tables.Resource(uuid=uuid, name=name, type=ResourceType.sound)
        self.insert(sound)
        return sound

    def get_sound(self, uuid):
        return self.select(tables.Sound, tables.Sound.uuid == uuid).first()

    def get_sounds(self):
        return self.select(tables.Sound)

    def remove_sound(self, uuid):
        sound = self.get_sound(uuid)
        if sound is None:
            return False
        self.delete(sound.resource)
        return True

    def remove_sounds(self, uuids=[]):
        for uuid in uuids:
            if not self.remove_sound(uuid):
                return False
        return True
