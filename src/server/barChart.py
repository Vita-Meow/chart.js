import pygal as pygal
from pygal.style import Style

MAPPING = {
    "AverageConsumedPerSession": {
        "display_name": "Average consumed per session",
        "color": "rgb(255,121,121)"
    }
}
custom_css = '''
     {{ id }}.axis .line {    
       stroke: rgb(211, 214 ,221);
       stroke-width: 2px;
     }

     {{ id }}.graph {  
       fill: rgb(128,128,128);
     }

     {{ id }}.axis .guide.line { 
         stroke-dasharray: 6,6;
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
     
     {{ id }}.reactive {
        fill-opacity: 1;
        stroke-opacity: 1;
        width: 8px !important;
     }


   '''
custom_css_file = '../../public/charts/stack_chart.css'
with open(custom_css_file, 'w') as f:
    f.write(custom_css)
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  transition='400ms ease-in',
  colors=('rgb(255,121,121)', 'rgb(255,220,51)', 'rgb(255,220,51)', 'rgb(252,141,0)'))
config = pygal.Config(range=(1, 100), show_x_guides=True, style=custom_style, show_legend=False, height=280, rounded_bars=1)
config.css.append('file://' + custom_css_file)
bar_chart = pygal.Bar(config)
bar_chart.title = 'Bar chart'
bar_chart.x_labels = map(str, range(1, 30))
bar_chart.y_labels = 0, 25, 50, 75, 100
bar_chart.add('Firefox', [2, 8, 10, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
res = bar_chart.render()
with open('../../public/charts/barChart.svg', 'w') as outfile:
    outfile.write(res.decode('utf-8'))
