from ting_file_management.queue import Queue
import re


def exists_word(word: str, instance: Queue):
    search_result = []
    for index in range(len(instance)):
        file_info = instance.search(index)
        file_search_result = {
            'palavra': word,
            'arquivo': file_info['nome_do_arquivo'],
            'ocorrencias': [],
        }
        for line, string in enumerate(file_info['linhas_do_arquivo']):
            if word.casefold() in string.casefold():
                file_search_result['ocorrencias'].append({
                    'linha': line + 1,
                })
        
        if len(file_search_result['ocorrencias']) > 0:
            search_result.append(file_search_result)

    return search_result


def search_by_word(word: str, instance: Queue):
    """search"""
