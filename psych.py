from lark import Lark, exceptions

grammar = """
start: "The patient feels" condition complaint*            

complaint: "The patient feels" condition
 | "The patient feels" condition "and" complaint
 | condition complaint
 | "and" condition
 | "and" complaint
 | "and feels" condition
 | "the patient feels" condition "and" complaint
 | "the patient feels" condition


//complaintconnector: "and" condition | "and complaint"
//| "and feels" condition


condition: negative | negative "and" condition


subjectiveclause: "painful" 
        | "horrible"
       | "chronic" 
       | "paralyzing"
       | "lingering" 
       | "constant"
       | "continuous" 
       | "deep" 
       | "deep rooted"
       | "recurrsing" 
       | "sustained"
       | "lifelong" 
       | "habitual" 
       | "incurable"


negative: negativeverb
| negativeverb "since" time
| negativeverb "that is" subjectiveclause


negativeverb: depressiont
| anxietyt
| adhdt
| angert
| ocdt
| schizophreniat //Add More
| phobiat


depressiont: "sad" 
    | "gloomy"
    | "bummed"
      | "unhappy" 
      | "miserable"
      | "down" 
      | "discouraged" 
      | "bad"
      | "guilt" 
      | "shame"
      | "lonely" 
      | "guilty" 
      | "bored"
      | "agony" 
      | "alienation"
      | "anguish" 
      | "apathy"
      | "aversion" 
      | "apprehension"
      | "demoralized" 
      | "terrible"
      | "horrible" 
      | "numb"
      | "hopeless" 
      | "alone"
      | "disheartened" 
      | "remorse"
      | "rejected" 
      | "revulsion"
      | "dread" 
      | "grief" 
      | "pain"
      | "hurt" 
      | "depressed"
      | "pessimism" 
      | negatedepression
      | "sick"

negatedepression: "not" depressiona

depressiona: "happy" 
        | "fulfilled" 
        | "glad" 
        | "content" 
        | "cheery"
       | "fortunate" 
       | "joyful" | "helpful" 
       | "favorable" 
       | "favored"
       | "deserving" 
       | "wanted" 
       | "loved" 
       | "interested" 
       | "excited"
       | "good"


anxietyt: "worried" 
    | "uneasy"
      |"pertubed" 
      | "troubled"
      | "concerned" 
      | "shocked"
      | "shock" 
      | "panic"
      | "distressed" 
      | "nervous" 
      | "despair"
      |"disturbed" 
      | "overwhelmed" 
      | "reluctant"
      |"anxious" 
      | "afraid" 
      | "fearful" 
      | "scared"
      | "suspicious" 
      | "hysteric" 
      | "envy"
      | "helpless" 
      | "wrong"
      | negateanxiety


negateanxiety: "not" anxietya


anxietya: "calm" 
    | "collected" 
    | "competent"
       | "bold" 
       | "brave" 
       | "capable"
       | "courageous" 
       | "unafraid"
       | "assured" 
       | "assertive" 
       | "smart" 
       | "intelligent"
       | "adequate" 
       | "efficient" 
       | "qualified" 
       | "skilled"
       | "adaptable" 
       | "proficient" 
       | "succesful"


adhdt: "restless" 
| "unfocused" 
| "aloof" | "inattentive" 
| "impulsive"
      | "dumb" 
      | "hyper" 
      | "hyperactive" 
      | "jumpy"



angert: "angry" 
| "enraged" 
| "furious"
      | "ire" 
      | "resentment"
      | "hatred" 
      | "annoyed"
      | "displeasure" 
      | "bipolar"
      | "outraged" 
      | "indignation" 
      | "antagonizing"
      | "agitated" 
      | "aggressive"
      | "spite" 
      | "smug" 
      | "stubborn"
      | "hate" 
      | "jealous" 
      | "jealousy"
      | "insulted" 
      | "irritated"
      | "loathing" 
      | "mad" 
      | "moody"
      | "pity" 
      | "possessive"


ocdt: dependent | "compulsive" | "obsessive" | "fixated"


schizophreniat: "watched" 
| "paranoid" 
| "hallucinating" 
| "stalked"
       |"hallucinating" 
       | "harassed" 
       | "harnessed"



//negatepositive: "not" positiveverb  //Redundant, but optional
//depressionnegate: negatepositive
//positiveverb: "happy" | "excited" | "good" | "smart" //Add more

dependent: "addicted to" noun | "obsessed with" noun


phobiat: "afraid of" noun | "phobic" | "scared of" noun
| "fearful of" noun | "avoidant of" noun


noun: /[^\s]+/ | "melons"


time: "yesterday" | "last" weekday
weekday: "monday" | "tuesday" | "wednesday" | "thursday" | "friday" |"saturday" | "sunday"




%import common.WORD
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
        #    print("---")
        #    print(child)

        if "condition" in str(tree): #First lets check that it is a valid parse. If not then don't bother checking everything else
            #parseWords = text.split()
            #if "sad" in parseWords:
            #    return "You have depression"

            key_findings = find_keys(tree) #I have the key diagnoses mapped to the word lists associated with it



            diagnoses = set(key_findings) #If there are multiple inputs that are associated with a diagnoses, just get rid of them.

            if len(diagnoses) == 1: #We just return one

                return f"I diagnose you with: {', '.join(diagnoses)}"
            
            elif len(diagnoses) > 1: #We want to have the second to last diagnoses have and in front of it.

                diagnoses_list = list(diagnoses)

                diagnoses_str = ", ".join(diagnoses_list[:-1])

                return f"I diagnose you with the following: {diagnoses_str} and {diagnoses_list[-1]}"
            
        
    except exceptions.LarkError:

        return "Invalid input, we only want doctor speak here. \nOr maybe you just misspelled something which in that case I diagnose you with Dysgraphia"



def find_keys(tree):

    diags = ["depressiont", "anxietyt", "angert", "adhdt", "schizophreniat", "ocdt", "phobiat"]

    conditions = []

    try:

        for child in tree.children:

            conditions += find_keys(child) #Go through the children of the tree and eventually add them to the condition list

    except AttributeError: #It occasionally has attribute errors so we can ignore as we just search for key phrases which are mapped to diagnoses

        pass

    for d in diags:

        if d in str(tree):

            conditions.append(d[:-1]) #remove the ending tag from the grammar

    return conditions #returns the list
        
text = input("How is the patient feeling? \n")

print(diagnose(text)) 
