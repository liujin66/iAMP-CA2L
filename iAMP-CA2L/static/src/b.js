var csvData = document.getElementById('csv').innerHTML;
var lines = csvData.split('\n');
// 遍历每一行
Highcharts.each(lines, function (line, lineNo) {
    var items = line.split(',');
    // 处理第一行，即分类
    if (lineNo === 0) {
        Highcharts.each(items, function (item, itemNo) {
            if (itemNo > 0) {
                options.xAxis.categories.push(item);
            }
        });
    }
    // 处理其他的每一行
    else {
        var series = {
            data: []
        };
        Highcharts.each(items, function (item, itemNo) {
            if (itemNo === 0) {
                series.name = item;   // 数据列的名字
            } else {
                series.data.push(parseFloat(item)); // 数据，记得转换成数值类型
            }
        });
        // 最后将数据 push 到数据列配置里
        options.series.push(series);
    }
});