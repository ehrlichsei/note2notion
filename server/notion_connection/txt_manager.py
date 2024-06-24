import os
import logging

class TxtManager:
    def __init__(self, input_file: str, output_file: str = None):
        """
        初始化 TxtCleaner 类。
        
        :param input_file: 输入的文本文件路径。
        :param output_file: 输出的文本文件路径。如果为 None，则覆盖输入文件。
        """
        self.input_file = input_file
        self.output_file = output_file if output_file else input_file
        logging.debug(f"input_file: {self.input_file}, output_file: {self.output_file}")

    def remove_blank_lines(self):
        logging.debug(f"Current working directory: {os.getcwd()}")

        """
        删除文本文件中的空行并保存结果。
        """
        with open(self.input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.writelines(non_blank_lines)
        logging.info(f"Removed blank lines from {self.input_file} and saved to {self.output_file}.")

if __name__ == '__main__':
    txt_manager = TxtManager('server/notion_connection/input.txt')
    txt_manager.remove_blank_lines()