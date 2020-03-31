from access.api import Api

import tables


class PresetApi(Api):
    def __init__(self, bind):
        super().__init__(bind=bind)
        
    def create_preset(self, name, description, json):
        obj = tables.Preset(uuid=tables.Preset.create_uuid(), name=name, description=description, json=json)
        self.insert(obj)
        return obj

    def get_preset(self, uuid):
        return self.select(tables.Preset, tables.Preset.uuid == uuid).first()

    def remove_preset(self, uuid):
        preset = self.get_preset(uuid)
        if preset is None:
            return False
        self.delete(preset)
        return True

    def get_preset_list(self):
        return self.select(tables.Preset)

    def remove_preset_list(self, uuids=[]):
        success = True
        for uuid in uuids:
            if not self.remove_preset(uuid):
                success = False
        return success

    def add_tag(self, preset_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        preset = self.get_preset(preset_uuid)
        if preset is None:
            return False
        preset.tags.append(tag)
        return True

    def remove_tag(self, preset_uuid, tag_uuid):
        tag = self.select(
            tables.Tag,
            tables.Tag.uuid == tag_uuid
        ).first()
        if tag is None:
            return False
        preset = self.get_preset(preset_uuid)
        if preset is None:
            return False
        preset.tags.remove(tag)
        return True

