title: Self Management
date: 2019-04-11



### 1. [Skill Tree](https://github.com/TeamStuQ/skill-map)

<div id="skillTree" style="width:100%;"></div>
<script type="text/javascript">
    var myChartContainer = document.getElementById('skillTree');

    var resizeContainer = function () {
        myChartContainer.style.height = window.innerHeight+'px';
    };
    resizeContainer();
    var myChart = echarts.init(myChartContainer);
    myChart.showLoading();
    
    $.get('../doc/skillTree.json', function (data) {
        myChart.hideLoading();
    
        myChart.setOption(option = {
            tooltip: {
                trigger: 'item',
                triggerOn: 'mousemove'
            },
            series: [
                {
                    type: 'tree',
    
                    data: [data],
    
                    top: '1%',
                    left: '10%',
                    bottom: '1%',
                    right: '25%',
    
                    symbolSize: 7,
    
                    label: {
                        normal: {
                            position: 'left',
                            verticalAlign: 'middle',
                            align: 'right',
                            fontSize: 12
                        }
                    },
    
                    leaves: {
                        label: {
                            normal: {
                                position: 'right',
                                verticalAlign: 'middle',
                                align: 'left',
                                fontSize: 12
                            }
                        }
                    },
    
                    expandAndCollapse: true,
                    animationDuration: 550,
                    animationDurationUpdate: 750
                }
            ]
        });
    });
    
    window.onresize = function () {
        resizeContainer();
        myChart.resize();
    };
</script>

### 2. Weekly Schedule

<br />

<table style="width: 100%;font-size: 13px;line-height:24px;">
<thead>
<tr>
<th align="center">Slot</th>
<th align="center">Sunday</th>
<th align="center">Monday</th>
<th align="center">Tuesday</th>
<th align="center">Wednesday</th>
<th align="center">Thursday</th>
<th align="center">Friday</th>
<th align="center">Saturday</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">06:00</td>
<td align="center">getup</td>
<td align="center">getup</td>
<td align="center">getup</td>
<td align="center">getup</td>
<td align="center">getup</td>
<td align="center">getup</td>
<td align="center">getup</td>
</tr>
<tr>
<td align="center">06:30</td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
</tr>
<tr>
<td align="center">07:00</td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
</tr>
<tr>
<td align="center">07:30</td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
<td align="center"><span style="color: blue"><strong>Java</strong></span></td>
</tr>
<tr>
<td align="center">08:00</td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
</tr>
<tr>
<td align="center">08:30</td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
</tr>
<tr>
<td align="center">09:00</td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"><span style="color: red"><strong>Algorithms</strong></span></td>
</tr>
<tr>
<td align="center">09:30</td>
<td align="center">OTR</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">10:00</td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">10:30</td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">11:00</td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">11:30</td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">12:00</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
</tr>
<tr>
<td align="center">12:30</td>
<td align="center"></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
</tr>
<tr>
<td align="center">13:00</td>
<td align="center"></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
<td align="center"><span style="color: green"><strong>AI</strong></span></td>
</tr>
<tr>
<td align="center">13:30</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">14:00</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">14:30</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">15:00</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">15:30</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">16:00</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">16:30</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">17:00</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">17:30</td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">18:00</td>
<td align="center"></td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
</tr>
<tr>
<td align="center">18:30</td>
<td align="center"></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"></td>
<td align="center">OTR</td>
</tr>
<tr>
<td align="center">19:00</td>
<td align="center"></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"></td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
</tr>
<tr>
<td align="center">19:30</td>
<td align="center"></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"></td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
</tr>
<tr>
<td align="center">20:00</td>
<td align="center"></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"><span style="color: orange"><strong>Cloud</strong></span></td>
<td align="center"></td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
</tr>
<tr>
<td align="center">20:30</td>
<td align="center"></td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center">OTR</td>
<td align="center"></td>
<td align="center"><span style="color: red"><strong>Security</strong></span></td>
</tr>
<tr>
<td align="center">21:00</td>
<td align="center"></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"></td>
<td align="center">OTR</td>
</tr>
<tr>
<td align="center">21:30</td>
<td align="center"></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">22:00</td>
<td align="center"></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"><span style="color: purple"><strong>Big Data</strong></span></td>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">22:30</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
<td align="center">SHW</td>
</tr>
</tbody>
</table>

