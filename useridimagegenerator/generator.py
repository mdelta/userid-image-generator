import io
from flask import (
    Blueprint, escape, send_file
)
from PIL import Image, ImageDraw, ImageFont
# from utils import display_pillow_image

bp = Blueprint('generator', __name__, url_prefix='/generator')


@bp.route('/<userid>', methods=['GET'])
def image_generator(userid):
    w = 200 # pixels width
    h = 200 # pixels height
    img = Image.new('RGBA', (w, h), color='#247963')
    canvas = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size=24)
    canvas.text((100, 100), escape(userid.upper()), anchor="ms", font=font, fill='#FFFFFF')
    canvas.rectangle([(50, 150), (80,180)], fill="#EE8324")

    img_io = io.BytesIO()
    img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
