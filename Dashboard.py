#IMPORTING NECESSARY MODULES

import ssl
import pandas as pd
import numpy as np
import panel as pn
import hvplot.pandas
import holoviews as hv
pn.extension('tabulator')
hv.extension('bokeh')

from math import pi
from bokeh.palettes import Category20b,RdPu4,Oranges6,PiYG,Greens,Category20b_19
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

#DATA COLLECTION AND CLEANING

df=pd.read_csv('responses.csv')

df['fe'] = df['fe'].apply(lambda x: "Positive" if x == 'pos' else x)
df['fe'] = df['fe'].apply(lambda x: "Negative" if x == 'neg' else x)
df['fe'] = df['fe'].apply(lambda x: "Neutral" if x == 'neu' else x)

df1=pd.DataFrame(df)

df['tm'] = df['tm'].apply(lambda x: "High" if x == 'Excellent' else x)
df['tm'] = df['tm'].apply(lambda x: "Medium" if x == 'Average' else x)
df['tm'] = df['tm'].apply(lambda x: "Low" if x == 'Poor' else x)

df['sl'] = df['sl'].apply(lambda x: "High" if x == 'Often' else x)
df['sl'] = df['sl'].apply(lambda x: "Medium" if x == 'Sometimes' else x)
df['sl'] = df['sl'].apply(lambda x: "Low" if x == 'Rarely' else x)

df['pa'] = df['pa'].apply(lambda x: "High" if x == 'Often' else x)
df['pa'] = df['pa'].apply(lambda x: "Medium" if x == 'Sometimes' else x)
df['pa'] = df['pa'].apply(lambda x: "Low" if x == 'Rarely' else x)

df=df.rename(columns={"tm":"Time Management","sl":"Sleeping","pa":"Physical Activity"})


#WIDGET FOR DAILY HABITS VS FREQUENCY PLOT
select_sent=pn.widgets.Select(name="Select Category", options=["All","Positive","Neutral","Negative"])
select_sent.width=200


#DAILY HABITS VS FREQUENCY PLOT
def plot_bar(category):
    if category == 'All':
        a=df["Time Management"].value_counts().sort_index().rename("Time Management")
        b=df["Physical Activity"].value_counts().sort_index().rename("Physical Activity")
        c=df["Sleeping"].value_counts().sort_index().rename("Sleeping")

        

    else:
        a = df[df['fe'] == category]["Time Management"].value_counts().sort_index().rename("Time Management")
        b = df[df['fe'] == category]["Physical Activity"].value_counts().sort_index().rename("Physical Activity")
        c = df[df['fe'] == category]["Sleeping"].value_counts().sort_index().rename("Sleeping")

    plot_df1=pd.concat([a,b,c],axis=1)
    
    plot1=plot_df1.hvplot.bar(xlabel="Categorical Variable",ylabel="Count",
        y=["Time Management","Physical Activity","Sleeping"],title="Daily Habits vs Frequency",
        legend=True,color=["paleturquoise","darkturquoise","cadetblue"])
    
    plot1=plot1.opts(multi_level=False)
    return plot1


# PLOT FUNCTION
@pn.depends(select_sent.param.value)
def update_plot(category):
    plot1 = plot_bar(category)
    return plot1

bar_plot=pn.Row(update_plot)
bar_plot[0].width=600
bar_plot[0].height=350


#DATA FOR PIE CHART
data=df["fe"].value_counts()
data = pd.Series(data).reset_index(name='value').rename(columns={'index': 'emotion'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Greens[len(data)]

#PLOTTING PIE CHART
p = figure(height=300, width=350,title="Overall Sentiment Distribution", toolbar_location=None,
           tools="hover",tooltips="@fe : @value")

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='fe', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None



#OPTIONS AND WIDGETS FOR DEPENDENCE OF DAILY HABITS
fixed_options = ["Time Management","Sleeping","Physical Activity"]
second_options = ["High","Medium","Low"]

fixed_select = pn.widgets.Select(name="Variable",  options=fixed_options)
second_select = pn.widgets.Select(name="Level",  options=second_options)


#PLOTTING DEPENDENCE OF DAILY HABITS
def plot_func(first_select,second_select):

    #fixed_options = ["Time Management","Sleeping","Physical Activity"]
    options = [x for x in fixed_options if x != first_select]

    plot_df = pd.DataFrame()

    for i in options:
        temp = df[df[first_select] == second_select][i].value_counts().sort_index().rename(i)
        plot_df = pd.concat([plot_df, temp], axis=1)
        
    plot = plot_df.hvplot.bar(y=[i for i in options],title="Dependence of Daily Habit Variables" ,height=400,rot=90,legend='top_right',color=[RdPu4[1],RdPu4[2]],xlabel="Categorical Variable",ylabel="Count")
    
    plot=plot.opts(multi_level=False)
    return plot


#COMBINING BOTH WIDGETS
form_component = pn.Column(fixed_select, second_select, sizing_mode='stretch_width')
form_component[0].width=200
form_component[1].width=200

#BINDING PLOT AND WIDGETS
plot_component = pn.bind(plot_func, first_select=fixed_select, second_select=second_select)

#FINAL PLOTTING
bar_plot2 = pn.Row(plot_component)
bar_plot2[0].width=470
bar_plot2[0].height=400

#IMPORTING IMAGE
jpg_pan=pn.pane.Image("static/Website_Images/mental_health.jpg")
jpg_pan.width=230
jpg_pan.height=300

#FINAL TEMPLATE OF DASHBOARD
template = pn.template.FastListTemplate(
    header_background=Category20b_19[-3] ,
    title="Sentiment Analysis - Dashboard",
    sidebar_width=250,
    sidebar=[
        pn.pane.Markdown("### *SDG 3 - Good Health and Mental Well Being*"),
     pn.pane.Markdown("") , pn.pane.Markdown("") ,jpg_pan,   
        form_component
    ],
    main=[
        pn.Row(bar_plot,select_sent),
        pn.Row(bar_plot2,p)       
    ]
)

pn.serve(template,show = False,  port=62097)

template.show()