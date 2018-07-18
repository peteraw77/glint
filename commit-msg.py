#!/usr/bin/python
import sys
import spacy

# words that should not appear in an imperative sentence
non_imperative_words = {'i', 'please', 'you'}
# words handled poorly by spacy
problem_words = {'rework', 'update', 'fix'}

def is_imperative(msg):
    nlp = spacy.load('en_core_web_sm')
    out = nlp(msg)

    #TODO find a more elegant solution for problem words
    if out[0].tag_ != 'VB':
        text = out[0].text.lower()
        if text not in problem_words:
            print('%s is not a simple verb' % text)
            return False

    # check if there is a subject
    for word in out:
        if word.text.lower() in non_imperative_words:
            return False

    return True

def get_commit_msg():
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg

def main():
    msg = get_commit_msg()
    header = msg.split('\n')[0]

    # check for capitalization
    if header[0] == header[0].lower():
        print('Commit title must start with a capital letter')
        sys.exit(1)

    # check for punctuation
    if header[-1] in {'.','!','?'}:
        print('Trailing punctuation is not permitted')
        sys.exit(1)

    # check for length
    if len(header) > 50:
        print('Commit title must be less than 50 characters')
        sys.exit(1)
    if len(msg) > 124:
        # length is including the \n character
        print('Commit body must be 72 characters or less')
        sys.exit(1)

    # check tense
    if not is_imperative(header):
        print('Commit title must be in imperative tense.')
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
