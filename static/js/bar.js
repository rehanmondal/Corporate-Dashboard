window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Our Progress"
	},
	axisY: {
		title: "Sales"
	},
	data: [{
		type: "column",
		showInLegend: true,
		legendMarkerColor: "grey",
		legendText: "Projects - Leads",
		dataPoints: [
			{ y: 300878, label: "ML & AI" },
			{ y: 266455,  label: "Cloud" },
			{ y: 169709,  label: "Data" },
			{ y: 158400,  label: "Software" },
			{ y: 242503,  label: "Android" },
			{ y: 101500, label: "Web Application" },
			{ y: 121500,  label: "UI/UX" },
			{ y: 80000,  label: "Domain & Hosting" }
		]
	}]
});
chart.render();

}