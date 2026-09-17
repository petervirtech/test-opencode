"""
Minimal Flask web UI for PM Buddy.

Uses Jinja2 templates located in ``templates`` directory relative to this file.
"""

from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path

from .service import PMBuddyService

app = Flask(__name__)
# Ensure template folder is correct when run from package root
BASE_DIR = Path(__file__).parent
app.template_folder = str(BASE_DIR / "templates")
service = PMBuddyService()

@app.route('/')
def index():
    epics = service.list_epics()
    return render_template('index.html', epics=epics)

@app.route('/add_epic', methods=['GET','POST'])
def add_epic():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form.get('description','')
        service.add_epic(title,desc)
        return redirect(url_for('index'))
    return render_template('add_epic.html')

@app.route('/epic/<int:epic_id>')
def epic_detail(epic_id):
    epics = service.list_epics()
    epic = next((e for e in epics if e.id==epic_id), None)
    features = service.list_features(epic_id) if epic else []
    return render_template('epic_detail.html', epic=epic, features=features)

@app.route('/add_feature/<int:epic_id>', methods=['GET','POST'])
def add_feature(epic_id):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form.get('description','')
        service.add_feature(epic_id,title,desc)
        return redirect(url_for('epic_detail', epic_id=epic_id))
    return render_template('add_feature.html', epic_id=epic_id)

@app.route('/feature/<int:feature_id>')
def feature_detail(feature_id):
    # Find parent epic for breadcrumb
    epics = service.list_epics()
    feature=None; epic_parent=None
    for e in epics:
        fs=service.list_features(e.id)
        if any(f.id==feature_id for f in fs):
            feature=[f for f in fs if f.id==feature_id][0]
            epic_parent=e
            break
    stories=service.list_stories(feature_id) if feature else []
    return render_template('feature_detail.html', epic=epic_parent, feature=feature, stories=stories)

@app.route('/add_story/<int:feature_id>', methods=['GET','POST'])
def add_story(feature_id):
    if request.method == 'POST':
        title=request.form['title']
        desc=request.form.get('description','')
        service.add_story(feature_id,title,desc)
        return redirect(url_for('feature_detail', feature_id=feature_id))
    return render_template('add_story.html', feature_id=feature_id)

@app.route('/sync')
def sync():
    # Stub: call adapter sync_to_azure
    from .app import AzureAdapter
    AzureAdapter(service.open_db()).sync_to_azure()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
