def exists_word(word, instance):
   result = []
   for data in instance.data:
      currences = []
      for lines in  data['linhas_do_arquivo']:
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

a = 'oiiooiioio'
if a.count('z'):
   print(a.count('z'))

#  {
#   'linhas_do_arquivo': ['Aqui contem um texto que fala sobre um menino pobre '
#                         'chamado Pedro.'],
#   'nome_do_arquivo': 'statics/nome_pedro.txt',
#   'qtd_linhas': 1,
#  }

   #  {
   #      "palavra": "Pedro",
   #      "arquivo": "statics/nome_pedro.txt",
   #      "ocorrencias": [{"linha": 1}],
   #  }