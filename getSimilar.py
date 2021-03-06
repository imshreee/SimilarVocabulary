#!/usr/bin/env python
import spacy

def family_check(word1,word2):
    if len(word1) < len(word2):
        return word2.find(word1)
    else:
        return word1.find(word2)

if __name__ == '__main__':
    words = ""
    f = open('20k.txt')
    line = f.read() 
    while True:
        if line != "":
            words += line.replace("\n"," ")
            line = f.read()
        else:
            break

    nlp = spacy.load('en_core_web_lg')
    print("modal loaded.")
    tokens = nlp(words)


    threshold = 0.0
    while threshold <= 0.0:
        try:
            threshold = float(input("input threshold value:"))
        except:
            threshold = 0.0

    length = 3
    try:
        length = int(input("input result length:"))
    except:
        length = 3

    while True:
        queue = [] #[['dog',0.1],['cat',0.2]...]
        i = input("input your word:")
        if i != "":
            txt = nlp(i)
            for token in tokens:
                score = token.similarity(txt)
                if score >= threshold and family_check(txt.text.strip(),token.text.strip()) < 0:
                    if len(queue) >= length:
                        index = 0 # in order to contrast 
                        value = 1.0
                        for i in range(0,len(queue)):
                            if queue[i][1] < value:
                                value = queue[i][1]
                                index = i
                        if value < score:
                            queue[index] = [token.text,score]

                    else:
                        queue.append([token.text,score])

        print(queue)

