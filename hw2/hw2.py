# Robert Massaroni
# Cite any sources you used to help with the homework 
# including TAs and classmates

def exchange(str):
    """
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """
    if len(str) == 1:
        return str
    s = str[-1] + str[1:-1] + str[0]
    return str[-1] + str[1:-1] + str[0]


def remove_range(alist, min, max):
    """
    Use comprehension to write a method named removeRange that accepts a list of
    integers and two integer values min and max as parameters and removes all elements
    values in the range min through max (inclusive).
    For example, if a alist named list stores
    [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], the call of remove_range(alist, 5, 7);
    should change the list to store [9, 4, 2, 3, 1, 8].

   *** Important: your code must use comprehensions and should not be more than
   two lines of code including the return statement ***
    """
    newlist = [n for n in alist if n < min or n > max]
    return newlist


def word_count_in_set(words):
    """
    Write a function named wordCount that accepts a list of strings as a parameter and
    returns a count of the number of unique words in the list. Do not worry about
    capitalization and punctuation; for example, "Hello" and "hello" and "hello!!" are
    different words for this problem.
    *** Solution should not be more than 3 lines of code (can be less)
     including the return statement ***
    """
    newlist = [words[x] for x in range(len(words)) if words[x] not in words[0:x]]
    return len(newlist)



def topping1(dictionary):
    """
    Given a dictionary of food keys and topping values, modify and return the dictionary
    as follows:
    if the key "ice cream" is present, set its value to "cherry".
    In all cases, set the key "bread" to have the value "butter".
    Examples:
    topping1({"ice cream": "peanuts"}) returns {"bread": "butter", "ice cream": "cherry"}
    topping1({})  {"bread": "butter"} returns {"bread": "butter"}
    topping1({"pancake": "syrup"}) returns {"bread": "butter", "pancake": "syrup"}
    """
    dictionary.update({"bread":"butter"})
    for k in dictionary.keys():
        if k == "ice cream":
            dictionary.update({"ice cream":"cherry"})
    return dictionary


def word_count(strings):
    """
    The classic word-count algorithm: given an array of strings, return a dictionary with
    a key for each different string, with the value the number of times that string appears in the
    list.
    Examples:
    word_count(["a", "b", "a", "c", "b"]) returns {"a": 2, "b": 2, "c": 1}
    word_count(["c", "b", "a"]) returns {"a": 1, "b": 1, "c": 1}
    word_count(["c", "c", "c", "c"]) returns {"c": 4}
    *** Important: your code must use comprehensions and should not be more than two
    lines of code including the return statement ***
    """
    d = dict()
    for s in strings:
        if s not in d:
            d.update({s:1})
        else:
            d.update({s:d.get(s) + 1})
    return d



def friend_list(friend_dictionary):
    """
    Write a method named friendList that accepts a dictionary as a parameter and reads
    friend relationships and stores them into a new dictionary that is returned.
    You should create a new dictionary where each key is a person's name from the original
    simple dictionary, and the value associated with that key is a list of all friends of
    that person. Friendships are bi-directional:
    if Marty is friends with Danielle, Danielle is friends with Marty.

    The dictionary parameter contains one friend relationship per key/value pair,
    consisting of two names. If the dictionary parameter,friendMap looks like this:
    Marty: Cynthia
    Danielle: Marty
    Then the call of friendList(friendMap) should return a dictionary with the following
    contents:
    {Cynthia:[Marty], Danielle:[Marty], Marty:[Cynthia, Danielle]}
    """
    d = dict()
    for k in friend_dictionary.keys():
        v = friend_dictionary.get(k)
        if k in d.keys():
            if v not in d.get(k):
                #
                d[k].append(v)
                #d.update({k:d.get(k).append(v)})
        if k not in d.keys():
            #
            list = [v]
            d[k] = list
            #d(k).append(v)
            #d.update({k:{}})
            #d.update({k:d.get(k).append(v)})
        if v not in d.keys():
            # 
            #d.update({v:{}})
            #d.update({v:d.get(v).append(k)})
            list = [k]
            d[v] = list
            #d(v).append(k)
        if v in d.keys():
            if k not in d.get(v):
                # 
                #d.update({v:d.get(v).append(k)})
                #d[v] = d[v].append(k)
                d[v].append(k)
    return d



# Test functions
assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert word_count(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}, 'expected {"a": 2, "b": 2, "c": 1}'
print("correct")
assert word_count(["c", "b", "a"]) == {"a": 1, "b": 1, "c": 1}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")
assert word_count(["c", "c", "c", "c"]) == {"c": 4}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# Problems found on https://codingbat.com/python
