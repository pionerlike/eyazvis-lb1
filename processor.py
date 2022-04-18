import nltk
import numpy as np


class Phrases:
    def __init__(self, text):
        self.text = text
        self.phrases = np.array([])
        self.word_list = np.array([])
        self.list_of_phrases = np.array([[]])
        self.stemmer = nltk.stem.PorterStemmer()
        self.grammar = r"""Chunk: {<DT.?>*<JJ.?>+<NN>+}"""

        self.__make_chunk()
        self.phrases = np.unique(self.phrases)
        self.phrases = np.sort(self.phrases)

        self.__make_word_list()
        self.word_list = np.unique(self.word_list)
        self.word_list = np.sort(self.word_list)

        self.__make_list_of_phrases()
        self.list_of_phrases = np.reshape(self.list_of_phrases, (-1, 2))

    def __make_chunk(self):
        tokenizer = nltk.tokenize.PunktSentenceTokenizer()
        tokenized = tokenizer.tokenize(self.text)

        for element in tokenized:
            words = nltk.word_tokenize(element)
            tagged = nltk.pos_tag(words)
            chunkParser = nltk.RegexpParser(self.grammar)
            chunked = chunkParser.parse(tagged)

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                text = ""
                for i in range(len(subtree.leaves())):
                    text += subtree.leaves()[i][0] + " "
                self.phrases = np.append(
                    self.phrases,
                    [text]
                )

    def __make_word_list(self):
        for element in self.phrases:
            phrase = element.split(" ")
            phrase.pop()
            for word in phrase:
                word = self.stemmer.stem(word)
                self.word_list = np.append(
                    self.word_list,
                    word
                )

    def __make_list_of_phrases(self):
        for word in self.word_list:
            array = np.array([])
            array = np.append(array, word)
            string = ""
            for phrase in self.phrases:
                words = phrase.split(" ")
                words.pop()
                for element in words:
                    stemmed_word = self.stemmer.stem(element)
                    if word == stemmed_word:
                        string = string + str(phrase[:-1]) + ", "
            array = np.append(array, string)
            self.list_of_phrases = np.append(self.list_of_phrases, array)

    def find(self, symbols):
        if symbols:
            symbols = self.stemmer.stem(str(symbols))
            string = ""
            for word in self.list_of_phrases:
                if symbols in word[0]:
                    string = string + word[0] + ": " + word[1][0:-2] + "\n"
            if string != "":
                return string
            else:
                return str("Данное слово не найдено")
        else:
            string = ""
            for element in self.list_of_phrases:
                string = string + element[0] + ": " + element[1][0:-2] + "\n"
            return string

