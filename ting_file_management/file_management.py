# ref >>>
# https://www.geeksforgeeks.org/python-string-splitlines-method/
# https://www.delftstack.com/howto/python/python-print-to-stderr/
import sys

def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            return sys.stderr.write('Formato inválido\n')
        path = open(path_file)        
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    with path as file:
        return file.read().splitlines()