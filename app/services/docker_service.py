import docker
import os

client = docker.from_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NGINX_HTML_PATH = os.path.join(BASE_DIR, "nginx")


def list_containers():
    return client.containers.list(all=True)


def create_container(name):
    return client.containers.run(
        image="nginx:latest",
        name=name,
        detach=True,
        ports={"80/tcp": None},
        volumes={
            NGINX_HTML_PATH: {
                "bind": "/usr/share/nginx/html",
                "mode": "ro"
            }
        }
    )


def start_container(container_id):
    client.containers.get(container_id).start()


def stop_container(container_id):
    client.containers.get(container_id).stop()


def delete_container(container_id):
    client.containers.get(container_id).remove(force=True)

def restart_container(container_id):
    client.containers.get(container_id).restart()

def get_container_logs(container_id, lines=50):
    container = client.containers.get(container_id)
    return container.logs(tail=lines).decode("utf-8")
