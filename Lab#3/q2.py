def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {subject: score}
    else:
        subject_score[student][subject] = score
    return subject_score


def calc_average_score(subject_score):
    avg = dict()
    for s in subject_score:
        total = f'{sum(subject_score[s].values()) / len(subject_score[s].values()):.2f}'
        avg[s] = total
    return avg
