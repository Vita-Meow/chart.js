import pygal as pygal
from pygal.style import Style

UOM_MAPPING = {
    'weight': "Weight(kg)",
    'height': "Height(cm)",
    'head_circ': "Head Circ.(cm)"
}
def get_baby_growth_chart(name, min_of_y, max_of_y, min_of_x, max_of_x, data):
    print(name)
    custom_css = '''
     {{ id }}.axis .line {
      stroke: rgb(211, 214 ,221);
      stroke-width: 2px;
    }
    
    {{ id }}.graph {
      fill: rgb(128,128,128);
    }
    
    {{ id }}.axis text {
      font-size: 14px;
      font-family: Helvetica Neue;
      fill: rgb(128,128,128);
    }
    
    {{ id }}.axis.y text { 
      font-size: 16px;
      font-family: Helvetica Neue;
      color: rgb(142,141,147);
    }
    
    {{ id }}.axis.x text {
      font-size: 16px;
      font-family: Helvetica Neue;
      fill: rgb(142,141,147);
      transform: translateY(10px);
    }
    
    {{ id }}.title:first-child {
      fill: rgba(142,142,147,1);
      font-family: Helvetica Neue;
      font-size: 16px;
      transform: translate(337px, 0px);
    }
    
    {{ id }}.title:nth-child(2) {
      fill: rgba(142,142,147,1);
      font-family: Helvetica Neue;
      font-size: 16px;
      transform: translate(53px,-143px);
    }
    
    {{ id }}.axis.x .line{
      display: none;
    }
    
    {{ id }}.axis.x .guides .line{
      display: block;
    }
    
    {{ id }}.axis.y .line{
      display: none;
    }
    
    {{ id }}.axis.y .guides .line{
      display: block;
    }
    
    {{ id }}.axis .guide.line {
      stroke-dasharray: 8,8;
      stroke: rgba(211, 214 ,221, 0.8);
      stroke-width: 2px;
    }
    {{ id }}.axis .major.guide.line {
      stroke-dasharray: none;
      stroke: rgb(211, 214, 221);
      stroke-width: 2px;
    }
    {{ id }}.axis .axis.major.line {
      stroke-dasharray: none;
      stroke: rgb(211, 214, 221);
      stroke-width: 2px;
    }
    
    {{ id }}.axis .major+text {
      font-size: 14px;
      font-family: Helvetica Neue;
      fill: rgb(128,128,128) !important;
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

    uom = UOM_MAPPING[name]
    config = pygal.Config(
        range=(min_of_y, max_of_y),
        xrange=(min_of_x, max_of_x),
        show_x_guides=True, style=custom_style,
        margin_top=50, y_title=uom, x_title="Month",
        show_legend=False, height=300,
        x_labels_major_every=99999,
        y_labels_major_every=99999,
    )
    config.css.append('file://' + custom_css_file)
    line_chart = pygal.XY(config)
    line_chart.y_labels = [min_of_y]
    gap = round((max_of_y - min_of_y)/3);
    for x in range(3):
       line_chart.y_labels.append(int(line_chart.y_labels[x]+gap))
    line_chart.add('Average', data["Average"], show_dots=False, stroke_style={'width': 2})
    line_chart.add('Min', data["Min"], show_dots=True, stroke_style={'width': 2})
    line_chart.add('Max', data["Max"], show_dots=True, stroke_style={'width': 2})
    line_chart.add('RealData',  data["RealData"], stroke_style={'width': 3}, dots_size=6, allow_interruptions=False)
    res = line_chart.render()
    with open('../../public/charts/growthChart.svg', 'w') as outfile:
        outfile.write(res.decode('utf-8'))
    return res

data_example = {
  'Average': [(20, 82.7), (21, 83.7), (22, 84.6), (23, 85.5), (24, 86.4), (25, 86.6), (26, 87.4)] ,
  'Min': [(20, 75.7), (21, 76.5), (22, 77.3), (23, 78.1), (24, 78.9), (25, 79), (26, 79.7)] ,
  'Max': [(20, 89.7), (21, 90.8), (22, 91.9), (23, 92.9), (24, 93.9), (25, 94.2), (26, 95.2)],
  'RealData':[(20, 87.19),(20.722807449844964, 88.29), (21.065709768167725, 89.65), (21.394258609006346, 90.85),
              (21.722807449844964, 91.9), (22.03285488408386, 93.15), (22.361403724922482, 94.5), (22.689952565761104, 96.14), (23.03285488408386, 97.34),
              (23.361403724922482, 98.59), (23.689952565761104, 100.22), (24.0, 101.53), (24.32854884083862, 102.91), (24.657097681677243, 104.32), (24.985646522515864, 105.49),
              (25.295693956754757, 106.59), (25.62424279759338, 108.24), (26.03285488408386, 109.26)]
}

get_baby_growth_chart("weight", 66 ,141 ,20, 26 ,data_example )

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
