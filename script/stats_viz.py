import json
import csv
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", palette="muted", color_codes=True)

iterrogative_word = ['which', 'what', 'whose', 'who', 'whom', 'where', 'whither', 'whence', 'when', 'how', 'why', 'whether', 'whatsoever', 'whereby', 'wherefore']
yn_qa = ['did', 'was', 'were', 'is', 'are', 'does', 'will', 'would', 'do', 'have', 'has', 'can', 'should', 'could']
other_qa = ['give', 'name', 'describe', 'identify']
def training_stats():
    # init vars
    context_length = []
    # (length, is_impossible)
    question_global_info = []
    question_local_info = {}
    for w in iterrogative_word:
        question_local_info[w] = []
    for w in yn_qa:
        question_local_info[w] = []
    for w in other_qa:
        question_local_info[w] = []
    answer_length = []
    
    # iter training data stats
    print("Load {}....".format(sys.argv[1]))
    with open(sys.argv[1], 'r') as f:
        json_data = json.load(f)['data']
        # iterate each title(article)
        for article in json_data:
            # iterate each paragraph
            for paragraph in article['paragraphs']:
                qas = paragraph['qas'] # list of questions
                context = paragraph['context'] # string
                context_length.append(len(context.split()))
                for qa in qas:
                    question = qa['question'].lower()
                    is_impossible = qa['is_impossible']
                    question_global_info.append((len(question.split()), is_impossible))
                    question_word_count = 0
                    for w in iterrogative_word:
                        if w in question:
                            question_word_count += 1
                            question_local_info[w].append((len(question.split()), is_impossible))
                    if question_word_count == 0:
                        if question.split()[0] in yn_qa: 
                            question_word_count += 1
                            question_local_info[question.split()[0]].append((len(question.split()), is_impossible))
                            
                    if question_word_count == 0:
                        for w in other_qa:
                            if w in question:
                                question_word_count += 1
                                question_local_info[w].append((len(question.split()), is_impossible))
    """
                    if question_word_count == 0:
                        print(question)
    """
    # viz
    context_dist = sns.distplot(context_length, kde=False, color="b", axlabel="context length")
    context_dist.figure.savefig("../outputs/training_viz/context_dist.png")

    fig, ax = plt.subplots()
    possible_qa = list(map(lambda x: x[0], list(filter(lambda x: x[1] is True, question_global_info))))
    impossible_qa = list(map(lambda x: x[0], list(filter(lambda x: x[1] is False, question_global_info))))
    qa_dist = sns.distplot(possible_qa, ax = ax, label = "possible to answer", axlabel = 'question length')
    qa_dist = sns.distplot(impossible_qa, ax = ax, label = "impossible to answer", axlabel = 'question length')
    qa_dist.figure.savefig("../outputs/training_viz/qa_dist.png")
#    seaborn.kdeplot(df['col1'], ax=ax)
#    seaborn.kdeplot(df['col2'], ax=ax)


if __name__ == '__main__':
    training_stats()
