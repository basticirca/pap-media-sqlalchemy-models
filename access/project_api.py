from database.access.api import Api

from database import tables


class ProjectApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_project(self, name, description, json):
        obj = tables.Project(uuid=tables.Project.create_uuid(), name=name, description=description, json=json)
        self.insert(obj)
        return obj

    def get_project(self, uuid):
        return self.select(tables.Project, tables.Project.uuid == uuid).first()

    def remove_project(self, uuid):
        project = self.get_project(uuid)
        if project is None:
            return False
        self.delete(project)
        return True

    def get_project_list(self):
        return self.select(tables.Project)

    def remove_project_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_project(uuid):
                success = False
        return success

    def add_tag(self, project_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        project = self.get_project(project_uuid)
        if project is None:
            return False
        project.tags.append(tag)
        return True

    def remove_tag(self, project_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        project = self.get_project(project_uuid)
        if project is None:
            return False
        project.tags.remove(tag)
        return True

