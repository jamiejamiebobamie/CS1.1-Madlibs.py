import random

#run in python3

def inputWords():
        print("I don't care what the requirements say: you're not seeing my story until I get some words, so...")

        verbs = []
        while len(verbs) < 1:
            verb = input("Give me a verb.")
            if type(verb) is str and len(verb)>0:
                verbs.append(verb)
            #I used an array of one item in case I wanted to modify the story later to include more verbs.

        nouns = []
        while len(nouns) < 1:
            noun = input("Give me a noun.")
            if type(noun) is str and len(noun)>0:
                nouns.append(noun)
        while len(nouns) < 6:
            noun = input("Give me another noun.")
            if type(noun) is str and len(noun)>0:
                nouns.append(noun)

        adjectives = []
        while len(adjectives) < 1:
            adjective = input("Please enter an adjective.")
            if type(adjective) is str and len(adjective)>0:
                adjectives.append(adjective)
        while len(adjectives) < 2:
            adjective = input("Please enter another adjective.")
            if type(adjective) is str and len(adjective)>0:
                adjectives.append(adjective)

        myWordsTuple = (nouns, verbs, adjectives)


        return(myWordsTuple)



def showStory():
        myWords = inputWords()

        randNoun1 = myWords[0][random.randint(0,5)]
        randNoun2 = myWords[0][random.randint(0,5)]
        randNoun3 = myWords[0][random.randint(0,5)]
        randNoun4 = myWords[0][random.randint(0,5)]
        randNoun5 = myWords[0][random.randint(0,5)]
        randNoun6 = myWords[0][random.randint(0,5)]

        randVerb1 = myWords[1][0]

        randAdj1 = myWords[2][random.randint(0,1)]
        randAdj2 = myWords[2][random.randint(0,1)]

        print(" ")
        print(" ")
        print("Once there was a " + randNoun1 + " that had seven " + randNoun2 + "s. They all loved to " + randVerb1 + ".")
        print("One day they " + randVerb1 + "ed too much and had to sit down. That's when the trouble started.")
        print("You see, they couldn't "+ randVerb1 +" anymore, but they also couldn't not "+ randVerb1 +". It was")
        print("a conundrum. To "+randVerb1+" or not to "+randVerb1+". They decided to ask the grand "+randNoun3+" for advice.")
        print(" ")
        print("They prepared all day for their "+randAdj1+" journey. They would have to travel through the "+randAdj2+" woods,")
        print("and over the sea of "+randNoun4+", through the swampy folds of the forgotten "+randNoun5+", and into the")
        print(randNoun6+"\'s mouth to speak to the grand, wise-one.")
        print(" ")
        print("They did just that, and just like that they were there.")
        print("Before the wise one they stood.")
        print(" ")
        print("\"Oh wise one,\" they asked in unison, having prepared their words carfeully during the long trek.")
        print("\"We want to "+randVerb1+", but we can't anymore. If we "+randVerb1+" once more we'll be no more. Our frail bodies have")
        print(randVerb1+"ed too much. What should we do? We want to "+randVerb1+"!\" ")
        print(" ")
        print("But alas! The wise one was dead. He had sat their for millenia and finally expired. Everyone thought the wise one")
        print("was immortal, but as it turned out, he wasn't. He was quite dead.")
        print(" ")
        print("Not knowing what to do the troupe decided they just couldn't not "+randVerb1+" anymore, so they did. They "+randVerb1+"ed.")
        print("And just like that their bodies snapped in twain and they were dead too. And now it was like this massive massacre of")
        print("deceased beings. And that was that.")
        print(" ")
        print("The end.")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

showStory()
