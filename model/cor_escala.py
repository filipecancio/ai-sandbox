from enum import Enum

class CorEscala(Enum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
        
    def apresentar(self):
        print(self.value + " boa tarde"+'\033[0;0m')