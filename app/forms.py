from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileRequired(),
    FileAllowed(['jpg','png'])
    ])
   