import os
import sys
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
from nltk.corpus import framenet as fn

VERBNET_PATH = './verbnet/verbnet3.4/'

def generate_csv(output='vn-mappings.csv', path=VERBNET_PATH):
    output_set = set()
    for filename in os.listdir(path):
        with open(f"{path}{filename}") as xml:
            soup = BeautifulSoup(xml, "lxml-xml")
            for member in soup.find_all("MEMBER"):
                if member['wn'] != '' and member['fn_mapping'] != 'None':
                    for option in member['wn'].replace('?', '').split(' '):           
                        if len(option) > 1:
                            wn_syn = wn.synset_from_sense_key(f"{option}::")
                            wn_of = wn.ss2of(wn_syn).replace('-','')
                            
                            # NLTK API refers to Transition_to_a_state as Transition_to_state
                            if member['fn_mapping'] == 'Transition_to_a_state':
                                frame = fn.frame_by_name('Transition_to_state')
                            # And Appearance seems to be Give_impression based on its related verbs
                            elif member['fn_mapping'] == 'Appearance':
                                frame = fn.frame_by_name('Give_impression')
                            else:
                                frame = fn.frame_by_name(member['fn_mapping'])
                            converted_name = '.'.join(wn_syn.name().split('.')[:-1])
                            did_something = False
                            for lemma in wn_syn.lemmas():
                                converted_name = f'{lemma.name()}.v'
                                if converted_name in frame.lexUnit:
                                    lu_id = frame.lexUnit[converted_name].ID
                                    output_set.add((wn_of, lu_id))
                                    did_something = True
                            if not did_something:
                                for lemma in wn_syn.lemmas():
                                    for lunit in frame.lexUnit:
                                        if lunit.startswith(f"{lemma.name()} ") and lunit.endswith('.v'):
                                            lu_id = frame.lexUnit[lunit].ID
                                            output_set.add((wn_of, lu_id))
                                            break
    with open(output, 'w+') as out:
        for pair in sorted(list(output_set)):
            out.write(f"{pair[0]}, {pair[1]}\n")
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        generate_csv()
    elif len(sys.argv) == 2:
        generate_csv(output=sys.argv[-1])
    elif len(sys.argv) == 3:
        generate_csv(output=sys.argv[-2], path=sys.argv[-1])
