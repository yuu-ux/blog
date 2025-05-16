from flask_assets import Environment, Bundle
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class ScssBundler:
    def __init__(self, app):
        assets = Environment(app)
        self.scss = Bundle('../scss/main.scss', filters='libsass', output='css/dist.css', depends='../scss/**/*.scss')
        assets.register('scss_all', self.scss)

    def build(self):
        self.scss.build()

    def start_hot_build(self):
        event_handler = ScssWatchdogHandler(build_event=self.build)
        observer = Observer()
        observer.schedule(event_handler, path='./scss', recursive=True)
        observer.start()

class ScssWatchdogHandler(FileSystemEventHandler):
    def __init__(self, build_event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build_event = build_event

    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            self.build_event()
