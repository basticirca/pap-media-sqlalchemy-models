from access.api import Api

import tables


class ResourceApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_resource(self, name):
        obj = tables.Resource(uuid=tables.Resource.create_uuid(), name=name)
        self.insert(obj)
        return obj

    def get_resource(self, uuid):
        return self.select(tables.Resource, tables.Resource.uuid == uuid).first()

    def remove_resource(self, uuid):
        resource = self.get_resource(uuid)
        if resource is None:
            return False
        self.delete(resource)
        return True

    def get_resource_list(self):
        return self.select(tables.Resource)

    def remove_resource_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_resource(uuid):
                success = False
        return success

    def add_directory(self, resource_uuid, directory_uuid):
        directory = self.select(
            tables.Directory,
            tables.Directory.uuid == directory_uuid
        ).first()
        if directory is None:
            return False
        resource = self.get_resource(resource_uuid)
        if resource is None:
            return False
        resource.directories.append(directory)
        return True

    def remove_directory(self, resource_uuid, directory_uuid):
        directory = self.select(
            tables.Directory,
            tables.Directory.uuid == directory_uuid
        ).first()
        if directory is None:
            return False
        resource = self.get_resource(resource_uuid)
        if resource is None:
            return False
        resource.directories.remove(directory)
        return True

    def add_tag(self, resource_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        resource = self.get_resource(resource_uuid)
        if resource is None:
            return False
        resource.tags.append(tag)
        return True

    def remove_tag(self, resource_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        resource = self.get_resource(resource_uuid)
        if resource is None:
            return False
        resource.tags.remove(tag)
        return True

