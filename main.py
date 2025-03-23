from calculator import Calculator
from file_handler import FileHandler

def main():
    # Calculator demo
    calc = Calculator()
    print('Calculator Demo:')
    print(f'Addition: 5 + 3 = {calc.add(5, 3)}')
    print(f'Multiplication: 4 x 6 = {calc.multiply(4, 6)}')
    
    # File handling demo
    file_handler = FileHandler()
    file_handler.write_data('Hello, World!')
    data = file_handler.read_data()
    print(f'\nFile Content: {data}')

if __name__ == '__main__':
    main()