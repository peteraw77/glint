#!/usr/bin/python
import sys
import spacy

def is_imperative(msg):
    nlp = spacy.load('en_core_web_sm')
    out = nlp(msg)

    print(out[0])
    
    # check if the sentence begins with present tense verb
    if out[0].tag_ != 'VB':
        return False

    # check if there is a subject
    for word in out:
        if word.dep == spacy.symbols.nsubj:
            return False

    return True

def get_commit_msg():
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg

def main():
    msg = get_commit_msg()

    if not is_imperative(msg):
        print('Commit message must be in imperative tense.')
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
