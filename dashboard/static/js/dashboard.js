// --------------------------SPLINE CHART--------------------
var splineChartOptions = {
  series: [{
  name: 'National Clients',
  data: [7832, 7100, 7380, 7412, 8342, 7950, 8900, 8172, 8500, 8000, 8900, 8912]
}, {
  name: 'International',
  data: [1080, 1812, 1532, 1500, 570, 962, 12, 742, 412, 912, 900, 900]
}],
  chart: {
  height: 290,
  type: 'area',
  toolbar: {
    show: false
  },
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
xaxis: {
  type: 'category',
  categories: ['Jan', 'Febr', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sept','Oct','Nov','Dec'] // Replace datetime values with month names
},
tooltip: {
  x: {
    format: 'dd/MM/yy HH:mm'
  },
},
};

var chart = new ApexCharts(document.querySelector("#spline-area-chart"), splineChartOptions);
chart.render();

//---------------------------- BAR COLUMN CHART1-----------------------
var reclamation = {
  series: [{
  name: 'Reclamation percentage',
  data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
}],
  chart: {
  height: 350,
  type: 'bar',
  toolbar: {
    show: false
  },
},
plotOptions: {
  bar: {
    borderRadius: 10,
    dataLabels: {
      position: 'top', // top, center, bottom
    },
  }
},
dataLabels: {
  enabled: true,
  formatter: function (val) {
    return val + "%";
  },
  offsetY: -20,
  style: {
    fontSize: '12px',
    colors: ["#304758"]
  }
},

xaxis: {
  categories: [
    "Finance",
    "Maintenance",
    "Production Manager",
    "Sales Representative",
    "Customer Service",
    "Human Ressources",
    "Marketing",
    "Warehouse Supervisor",
    "IT Support Specialist",
    "Shipping Coordinator",
    "Administrative Assistant",
    "Operations Manager"
],
  position: 'top',
  axisBorder: {
    show: false
  },
  axisTicks: {
    show: false
  },
  crosshairs: {
    fill: {
      type: 'gradient',
      gradient: {
        colorFrom: '#D8E3F0',
        colorTo: '#BED1E6',
        stops: [0, 100],
        opacityFrom: 0.4,
        opacityTo: 0.5,
      }
    }
  },
  tooltip: {
    enabled: true,
  }
},
yaxis: {
  axisBorder: {
    show: false
  },
  axisTicks: {
    show: false,
  },
  labels: {
    show: false,
    formatter: function (val) {
      return val + "%";
    }
  }

},
title: {
  text: 'Complaints Per Role',
  floating: true,
  offsetY: 330,
  align: 'center',
  style: {
    color: '#444'
  }
}
};

var chart = new ApexCharts(document.querySelector("#reclamation-chart"), reclamation);
chart.render();
//---------------------------- BAR COLUMN CHART2-----------------------
var conge = {
  series: [{
  name: 'Holidays Demands Percentage',
  data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
}],
  chart: {
  height: 350,
  type: 'bar',
  toolbar: {
    show: false
  },
},
plotOptions: {
  bar: {
    borderRadius: 10,
    dataLabels: {
      position: 'top', // top, center, bottom
    },
  }
},
dataLabels: {
  enabled: true,
  formatter: function (val) {
    return val + "%";
  },
  offsetY: -20,
  style: {
    fontSize: '12px',
    colors: ["#304758"]
  }
},

xaxis: {
  categories: ['Jan', 'Febr', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sept','Oct','Nov','Dec'] ,
  position: 'top',
  axisBorder: {
    show: false
  },
  axisTicks: {
    show: false
  },
  crosshairs: {
    fill: {
      type: 'gradient',
      gradient: {
        colorFrom: '#D8E3F0',
        colorTo: '#BED1E6',
        stops: [0, 100],
        opacityFrom: 0.4,
        opacityTo: 0.5,
      }
    }
  },
  tooltip: {
    enabled: true,
  }
},
yaxis: {
  axisBorder: {
    show: false
  },
  axisTicks: {
    show: false,
  },
  labels: {
    show: false,
    formatter: function (val) {
      return val + "%";
    }
  }

},
title: {
  text: 'Holidays Demands Per Month',
  floating: true,
  offsetY: 330,
  align: 'center',
  style: {
    color: '#444'
  }
}
};

var chart = new ApexCharts(document.querySelector("#conge-chart"), conge);
chart.render();
//---------------------------- HORIZONTAL BAR -------------------------
var horiz = {
  series: [{
    name: 'Years of partnership',
    data: [4, 3, 8, 5, 1, 1]
}],
  chart: {
  type: 'bar',
  height: 350,
  toolbar: {
    show: false
  },
},
plotOptions: {
  bar: {
    borderRadius: 4,
    horizontal: true,
  }
},
dataLabels: {
  enabled: false
},
xaxis: {
  categories: ['Versace', 'John Deere', 'Rennegemeinschaft Wipptal', 'Sober', 'Tunisian Armed Forces', 'The Ministry of Natonal Defence'
  ],
}
};

var chart = new ApexCharts(document.querySelector("#basic-barchar"), horiz);
chart.render();
//---------------------------- DONUT BAR -------------------------
var don = {
  series: [43, 5, 3, 2, 4],
  chart: {
  height: 390,
  type: 'radialBar',
},
plotOptions: {
  radialBar: {
    offsetY: 0,
    startAngle: 0,
    endAngle: 180,
    hollow: {
      margin: 5,
      size: '30%',
      background: 'transparent',
      image: undefined,
    },
    dataLabels: {
      name: {
        show: false,
      },
      value: {
        show: false,
      }
    }
  }
},
colors: ['#1ab7ea', '#0084ff', '#39539E'],
labels: [
  "Embroidery",
  "Maintenance",
  "Finance",
  "Human Ressources",
  "IT",
],
legend: {
  show: true,
  floating: true,
  fontSize: '10px',
  position: 'left',
  offsetX: 100,
  offsetY: 15,
  labels: {
    useSeriesColors: true,
  },
  markers: {
    size: 0
  },
  formatter: function(seriesName, opts) {
    return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
  },
  itemMargin: {
    vertical: 1
  }
},
responsive: [{
  breakpoint: 480,
  options: {
    legend: {
        show: false
    }
  }
}]
};

var chart = new ApexCharts(document.querySelector("#donut-char"), don);
chart.render();