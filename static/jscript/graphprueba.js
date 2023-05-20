// Datos iniciales
var data1 = [{
    name: 'Hombres',
    y: 60
  }, {
    name: 'Mujeres',
    y: 40
  }];
  var data2 = [{
    name: 'Sin Discapacidad',
    y: 96
  }, {
    name: 'Con Discapacidad',
    y: 4
  }];
  
  
  // Configuración del gráfico
  var chart = Highcharts.chart('container', {
    title: {
      text: 'Poblacion De El Salvador'
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
      type: 'pie',
      name: 'Datos 1',
      data: data1
    }]
  });
  
  //const selectElement = document.querySelector("#dataSelect");
  // Cambio de datos al seleccionar una opción del combobox
  document.getElementById('dataSelect').addEventListener('change', function(events){
    var selectedValue = this.value;
    var newData;
    const resultado = document.querySelector('.resultado');
    switch (selectedValue) {
      case '1':
        newData = data1;
        break;
      case '2':
        newData = data2;
        break;
      case '3':
        newData = data3;
        break;
    }
  
    chart.series[0].setData(newData);

    chart.update({
        series: [{
          data: newData
        }]
      });

  });
  
  //Gráfico de pastel con datos cambiantes
  //Pie chart with 4 slices.
  
