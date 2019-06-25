import pygal as pygal
from pygal.style import Style
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#fecf33', '#fecf33', '#fecf33', '#fc8d00'))

# params
# ***** name *******:
# ***** data *******：
# key as legend(distinguish three standard lines and real user data), value is the data set
# data：{
#   "Average": [(0, 37), (2, 38.1), (3, 39), (4, 39.1)],
#   "Min": [(0, 37), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)]，
#   "Max": [(0, 37), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)],
#   "RealData": [(0.1, 37.7), (0.8, 37.7), (1.1, 38.1), (2.2, 39), (3.3, 39.1), (4, 40.1)],
# }
# (month<float>, value<float>)
# ***** sum_of_month ******
# ***** max_of_y ******
# ***** min_of_y ******

sum_of_month = 5
max_of_y = 39
min_of_y = 36


line_chart = pygal.XY(range=(min_of_y, max_of_y), style=custom_style, show_legend=False)
line_chart.x_labels = map(str, range(0, sum_of_month))
line_chart.y_labels = 35, 37, 39, 41
line_chart.add('Average', [(0, 37), (2, 38.1), (3.5, 39), (4, 39.1)], show_dots=False)
line_chart.add('Min', [(0, 37), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)], show_dots=False)
line_chart.add('Max', [(0, 37.7), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)], show_dots=False)
line_chart.add('RealData', [(0.1, 37.7), (0.8, 37.7), (1.1, 38.1), (2.2, 39), (3.3, 39.1), (4, 40.1)], allow_interruptions=False)
res = line_chart.render()
with open('../../public/charts/growthChart.svg', 'w') as outfile:
    outfile.write(res.decode('utf-8'))



