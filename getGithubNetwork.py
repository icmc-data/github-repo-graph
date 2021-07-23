import os
import dotenv
import json
import argparse

from make.network.getDependencies import *

def setup():
	parser = argparse.ArgumentParser(description = 'Get Github network from a given repository, using Github GraphQL API')
	parser.add_argument('-r', '--repository', help = 'Repository name, like "pytorch/pytorch"', required=True)
	parser.add_argument('-o', '--out', help = 'Destination json filename', required=True)
	parser.add_argument('-d', '--depth', type=int, default=1, help='Depth of search')
	args = parser.parse_args()
	
	return args

def main():
	args = setup()
	dotenv.load_dotenv()
	token = os.environ.get('GITHUB_TOKEN')

	git = GithubGraph(token = token)
	owner, name = args.repository.split('/')
	jsonGraph = git.modelGithubRepoGraph(owner, name, depth = args.depth)

	jsonGraph = open("dataset/json/{}".format(args.out), "w")
	json.dump(git.json, jsonGraph, indent=4)
	jsonGraph.close()

if __name__ == '__main__':
	main()