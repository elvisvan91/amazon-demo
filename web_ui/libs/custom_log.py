"""
This is a customized logger module

@Author: Van.Vo
"""
import os
import inspect
import logging
import logging.config
import time
from datetime import datetime

STEP_LEVEL_NUM = 32
TC_NAME_NUMBER = 31
logging.addLevelName(STEP_LEVEL_NUM, 'STEP')
logging.addLevelName(TC_NAME_NUMBER, 'TESTCASE')


def custom_logger(log_level=logging.WARNING):
    """
    This method use to customize logging
    """
    # Gets the name of the class / method from where this method is called
    folder_name = "run_" + datetime.now().strftime("%B_%d_%Y")
    try:
        os.makedirs(os.path.join('logs', folder_name))
    except OSError:  # Exists
        pass

    logger_name = inspect.stack()[3][1]
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    if logger.hasHandlers():
        # Logger is already configured, remove all handlers
        logger.handlers = []
    # Log STEP
    step_log = datetime.now().strftime("step_%b_%d_%Y.log")
    step_handler = logging.FileHandler(filename=os.path.join('logs/' + folder_name, step_log))
    step_handler.setLevel(logging.WARNING)
    step_handler.setFormatter(formatter)
    logger.addHandler(step_handler)
    # Log all messages
    logger.setLevel(logging.DEBUG)
    log_file = datetime.now().strftime("console_%b_%d_%Y.log")
    file_handler = logging.FileHandler(filename=os.path.join('logs/' + folder_name, log_file))
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def INFO(msg):
    """
    Logs an info message.
    """
    log = custom_logger(logging.INFO)
    log.info(msg)


def DEBUG(msg):
    """
    Logs an debug message.
    """
    log = custom_logger(logging.DEBUG)
    log.debug(msg)


def assert_true(expr, fail_msg, pass_msg=None):
    """
    Throws Test Error with fail_msg if val != True,
    else logs pass_msg
    """
    if not expr:
        raise Exception(fail_msg)
    else:
        if pass_msg is not None:
            INFO(pass_msg)


def wait_time(_time):
    """
    Wait time.
    """
    time.sleep(_time)


def tc_name(self, msg, *args, **kwargs):
    if self.isEnabledFor(TC_NAME_NUMBER):
        self._log(TC_NAME_NUMBER, msg, args, **kwargs)


logging.Logger.tc_name = tc_name


def TESTCASE(msg):
    """
    Logs an debug message.
    """
    log = custom_logger(logging.INFO)
    log.tc_name(msg)


def step(self, msg, *args, **kwargs):
    if self.isEnabledFor(STEP_LEVEL_NUM):
        self._log(STEP_LEVEL_NUM, msg, args, **kwargs)


logging.Logger.step = step


def STEP(msg):
    """
    Logs an debug message.
    """
    log = custom_logger(logging.INFO)
    log.step('-' * 60)
    log.step('%d. ' % step.step_counter + msg)
    log.step('-' * 60)
    step.step_counter += 1


step.step_counter = 1


def reset_step():
    step.step_counter = 1
    wait_time(1)
