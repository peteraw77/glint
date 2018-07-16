#!/usr/bin/python
import sys
import spacy

# words that should not appear in an imperative sentence
bad_words = ['i', 'please', 'you']

def is_imperative(msg):
    nlp = spacy.load('en_core_web_sm')
    out = nlp(msg)

    #TODO fix the word rework
    if out[0].tag_ != 'VB':
        print('%s is not a simple verb' % out[0].text)
        return False

    # check if there is a subject
    for word in out:
        if word.text.lower() in bad_words:
            return False

    return True

def get_commit_msg():
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg

def main():
    msg = get_commit_msg()

    # check for capitalization
    if msg[0] == msg[0].lower():
        print('Commit messages must start with a capital letter')
        sys.exit(1)

    if not is_imperative(msg):
        print('Commit message must be in imperative tense.')
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
