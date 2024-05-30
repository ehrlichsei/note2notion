class TxtLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = self.load_txt_file()

    def load_txt_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    
    def test_loading(self):
        if self.lines:
            print('loading txt successfully')
        else:
            print('loading txt failed')
    
    def get_lines(self):
        return self.lines
    
    def print_lines(self):
        for line in self.lines:
            print(line)

    def remove_newline(self, strings):
        return [s.strip() for s in strings]
    
    def process_lines(self):
        lines = self.remove_newline(self.lines)
        self.lines = lines

    
if __name__ == '__main__':
    file_path = 'demo.txt'
    loader = TxtLoader(file_path)
    loader.test_loading()
    print(loader.get_lines())

    loader.process_lines()
    print(loader.get_lines())