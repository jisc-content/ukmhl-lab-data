from fieldaggregator import FieldAggregator
import plotly.plotly as py
import plotly.graph_objs as go

class PublicationPlaceAggregator(FieldAggregator):

	def normalise_value(self, value):
		return value.lstrip().rstrip()

publication_place_aggregator = PublicationPlaceAggregator()
aggregated_fields = publication_place_aggregator.aggregate_field("/Users/danielneedham/tmp/sample/anatomy/publications.csv","publication places")

labels = aggregated_fields.keys()
values = aggregated_fields.values()

fig = {
    'data': [{'labels': labels,
              'values': values,
              'type': 'pie'}],
    'layout': {'title': 'Publication places'}
     }


py.plot(fig)
		
