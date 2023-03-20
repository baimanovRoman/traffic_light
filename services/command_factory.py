from services.command_off import CommandOff
from services.command_not_found import CommandNotFound
from services.command_on import CommandOn

class CommandFactory:

    def __init__(self):
        self.command_map = {
            'off': CommandOff,
            'on': CommandOn,
            'not_found': CommandNotFound
        }

    def create_command(self, command):
        return self.command_map.get(command)() if self.command_map.get(command, False) \
            else self.command_map.get('not_found')()
