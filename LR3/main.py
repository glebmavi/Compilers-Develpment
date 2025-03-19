
grammar = {
    'S': { 'b': ['A', 'A', 'B', 'C'] },
    'A': { 'b': ['b', "A'"] },
    "A'": {
         'a': ["a", "A'"],
         'b': ["A", "a", "A'"],
         'c': ['ε']
    },
    'B': { 'b': ['b', 'X'] },
    'X': {
         'a': ['C'],
         'b': ['A'],
         'c': ['C'],
         '$': ['ε']
    },
    'C': {
         'a': ['aa'],
         'b': ['bb'],
         'c': ['cc']
    }
}

def parse(input_tokens):
    input_tokens.append('$')
    stack = ['$','S']
    index = 0

    while stack:
        top = stack.pop()
        current = input_tokens[index]
        if top == current == '$':
            print("Разбор завершён успешно!")
            return True
        # Если верх стека – терминал
        if top in ['a','b','c','$']:
            if top == current:
                index += 1
            else:
                print(f"Ошибка: ожидалось '{top}', а найдено {current}")
                return False
        else:
            # Нетерминал – ищем правило по таблице
            production = grammar.get(top, {}).get(current)
            if not production:
                print(f"Ошибка: нет правила для {top} при токене {current}")
                return False
            if production != ['ε']:
                # Правило записано как список символов – добавляем в стек в обратном порядке
                for symbol in reversed(production):
                    stack.append(symbol)
    return False


tokens = ['b', 'b', 'c', 'b', 'a', 'a']
parse(tokens)
