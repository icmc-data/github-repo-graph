import argparse
from scraping.features.stars import getNumberOfStars

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="OAuth token from GitHub", required=True)
    args = parser.parse_args()
    return args


def main():
    args = setup()
    authToken = args.token
    print(authToken)

    urls = ["tensorflow/tensorflow", "keras-team/keras", "pytorch/pytorch"]
    for repoURL in urls:
        print("{} = {} stars".format(repoURL, getNumberOfStars(authToken, repoURL)))

if __name__ == '__main__':
    main()
    