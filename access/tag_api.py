from database.access.api import Api

from database import tables


class TagApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_tag(self, name, description):
        obj = tables.Tag(uuid=tables.Tag.create_uuid(), name=name, description=description)
        self.insert(obj)
        return obj

    def get_tag(self, uuid):
        return self.select(tables.Tag, tables.Tag.uuid == uuid).first()

    def remove_tag(self, uuid):
        tag = self.get_tag(uuid)
        if tag is None:
            return False
        self.delete(tag)
        return True

    def get_tag_list(self):
        return self.select(tables.Tag)

    def remove_tag_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_tag(uuid):
                success = False
        return success

    def add_resource(self, tag_uuid, resource_uuid):
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.resources.append(resource)
        return True

    def remove_resource(self, tag_uuid, resource_uuid):
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.resources.remove(resource)
        return True

    def add_preset(self, tag_uuid, preset_uuid):
        preset = self.select(
            tables.Preset,
            tables.Preset.uuid == preset_uuid
        ).first()
        if preset is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.presets.append(preset)
        return True

    def remove_preset(self, tag_uuid, preset_uuid):
        preset = self.select(
            tables.Preset,
            tables.Preset.uuid == preset_uuid
        ).first()
        if preset is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.presets.remove(preset)
        return True

    def add_project(self, tag_uuid, project_uuid):
        project = self.select(
            tables.Project,
            tables.Project.uuid == project_uuid
        ).first()
        if project is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.projects.append(project)
        return True

    def remove_project(self, tag_uuid, project_uuid):
        project = self.select(
            tables.Project,
            tables.Project.uuid == project_uuid
        ).first()
        if project is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.projects.remove(project)
        return True

    def add_playlist(self, tag_uuid, playlist_uuid):
        playlist = self.select(
            tables.Playlist,
            tables.Playlist.uuid == playlist_uuid
        ).first()
        if playlist is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.playlists.append(playlist)
        return True

    def remove_playlist(self, tag_uuid, playlist_uuid):
        playlist = self.select(
            tables.Playlist,
            tables.Playlist.uuid == playlist_uuid
        ).first()
        if playlist is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.playlists.remove(playlist)
        return True

    def add_album(self, tag_uuid, album_uuid):
        album = self.select(
            tables.Album,
            tables.Album.uuid == album_uuid
        ).first()
        if album is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.albums.append(album)
        return True

    def remove_album(self, tag_uuid, album_uuid):
        album = self.select(
            tables.Album,
            tables.Album.uuid == album_uuid
        ).first()
        if album is None:
            return False
        tag = self.get_tag(tag_uuid)
        if tag is None:
            return False
        tag.albums.remove(album)
        return True

