import os
import logging

class TxtManager:
    def __init__(self, input_file: str, output_file: str = None):
        """
        initialize
        
        :param input_file: path of input file
        :param output_file: path of output file
        """
        self.input_file = input_file
        self.output_file = output_file if output_file else input_file
        logging.debug(f"input_file: {self.input_file}, output_file: {self.output_file}")

    def remove_blank_lines(self):
        logging.debug(f"Current working directory: {os.getcwd()}")

        
        # delete blank lines from input file and save to output file
        
        with open(self.input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.writelines(non_blank_lines)
        logging.info(f"Removed blank lines from {self.input_file} and saved to {self.output_file}.")

if __name__ == '__main__':
    txt_manager = TxtManager('server/notion_connection/input.txt')
    txt_manager.remove_blank_lines()