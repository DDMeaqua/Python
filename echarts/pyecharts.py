from pyecharts import Line

line = Line()
line.add_xaxis(['英国', '美国', '中国'])
line.add_yaxis('GDP', [10, 30, 20])

line.render()