from abc import ABC, abstractmethod
from typing import Dict

class FieldParser(ABC):

    def __init__(self):
        self.expanders = self.initialize_expanders()
  

    @abstractmethod
    def initialize_expanders(self) -> Dict[str, object]:
        pass

    @abstractmethod
    def parse(self, field: str) -> list:
        pass

    def is_valid_range(self, value_range, valid_range) -> Dict[str, object]:
        if value_range[0] < valid_range[0] and value_range[-1] > valid_range[-1]:
            return False
        return True
