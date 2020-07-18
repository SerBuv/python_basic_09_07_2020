'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.'''

def int_func(word1, word2):
    word1 = word1[0].upper() + word1[1:]
    word2 = word2.upper()
    return word1, word2

print(int_func('hello', 'h e l l o'))






