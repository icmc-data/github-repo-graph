import json
import networkx as nx

JSON_PATH = 'dataset/json/'

def main():

	with open(JSON_PATH + 'depth2.json') as f:
		json_data = json.load(f)

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



if __name__ == '__main__':
	main()