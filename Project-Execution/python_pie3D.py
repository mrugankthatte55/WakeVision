import headers as headers

def python_pie3D(l1,l2) :
  # initialize chart object, 250 x 250 pixels
  chart = headers.PieChart3D(700, 250)
  # pass your data to the chart object
  chart.add_data(l1)

  # make labels for the slices
  chart.set_pie_labels(l2)

  # render the image
  chart.download('pie chart.png')

