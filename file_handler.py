class FileHandler:
    def __init__(self, filename: str = 'data.txt'):
        self.filename = filename
    
    def write_data(self, data: str) -> None:
        with open(self.filename, 'w') as f:
            f.write(data)
    
    def read_data(self) -> str:
        try:
            with open(self.filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return 'No data found'