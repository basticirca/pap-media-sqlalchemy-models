from access.api import Api

import tables


class AlbumApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_album(self, name, description):
        obj = tables.Album(uuid=tables.Album.create_uuid(), name=name, description=description)
        self.insert(obj)
        return obj

    def get_album(self, uuid):
        return self.select(tables.Album, tables.Album.uuid == uuid).first()

    def remove_album(self, uuid):
        album = self.get_album(uuid)
        if album is None:
            return False
        self.delete(album)
        return True

    def get_album_list(self):
        return self.select(tables.Album)

    def remove_album_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_album(uuid):
                success = False
        return success

    def add_image(self, album_uuid, image_uuid):
        image = self.select(
            tables.Image,
            tables.Image.uuid == image_uuid
        ).first()
        if image is None:
            return False
        album = self.get_album(album_uuid)
        if album is None:
            return False
        album.images.append(image)
        return True

    def remove_image(self, album_uuid, image_uuid):
        image = self.select(
            tables.Image,
            tables.Image.uuid == image_uuid
        ).first()
        if image is None:
            return False
        album = self.get_album(album_uuid)
        if album is None:
            return False
        album.images.remove(image)
        return True

    def add_tag(self, album_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        album = self.get_album(album_uuid)
        if album is None:
            return False
        album.tags.append(tag)
        return True

    def remove_tag(self, album_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        album = self.get_album(album_uuid)
        if album is None:
            return False
        album.tags.remove(tag)
        return True

