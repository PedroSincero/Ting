# from .queue import Queue
from .file_management import txt_importer
import sys


def process(path_file, instance):

    for index in range(len(instance.data)):
        if path_file == instance.search(index)['nome_do_arquivo']:
            return None
    file_txt = txt_importer(path_file)
    len_file = len(file_txt)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len_file,
        'linhas_do_arquivo': file_txt
    }
    instance.enqueue(data)
    return sys.stdout.write(str(data))


def remove(instance):
    if not len(instance.data):
        return sys.stdout.write('Não há elementos\n')

    remove_file = instance.dequeue()
    sys.stdout.write(f"Arquivo {remove_file['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
    except IndexError:
        sys.stderr.write('Posição inválida')
    else:
        sys.stdout.write(str(path_file))

# Agradecimentos a Alessandra Rezende - Turma 10 - Tribo B 
# Pelo Auxilio na Refatoração do Codigo ^^