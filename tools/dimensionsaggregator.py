from fieldaggregator import FieldAggregator
import plotly.plotly as py
import plotly.graph_objs as go

class DimensionsAggregator(FieldAggregator):

	def normalise_value(self, value):
		return value.replace(" ","")

dimensions_aggregator = DimensionsAggregator()
aggregated_fields = dimensions_aggregator.aggregate_field("/Users/danielneedham/tmp/sample/anatomy/publications.csv","dimensions")

labels = aggregated_fields.keys()
values = aggregated_fields.values()

'''fig = {
    'data': [{'labels': labels,
              'values': values,
              'type': 'bar'}],
    'layout': {'title': 'Publication dimensions'}
     }'''
data = [go.Bar(
        x=labels,
        y=values
)]

py.plot(data)

		
