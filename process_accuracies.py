n = 1380
def process(dim, conf_mat, conf_mat_imp):
    [[true_positive, false_negative], [false_positive, true_negative]] = conf_mat
    [[_, _], [false_imp, true_imp]] = conf_mat_imp

    num_positive = true_positive + false_negative
    assert(num_positive == n)
    num_negative = true_negative + false_positive
    assert(num_negative == n)
    num_negative_imp = false_imp + true_imp
    assert(num_negative_imp == n)

    cols = [
        'dimensionality',
        'true positive',
        'false positive',
        'false negative',
        'true negative',
        'acc',
        'false positive imp',
        'true negative imp',
        'acc imp',
    ]
    data = [str("{:.2f}".format(x * 100)) if isinstance(x, float) else str(x) for x in [
        dim,
        true_positive,
        false_positive,
        false_negative,
        true_negative,
        (true_positive + true_negative)/2/n,
        false_imp,
        true_imp,
        (true_positive + true_imp)/2/n,
    ]]
    print(" & ".join(cols))
    print(" & ".join(data))
    return
    for x in list(zip(cols, data)):
        print(x)

print('*'*20)
print('5 epochs')
print('*'*20)
process(64, [[1106, 274], [279, 1101]], [[0, 0], [43, 1337]])
process(128, [[1115, 265], [283, 1097]], [[0, 0], [0, 1380]])
process(256, [[1071, 309], [180, 1200]], [[0, 0], [0, 1380]])
print()

print('*'*20)
print('20 epochs')
print('*'*20)
process(64, [[1347, 33], [0, 1380]], [[0, 0], [555, 825]])
process(128, [[1367, 13], [0, 1380]], [[0, 0], [1240, 140]])
process(256, [[1357, 23], [0, 1380]], [[0, 0], [938, 442]])
print()

print('*'*20)
print('20 epochs leaky')
print('*'*20)
process(64, [[1380, 0], [23, 1357]], [[0, 0], [313, 1067]])
process(128, [[1380, 0], [9, 1371]], [[0, 0], [296, 1084]])
process(256, [[1380, 0], [5, 1375]], [[0, 0], [350, 1030]])
