# github-repo-graph
Transform the dependency relationships between repositories into a graph and then perform exploratory data analysis and visualization. See this [blogpost](https://mostra-de-projetos-data.netlify.app/#popup-github-graph), in portuguese, for more details.

```
.
│
├── dataset/
|    ├── sqlite/        <- sqlite github database
|    └── json/          <- network as json files
|
├── notebooks/          <- Jupyter notebooks
|          
└── make/
    ├── features/       <- features getter
    └── network/        <- network getter (dependencies)
```
## Step 0 - Installing requirements

1. Clone this repo
2. Create a virtual environment ([`venv`](https://docs.python.org/3/library/venv.html))
3. Activate your environment: `$ source [ENVIRONMENT_NAME]/bin/activate`
4. Install dependencies: `$ pip install -r requirements.txt`
5. Have a Github personal token (generate [here](https://github.com/settings/tokens)) to insert on .env

## Using the repo

There are mainly 2 Python Scripts, one network visualization using D3.js and some EDA on a jupyter notebook.

### Fetching dependencies of a repository to a JSON file

Run this command:

```
$ python3 getGithubNetwork.py -r [REPO_NAME] -o [JSON_FILENAME] -d [DEPTH]
```

This script uses GitHub GraphQL API and a Depth Limited Search(DLS) to fetch dependencies until reach the depth limit. 

If you give `--depth 0`, then the script will try to find all dependencies, as far down as they go.

The Json file will be availabe at `dataset/json/` directory.

### Converting network from github-to-sqlite database to a JSON file

Initially you need to buil a database using **[github-to-sqlite](https://github.com/dogsheep/github-to-sqlite)**. Originally only the `scrape-dependents` script is available in the original repository. Our script to get dependencies was added on this forked [repository](https://github.com/AlvaroJoseLopes/github-to-sqlite)

Run this command:

```
$ python3 getNetworkFromSqlite.py -db [DATABASE_NAME] -s [MINIMUM_STARS] -o [JSON_FILENAME]
```

This script fetch a network from **dependents** table and convert it to a JSON file. The `--stars` parameter indicates the minimum number of stars that a repository must have in order to be added to the network.

If you provide `--stars 0`, then the script will add all repositories to the network.

The Json file will be availabe at `dataset/json/` directory.

### D3.js Visualization

D3.js was used to view a sample of the network. You can see [here](https://bl.ocks.org/AlvaroJoseLopes/a93e54ea8e61380d3cba9ea52a9e6e08) or opening `index.html` on a local host.

### EDA

The `notebooks/` contains some jupyter notebooks with some Exploratory Data Analysis.
