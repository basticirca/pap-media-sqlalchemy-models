from database.access.api import Api

from database import tables
from database.tables.resource import ResourceType


class ImageApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_image(self, name, local_path):
        resource = tables.Resource(
            uuid=tables.Resource.create_uuid(),
            type=ResourceType.image,
            name=name
        )
        image = tables.Image(uuid=resource.uuid, local_path=local_path)
        image.resource = resource
        self.insert_all([resource, image])
        return image

    def get_image(self, uuid):
        return self.select(tables.Image, tables.Image.uuid == uuid).first()

    def _get_resource(self, uuid):
        return self.select(tables.Resource, tables.Resource.uuid == uuid).first()

    def remove_image(self, uuid):
        resource = self._get_resource(uuid)
        if resource is None:
            return False
        image = self.get_image(uuid)
        self.delete(resource)
        self.delete(image)
        return True

    def get_image_list(self):
        return self.select(tables.Image)

    def remove_image_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_image(uuid):
                success = False
        return success

    def set_resource(self, image_uuid, resource_uuid):
        # TODO - remove from server
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        image = self.get_image(image_uuid)
        if image is None:
            return False
        image.resource = resource

    def add_album(self, image_uuid, album_uuid):
        album = self.select(
            tables.Album,
            tables.Album.uuid == album_uuid
        ).first()
        if album is None:
            return False
        image = self.get_image(image_uuid)
        if image is None:
            return False
        image.albums.append(album)
        return True

    def remove_album(self, image_uuid, album_uuid):
        album = self.select(
            tables.Album,
            tables.Album.uuid == album_uuid
        ).first()
        if album is None:
            return False
        image = self.get_image(image_uuid)
        if image is None:
            return False
        image.albums.remove(album)
        return True

