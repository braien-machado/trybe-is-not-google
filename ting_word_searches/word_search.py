from ting_file_management.queue import Queue


def get_occurrences(word: str, array, with_content: bool):
    result = []
    for i, string in enumerate(array):
        if word.casefold() in string.casefold() and with_content:
            result.append({
                'linha': i + 1,
                'conteudo': string,
            })
        elif word.casefold() in string.casefold():
            result.append({
                'linha': i + 1,
            })

    return result


def get_search_result(word: str, instance: Queue, with_content: bool):
    search_result = []
    for index in range(len(instance)):
        file_info = instance.search(index)
        file_search_result = {
            'palavra': word,
            'arquivo': file_info['nome_do_arquivo'],
            'ocorrencias': get_occurrences(
                word,
                file_info['linhas_do_arquivo'],
                with_content
            ),
        }

        if len(file_search_result['ocorrencias']) > 0:
            search_result.append(file_search_result)

    return search_result


def exists_word(word: str, instance: Queue):
    return get_search_result(word, instance, with_content=False)


def search_by_word(word: str, instance: Queue):
    return get_search_result(word, instance, with_content=True)
