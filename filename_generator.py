import datetime

def generate():
    basename = "message"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix, '.txt'])
    return filename