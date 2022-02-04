def exists_word(word, instance):
    result = []
    for data in instance.data:
        currences = []
        for lines in data['linhas_do_arquivo']:
            if not lines.count(word):
                return result
            currences.append({'linha': lines.count(word)})
        result.append({
            "palavra": word,
            "arquivo": data['nome_do_arquivo'],
            "ocorrencias": currences,
        })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
