import random 

class MakeRandom:
    def __init__(self, _file_name, _size = 100, _range = 5000):
        self.file_name = _file_name
        self.size = _size
        self.range = _range

    def run(self):
        with open(self.file_name, 'a') as f:
            for _ in range(self.size):
                f.write(str(random.randint(1, self.range)) + " ")
        print(f"Made RandomInt Values. ranges :(1, {self.range} size : {self.size}")     
        
            