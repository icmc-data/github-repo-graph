from data.features.stars import getNumberOfStars
import os
import dotenv

def main():
    dotenv.load_dotenv()
    authToken = os.environ.get('GITHUB_TOKEN')

    urls = ["tensorflow/tensorflow", "keras-team/keras", "pytorch/pytorch"]
    for repoURL in urls:
        print("{} = {} stars".format(repoURL, getNumberOfStars(authToken, repoURL)))

if __name__ == '__main__':
    main()
    