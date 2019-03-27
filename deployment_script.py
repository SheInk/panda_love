import requests
from subprocess import Popen


def get_panda_pics(panda_pics_url):
    try:
        Popen("wget %s" % panda_pics_url, shell=True)
        imgs_dir_name = 'images' # define name of the panda pics directory
        Popen("mkdir %s" % imgs_dir_name, shell=True)  # create a directory for panda pics (if needed)
        Popen('tar -xvzf pandapics.tar.gz -C %s ' % imgs_dir_name, shell=True)  # extract panda pics to directory
    except Exception as e:
        print 'failed to get panda pics with the following error: - %s' % e


def get_git_repo(git_url):
    try:
        Popen("git clone %s" % git_url, shell=True)  # cloning the panda_app repository
    except Exception as e:
        print 'failed to clone repository with the following error: - %s' % e


def build_docker_compose():
    try:
        Popen('docker-compose up -d', shell=True) # start the docker-compose process
    except Exception as e:
        print 'failed to start the docker-compose with the following error: - %s' % e


def test_app_health(test_url):
    r = requests.get(test_url)
    if r.status_code is not 200:
        return False
    return True


if __name__ == "__main__":
    panda_pics_url = 'https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz'
    git_url = 'https://github.com/bigpandaio/ops-exercise.git'
    test_url = 'http://localhost:3000/health'
    get_panda_pics(panda_pics_url)
    get_git_repo(git_url)
    build_docker_compose()
