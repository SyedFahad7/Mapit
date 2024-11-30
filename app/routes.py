import os
from flask import Blueprint, request, Response
from werkzeug.utils import secure_filename
from .utils import get_directory_structure
import tempfile
import zipfile

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Project Visualizer API'

@main.route('/upload', methods=['POST'])
def upload_folder():
    if 'files[]' not in request.files:
        return Response("No files uploaded", status=400)

    files = request.files.getlist('files[]')

    with tempfile.TemporaryDirectory() as temp_dir:
        # Save files to the temporary directory
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(temp_dir, filename)
                file.save(file_path)

                # Extract if it's a ZIP file
                if zipfile.is_zipfile(file_path):
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

        # Generate the directory structure excluding unnecessary folders
        formatted_structure = get_directory_structure(temp_dir)

    # Return the response as plain text
    return Response(formatted_structure, mimetype="text/plain")
