import json
import sys
import time
from flask import render_template
from rq import get_current_job
from app import create_app, db
from app.models import User, SystemEvent, Task
from app.email import send_email


app = create_app()
app.app_context().push()


def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(),
                                                     'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()


def export_system_events(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        events = SystemEvent.query
        _set_task_progress(0)
        data = []
        i = 0
        total_events = events.count()
        for event in events.order_by(SystemEvent.timestamp.asc()):
            data.append(event.from_dict)
            time.sleep(5)
            i += 1
            _set_task_progress(100 * i // total_events)

        send_email('СКУД. Системные события',
                sender=app.config['ADMINS'][0], recipients=[user.email],
                text_body=render_template('email/export_system_events.txt', user=user),
                html_body=render_template('email/export_system_events.html',
                                          user=user),
                attachments=[('events.json', 'application/json',
                              json.dumps({'events': data}, indent=4))],
                sync=True)
    except:
        _set_task_progress(100)
        app.logger.error('Unhandled exception', exc_info=sys.exc_info())
