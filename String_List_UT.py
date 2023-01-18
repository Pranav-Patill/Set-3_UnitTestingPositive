import unittest
stri = "The dance, held in the school gym, ended at midnight."
def splitWords(str):
    sep_list=[]
    word_list=[]
    final_list=[]
    temp=""
    for i in range(len(str)):
        temp+=str[i]
        if str[i] in [" ",","]:
            sep_list.append(str[i])
            if temp not in [" ",","]:word_list.append(temp[:-1])
            temp=""
        elif i==len(str)-1:
            word_list.append(temp)
            temp=""
    final_list+=[word_list,sep_list]
    return(final_list)

print(splitWords(stri))

class TestsplitWords(unittest.TestCase):
    
    def setUp(self):
        self.str_test="The dance, held in the school gym, ended at midnight."

    # funtion name shoud always start with 'test'
    def test_splitWords(self):
        self.assertEqual(
            splitWords(self.str_test),
            [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ',', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ']]
            )
if (__name__ == '__main__'):
    unittest.main()