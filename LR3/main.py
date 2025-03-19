grammar = {
    'S': {
        'b': ['A', 'A', 'B', 'C']
    },
    'A': {
        'b': ['b', "A'"]
    },
    "A'": {
        'a': ["a", "A'"],
        'b': ["b", "A'"],
        'c': ["c", "a", "A'"],
        'd': ["d"],
    },
    'B': {
        'b': ['b', 'X']
    },
    'X': {
        'a': ['a', 'A'],
        'b': ['B'],
        'c': ['c', 'C'],
        'd': ['d', 'd']
    },
    'C': {
        'a': ['a', 'a'],
        'b': ['b', 'b'],
        'c': ['c', 'c']
    }
}

def parse(input_tokens):
    input_tokens.append('$')
    stack = ['$', 'S']
    index = 0

    while stack:
        top = stack.pop()
        current = input_tokens[index]
        if top == current == '$':
            print("Разбор завершён успешно!")
            return True
        # Если верх стека – терминал
        if top in ['a','b','c','d','$']:
            if top == current:
                index += 1
            else:
                print(f"Ошибка на позиции {index + 1}: ожидалось '{top}', а найдено '{current}'")
                return False
        else:
            # Нетерминал – ищем правило по таблице
            production = grammar.get(top, {}).get(current)
            if not production:
                print(f"Ошибка на позиции {index + 1}: нет правила для '{top}' при токене '{current}'")
                return False
            if production != ['ε']:
                # Правило записано как список символов – добавляем их в стек в обратном порядке
                for symbol in reversed(production):
                    stack.append(symbol)
    return False


tokens = list('bdbdbddcc')
parse(tokens) # правильно
tokens = list('adbabddacc')
parse(tokens) # неправильно
tokens = list('bddbadbad')
parse(tokens) # неправильно
tokens = list('bbabcadbdbbddaa')
parse(tokens) # правильно
