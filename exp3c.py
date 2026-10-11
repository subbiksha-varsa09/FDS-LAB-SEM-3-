import matplotlib.pyplot as election

labels = ['CANDIDATE 1', 'CANDIDATE 2', 'CANDIDATE 3', 'CANDIDATE 4']
Votes = [315, 130, 245, 210]

colors = ['green', 'yellow', 'red', 'orange']

explode = (0.2, 0, 0, 0)

election.pie(
    Votes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%0.2f%%'
)

election.title('Election Results')
election.show()