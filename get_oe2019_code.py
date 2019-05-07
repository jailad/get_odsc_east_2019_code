"""
Pre-requisites:
    * git should be installed
    * requests module should be installed
        * pip install requests

Running the script:
    * python get_oe2019_code.py
"""
import os
import requests

CODE_PARENT_NAME = "ODSC_EAST_2019_CODE"

REPOS = [
    "https://github.com/tdpetrou/integrating-pandas-with-scikit-learn",
    "https://github.com/Calysto/conx-notebooks/tree/master/collections/odsc-2018",
    "https://github.com/lukas/ml-class",
    "https://github.com/amueller/ml-workshop-1-of-4",
    "https://github.com/jaredlander/LearningR",
    "https://github.com/matthewbrems/missing-data-workshop",
    "https://github.com/matthewbrems/data-viz-workshop",
    "https://github.com/amueller/ml-workshop-2-of-4",
    "https://github.com/bentoayr/Graph-Matching-Tutorial",
    "https://github.com/newfront/odsc-east-realish-predictions",
    "https://github.com/rajshah4/inter_workshop",
    "https://github.com/rerickson-usgs/OSDC-East-2019",
    "https://github.com/numeristical/introspective"
    "https://github.com/manifoldai/docker-cookiecutter-data-science",
    "https://github.com/guyroyse/deep-learning-like-a-viking",
    "https://github.com/cyberutkarsh/odsc-east-2019",
    "https://github.com/nswamy/deeplearning-workshop",
    "https://github.com/Hydrospheredata/hydro-serving-kubeflow-demo",
    "https://github.com/cscherrer/Soss.jl",
    "https://github.com/topepo/odsc-2019",
    "https://github.com/koul/odsc-workshop",
    "https://github.com/YuriyGuts/odsc-target-leakage-workshop",
    "https://github.com/ray-project/tutorial",
    "https://github.com/laseaman/introduction_to_meta_kaggle",
    "https://github.com/GarrettHoffman/ODSC_East_2019_Deploy_DS_Apps",
    "https://github.com/pm0kjp/mapping-geographic-data-in-r",
    "https://github.com/harterrt/when_the_bootstrap_breaks",
    "https://github.com/andrewwlong/odsc_workshop",
    "https://github.com/bradleyfay/odsceast2019",
    "https://github.com/uwdata/visualization-curriculum/",
    "https://github.com/altair-viz/altair-tutorial/",
    "https://github.com/bardess/odsc_2019_workshop",
    "https://github.com/Dell-AI/ODSC-east-2019",
    "https://github.com/SethHWeidman/Conference_talks"
]


def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def change_directory(folder_name):
    os.chdir(folder_name)


def clone_repo(repo_url):
    print("Started Cloning : " + repo_url)
    os.system("git clone " + repo_url)


def clone_repos(repo_urls):
    for repo_url in repo_urls:
        clone_repo(repo_url)


if __name__ == '__main__':
    create_directory(CODE_PARENT_NAME)
    change_directory(CODE_PARENT_NAME)
    clone_repos(REPOS)
