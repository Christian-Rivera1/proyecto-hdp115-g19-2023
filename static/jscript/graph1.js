var data1 = [{name : 'Hombres', y : 61}, { name : 'Mujeres' , y : 39}];
    var data2 = [{name : 'Sin Discapacidad', y : 75}, { name : 'Con Discapacidad' , y : 25}];
    Highcharts.chart('container', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Poblacion De el Salvador',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Pobalcion de El Salvador',
        colorByPoint: true,
        type: 'pie',
        data: data1
    }],

    events: {
            load: function () {
              document.getElementById('dataSelect').addEventListener('change', function() {
              var selectedValue = this.value;
              var newData;

              switch (selectedValue) {
                case '1':
                  newData = data1;
                  break;
                case '2':
                  newData = data2;
                  break;
              }
              chart.update({
                series: [{
                  data: newData
                }]
              });
            });   
          }
        }
  });

  const selecciones = document.querySelector('#dataSelect').value;

  console.log(selecciones)

  /*document.getElementById('dataSelect').addEventListener('change', function() {
  var selectedValue = this.value;
  var newData;

  switch (selectedValue) {
    case '1':
      newData = data1;
      break;
    case '2':
      newData = data2;
      break;
  }
  chart.update({
    series: [{
      data: newData
    }]
  });

  
  
});*/
