// datos iniciales del gráfico
/*var data1 = [
    ['Manzanas', 5],
    ['Naranjas', 3],
    ['Plátanos', 4]
  ];
  var data2 = [
    ['Manzanas', 3],
    ['Naranjas', 7],
    ['Plátanos', 2]
  ];
  var data3 = [
    ['Manzanas', 2],
    ['Naranjas', 2],
    ['Plátanos', 6]
  ];
  */

  // opciones del gráfico
  var datos = '{{ datos|safe }}';
  var datosjson = JSON.parse('{{ datos|safe }}');
  console.log(datosjson.data1);


  var options = {
    chart: {
      type: 'pie'
    },
    series: [{
      name: 'Frutas',
      data: datosjson.data1
    }],

    title: {
      text: 'Frutas'
    }
  }
  
  // crea el gráfico
  var chart = Highcharts.chart('container', options);
 
  
  // función para actualizar el gráfico
  function updateChart() {
    var selectedOption = document.getElementById('dataSelect').value;
    
    // actualiza los datos del gráfico según la opción seleccionada
    /*if (selectedOption === '1') {
      chart.series[0].setData(data1);
    } else if (selectedOption === '2') {
      chart.series[0].setData(data2);
    } else if (selectedOption === '3') {
      chart.series[0].setData(data3);
    }*/

    

    switch (selectedOption) {
      case '1':
        chart.series[0].setData(datosjson.data1);
        break;
      case '2':
        chart.series[0].setData(datosjson.data2);
        break;
      case '3':
        chart.series[0].setData(datosjson.data3);
        break;
    }

  }
  
  // ejecuta la función updateChart cada vez que se cambia la opción seleccionada
  document.getElementById('dataSelect').addEventListener('change', updateChart);
