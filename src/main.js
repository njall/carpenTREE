var fs = require("fs");

var content = fs.readFileSync("../example_json_format.json");
console.log("Output Content : \n"+ content);


var node_graph = {
    nodes: [
            { data: { id: 'j', name: 'Jerry' } },
            { data: { id: 'e', name: 'Elaine' } },
            { data: { id: 'k', name: 'Kramer' } },
            { data: { id: 'g', name: 'George' } }
        ],
    edges: [
        { data: { source: 'j', target: 'e' } },
        { data: { source: 'j', target: 'k' } },
        { data: { source: 'j', target: 'g' } },
        { data: { source: 'e', target: 'j' } },
        { data: { source: 'e', target: 'k' } },
        { data: { source: 'k', target: 'j' } },
        { data: { source: 'k', target: 'e' } },
        { data: { source: 'k', target: 'g' } },
        { data: { source: 'g', target: 'j' } }
    ]
}

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