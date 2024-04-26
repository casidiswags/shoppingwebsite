from chartit import DataPool, Chart

def sales_chart(request):
    # Data source
    ds = DataPool(
        series=[{
            'options': {
                'source': Sales.objects.all()
            },
            'terms': [
                'date',
                'amount'
            ]
        }]
    )

    # Chart object
    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'line',
                'stacking': False
            },
            'terms': {
                'date': ['amount']
            }
        }],
        chart_options={
            'title': {
                'text': 'Sales Trend'
            },
            'xAxis': {
                'title': {
                    'text': 'Date'
                }
            }
        }
    )

    return render(request, 'sales_chart.html', {'cht': cht})
