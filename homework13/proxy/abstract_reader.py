from abc import ABC, abstractmethod


class Reader(ABC):
    """
    Abstract reader from lesson.
    """

    @abstractmethod
    def read_file(self):
        pass
