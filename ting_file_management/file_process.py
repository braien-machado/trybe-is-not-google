import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    lines = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    if not instance.in_queue(file_info['nome_do_arquivo']):
        instance.enqueue(file_info)

        print(file_info)


def remove(instance: Queue):
    if len(instance) == 0:
        print('Não há elementos')
    else:
        removed_file = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {removed_file} removido com sucesso')


def file_metadata(instance: Queue, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
