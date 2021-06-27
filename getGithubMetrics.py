import json
import os
import networkx as nx

JSON_PATH = 'data/json/'

def main():

	# Grafo com depth 3
	with open(JSON_PATH + 'graph.json') as f:
		json_data = json.load(f)
		f.close()

	G = nx.DiGraph()
	G.add_nodes_from(
		node['id']
		for node in json_data['nodes']
	)

	G.add_edges_from(
		(link['source'], link['target'])
		for link in json_data['links']
	)

	print('Number of nodes: {}'.format(G.number_of_nodes()))
	print('Number of edges: {}'.format(G.number_of_edges()))

	print('\n\nDegree Centrality:')
	centralities = nx.degree_centrality(G)
	sorted_nodes = sorted(centralities, key = centralities.get, reverse=True)
	for i, node in enumerate(sorted_nodes[:10]):
		print("{}) {} - score {}".format(i+1, node, centralities[node]))

	print('\n\nEigenVector Centrality:')
	centralities = nx.eigenvector_centrality(G)
	sorted_nodes = sorted(centralities, key = centralities.get, reverse=True)
	for i, node in enumerate(sorted_nodes[:10]):
		print("{}) {} - score {}".format(i+1, node, centralities[node]))


if __name__ == '__main__':
	main()