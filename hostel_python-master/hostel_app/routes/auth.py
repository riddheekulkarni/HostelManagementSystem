from flask import Blueprint, redirect, render_template, request, session

from hostel_app.db import get_db_connection


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    return redirect("/dashboard")
