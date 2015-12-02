import random
from nGramModel import *


# -----------------------------------------------------------------------------
# TrigramModel class ----------------------------------------------------------
# Core functions to implement: trainModel, trainingDataHasNGram, and
# getCandidateDictionary

class TrigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  this is the TrigramModel constructor, which is done
                  for you. It allows TrigramModel to access the data
                  from the NGramModel class.
        """
        super(TrigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.

                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        text = self.prepData(text)
        for i in range(0, len(text)):
            for j in range(2, len(text[i]) - 2):
                unigram1 = text[i][j]
                unigram2 = text[i][j + 1]
                unigram3 = text[i][j + 2]
                count = 0
                # if unigram1 has not appeared in nGramCounts, we should make it to be the  key of the 1st demension
                if (self.nGramCounts).get(unigram1, 'N/A') == 'N/A':
                    self.nGramCounts[unigram1] = {}
                # if unigram2 has not appeared in nGramCounts, we should make it to be the  key of the 2nd demension
                if (self.nGramCounts[unigram1]).get(unigram2, 'N/A') == 'N/A':
                    self.nGramCounts[unigram1][unigram2] = {}
                # if unigram3 has appeared as a 3rd-dimension key, we should not count the trigram repeatedly
                if (self.nGramCounts[unigram1][unigram2]).get(unigram3, 'N/A') == 'N/A':
                    for k in range(i, len(text)):
                        # find the indexes of all unigram1 in text[k]
                        indexOfUnigram1 = []
                        for index,token in enumerate(text[k]):
                            if token == unigram1:
                                indexOfUnigram1.extend([index])
                        # count how many times this trigram appears when unigram1 exists in text[k]
                        if indexOfUnigram1 != []:
                             for index in indexOfUnigram1:
                                 if (text[k][index + 1] == unigram2 and text[k][index + 2] == unigram3):
                                     count += 1
                # update nGramCounts with trigram pair
                if count != 0:
                    self.nGramCounts[unigram1][unigram2][unigram3] = count

        return

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined fro the TrigramModel, see the spec.
        """
        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  TrigramModel sees as candidates, see the spec.
        """
        return {}


# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence = [ 'the', 'quick', 'brown' ]
    trigramModel = TrigramModel()
    # add your own testing code here if you like


