from bson.errors import InvalidId
from flask import Blueprint, render_template
from models.projectModel import ProjectModel
from models.querys import _project_id, _task_id

project_controller = Blueprint("project", __name__)


def _get_project_or_task(id):
    project = ProjectModel.find(id)
    return [task.to_dict() for task in project]


@project_controller.route("/")
@project_controller.route("/projects")
def home():
    projects = ProjectModel.separate_projects()
    return render_template("home.html", projects=projects)


@project_controller.route("/projects/<id>")
def project(id):
    project = _get_project_or_task(_project_id(id))
    if not project:
        return render_template("404.html"), 404
    return render_template("project.html", project=project)


@project_controller.route("/task/<id>")
def task(id):
    try:
        task = _get_project_or_task(_task_id(id))

        if not task:
            return render_template("404.html"), 404
        return render_template("task.html", task=task[0])

    except InvalidId:
        return render_template("404.html"), 404
