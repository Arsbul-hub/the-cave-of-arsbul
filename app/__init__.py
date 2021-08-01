

from flask import Flask




def create_app():
    application = Flask(__name__)

    from .errors import bp as errors_bp
    application.register_blueprint(errors_bp)
    

    from .main import bp as main_bp
    application.register_blueprint(main_bp)

    from .blog import bp as blog_bp
    application.register_blueprint(blog_bp)

    from .example import bp as example_bp
    application.register_blueprint(example_bp)

    return application

application = create_app()

