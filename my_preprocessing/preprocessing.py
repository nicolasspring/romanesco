#!/usr/bin/python

import os
import nltk
from dehyphenate import join_lines
from dehyphenate import join_pages


def main():
    inpath = '../my_dataset/war_and_peace.txt'
    outpath = '../my_dataset/war_and_peace.preprocessed'
    tempfile = '../my_dataset/war_and_peace.temp'

    # Getting rid of OCR line breaks
    with open(tempfile, mode='w') as tempout:
        join_pages([inpath], tempout)

    # Tokenizing with one sentence per line
    with open(tempfile, mode='r',) as tempin, open(outpath, mode='w') as outfile:
        my_sents = (nltk.sent_tokenize(line) for line in tempin)
        for sentslist in my_sents:
            if sentslist == ['\n'] or sentslist == []:
                outfile.write('\n')
            else:
                for sent in sentslist:
                    tokenized = nltk.word_tokenize(sent)
                    outfile.write(' '.join(tokenized)+'\n')
    os.remove(tempfile)


if __name__ == '__main__':
    main()