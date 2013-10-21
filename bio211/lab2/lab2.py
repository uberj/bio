import matplotlib.pyplot as plt
import numpy as np

import pprint as pp

data = {
    'no-caffeine': {
        'before': list(reversed([82, 82, 98, 86, 70])),
        'after': list(reversed([110, 102, 112, 108, 170])),
        'recovery': list(reversed([60, 90, 120, 60, 120])),
    },
    'caffeine': {
        'before': list(reversed([64, 70, 76, 72, 60])),
        'after': list(reversed([160, 76, 124, 126, 140])),
        'recovery': list(reversed([120, 90, 60, 3 * 60, 4 * 60])),
    }
}


def avg(l):
    return sum(l) / float(len(l))


def diffl(l1, l2):
    diff = []
    for i, j in zip(l1, l2):
        diff.append(j - i)
    return diff


def table_line(s):
    return s + ' \\\\ \\hline'


def latex_table():
    s = calc_stats()
    lines = []
    header = 'Condition & '
    num_groups = s['num-groups']
    for gn in range(num_groups):
        header += 'Group %s & ' % str(gn)

    header += 'Average'

    lines.append(header)

    n_c_tb = 'No Caffeine & '
    for d in s['no-caffeine-diff']:
        n_c_tb += '%s & ' % d

    n_c_tb += str(s['no-caffeine-diff-avg'])
    lines.append(n_c_tb)

    c_tb = 'Caffeine & '
    for d in s['caffeine-diff']:
        c_tb += '%s & ' % d

    c_tb += str(s['caffeine-diff-avg'])
    lines.append(c_tb)

    table = "\\begin{{tabular}}{{| l {groups} | l |}}".format(
        groups=' | l ' * num_groups
    )
    table += "\n\\hline\n"
    table += '\n'.join(map(table_line, lines))
    table += "\n\\end{tabular}"

    return table


def latex_graph():
    s = calc_stats()
    N = s['num-groups']

    ind = np.arange(N + 1)  # the x locations for the groups
    width = 0.35        # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(
        ind, data['no-caffeine']['recovery'] + [s['no-caffeine-recovery-avg']],
        width, color='r'
    )

    rects2 = ax.bar(
        ind + width,
        data['caffeine']['recovery'] + [s['caffeine-recovery-avg']],
        width, color='y'
    )

    ax.set_ylabel('Recovery Time By Seconds')
    ax.set_title('Recovery Time By Group')
    ax.set_xticks(ind + width)
    ticks = tuple(['Group ' + str(i) for i in range(N)] + ['Average'])
    ax.set_xticklabels(ticks)

    ax.legend((rects1[0], rects2[0]), ('No Caffeine', 'Caffeine'))

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2.0, 1.05 * height,
                '%d' % int(height), ha='center', va='bottom'
            )

    autolabel(rects1)
    autolabel(rects2)
    return fig


def calc_stats():
    n_c_diff = diffl(
        data['no-caffeine']['before'], data['no-caffeine']['after']
    )
    c_diff = diffl(data['caffeine']['before'], data['caffeine']['after'])

    return {
        'no-caffeine-before-avg': avg(data['no-caffeine']['before']),
        'no-caffeine-after-avg': avg(data['no-caffeine']['after']),
        'no-caffeine-recovery-avg': avg(data['no-caffeine']['recovery']),
        'no-caffeine-diff': n_c_diff,
        'no-caffeine-diff-avg': avg(n_c_diff),

        'caffeine-before-avg': avg(data['caffeine']['before']),
        'caffeine-after-avg': avg(data['caffeine']['after']),
        'caffeine-recovery-avg': avg(data['caffeine']['recovery']),
        'caffeine-diff': c_diff,
        'caffeine-diff-avg': avg(c_diff),

        'num-groups': len(data['caffeine']['before']),
        'recovery-max': max(
            data['no-caffeine']['recovery'] +
            data['caffeine']['recovery']
        )
    }

if __name__ == '__main__':
    pp.pprint(calc_stats())
    #print latex_table()
    print latex_graph()
    plt.show()
