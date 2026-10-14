import logging
import os

log_dir = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    filename=  os.path.join(log_dir,"pipeline_LOGS.log"),
    filemode= "w",
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

def make_logger(name,filename):

    my_logger = logging.getLogger(name)

    my_logger.setLevel(logging.INFO)

    file_handller = logging.FileHandler(os.path.join(log_dir,filename), "w")

    file_handller.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )

    my_logger.addHandler(file_handller)
    return my_logger

extract_log = make_logger("extract", "extract.log")
transform_log = make_logger("transform", "transform.log")
load_log = make_logger("load", "load.log")
pipeline_log = make_logger("pipeline","pipeline_run.log")