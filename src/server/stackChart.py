import pygal as pygal
from pygal.style import Style

def get_stack_chart(name, data,labels_of_x ,max_of_y, uom):
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
            width: 10px !important;
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
         
         {{ id }}.title {
            fill: rgba(142,142,147,1);
            font-family: Helvetica Neue;
            font-size: 19px;
            transform: translate(35px,-131px);
         }
         {{ id }}.stackedbar-graph .plot {
             transform: translate(45px, 36px);
         }
         {{ id }} .legends .legend text {
            fill-opacity: 1;
            fill: rgba(51,51,51);
            font-family: Helvetica Neue,"ProximaNova-Regular";
            font-size: 20px;
         }
         
         {{ id }} .legends {
              transform: translate(84px,259px)!important;
         }
         
         {{ id }} .bars .bar rect {
            transform: translate(-7px,0)!important;
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
           
          {{ id }}.legends .legend rect{
                width: 20px!important;
                height: 20px!important;
                rx: 5;
          }
          
          {{ id }}.legends .legend:first-child text{
            transform: translate(10px, 7px);
          }
          
            {{ id }}.legends .legend:nth-child(2) text{
            transform: translate(10px, 7px);
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
                          height=280,legend_at_bottom=True,legend_at_bottom_columns=2,y_title=uom,
                              rounded_bars=2)
    config.css.append('file://' + custom_css_file)
    stack_chart = pygal.StackedBar(config)
    stack_chart.x_labels = labels_of_x
    stack_chart.y_labels = [0]
    gap = round((max_of_y - 0) / 3);
    for x in range(3):
        stack_chart.y_labels.append(int(stack_chart.y_labels[x] + gap))
    for legend, series_data in data.items():
       stack_chart.add(legend, series_data)


    res = stack_chart.render()
    with open('../../public/charts/stackChart.svg', 'w') as outfile:
        outfile.write(res.decode('utf-8'))

data_of_example = {
   'Daytime sleep':[85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,85.8, 84.6, 84.7, 74.5],
   'Daytime sleep2': [31.3, 31.3, 31.3, 26.6,  31.3, 31.3, 31.3, 26.6,   31.3, 31.3, 31.3, 16.6, 31.3, 31.3, 31.3, 26.6,]
}
labels_for_x = ['5 Jan','6 Jan', '7 Jan', '8 Jan', '9 Jan', '10 Jan','11 Jan','12 Jan', '13 Jan', '14 Jan', '15 Jan', '16 Jan'
                ,'17 Jan', '18Jan', '19Jan', "20 Jan", "21 Jan", "22 Jan", "23 Jan", "24 Jan", "25 Jan",'26 Jan', '27 Jan', "28 Jan" ,"30 Jan", "31 Jan" ,"1 Feb", "2 Feb", "3 Feb"
                '4 Feb', '5 Feb']

get_stack_chart('diapper', data_of_example,labels_for_x ,120, "hours" )

#  stack chart params
# get_stack_chart(name, data,labels_of_x ,max_of_y, uom )
# ***** name *******:

# ***** data *******：
# key as legend(distinguish three standard lines and real user data), value is the data set
# data：{
#   "Pop": [85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,85.8, 84.6, 84.7, 74.5 ...],
#   "Pee": [85.8, 84.6, 84.7, 74.5, 5.8, 84.6, 84.7, 74.5,  85.8, 84.6, 84.7, 74.5,85.8, 84.6, 84.7, 74.5 ...]，
# }
# If there is no record on a certain day, it is regarded as 0)
#  data's key should be legend name

# ***** labels_of_x ******
#['5 Jan','6 Jan','7 Jan','8 Jan',......,'4 Feb']

# ***** max_of_y ******
# max value  of pop‘s data  + max  value of pee‘s data +....

# ***** uom ******
# should be times or hrs ....