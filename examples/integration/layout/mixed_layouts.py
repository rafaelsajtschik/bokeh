from __future__ import absolute_import

from bokeh.plotting import figure, save
from bokeh.models import Row, Column

template = """
{% block preamble %}
<style>
    body * {
        box-sizing: border-box;
    }
    .view {
        width: 1000px;
        background-color: lightgray;
    }
    .root {
        display: inline-block;
        background-color: black;
        min-width: 800px;
    }
    .root > div > div {
        background-color: gray;
    }
</style>
{% endblock %}
{% block contents %}
<div class="view">{{ super() }}</div>
{% endblock %}
{% block root %}
<div class="root {{ root.name }}">{{ super() }}</div>
{% endblock %}
"""

def fig1():
    p = figure(width_policy="max", height=200, toolbar_location=None)
    p.scatter([1, 5, 10], [1, 5, 10])
    return p

def fig2():
    p = figure(width=300, height=200, toolbar_location=None)
    p.scatter([1, 5, 10], [1, 5, 10])
    return p

def fig(w, h):
    p = figure(width=w, height=h, toolbar_location=None)
    p.scatter([0, 5, 10], [0, 5, 10], radius=1)
    return p

f = lambda: fig(100, 100)

r0 = [
    Row(name="r00", children=[f(), f(), f(), f()], cols=100, width_policy="auto"),
    Row(name="r01", children=[f(), f(), f(), f()], cols=150, width_policy="auto"),
    Row(name="r02", children=[f(), f(), f(), f()], cols=200, width_policy="auto"),
    Row(name="r03", children=[f(), f(), f(), f()], cols=250, width_policy="auto"),

    Row(name="r10", children=[f(), f(), f(), f()], cols=100, width_policy="min"),
    Row(name="r11", children=[f(), f(), f(), f()], cols=150, width_policy="min"),
    Row(name="r12", children=[f(), f(), f(), f()], cols=200, width_policy="min"),
    Row(name="r13", children=[f(), f(), f(), f()], cols=250, width_policy="min"),

    Row(name="r20", children=[f(), f(), f(), f()], cols=100, width_policy="max"),
    Row(name="r21", children=[f(), f(), f(), f()], cols=150, width_policy="max"),
    Row(name="r22", children=[f(), f(), f(), f()], cols=200, width_policy="max"),
    Row(name="r23", children=[f(), f(), f(), f()], cols=250, width_policy="max"),

    Row(name="r30", children=[f(), f(), f(), f()], cols=100, width_policy="fixed", width=700),
    Row(name="r31", children=[f(), f(), f(), f()], cols=150, width_policy="fixed", width=700),
    Row(name="r32", children=[f(), f(), f(), f()], cols=200, width_policy="fixed", width=700),
    Row(name="r33", children=[f(), f(), f(), f()], cols=250, width_policy="fixed", width=700),
]

r1 = [
    Row(name="r00", children=[f(), f(), f(), f()], cols="auto", width_policy="auto"),
    Row(name="r01", children=[f(), f(), f(), f()], cols="auto", width_policy="auto"),
    Row(name="r02", children=[f(), f(), f(), f()], cols="auto", width_policy="auto"),
    Row(name="r03", children=[f(), f(), f(), f()], cols="auto", width_policy="auto"),

    Row(name="r10", children=[f(), f(), f(), f()], cols="auto", width_policy="min"),
    Row(name="r11", children=[f(), f(), f(), f()], cols="auto", width_policy="min"),
    Row(name="r12", children=[f(), f(), f(), f()], cols="auto", width_policy="min"),
    Row(name="r13", children=[f(), f(), f(), f()], cols="auto", width_policy="min"),

    Row(name="r20", children=[f(), f(), f(), f()], cols="auto", width_policy="max"),
    Row(name="r21", children=[f(), f(), f(), f()], cols="auto", width_policy="max"),
    Row(name="r22", children=[f(), f(), f(), f()], cols="auto", width_policy="max"),
    Row(name="r23", children=[f(), f(), f(), f()], cols="auto", width_policy="max"),

    Row(name="r30", children=[f(), f(), f(), f()], cols="auto", width_policy="fixed", width=700),
    Row(name="r31", children=[f(), f(), f(), f()], cols="auto", width_policy="fixed", width=700),
    Row(name="r32", children=[f(), f(), f(), f()], cols="auto", width_policy="fixed", width=700),
    Row(name="r33", children=[f(), f(), f(), f()], cols="auto", width_policy="fixed", width=700),
]

r2 = [
    Row(name="r00", children=[f(), f(), f(), f()], cols="min", width_policy="auto"),
    Row(name="r01", children=[f(), f(), f(), f()], cols="min", width_policy="auto"),
    Row(name="r02", children=[f(), f(), f(), f()], cols="min", width_policy="auto"),
    Row(name="r03", children=[f(), f(), f(), f()], cols="min", width_policy="auto"),

    Row(name="r10", children=[f(), f(), f(), f()], cols="min", width_policy="min"),
    Row(name="r11", children=[f(), f(), f(), f()], cols="min", width_policy="min"),
    Row(name="r12", children=[f(), f(), f(), f()], cols="min", width_policy="min"),
    Row(name="r13", children=[f(), f(), f(), f()], cols="min", width_policy="min"),

    Row(name="r20", children=[f(), f(), f(), f()], cols="min", width_policy="max"),
    Row(name="r21", children=[f(), f(), f(), f()], cols="min", width_policy="max"),
    Row(name="r22", children=[f(), f(), f(), f()], cols="min", width_policy="max"),
    Row(name="r23", children=[f(), f(), f(), f()], cols="min", width_policy="max"),

    Row(name="r30", children=[f(), f(), f(), f()], cols="min", width_policy="fixed", width=700),
    Row(name="r31", children=[f(), f(), f(), f()], cols="min", width_policy="fixed", width=700),
    Row(name="r32", children=[f(), f(), f(), f()], cols="min", width_policy="fixed", width=700),
    Row(name="r33", children=[f(), f(), f(), f()], cols="min", width_policy="fixed", width=700),
]

#save(r1, template=template)

from bokeh.models.widgets import Div

logo = """\
<a href="http://panel.pyviz.org">
    <img src="https://panel.pyviz.org/_static/logo_stacked.png" width="150" height="127" align="left" style="margin: 20px"></img>
</a>
"""
c = Column(children=[Div(text=logo), Div(text="<b>ABC</b><br><br><b>DEF</b>")])

save(c) #, template=template)
