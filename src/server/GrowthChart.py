import pygal as pygal
from pygal.style import Style


def get_baby_growth_chart(name, min_of_y, max_of_y, sum_of_month, data):
    print(name)
    custom_css = '''
      {{ id }}.axis .line {    
        stroke: rgb(211, 214 ,221);
        stroke-width: 2px;
      }

      {{ id }}.graph {  
        fill: rgb(128,128,128);
      }

      {{ id }}.axis .guide.line { 
          stroke-dasharray: 12,8;
          stroke: rgb(211, 214 ,221);
          stroke-width: 2px;
      }
      
      {{ id }}.axis.y .guides:first-child { 
          display: none;
      }
      
      {{ id }}.axis text { 
          font-size: 14px;
          font-family: Helvetica Neue;
          color: rgb(128,128,128);
      }
      
      
    '''
    custom_css_file = '../../public/charts/growthChart.css'
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
    line_chart.y_labels = [min_of_y]
    gap = round((max_of_y - min_of_y)/3);
    for x in range(3):
       line_chart.y_labels.append(int(line_chart.y_labels[x]+gap))
    line_chart.add('Average', data["Average"], show_dots=False, stroke_style={'width': 2})
    line_chart.add('Min', data["Min"], show_dots=False, stroke_style={'width': 2})
    line_chart.add('Max', data["Max"], show_dots=False, stroke_style={'width': 2})
    line_chart.add('RealData',  data["RealData"], stroke_style={'width': 3}, dots_size=6, allow_interruptions=False)
    res = line_chart.render()
    with open('../../public/charts/growthChart.svg', 'w') as outfile:
        outfile.write(res.decode('utf-8'))
    return res

data_example = {
  'Average': [(0, 37), (2, 38.1), (3.5, 39), (4, 39.1)],
  'Min': [(0, 37), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)],
  'Max': [(0, 37.7), (1, 38.1), (2, 39), (3, 39.1), (4, 40.1)],
  'RealData':[(0.1, 37.7), (0.8, 37.7), (1.1, 38.1), (2.2, 39), (3.3, 39.1), (4, 40.1)]

}

get_baby_growth_chart("Weight(kg)", 35, 43, 5, data_example )

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
