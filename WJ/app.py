from flask import Flask

app = Flask(__name__)

@app.route("/view_projects/<int:user_id>)
def all_projects(user_id):
    projects= Expense.query.filter_by(user_id=user_id).all()
    if projects:
        return jsonify([*map(projects_serializer, projects)])
    else:
        return jsonify({'404': 'No projects found'})


if __name__ == "__main__":
    app.run(debug=True)