#Finding Anagrams in two words or sentences

def finding_anagram(word, anagram) :

    #converting the inputs to lowercase letters

    word = word.lower()
    anagram = anagram.lower()

    #Removing the whitespaces

    word = word.replace(" ","")
    anagram = anagram.replace(" ","")

    #Sorting out the contents of the containers

    return (print("Calling find_anagram with",word + " & "+anagram)), print(sorted(word) == sorted(anagram))

finding_anagram(str(input("Enter First Word : ")),str(input("Enter Second Word : ")))
