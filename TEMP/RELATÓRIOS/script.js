const ctx = document.getElementById('graficoPizza').getContext('2d');
const graficoPizza = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['competência 1', 'competência 2', 'competência 3', 'competência 4', 'competência 5'],
    datasets: [{
      label: 'Desempenho',
      data: [20, 20, 20, 20, 20],
      backgroundColor: ['#ffb380', '#ff9933', '#cc5200', '#ff751a', '#ffa64d'],
      borderColor: '#2a1035',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: false
      }
    }
  }
});
