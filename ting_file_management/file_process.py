# from .queue import Queue
from .file_management import txt_importer
import sys

def process(path_file, instance):

    if path_file not in instance.data:
        file_txt = txt_importer(path_file)
        len_file = len(file_txt)
        instance.enqueue(path_file)
        data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len_file,
            'linhas_do_arquivo': file_txt
        }
        return sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
