# Функция нечеткого сравнения строк
def compare(lhs_str, rhs_str):
    ngrams = [
        lhs_str[i: i + 3] for i in range(len(lhs_str))
    ]
    count = 0
    for ngram in ngrams:
        count += rhs_str.count(ngram)
    return count / max(len(lhs_str), len(rhs_str))


# Функция ключи элемнов словоря, значения по которым удовлетворяют поисковому запросу с заданной степенью совпадения.
# dictionary - словарь
# search_query - поисковая строка
# match_threshold - минимальный порог совпадения
def search_dict(dictionary, search_query, match_threshold=0.25):
    search_result = [];
    for key, value in dictionary.items():
        match_share = compare(value.lower(), search_query.lower())
        if match_share > 0 and match_share >= match_threshold:
            search_result.append(key)
    return search_result


words = {
    'key1': 'Функция', 'key2': 'выводит', 'key3': 'элементы',
    'key4': 'списка', 'key5': 'удовлетворяющие', 'key6': 'поисковому',
    'key7': 'запросу', 'key8': 'заданной', 'key9': 'степенью', 'key10': 'совпадения'
}

query = 'запр'
threshold = 0.30

print('Поис элементов в списке слов:')
print(words)
print('По запросу: ' + query)

print('Результат поиска c минимальным порогом соотвествия ' + str(threshold * 100) + '%:')
print(search_dict(words, query, threshold))

threshold = 0.20
print('Результат поиска c минимальным порогом соотвествия ' + str(threshold * 100) + '%:')
print(search_dict(words, query, threshold))
