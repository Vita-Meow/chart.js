import pygal as pygal

stack_chart = pygal.StackedBar()
stack_chart.title = 'stack bar chart'
stack_chart.x_labels = map(str, range(2002, 2013))
stack_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
stack_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
stack_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
stack_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
res = stack_chart.render()
with open('../../public/charts/stackChart.svg', 'w') as outfile:
    outfile.write(res.decode('utf-8'))
