from services.base_command import BaseCommand


class CommandNotFound(BaseCommand):

    def get_result(self):
        return None

    def set_metadata(self, metadata):
        return None
