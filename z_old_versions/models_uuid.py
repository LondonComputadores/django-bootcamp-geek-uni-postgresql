import uuid
"""
  Generally used on models to avoid files/photos
  naming conflicts through the ImageField()
"""


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename