import logging
import time
from daemon import runner
class test():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/var/run/test/test.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print time.time()
            logger.debug("Debug")
            logger.info("info")
            logger.warn("Warning")
            logger.error("Error")
            time.sleep(10)
            

test = test()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/testdaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(test)
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()


    