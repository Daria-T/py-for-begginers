# Функция нечеткого сравнения строк
def compare(lhs_str, rhs_str):
    ngrams = [
        lhs_str[i: i + 3] for i in range(len(lhs_str))
    ]
    count = 0
    for ngram in ngrams:
        count += rhs_str.count(ngram)
    return count / max(len(lhs_str), len(rhs_str))


# Функция выводит элементы списка, удовлетворяющие поисковому запросу с заданной степенью совпадения.
# items - набор строк
# search_query - поисковая строка
# match_threshold - минимальный порог совпадения
def search_list(items, search_query, match_threshold=0.25):
    search_result = [];
    for item in items:
        match_share = compare(item.lower(), search_query.lower())
        if match_share > 0 and match_share >= match_threshold:
            search_result.append(item)
    return search_result


words = ['Функция', 'выводит', 'элементы', 'списка',
         'удовлетворяющие', 'поисковому', 'запросу',
         'заданной', 'степенью', 'совпадения'
         ]

query = 'запр'
threshold = 0.30

print('Поис элементов в списке слов:')
print(words)
print('По запросу: ' + query)

print('Результат поиска c минимальным порогом соотвествия ' + str(threshold * 100) + '%:')
print(search_list(words, query, threshold))

threshold = 0.20
print('Результат поиска c минимальным порогом соотвествия ' + str(threshold * 100) + '%:')
print(search_list(words, query, threshold))
