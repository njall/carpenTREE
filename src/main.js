
var node_graph = {"nodes": [{"data": {"name": "Loops", "id": "http://swcarpentry.github.io/shell-novice/05-loop/index.html"}},
{"data": {"id": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html", 
    "name": "Looping Data Sets"}},
{"data": {"name": "Running and Quitting", "id": "http://swcarpentry.github.io/01-run-quit/index.html"}}, {"data": {"name": "Variables and Assignment", "id": "http://swcarpentry.github.io/02-variables/index.html"}}, {"data": {"name": "Data Types and Type Conversion", "id": "http://swcarpentry.github.io/03-types-conversion/index.html"}}, {"data": {"name": "Built-in Functions and Help", "id": "http://swcarpentry.github.io/04-built-in/index.html"}}, {"data": {"name": "Libraries", "id": "http://swcarpentry.github.io/06-libraries/index.html"}}, {"data": {"name": "Reading Tabular Data into DataFrames", "id": "http://swcarpentry.github.io/07-reading-tabular/index.html"}}, {"data": {"name": "Pandas DataFrames", "id": "http://swcarpentry.github.io/08-data-frames/index.html"}}, {"data": {"name": "Plotting", "id": "http://swcarpentry.github.io/09-plotting/index.html"}}, {"data": {"name": "Lists", "id": "http://swcarpentry.github.io/11-lists/index.html"}}, {"data": {"name": "For Loops", "id": "http://swcarpentry.github.io/12-for-loops/index.html"}}, {"data": {"name": "Looping Over Data Sets", "id": "http://swcarpentry.github.io/13-looping-data-sets/index.html"}}, {"data": {"name": "Writing Functions", "id": "http://swcarpentry.github.io/14-writing-functions/index.html"}}, {"data": {"name": "Variable Scope", "id": "http://swcarpentry.github.io/15-scope/index.html"}}, {"data": {"name": "Conditionals", "id": "http://swcarpentry.github.io/17-conditionals/index.html"}}, {"data": {"name": "Programming Style", "id": "http://swcarpentry.github.io/18-style/index.html"}}, {"data": {"name": "Wrap-Up", "id": "http://swcarpentry.github.io/19-wrap/index.html"}}, {"data": {"name": "Feedback", "id": "http://swcarpentry.github.io/20-feedback/index.html"}}], "edges": [{"data": {"source": "http://swcarpentry.github.io/shell-novice/05-loop/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/01-run-quit/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/02-variables/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/03-types-conversion/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/04-built-in/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/06-libraries/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/07-reading-tabular/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/08-data-frames/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/09-plotting/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/11-lists/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/12-for-loops/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/13-looping-data-sets/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/14-writing-functions/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/15-scope/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/17-conditionals/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/18-style/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/19-wrap/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}, {"data": {"source": "http://swcarpentry.github.io/20-feedback/index.html", "target": "http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html"}}]}

document.addEventListener('DOMContentLoaded', function(){
    var cy = window.cy = cytoscape({
        container: document.getElementById('cy'),
        layout: {
        name: 'grid',
        rows: 2,
        cols: 2
        },

        style: [
        {
            selector: 'node[name]',
            style: {
            'content': 'data(name)'
            }
        },
        {
            selector: 'edge',
            style: {
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle'
            }
        }
        ],

        elements: node_graph
    });
});