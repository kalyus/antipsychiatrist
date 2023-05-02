from lark import Lark, exceptions

grammar = """
start: complaint+              

// Allow optional punctuation after each word
complaint: "The patient feels" condition
   | "The patient feels" condition "and" complaint
   | condition complaint
   | "and" condition
   | "the patient feels" condition "and" complaint
   | "the patient feels" condition
  

condition: negative | negatepositive | dependent | negative "and" condition



subjectiveclause: "painful" | "horrible" //Add List of words


negative: negativeverb
| negativeverb "since" time
| negativeverb "that is" subjectiveclause


negatepositive: "not" positiveverb | positiveverb //Redundant, but optional




negativeverb: "sad" | "angry" | "bad" | "worried" //Add More


positiveverb: "happy" | "excited" | "good" | "smart" //Add more


dependent: "addicted to" noun | "obsessed with" noun | "confused by" noun


//Add FEARS/PHOBIAS

noun: "gambling" //use common.word


time: "yesterday" | "last" weekday
weekday: "monday" | "tuesday" | "wednesday" | "thursday" | "friday" |"saturday" | "sunday"




%import common.WS
%ignore WS

"""

#parser = Lark(grammar)

#program = "The patient feels sad"

#parse_tree = parser.parse(program)
def diagnose(text):
    try:
        parser = Lark(grammar)
        tree = parser.parse(text)
        #print (str(tree))

        if "condition" in str(tree):

            parseWords = text.split()
            if "sad" in parseWords:
                return "You have depression"
            return "Valid condition start parsing"
        

            #return "You have depression."
        else:
            return "You have some unknown conditions."
    except exceptions.LarkError:
        return "Invalid input, we only want doctor speak here. \nOr maybe you just misspelled something which in that case I diagnose you with Dysgraphia"

text2 = input("How is the patient feeling? \n")
text = "The patient feels sad"
print(diagnose(text2)) # Output: You have depression.