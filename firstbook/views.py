from django.shortcuts import render
from firstbook.models import Study
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components


def homepage(request):
    return render(request, 'firstbook/homepage.html')


def graph(request):

    dict = {}
    for i in Study.objects.all():
        dict[i.__str__()] = i.meanrate()

    dict_sorted = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]))

    x_list = [element[0] for element in dict_sorted]
    y_list = [element[1] for element in dict_sorted]

    x = x_list
    y = y_list

    plot = figure(x_range=x_list, plot_height=400, title="Study Rates", toolbar_location=None, tools="")

    plot.vbar(x=x_list, top=y_list, width=0.5, color='firebrick')

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    script, div = components(plot)

    return render(request, 'firstbook/study_graph.html', {'script': script, 'div': div})


