import re
import sys


last_word, last_doc, last_tf, running_sum = None, None, None, 0
result = list()
temp = dict()

for line in sys.stdin:
    line = line.replace('\n', '')
    word, value = line.split('\t')
    doc_no, tf, num = value.split(';')

    if last_word and last_doc and last_word != word and last_doc != doc_no:
        result.append((last_word + '#' + last_doc, last_tf, str(running_sum)))
        (last_word, last_doc, last_tf, running_sum) = (word, doc_no, tf, 1)
    elif last_word and last_doc and last_word == word and last_doc != doc_no:
        result.append((last_word + '#' + last_doc, last_tf, str(running_sum)))
        (last_word, last_doc, last_tf, running_sum) = (word, doc_no, tf, 1)
    elif last_word and last_doc and last_word != word and last_doc == doc_no:
        result.append((last_word + '#' + last_doc, last_tf, str(running_sum)))
        (last_word, last_doc, last_tf, running_sum) = (word, doc_no, tf, 1)
    else:
        (last_word, last_doc, last_tf, running_sum) = (word, doc_no, tf, running_sum + 1)

result.append((last_word + '#' + last_doc, last_tf, str(running_sum)))

for elem in result:
    word = re.search(r'\w+', elem[0]).group(0)
    if temp.get(word):
        temp.update({word: temp.get(word) + 1})
    else:
        temp.update({word: 1})

for elem in result:
    word = re.search(r'\w+', elem[0]).group(0)
    print(elem[0], elem[1], temp.get(word), sep='\t')
