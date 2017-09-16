var svg = d3.select("svg"),
margin = {top: 20, right: 20, bottom: 30, left: 50},
width = +svg.attr("width") - margin.left - margin.right,
height = +svg.attr("height") - margin.top - margin.bottom,
g = svg.append("g") .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleUtc()
  .rangeRound([0, width]);

var y = d3.scaleLinear()
  .rangeRound([height, 0]);

var line = d3.line()
  .x(function(d) { return x(d.date); })
  .y(function(d) { return y(d.bg); });

var parseTime = function(dateStr) {
  let time = dateStr.slice(1,-1).split(',').map(n => parseInt(n));
  return new Date(Date.UTC(2017,0,0,time[0],time[1]));
};

d3.json("/graph", function(d) {
  d.forEach(function(elem) {
      elem.date = parseTime(elem.date);
  });

  x.domain(d3.extent(d, function(d) { return d.date; }));
  y.domain(d3.extent(d, function(d) { return d.bg; }));

  g.append("g")
      .attr("transform", "translate(0," + height + ")")
      .attr("class","axis")
      .call(d3.axisBottom(x))
    .select(".domain")
      .remove();

  var yAxis = d3.axisLeft(y);
  g.append("g")
      .attr("class","axis")
      .call(yAxis)
    .append("text")
      .attr("fill", "#FFF")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Blood Glucose (mg/dl)");

  g.append("path")
      .datum(d)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("stroke-width", 1.5)
      .attr("d", line);

  d3.selectAll("text").attr("fill","#FFF");
});


