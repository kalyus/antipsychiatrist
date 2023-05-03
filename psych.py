from lark import Lark, exceptions

grammar = """
start: complaint+             

// Allow optional punctuation after each word
complaint: "The patient feels" condition
  | "The patient feels" condition "and" complaint
  | condition complaint
  | condition
  | "the patient feels" condition "and" complaint
  | "the patient feels" condition




condition: negative | negatepositive | negative "and" condition



subjectiveclause: "painful" | "horrible" //Add List of words

negative: negativeverb
| negativeverb "since" time
| negativeverb "that is" subjectiveclause



negativeverb: depressiont | anxietyt| adhdt | angert | ocdt | schizophreniat //Add More


depressiont: "sad" | "gloomy" | "unhappy" | "miserable"
       | "down" | "discouraged" | "bad" | "guilt" | "shame"
       | "lonely" | "guilty" | "bored" | "agony" | "alienation"
       | "anguish" | "apathy" | "aversion" | "apprehension"
       | "demoralized" | "terrible" | "horrible" | "numb"
       | "hopeless" | "alone" | "disheartened" | "remorse"
       | "rejected" | "revulsion" | "dread" | "grief"
       | "hurt" | "depressed" | "pessimism"


anxietyt: "worried" | "uneasy" |"pertubed" | "troubled"
       | "concerned" | "shocked" | "shock" | "panic"
       | "distressed" | "nervous" | "despair"
       |"disturbed" | "overwhelmed" | "reluctant"
       |"anxious" | "afraid" | "fearful" | "scared"
       | "suspicious" | "hysteric" | "envy"


adhdt: "restless" | "unfocused" | "aloof" | "inattentive" | "impulsive"
       | "dumb" | "hyper" | "hyperactive" | "jumpy"


angert: "angry" | "enraged" | "furious" | "ire" | "resentment"
       | "hatred" | "annoyed" | "displeasure" | "bipolar"
       | "outraged" | "indignation" | "antagonizing"
       | "agitated" | "aggressive" | "spite" | "smug" | "stubborn"
       | "hate" | "jealous" | "jealousy" | "insulted" | "irritated"
       | "loathing" | "mad" | "moody"


ocdt: dependent | "compulsive"

schizophreniat: "watched" | "paranoid" | "hallucinating" | "stalked" 


negatepositive: "not" positiveverb  //Redundant, but optional
depressionnegate: negatepositive
positiveverb: "happy" | "excited" | "good" | "smart" //Add more


dependent: "addicted to" noun | "obsessed with" noun


//Add FEARS/PHOBIAS

noun: "words" | "soap"


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
        #print(str(tree))
        #key_phrases = find_key_phrases(tree)
        #print("Key phrases:", key_phrases)

        #for child in tree.children:
        #    print(child)

        if "condition" in str(tree):
            #parseWords = text.split()
            #if "sad" in parseWords:
            #    return "You have depression"

            key_findings = find_keys(tree)


            #return f"I diagnose you with the following: {' '.join(set(key_findings))}"

            diagnoses = set(key_findings)
            if len(diagnoses) == 1:
                return f"I diagnose you with: {', '.join(diagnoses)}"
            elif len(diagnoses) > 1:
                diagnoses_list = list(diagnoses)
                diagnoses_str = ", ".join(diagnoses_list[:-1])
                return f"I diagnose you with the following: {diagnoses_str} and {diagnoses_list[-1]}"
        else:
            return "You have some unknown conditions."
    except exceptions.LarkError:
        return "Invalid input, we only want doctor speak here. \nOr maybe you just misspelled something which in that case I diagnose you with Dysgraphia"


#Recursive approach
def find_keys(tree):
    diags = ["depressiont", "anxietyt", "angert", "adhdt", "schizophreniat", "ocdt"]
    conditions = []

    if len(tree.children) > 0:
        for child in tree.children:
            conditions += find_keys(child)

    for d in diags:
        if d in str(tree):
            conditions.append(d[:-1])

    return conditions

#Iterative approach
'''   
def find_keys(tree):
    diags = ["depressiont", "anxietyt", "angert", "adhdt", "schizophreniat", "ocdt"]
    conditions = []

    for child in tree.children:
        for d in diags:
            child_list = str(child)
            if d in child_list:
                conditions.append(d[:-1])

        #conditions += find_keys(child)

    return conditions
'''

        
text2 = input("How is the patient feeling? \n")

print(diagnose(text2)) # Output: You have depression.
