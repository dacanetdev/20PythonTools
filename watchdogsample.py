from watchdog.observers import Observer
from watchdog.events import (
  PatternMatchingEventHandler, FileModifiedEvent, FileCreatedEvent
)

observer = Observer()

class Handler(PatternMatchingEventHandler):
  def on_created(self, event: FileCreatedEvent):
    print('File Created: ', event.src_path)

  def on_modified(self, event: FileModifiedEvent):
    print('File Modified: %s [%s]' % (event.src_path, event.event_type))

observer.schedule(event_handler=Handler('*'), path='.')
observer.daemon = False
observer.start()
try:
  observer.join()
except KeyboardInterrupt:
  print('Stopped')
  observer.stop()
  observer.join()


