# from .queue import Queue
from .file_management import txt_importer
import sys


def process(path_file, instance):

    if path_file not in instance.data:
        instance.enqueue(path_file)
    file_txt = txt_importer(path_file)
    len_file = len(file_txt)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len_file,
        'linhas_do_arquivo': file_txt
    }
    return sys.stdout.write(str(data))


def remove(instance):
    if not len(instance.data):
        return sys.stdout.write('Não há elementos\n')

    sys.stdout.write(f"Arquivo {instance.data[0]} removido com sucesso\n")
    instance.dequeue()


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        result = process(path_file, instance)
        return sys.stderr.write(str(result))
    except IndexError:
        sys.stderr.write('Posição inválida')

