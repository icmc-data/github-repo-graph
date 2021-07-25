import requests

class GithubGraph:
	'''
	Grafo da rede do github.
	Atributos:
		token				Personal access token do Github para acessar a GraphQL API
		vertices			Lista contendo todos os vertices(nós)
		json				Dicionário contendo a estrutura do grafo em arquivo json.
	'''
	def __init__(self, token : str):
		self.token = token
		self.neighbors = []
		self.vertices = []
		self.json = {"nodes": [], "links": []}
	
	def getDependencies(self, owner : str, name : str, depth : int = 1, max = 20):
		query = '''
        {
          	repository(owner: "%s", name: "%s") {
            description
            dependencyGraphManifests(first: 50) {
              nodes {
                blobPath
                dependencies {
                  nodes {
                    packageName
                    repository {
                      name
                      owner {
                        login
                      }
                      primaryLanguage {
                        name
                      }
                    }
                    requirements
                    hasDependencies
                  }
                }
              }
            }
          }
        }
        '''
		seen = set()

		results = self.runQuery(query % (owner, name))
		for manifest in results['data']['repository']['dependencyGraphManifests']['nodes']:
			for dependencie in manifest['dependencies']['nodes']:
		
				dependencie['level'] = len(self.neighbors)

				if (dependencie['repository'] == None):
					continue

				if (dependencie['packageName'] in seen):
					continue

				seen.add(dependencie['packageName'])

				source = '{}/{}'.format(
					dependencie['repository']['owner']['login'],
					dependencie['repository']['name']
				)

				if (source not in self.vertices):
					self.json['nodes'].append(
						{"id": source}
					)
					self.vertices.append(source)

				self.json['links'].append(
					{"source": source, 
					"target": "{}/{}".format(owner, name),
					"value": 1}
				)

				if ((len(self.neighbors) + 1 < depth or depth == 0) and dependencie['hasDependencies'] == True):
					if source not in self.neighbors:
						self.neighbors.append(source)
						self.getDependencies(
							dependencie['repository']['owner']['login'],
							dependencie['repository']['name'],
							depth
						)
						self.neighbors.pop()
	
	def runQuery(self, query : str) -> dict:
		headers = {
			"Authorization": "Bearer {}".format(self.token),
			"Accept": "application/vnd.github.hawkgirl-preview+json"
		}

		resp = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
		if resp.status_code == 200:
			return resp.json()
		else:
			raise Exception("Falha na query. Retornou erro de código {}. Query: {}\n".format(resp.status_code, query))
	
	def modelGithubRepoGraph(self, owner, name, depth = 1):
		self.json['nodes'].append(
			{"id": "{}/{}".format(owner, name)}
		)
		self.vertices.append("{}/{}".format(owner, name))

		self.getDependencies(owner, name, depth)

		return self.json