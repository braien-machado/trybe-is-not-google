import sys

def txt_importer(path_file: str):
    try:
        if path_file.split('.')[-1] != 'txt':
            raise ValueError('Formato inválido')

        with open(path_file, "r") as file:
            return file.read().split('\n')

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
    except ValueError:
        print('Formato inválido', file=sys.stderr)