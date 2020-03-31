from access.api import Api

import tables


class PlaylistApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_playlist(self, name, description, sound_uuids=[]):
        obj = tables.Playlist(uuid=tables.Playlist.create_uuid(), name=name, description=description)
        if len(sound_uuids) > 0:
            obj.sounds = self.select(tables.Sound, tables.Sound.uuid.in_(sound_uuids)).all()
        self.insert(obj)
        return obj

    def get_playlist(self, uuid):
        return self.select(tables.Playlist, tables.Playlist.uuid == uuid).first()

    def remove_playlist(self, uuid):
        playlist = self.get_playlist(uuid)
        if playlist is None:
            return False
        self.delete(playlist)
        return True

    def get_playlist_list(self):
        return self.select(tables.Playlist)

    def remove_playlist_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_playlist(uuid):
                success = False
        return success

    def add_sound(self, playlist_uuid, sound_uuid):
        sound = self.select(
            tables.Sound,
            tables.Sound.uuid == sound_uuid
        ).first()
        if sound is None:
            return False
        playlist = self.get_playlist(playlist_uuid)
        if playlist is None:
            return False
        playlist.sounds.append(sound)
        return True

    def remove_sound(self, playlist_uuid, sound_uuid):
        sound = self.select(
            tables.Sound,
            tables.Sound.uuid == sound_uuid
        ).first()
        if sound is None:
            return False
        playlist = self.get_playlist(playlist_uuid)
        if playlist is None:
            return False
        playlist.sounds.remove(sound)
        return True

    def add_tag(self, playlist_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        playlist = self.get_playlist(playlist_uuid)
        if playlist is None:
            return False
        playlist.tags.append(tag)
        return True

    def remove_tag(self, playlist_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        playlist = self.get_playlist(playlist_uuid)
        if playlist is None:
            return False
        playlist.tags.remove(tag)
        return True

