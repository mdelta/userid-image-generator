import io
from flask import (
    Blueprint, escape, send_file
)
from PIL import (Image, ImageDraw, ImageFont)

bp = Blueprint('generator', __name__, url_prefix='/generator')


@bp.route('/<userid>', methods=['GET'])
def image_generator(userid):
    w = 200 # pixels width
    h = 200 # pixels height

    img = Image.new('RGBA', (w, h), color='#247963')
    canvas = ImageDraw.Draw(img)

    # Constants for the box creation:
    NUMBER_BOXES = 3
    BOX_SIZE = 30
    BOX_POS_Y = 150
    BOX_COLOR = "#EE8324"

    # We need three boxes. That means we separate the image into 4 rectangles:
    # ---------
    # | | | | |
    # | | | | |
    # | | | | |
    # ---------
    #
    # The "separation line" of each rectangle is the center for our box (|>|<| | |). Therefore we divide the box into two halves and set the position.

    grid_distance = w / (NUMBER_BOXES + 1)
    for i in range(NUMBER_BOXES):
        grid_line = grid_distance * (i + 1)
        canvas.rectangle([(grid_line - (BOX_SIZE/2), BOX_POS_Y), (grid_line + (BOX_SIZE/2), BOX_POS_Y + BOX_SIZE)], fill=BOX_COLOR)

    # Create the user ID as text
    font = ImageFont.truetype('arial.ttf', size=64)
    canvas.text((100, 100), escape(userid.upper()), anchor="ms", font=font, fill='#FFFFFF')

    # Create the image
    img_io = io.BytesIO()
    img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
