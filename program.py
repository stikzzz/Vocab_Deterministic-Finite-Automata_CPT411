DEBUG = False  # Set to True to see step-by-step DFA simulation, False to skip and show results

class State:
    def __init__(self, name, is_initial=False, is_final=False):
        self.name = name
        self.is_initial = is_initial
        self.is_final = is_final

        self.transitions = {}

    def add_transition(self, char, next_state):
        self.transitions[char] = next_state

    def process_input(self, char):
        """
        Returns the next State object if the character is accepted.
        Returns None if there is no transition for this character (Trap State).
        """
        if char in self.transitions:
            return self.transitions[char]
        return None

# --- Testing it out ---
if __name__ == "__main__":
    # 1. Create the states
    q0 = State(name="q0", is_initial=True)

    # Build a DFA that accepts "a", "at", "an", "and"
    q1 = State(name="q1", is_final=True) # accepts "a"
    q0.add_transition('a', q1)
    
    q2 = State(name="q2", is_final=True) # accepts "an"
    q1.add_transition('n', q2)
    
    q3 = State(name="q3", is_final=True) # accepts "and"
    q2.add_transition('d', q3)
    
    q4 = State(name="q4", is_final=True) # accepts "at"
    q1.add_transition('t', q4)

    # DFA that accepts "but"
    q5 = State(name="q5")
    q0.add_transition('b', q5)
    
    q6 = State(name="q6")
    q5.add_transition('u', q6)
    
    q7 = State(name="q7", is_final=True) # accepts "but"
    q6.add_transition('t', q7)

    # DFA that accepts "can"
    q8 = State(name="q8")
    q0.add_transition('c', q8)
    
    q9 = State(name="q9")
    q8.add_transition('a', q9)
    
    q10 = State(name="q10", is_final=True) # accepts "can"
    q9.add_transition('n', q10)

    # DFA that accepts "from"
    q11 = State(name="q11")
    q0.add_transition('f', q11)
    
    q12 = State(name="q12")
    q11.add_transition('r', q12)
    
    q13 = State(name="q13")
    q12.add_transition('o', q13)
    
    q14 = State(name="q14", is_final=True) # accepts "from"
    q13.add_transition('m', q14)

    # DFA that accepts "he"
    q15 = State(name="q15")
    q0.add_transition('h', q15)
    
    q16 = State(name="q16", is_final=True) # accepts "he"
    q15.add_transition('e', q16)

    # DFA that accepts "i", "in"
    q17 = State(name="q17", is_final=True) # accepts 'i'
    q0.add_transition('i', q17)
    
    q18 = State(name="q18", is_final=True) # accepts 'in'
    q17.add_transition('n', q18)

    # DFA that accepts "my", "may", "must"
    q19 = State(name="q19")
    q0.add_transition('m', q19)
    
    q20 = State(name="q20", is_final=True) # accepts 'my'
    q19.add_transition('y', q20)
    
    q21 = State(name="q21")
    q19.add_transition('a', q21)
    
    q22 = State(name="q22", is_final=True) # accepts 'may'
    q21.add_transition('y', q22)
    
    q23 = State(name="q23")
    q19.add_transition('u', q23)
    
    q24 = State(name="q24")
    q23.add_transition('s', q24)
    
    q25 = State(name="q25", is_final=True) # accepts 'must'
    q24.add_transition('t', q25)

    # DFA that accepts "on", "or"
    q26 = State(name="q26")
    q0.add_transition('o', q26)
    
    q27 = State(name="q27", is_final=True) # accepts 'on'
    q26.add_transition('n', q27)
    
    q28 = State(name="q28", is_final=True) # accepts 'or'
    q26.add_transition('r', q28)

    # DFA that accepts "she", "so", "should"
    q29 = State(name="q29")
    q0.add_transition('s', q29)
    
    q30 = State(name="q30", is_final=True) # accepts 'so'
    q29.add_transition('o', q30)
    
    q31 = State(name="q31")
    q29.add_transition('h', q31)
    
    q32 = State(name="q32", is_final=True) # accepts 'she'
    q31.add_transition('e', q32)
    
    q33 = State(name="q33")
    q31.add_transition('o', q33)
    
    q34 = State(name="q34")
    q33.add_transition('u', q34)
    
    q35 = State(name="q35")
    q34.add_transition('l', q35)
    
    q36 = State(name="q36", is_final=True) # accepts 'should'
    q35.add_transition('d', q36)

    # DFA that accepts "the", "this", "they", "to"
    q37 = State(name="q37")
    q0.add_transition('t', q37)
    
    q38 = State(name="q38", is_final=True) # accepts 'to'
    q37.add_transition('o', q38)
    
    q39 = State(name="q39")
    q37.add_transition('h', q39)
    
    q40 = State(name="q40", is_final=True) # accepts 'the'
    q39.add_transition('e', q40)
    
    q41 = State(name="q41", is_final=True) # accepts 'they'
    q40.add_transition('y', q41)
    
    q42 = State(name="q42")
    q39.add_transition('i', q42)
    
    q43 = State(name="q43", is_final=True) # accepts 'this'
    q42.add_transition('s', q43)

    # DFA that accepts "we", "will"
    q44 = State(name="q44")
    q0.add_transition('w', q44)
    
    q45 = State(name="q45", is_final=True) # accepts 'we'
    q44.add_transition('e', q45)
    
    q46 = State(name="q46")
    q44.add_transition('i', q46)
    
    q47 = State(name="q47")
    q46.add_transition('l', q47)
    
    q48 = State(name="q48", is_final=True) # accepts 'will'
    q47.add_transition('l', q48)

    # DFA that accepts "you"
    q49 = State(name="q49")
    q0.add_transition('y', q49)

    q50 = State(name="q50")
    q49.add_transition('o', q50)

    q51 = State(name="q51", is_final=True) # accepts 'you'
    q50.add_transition('u', q51)

    import re
    import string
    filename = "text2.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            token_matches = re.finditer(r"\S+", text)

            # Track accepted words and their positions
            accepted_words = []  # List of (start_pos, end_pos) spans in original text
            occurrences = {}  # {word: count}
            positions = {}    # {word: [list of starting positions]}

            for token_match in token_matches:
                original_word = token_match.group(0)
                word_position = token_match.start()
                word_end = token_match.end()

                clean_word = original_word.strip(string.punctuation).lower()
                if not clean_word:
                    continue

                if DEBUG:
                    print(f"\n=============== Simulating Input: '{clean_word}' ===============")
                    print("Press enter to continue next state...\n")

                current_state = q0

                for char in clean_word:
                    prev_state_name = current_state.name
                    next_state = current_state.process_input(char)

                    if next_state is None:
                        if DEBUG:
                            print(f"State: {prev_state_name} | Processing: {char} | next state: Trap")
                            input()
                            print("\n=> Hit a Trap State! Input rejected.")
                        current_state = None
                        break
                    else:
                        if DEBUG:
                            print(f"State: {prev_state_name} | Processing: {char} | next state: {next_state.name}")
                            input()
                        current_state = next_state

                if current_state and current_state.is_final:
                    if DEBUG:
                        print(f"\n=> Reached {current_state.name} which is a Final State. Word ACCEPTED!")
                    accepted_words.append((word_position, word_end))
                    # Track occurrences
                    if clean_word in occurrences:
                        occurrences[clean_word] += 1
                    else:
                        occurrences[clean_word] = 1
                    # Track positions
                    if clean_word in positions:
                        positions[clean_word].append(word_position)
                    else:
                        positions[clean_word] = [word_position]
                elif current_state:
                    if DEBUG:
                        print("\n=> Word REJECTED (Not in a final state).")

            # === VISUALIZATION WITH BOLDFACE ===
            print("\n" + "="*80)
            print("ORIGINAL TEXT WITH ACCEPTED WORDS HIGHLIGHTED (BOLD):")
            print("="*80)

            # Build highlighted output from original text spans to avoid index shifts.
            highlighted_parts = []
            last_index = 0
            for start_pos, end_pos in accepted_words:
                highlighted_parts.append(text[last_index:start_pos])
                highlighted_parts.append(f"\033[43m{text[start_pos:end_pos]}\033[0m")
                last_index = end_pos
            highlighted_parts.append(text[last_index:])
            highlighted_text = "".join(highlighted_parts)

            print(highlighted_text)

            # === SUMMARY TABLE ===
            print("\n" + "="*80)
            print("SUMMARY TABLE: ACCEPTED WORDS")
            print("="*80)
            print(f"{'Word':<15} {'Occurrences':<15} {'Positions':<50}")
            print("-"*80)

            for word in sorted(occurrences.keys()):
                count = occurrences[word]
                pos_list = positions[word]
                pos_str = ", ".join(map(str, pos_list))
                print(f"{word:<15} {count:<15} {pos_str:<50}")

            print("-"*80)
            print(f"{'TOTAL':<15} {len(accepted_words):<15} {len(occurrences)} unique words found")

    except FileNotFoundError:
        print(f"File {filename} not found.")
