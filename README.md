# github-repo-graph
Transformar o github num grafo, realizar processos de aprendizado e exploração e, posteriormente, visualização.

```
.
├── data/               <- dataset
│   
└── scraping/
    ├── features/       <- scrapping das features
    └── network/        <- scrapping da rede(dependências e dependentes)
```
## Step 0 - Installing requirements

1. Clone this repo
2. Create a virtual environment (I use [`venv`](https://docs.python.org/3/library/venv.html))
3. Activate your environment: `$ source [ENVIRONMENT_NAME]/bin/activate`
4. Install dependencies: `$ pip install -r requirements.txt`
5. Have a Github personal token (generate here: https://github.com/settings/tokens) to insert on Makefile