def popular_words (text, words):
    d={}
    text1 = text.lower().split()

    for i in words:
        d[i] = text1.count(i)
    return d

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
