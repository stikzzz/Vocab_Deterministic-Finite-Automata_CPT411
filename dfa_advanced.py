import string

categories = {
    "Conjunction": ["and", "or", "but", "so"],
    "Determiner": ["the", "a", "an", "my", "this"],
    "Pronoun": ["i", "you", "he", "she", "we", "they"],
    "Modal": ["can", "will", "may", "must", "should"],
    "Preposition": ["in", "on", "at", "to", "from"]
}

# Auto-build our DFA transitions and accept states based on the vocabulary
# This avoids manually typing 100+ character transitions!
transitions = {}
accept_states = {} # maps an accept state to its Category

for category, words in categories.items():
    for word in words:
        current_state = 'START'
        for i, char in enumerate(word):
            # Create a unique state name for the path
            next_state = f"{current_state}-{char}" if current_state == 'START' else f"{current_state}{char}"
            
            # Map the transition
            transitions[(current_state, char)] = next_state
            
            current_state = next_state
            
            # If it's the last character, mark it as an accept state
            if i == len(word) - 1:
                accept_states[current_state] = category

print("--- Generated DFA Transition Table ---")
for (state, char), next_state in transitions.items():
    print(f"({state}, '{char}') -> {next_state}")
print("--------------------------------------\n")

def run_dfa(word):
    current_state = 'START'
    for char in word:
        if (current_state, char) in transitions:
            current_state = transitions[(current_state, char)]
        else:
            return None # Word deviated from known vocabulary
            
    # If the final state is an accept state, return the specific category
    if current_state in accept_states:
        return accept_states[current_state]
    return None

# take input
filename = "text3.txt"
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        
        words = text.split()
        
        for w in words:
            clean_word = w.strip(string.punctuation).lower()
            if not clean_word:
                continue
            
            tokens = " ".join(list(clean_word))
            print(f"Word: {clean_word}")
            print(f"Tokens: {tokens}")
            
            # Use our dictionary-based DFA
            category = run_dfa(clean_word)
            if category:
                print(f"Status: accept ({category})\n")
            else:
                print("Status: reject\n")

except FileNotFoundError:
    print("File not found.")
