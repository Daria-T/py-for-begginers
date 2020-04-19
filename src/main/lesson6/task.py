class Person:
    NAME_QUERY_KEYWORDS = ['имя', 'зовут']
    FAMILY_QUERY_KEYWORDS = ['фамилия']
    AGE_QUERY_KEYWORDS = ['возраст', 'старше', 'младше']
    ADDRESS_QUERY_KEYWORDS = ['живет на', 'дом', 'квартира']
    SALARY_QUERY_KEYWORDS = ['зарплата', 'зарабатывает более', 'зарабатывает менее']
    EXPERIENCE_QUERY_KEYWORDS = ['опыт работы', 'работает более', 'работает менее']

    def __init__(self, name, family, age, address, experience, salary):
        self.name = name
        self.family = family
        self.age = age
        self.address = address
        self.experience = experience
        self.salary = salary
        self.key = (self.name, self.address)

    def __repr__(self):
        return "Person('%s', '%s', '%s', '%s')" % (self.name, self.family, self.age, self.address)

    def __eq__(self, other):
        # Не знаю как в питоне, но обычно реализация оператора ==
        # подразумевает сопоставление с объектом того же класса.
        # Иначе это очень запутывает.
        is_equal = type(other) == Person
        is_equal = is_equal and self.name == other.name
        is_equal = is_equal and self.family == other.family
        is_equal = is_equal and self.age == other.age
        is_equal = is_equal and self.address == other.address
        is_equal = is_equal and self.experience == other.experience
        is_equal = is_equal and self.salary == other.salary
        return is_equal

    def __extract_keyword(self, query, keywords):
        res = [ele for ele in keywords if (ele in query)]
        if res and len(res) == 1:
            return res[0]
        else:
            return None

    def __extract_value(self, keyword, query):
        return query.replace(keyword + ' ', '')

    def __fuzzy_comapre(self, lhs_str, rhs_str, threshold):
        ngrams = [
            lhs_str[i: i + 3] for i in range(len(lhs_str))
        ]
        count = 0
        for ngram in ngrams:
            count += rhs_str.count(ngram)
        return count / max(len(lhs_str), len(rhs_str)) > threshold

    def __match_name(self, keyword, name):
        return self.__fuzzy_comapre(self.name, name, 0.89)

    def __match_family(self, keyword, family):
        return self.__fuzzy_comapre(self.family, family, 0.19)

    def __match_age(self, keyword, age):
        if keyword == 'возраст':
            return self.age == age
        if keyword == 'старше':
            return self.age > age
        if keyword == 'младше':
            return self.age < age
        return False

    def __match_address(self, keyword, address):
        return self.__fuzzy_comapre(self.address, address, 0.29)

    def __match_salary(self, keyword, salary):
        if keyword == 'зарплата':
            return self.salary == salary
        if keyword == 'зарабатывает более':
            return self.salary > salary
        if keyword == 'зарабатывает менее':
            return self.salary < salary
        return False

    def __match_experience(self, keyword, experience):
        if keyword == 'опыт работы':
            return self.experience == experience
        if keyword == 'работает более':
            return self.experience > experience
        if keyword == 'работает менее':
            return self.experience < experience
        return False

    def match_query(self, query):
        value = None
        keyword = self.__extract_keyword(query, self.NAME_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)
            return self.__match_name(keyword, value)

        keyword = self.__extract_keyword(query, self.FAMILY_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)

            return self.__match_family(keyword, value)

        keyword = self.__extract_keyword(query, self.AGE_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)
            return self.__match_age(keyword, int(value))

        keyword = self.__extract_keyword(query, self.ADDRESS_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)
            return self.__match_address(keyword, value)

        keyword = self.__extract_keyword(query, self.SALARY_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)
            return self.__match_salary(keyword, int(value))

        keyword = self.__extract_keyword(query, self.EXPERIENCE_QUERY_KEYWORDS)
        if keyword:
            value = self.__extract_value(keyword, query)
            return self.__match_experience(keyword, int(value))

        return False


lena = Person('Лена', 'Кривцова', 19, 'Пушкина, 14, 115', 5, 3400)
oleg = Person('Олег', 'Бахтин', 30, 'Ленского, 10, 11', 3, 2700)
olga = Person('Ольга', 'Онегина', 28, 'Онегина, 1, 9', 7, 4563)
nata = Person('Наташа', 'Полыгалова', 17, 'Ростова, 23, 56', 2, 1367)


people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata
}


# Синтаксис запросов:
# 1. Запрос на имя. Ключевые слова: имя, зовут
# 2. Запрос на фамилию. Ключевые слова: фамилия
# 3. Запрос на возраст. Ключевые слова: возраст, старше, младше
# 4. Запрос на уровен зарплаты. Ключевые слова: зарплата, зарабатывает более, зарабатывает менее
# 5. Запрос на опыт. Ключевые слова: работает, работает более, работает менее
# 6. Запрос на адресс. Ключевые слова: живет на, дом, квартира
queries = [
    'имя Ольга',
    'возраст 30',
    'старше 20',
    'младше 20',
    'живет на Пушкина',
    'Ленского дом 10',
    'живет на Ростова',
    'зовут наташа',
    'зарабатывает более 4000',
    'работает менее 3',
    'фамилия ова',
]


for q in queries:
    print('\n\nИщем людей по запросу: ' + q)
    print('Результат поиска:')
    result = []
    for key, person in people.items():
        if person.match_query(q):
            result.append(person)

    if len(result) > 0:
        for item in result:
            print(item)
    else:
        print('Людей, удовлетворяющих запросу не найдено.')

