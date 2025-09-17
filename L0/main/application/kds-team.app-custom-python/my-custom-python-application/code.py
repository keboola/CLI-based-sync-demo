from keboola.component import CommonInterface
ci = CommonInterface()
# access user parameters
print(ci.configuration.parameters)
print(ci.configuration.parameters['#passwordk'].split('a'))