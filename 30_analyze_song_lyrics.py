# -*- coding: utf-8 -*-
"""
Write 3 function,
1. Create a "frequency dictionary" mapping str:int
2. find "word that occurs the most" and how many times
    i. use a list, in case there is more than one word
    ii. return a tuple (list, int) for (words_list, highest_freq)
3. find the "words that occur at least X times"
    i. let user choose "at least X times", so allow as parameter S
    ii. return a list of tuples, each tuple is a (list, int) containing the list of words ordered by their frequency
    iii. IDEA: from song dictionary, find most frequent word, delete most common word, repeat, it works because you are mutating the song dictionary

@author: ibrahim
"""
    
she_loves_you = """She loves you, yeah, yeah, yeah /n
She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah, yeah

You think you lost your love
Well, I saw her yesterday
It's you she's thinking of
And she told me what to say

She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad

She said you hurt her so
She almost lost her mind
But now she says she knows
You're not the hurting kind

She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad, ooh

She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
And with a love like that
You know you should be glad

You know it's up to you
I think it's only fair
Pride can hurt you too
Apologize to her

Because she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad, ooh

She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
With a love like that
You know you should be glad
With a love like that
You know you should be glad
With a love like that
You know you should be glad
Yeah, yeah, yeah
Yeah, yeah, yeah, yeah loves loves loves loves loves loves"
"""
## Removes all unnecessary commas
##she_loves_you = she_loves_you.replace(",", "")
# converts that string into a list with each word as element
she_loves_you = she_loves_you.split(" ")


## Creating a dictionary
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    


beatles = lyrics_to_frequencies(she_loves_you)


# using the dictionary to find the most commomn word
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if(freqs[k] == best):
            words.append(k)
    return(words, best)
    

(w, b) = most_common_words(beatles)
# w = ['loves', 'yeah,']
# b = 18





# leveraging dictionary properties
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if(temp[1] >= minTimes):
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result
    

print(words_often(beatles, 5))
    