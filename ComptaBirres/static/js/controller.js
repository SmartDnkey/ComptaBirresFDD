
let dataBirres = [];
let updateInterval = 5000;
let dps = [];
let chart;

function actualitzarDadesTotals() {

    let xhttp = new XMLHttpRequest();

  	xhttp.onreadystatechange = function() {

		if (this.readyState == 4 && this.status == 200) {

			if(document.getElementById("totalBirres").innerText != this.responseText){
				document.getElementById("totalBirres").innerText = this.responseText;
			}
		}
  	};

  	xhttp.open("GET", "/api/totalBirres/", true);
  	xhttp.send();

}

function totalBirresPeriodic() {
	setInterval(function() {actualitzarDadesTotals();},1000)
}

function renderChart() {
	chart = new CanvasJS.Chart("chartContainer", {

		title: {
			text: "Evolució del Consum"
		},
		axisY: {
			includeZero: false

		},
		data: [{
			type: "column",
			color: "firebrick",
			dataPoints: dps,
			indexLabel: "{y}",
			indexLabelPlacement: "outside",
        	indexLabelOrientation: "horizontal",
		}],
		backgroundColor: "white",
	});
}

function updateData() {

    let xhttp = new XMLHttpRequest();

  	xhttp.onreadystatechange = function() {

		if (this.readyState == 4 && this.status == 200) {

			dataBirres = JSON.parse(this.responseText);

		}

  	};

  	xhttp.open("GET", "/api/dataBirres/", true);
  	xhttp.send();

}


function updateChart() {

	updateData();

	dps = [
			{ y: dataBirres[10][0], label: "10:00" },
			{ y: dataBirres[10][1], label: "10:15" },
			{ y: dataBirres[10][2], label: "10:30" },
			{ y: dataBirres[10][3], label: "10:45" },

			{ y: dataBirres[11][0], label: "11:00" },
			{ y: dataBirres[11][1], label: "11:15" },
			{ y: dataBirres[11][2], label: "11:30" },
			{ y: dataBirres[11][3], label: "11:45" },

			{ y: dataBirres[12][0], label: "12:00" },
			{ y: dataBirres[12][1], label: "12:15" },
			{ y: dataBirres[12][2], label: "12:30" },
			{ y: dataBirres[12][3], label: "12:45" },

			{ y: dataBirres[13][0], label: "13:00" },
			{ y: dataBirres[13][1], label: "13:15" },
			{ y: dataBirres[13][2], label: "13:30" },
			{ y: dataBirres[13][3], label: "13:45" },

			{ y: dataBirres[14][0], label: "14:00" },
			{ y: dataBirres[14][1], label: "14:15" },
			{ y: dataBirres[14][2], label: "14:30" },
			{ y: dataBirres[14][3], label: "14:45" },

			{ y: dataBirres[15][0], label: "15:00" },
			{ y: dataBirres[15][1], label: "15:15" },
			{ y: dataBirres[15][2], label: "15:30" },
			{ y: dataBirres[15][3], label: "15:45" },

			{ y: dataBirres[16][0], label: "16:00" },
			{ y: dataBirres[16][1], label: "16:15" },
			{ y: dataBirres[16][2], label: "16:30" },
			{ y: dataBirres[16][3], label: "16:45" },

			{ y: dataBirres[17][0], label: "17:00" },
			{ y: dataBirres[17][1], label: "17:15" },
			{ y: dataBirres[17][2], label: "17:30" },
			{ y: dataBirres[17][3], label: "17:45" },

			{ y: dataBirres[18][0], label: "18:00" },
			{ y: dataBirres[18][1], label: "18:15" },
			{ y: dataBirres[18][2], label: "18:30" },
			{ y: dataBirres[18][3], label: "18:45" },

			{ y: dataBirres[19][0], label: "19:00" },
			{ y: dataBirres[19][1], label: "19:15" },
			{ y: dataBirres[19][2], label: "19:30" },
			{ y: dataBirres[19][3], label: "19:45" }
		]
	renderChart();
	chart.render();
};

function autoLoadChart(){

	setInterval(function(){updateChart()}, updateInterval);

}






