from enum import Enum
import colored

class CorEscala(Enum):
    RED = colored.foreground('red')
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    BLACK = '\033[40m'
    GREY = '\033[47m'
        
    def apresentar(self,text):
        print(self.value + text +'\033[0;0m')
        
    def apresentar2(self,text):
        print(self.value, text)