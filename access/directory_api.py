from database.access.api import Api

from database import tables


class DirectoryApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_directory(self, name):
        obj = tables.Directory(uuid=tables.Directory.create_uuid(), name=name)
        self.insert(obj)
        return obj

    def get_directory(self, uuid):
        return self.select(tables.Directory, tables.Directory.uuid == uuid).first()

    def remove_directory(self, uuid):
        directory = self.get_directory(uuid)
        if directory is None:
            return False
        self.delete(directory)
        return True

    def get_directory_list(self):
        return self.select(tables.Directory)

    def remove_directory_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_directory(uuid):
                success = False
        return success

    def add_children_directory(self, directory_uuid, children_directory_uuid):
        children_directory = self.select(
            tables.Directory,
            tables.Directory.uuid == children_directory_uuid
        ).first()
        if children_directory is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.children.append(children_directory)
        return True

    def remove_children_directory(self, directory_uuid, children_directory_uuid):
        children_directory = self.select(
            tables.Directory,
            tables.Directory.uuid == children_directory_uuid
        ).first()
        if children_directory is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.children.remove(children_directory)
        return True

    def add_resource(self, directory_uuid, resource_uuid):
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.resources.append(resource)
        return True

    def remove_resource(self, directory_uuid, resource_uuid):
        resource = self.select(
            tables.Resource,
            tables.Resource.uuid == resource_uuid
        ).first()
        if resource is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.resources.remove(resource)
        return True

    def add_parents_directory(self, directory_uuid, parents_directory_uuid):
        parents_directory = self.select(
            tables.Directory,
            tables.Directory.uuid == parents_directory_uuid
        ).first()
        if parents_directory is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.parents.append(parents_directory)
        return True

    def remove_parents_directory(self, directory_uuid, parents_directory_uuid):
        parents_directory = self.select(
            tables.Directory,
            tables.Directory.uuid == parents_directory_uuid
        ).first()
        if parents_directory is None:
            return False
        directory = self.get_directory(directory_uuid)
        if directory is None:
            return False
        directory.parents.remove(parents_directory)
        return True

