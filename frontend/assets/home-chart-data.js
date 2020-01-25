const yLabels = {
  0: 'This is fine. Everything is fine.',
  1: 'What\'s refactoring?',
  2: 'Script kiddie',
  3: 'Copied source from StackOverflow',
  4: '> has algos TA on team',
  5: 'Beaucoup bucks baby',
  6: 'Too many frameworks',
  7: 'Chaos reigns again',
  8: '; DROP TABLE users;',
  9: 'Vodka + RAM',
  10: 'It\'s tomorrow\'s problem',
}
export const homeChartData = {
  type: 'line',
  data: {
    labels: [
      'Missing semicolon',
      'Unreachable code',
      '\'foo\' + + \'foo\' = \'fooNaN\'',
      'Thresafead probty lems',
      'Wrote merge sort, no tears',
      'Solved the Halting problem',
      'Undefined is not a function',
      'Race conditions',
      'SQL Injection exploited',
      'What\'s that burning smell? ',
      'Woohoo!'
    ],
    datasets: [{ // one line graph
      data: [45, 40, 35, 26, 10, 97, 50, 20, 13, 5, 1],
      backgroundColor: ['rgba(255, 255, 255, .25)'],
      borderColor: ['#FFFFFF'],
      borderWidth: 3,
      pointRadius: 5,
      pointBackgroundColor: 'white',
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(239,83,80, 0.7)',
      pointHoverBorderColor: 'rgba(239,83,80, 0.7)',
    }, ]
  },
  options: {
    responsive: true,
    lineTension: 50,
    maintainAspectRatio: false,
    tooltips: {
      mode: 'index',
      axis: 'x',
      intersect: false,
      enabled: true,
      callbacks: {
        title: function (tooltipItem, data) {
          return data['labels'][tooltipItem[0]['index']];
        },
        label: function (tooltipItem, data) {
          var index = [tooltipItem['index']];
          return yLabels[index];
        }
      },
      backgroundColor: 'rgba(255, 255, 255, 0.7)',
      titleFontSize: 14,
      titleFontColor: 'rgba(239,83,80, 0.7)',
      titleFontFamily: "Share Tech Mono",
      titleFontStyle: 'bold',
      bodyFontColor: '#616161',
      bodyFontSize: 13,
      bodyFontFamily: "Share Tech Mono",
      displayColors: false,
      cornerRadius: 4,
      borderColor: '#FFFFFF',
      borderWidth: '2',
    },
    hover: {
      mode: 'nearest',
      intersect: false
    },
    legend: {
      display: false,
    },
    scales: {
      yAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Programming Skill',
          fontColor: "white",
          fontFamily: "Share Tech Mono",
          fontStyle: 'bold',
          fontSize: '24',
        },
        ticks: {
          callback: function (value, index, values) {
            return yLabels[value];
          },
          beginAtZero: true,
          padding: 15,
          fontColor: "white",
          fontFamily: "Share Tech Mono",
          fontStyle: 'bold',
          fontSize: '16',
          display: false,
          max: 100,
        },
        gridLines: {
          color: 'rgba(255, 255, 255, 0.1)',
          display: true,
          zeroLineColor: '#FFFFFF',
          zeroLineWidth: 3,
        }
      }],
      xAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Shots Taken',
          fontColor: "white",
          fontFamily: "Share Tech Mono",
          fontStyle: 'bold',
          fontSize: '24',
        },
        ticks: {
          callback: function (value, index, values) {
            return index;
          },
          beginAtZero: true,
          padding: 15,
          fontColor: "white",
          fontFamily: "Share Tech Mono",
          fontStyle: 'bold',
          fontSize: '16',
          max: 12,
        },
        gridLines: {
          color: 'rgba(255, 255, 255, 0.1)',
          display: true,
          zeroLineColor: '#FFFFFF',
          zeroLineWidth: 3,
        }
      }]
    }
  }
}

export default homeChartData;
