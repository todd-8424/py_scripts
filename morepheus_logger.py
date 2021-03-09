"""
Author: Todd A. Kearney
Support: none
Date: 9 March 2021
Description: Used to create a logger file to log results in /tmp/test.log
Requirements: This script is designed to be used with Morphues as a Python task in an operational workflow.
              This will take the output of the previous tasks and log them in /tmp/test.log  
"""

import logging
import logging.config
logger = logging.getLogger("fileLogger")
logging.basicConfig(filename='/tmp/test.log', format='%(filename)s: %(message)s',level=logging.DEBUG)
                    
logger.info(json.dumps(morpheus['results']))