from database.access.api import Api

from database import tables


class WorldApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_world(self, name, description):
        obj = tables.World(uuid=tables.World.create_uuid(), name=name, description=description)
        self.insert(obj)
        return obj

    def get_world(self, uuid):
        return self.select(tables.World, tables.World.uuid == uuid).first()

    def remove_world(self, uuid):
        world = self.get_world(uuid)
        if world is None:
            return False
        self.delete(world)
        return True

    def get_world_list(self):
        return self.select(tables.World)

    def remove_world_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_world(uuid):
                success = False
        return success

    def set_image(self, world_uuid, image_uuid):
        image = self.select(
            tables.Image,
            tables.Image.uuid == image_uuid
        ).first()
        if image is None:
            return False
        world = self.get_world(world_uuid)
        if world is None:
            return False
        world.image = image