from abc import ABC, abstractmethod


class BaseCommand(ABC):

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def set_metadata(self, metadata):
        pass
