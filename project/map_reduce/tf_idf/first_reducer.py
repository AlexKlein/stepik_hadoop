import sys


last_word, last_doc, running_sum = None, None, 0
key_set = set()

for line in sys.stdin:
    line = line.replace('\n', '')
    key_pair, value = line.split('\t')
    word, doc_no = key_pair.split('#')

    if last_word and last_doc and last_word != word and last_doc != doc_no:
        print(last_word, last_doc, str(running_sum), sep='\t')
        (last_word, last_doc, running_sum) = (word, doc_no, 1)
    elif last_word and last_doc and last_word == word and last_doc != doc_no:
        print(last_word, last_doc, str(running_sum), sep='\t')
        (last_word, last_doc, running_sum) = (word, doc_no, 1)
    elif last_word and last_doc and last_word != word and last_doc == doc_no:
        print(last_word, last_doc, str(running_sum), sep='\t')
        (last_word, last_doc, running_sum) = (word, doc_no, 1)
    else:
        (last_word, last_doc, running_sum) = (word, doc_no, running_sum + 1)

print(last_word, last_doc, str(running_sum), sep='\t')
