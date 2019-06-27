import pygal as pygal
from pygal.style import Style

custom_css = '''
     {{ id }}.axis .line {    
       stroke: rgb(211, 214 ,221,0.6);
       stroke-width: 2px;
     }

     {{ id }}.graph {  
       fill: rgb(128,128,128);
     }

     {{ id }}.axis .line { 
        stroke-dasharray: 7,7;
        stroke: rgb(211,214,221,0.6);;
        stroke-width: 2px;
     }

     {{ id }}.axis .guide.line { 
         stroke-dasharray: 7,7;
         stroke: rgb(211,214,221,0.6);;
         stroke-width: 2px;
     }

     {{ id }}.axis .major.line {
        stroke: rgb(211, 214 ,221,0.6);
     }


     {{ id }}.axis text { 
         font-size: 14px;
         font-family: Helvetica Neue;
         color: rgb(128,128,128);
     }

     {{ id }}.reactive {
        fill-opacity: 1;
        stroke-opacity: 1;
        width: 11px !important;
     }
     
     {{ id }}.axis text {
        font-size: 18px;
        font-family: Helvetica Neue;
        color: rgb(142,141,147);
     }
     
     {{ id }}.axis.x text {
        display: none;
     }
     
      {{ id }}.axis.x text {
        display: none;
     }
     
      {{ id }}.axis.x .guides:nth-child(6) text{ 
          display: block;
      }
      
      {{ id }}.axis.x .guides:nth-child(11) text{ 
          display: block;
      }
      
       {{ id }}.axis.x .guides:nth-child(16) text{ 
          display: block;
      }
      
        
       {{ id }}.axis.x .guides:nth-child(21) text{ 
          display: block;
      }
      
       {{ id }}.axis.x .guides:nth-child(26) text{ 
          display: block;
      }
      
      {{ id }}.axis.x .guides:nth-child(31) text{ 
         display: block;
      }
      



   '''
custom_css_file = '../../public/charts/growthChart.css'
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  transition='400ms ease-in',
  colors=('rgb(91,98,210)','rgb(255,199,35)','rgb(71,197,255)','rgb(40,215,205)'))
with open(custom_css_file, 'w') as f:
    f.write(custom_css)
config = pygal.Config(range=(0, 120), show_x_guides=True, style=custom_style, show_legend=True,
                      height=280,legend_at_bottom=True,legend_at_bottom_columns=4,
                          rounded_bars=2)
config.css.append('file://' + custom_css_file)
stack_chart = pygal.StackedBar(config)
stack_chart.x_labels = map(str, range(1, 30))
stack_chart.y_labels = 0, 40, 80, 120
stack_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,85.8, 84.6, 84.7, 74.5,  ])
stack_chart.add('Firefox', [31.3, 31.3, 31.3, 26.6,  31.3, 31.3, 31.3, 26.6,   31.3, 31.3, 31.3, 16.6, 31.3, 31.3, 31.3, 26.6,])


res = stack_chart.render()
with open('../../public/charts/stackChart.svg', 'w') as outfile:
    outfile.write(res.decode('utf-8'))
