def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score


def calc_average_score(subject_score):
    total, amount = 0, 0
    for x in subject_score.keys():
        total += subject_score[x]
        amount += 1
    return f'{total/amount:.2f}'
