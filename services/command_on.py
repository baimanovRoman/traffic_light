from services.base_command import BaseCommand


class CommandOn(BaseCommand):

    def get_result(self):
        return f"Command on metadata {self.metadata}"

    def set_metadata(self, metadata):
        self.metadata = metadata
