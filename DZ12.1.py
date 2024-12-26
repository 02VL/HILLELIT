import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        file = file.read()
        file1 = list(file)
        a = 0
        c = file1.count("<")
        while a<c:
            i1 = file1.index("<")
            i2 = file1.index(">")
            file1[i1:i2 + 1] = []
            a += 1
        file2 = "".join(file1)
        print(file2)
    with codecs.open(result_file, "w", 'utf-8') as clear:
        clear.write(file2)
delete_html_tags('draft.html', 'cleaned.txt')
