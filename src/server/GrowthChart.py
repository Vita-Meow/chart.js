import pygal as pygal
from pygal.style import Style
from tempfile import NamedTemporaryFile


sum_of_month = 5
max_of_y = 39
min_of_y = 36

def get_baby_growth_chart():
    custom_css = '''
      {{ id }}.axis .line {    
        stroke: rgb(211, 214 ,221);
      }

      {{ id }}.graph {  
        fill: rgb(128,128,128);
      }

      {{ id }}.axis .guide.line { 
          stroke-dasharray: 10,6;
          stroke: rgb(211, 214 ,221);
      }
      
    '''
    custom_css_file = '/tmp/pygal_custom_style.css'
    with open(custom_css_file, 'w') as f:
      f.write(custom_css)
    custom_style = Style(
      background='transparent',
      plot_background='transparent',
      transition='400ms ease-in',
      colors=('rgb(255,220,51)', 'rgb(255,220,51)', 'rgb(255,220,51)', 'rgb(252,141,0)'))
    config = pygal.Config(range=(min_of_y, max_of_y), show_x_guides=True, style=custom_style, show_legend=False, height=280)
    config.css.append('file://' + custom_css_file)

    line_chart = pygal.XY(config)
    line_chart.x_labels = map(str, range(0, sum_of_month))
    line_chart.y_labels = 35, 37, 39, 41
    line_chart.add('50%', [(0, 37), (2, 38.1), (3.5, 39), (4, 39.1)], show_dots=False, stroke_style={'width': 2})
    line_chart.add('1%', [(0, 37), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)], show_dots=False, stroke_style={'width': 2})
    line_chart.add('99%', [(0, 37.7), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)], show_dots=False, stroke_style={'width': 2})
    line_chart.add('RealData', [(0.1, 37.7), (0.8, 37.7), (1.1, 38.1), (2.2, 39), (3.3, 39.1), (4, 40.1)],
                   stroke_style={'width': 3}, dots_size=6, allow_interruptions=False)
    res = line_chart.render()
    with open('../../public/charts/growthChart.svg', 'w') as outfile:
        outfile.write(res.decode('utf-8'))
    return res



get_baby_growth_chart()

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
