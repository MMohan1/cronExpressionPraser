from abc import ABC, abstractmethod
from typing import Dict, Union, List

class BaseFormatter(ABC):
    @abstractmethod
    def format(self, parsed_cron: Dict[str, Union[List[int], str]]) -> str:
        pass
