from app import  application  # create_app


# application = create_app()

# application.logger.info('app create')
# application.logger.info('cli register application')

if __name__ == "__main__":
    # application.logger.info('app main')
    application.run(host='0.0.0.0')
'''
@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task, 'Skip': Skip,
            'SystemEvent': SystemEvent}
'''
