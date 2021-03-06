import sqlite3
import json
import argparse

DEPENDENTS_QUERY = '''SELECT repo, dependent FROM dependents'''
FETCH_FULL_NAME_QUERY = '''SELECT full_name, stargazers_count FROM repos WHERE id = %s'''

class DependentsTable:
	def __init__(self, db):
		self.connection = sqlite3.connect(db)
		self.cursor = self.connection.cursor()
		self.repos = {}
		self.json_data = {"nodes": [], "links": []} 
	
	def to_json(self, out, minimum = 0):
		dependents = self.__fetchAllDependents()

		for repo_id, dependent_id in dependents:
			
			flag_repo = True
			if repo_id not in self.repos:
				flag_repo = self.__fetchRepoFullName(repo_id, minimum) 

			flag_dependent = True
			if dependent_id not in self.repos:
				flag_dependent = self.__fetchRepoFullName(dependent_id, minimum)
			
			if flag_dependent and flag_repo:
				self.json_data['links'].append(
				{'source': self.repos[repo_id],
				'target': self.repos[dependent_id]}
				)

		jsonGraph = open(out, "w")
		json.dump(self.json_data, jsonGraph, indent=4)
		jsonGraph.close()

	
	def __fetchAllDependents(self):
		self.cursor.execute(DEPENDENTS_QUERY)
		return self.cursor.fetchall()

	def __fetchRepoFullName(self, id, minimum) -> bool:
		self.cursor.execute(FETCH_FULL_NAME_QUERY % (id))
		repo_full_name, stars = self.cursor.fetchone()

		if stars >= minimum:
			self.json_data["nodes"].append(
				{"id": repo_full_name}
			)
			self.repos[id] = repo_full_name
			return True
		else:
			return False
	
	def __close(self):
		if self.connection:
			self.connection.commit()
			self.cursor.close()
			self.connection.close()
	
	def __enter__(self):
		return self
	
	def __exit__(self, ext_type, exc_value, traceback) -> None:
		self.__close()

def setup():
	parser = argparse.ArgumentParser(description = 'Get Github network json file, from a given sqlite database(github-to-sqlite)')
	parser.add_argument('-db', '--database', help = 'Sqlite database name', required=True)
	parser.add_argument('-s', '--stars', help = 'Minimum star count. 0 to add all repos to the network', required=True, type=int)
	parser.add_argument('-o', '--out', help = 'Destination json filename', required=True)
	args = parser.parse_args()
	
	return args


def main():
	args = setup()
	db_name = 'dataset/sqlite/' + args.database
	json_filename = 'dataset/json/' + args.out
	minimum = args.stars

	with DependentsTable(db_name) as db:
		db.to_json(json_filename, minimum)



if __name__ == "__main__":
	main()