import os
from werkzeug.utils import secure_filename
from backend.utils.file_utils import save_uploaded_file

@profile_bp.route('/api/upload_photo', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({"error": "Файл не найден"}), 400

    file = request.files['file']
    upload_folder = "uploads"
    file_path = save_uploaded_file(file, upload_folder)

    if file_path:
        return jsonify({"status": "success", "file_path": file_path})
    return jsonify({"error": "Недопустимый формат файла"}), 400

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Проверяет, что файл имеет допустимое расширение."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, upload_folder):
    """Сохраняет загруженный файл на сервере."""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    return None

def delete_file(file_path):
    """Удаляет файл с сервера."""
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False