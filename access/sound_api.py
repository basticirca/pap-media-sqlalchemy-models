from access.api import Api

import tables
from tables.resource import ResourceType


class SoundApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_sound(self, name, local_path):
        resource = tables.Resource(
            uuid=tables.Resource.create_uuid(),
            type=ResourceType.sound,
            name=name
        )
        sound = tables.Sound(uuid=resource.uuid, local_path=local_path)
        sound.resource = resource
        self.insert_all([resource, sound])
        return sound

    def get_sound(self, uuid):
        return self.select(tables.Sound, tables.Sound.uuid == uuid).first()

    def _get_resource(self, uuid):
        return self.select(tables.Resource, tables.Resource.uuid == uuid).first()

    def remove_sound(self, uuid):
        resource = self._get_resource(uuid)
        if resource is None:
            return False
        sound = self.get_sound(uuid)
        self.delete(resource)
        self.delete(sound)
        return True

    def get_sound_list(self):
        return self.select(tables.Sound)

    def remove_sound_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_sound(uuid):
                success = False
        return success

    def set_resource(self, sound_uuid, resource_uuid):
        # TODO - remove from server
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        sound = self.get_sound(sound_uuid)
        if sound is None:
            return False
        sound.resource = resource

    def add_playlist(self, sound_uuid, playlist_uuid):
        playlist = self.select(
            tables.Playlist,
            tables.Playlist.uuid == playlist_uuid
        ).first()
        if playlist is None:
            return False
        sound = self.get_sound(sound_uuid)
        if sound is None:
            return False
        sound.playlists.append(playlist)
        return True

    def remove_playlist(self, sound_uuid, playlist_uuid):
        playlist = self.select(
            tables.Playlist,
            tables.Playlist.uuid == playlist_uuid
        ).first()
        if playlist is None:
            return False
        sound = self.get_sound(sound_uuid)
        if sound is None:
            return False
        sound.playlists.remove(playlist)
        return True

