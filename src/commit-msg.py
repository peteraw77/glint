import sys
from linguistic_analysis.sentence_analyzer import SentenceAnalyzer

def get_commit_msg():
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg

def main():
    msg = get_commit_msg()
    sa = SentenceAnalyzer()

    if !sa.is_imperative(msg):
        print('Commit message must be in imperative tense.')
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
