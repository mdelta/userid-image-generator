import io
from flask import (
    Blueprint, escape, send_file
)
from PIL import Image, ImageDraw, ImageFont
# from utils import display_pillow_image

bp = Blueprint('generator', __name__, url_prefix='/generator')


@bp.route('/<userid>', methods=['GET'])
def image_generator(userid):
    w = 100 # 100 pixels wide
    h = 100 # 100 pixels high
    img = Image.new('RGB', (w, h), color='#FF0000')

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')
