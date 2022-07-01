import subprocess

subprocess.run(["pyuic5", "main_page_interface.ui", "-o", "main_page_interface.py"])
subprocess.run(["pyuic5", "processing_interface.ui", "-o", "processing_interface.py"])
subprocess.run(["pyuic5", "user_guide_interface.ui", "-o", "user_guide_interface.py"])
