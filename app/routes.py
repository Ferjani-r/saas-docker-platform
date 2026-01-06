from flask import Blueprint, render_template, request, redirect, flash, jsonify
from app.services import docker_service
from app.utils.validators import is_valid_container_name, calculate_uptime

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    containers_data = []

    for c in docker_service.list_containers():
        ports = c.attrs["NetworkSettings"]["Ports"]
        port = "N/A"

        if ports and "80/tcp" in ports and ports["80/tcp"]:
            port = ports["80/tcp"][0]["HostPort"]

        started_at = c.attrs["State"].get("StartedAt")
        uptime = calculate_uptime(started_at, c.status)

        containers_data.append({
            "id": c.id,
            "name": c.name,
            "status": c.status,
            "uptime": uptime,
            "port": port
        })

    return render_template("index.html", containers=containers_data)


@routes.route("/create", methods=["POST"])
def create():
    name = request.form["name"].strip()

    if not is_valid_container_name(name):
        flash("Invalid container name.", "danger")
        return redirect("/")

    try:
        docker_service.create_container(name)
        flash(f"Container '{name}' created successfully.", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect("/")


@routes.route("/start/<id>")
def start(id):
    try:
        docker_service.start_container(id)
        flash("Container started successfully.", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect("/")


@routes.route("/stop/<id>")
def stop(id):
    try:
        docker_service.stop_container(id)
        flash("Container stopped successfully.", "warning")
    except Exception as e:
        flash(str(e), "danger")

    return redirect("/")


@routes.route("/restart/<id>")
def restart(id):
    try:
        docker_service.restart_container(id)
        flash("Container restarted successfully.", "info")
    except Exception as e:
        flash(str(e), "danger")

    return redirect("/")


@routes.route("/delete/<id>")
def delete(id):
    try:
        docker_service.delete_container(id)
        flash("Container deleted successfully.", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect("/")


@routes.route("/logs/<id>")
def logs(id):
    try:
        logs = docker_service.get_container_logs(id)
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
