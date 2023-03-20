from services.base_command import BaseCommand


class CommandOff(BaseCommand):

    def get_result(self):
        return f"Command off metadata {self.metadata}"

    def set_metadata(self, metadata):
        self.metadata = metadata
