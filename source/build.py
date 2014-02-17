import distutils.core
import subprocess
import os

# Needed to make build location-agnostic
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

try:
    import pelican
    PELICAN = True
except:
    PELICAN = False

def build_files():

    if PELICAN:

        # Set up file paths regardless of platform
        static_html_path = os.path.join(WORKING_DIR , 'static-html')
        output_path = os.path.join(WORKING_DIR , 'output')
        pages_path = os.path.join(output_path , 'pages')
        theme_path = os.path.join(WORKING_DIR , 'theme')
        settings_path = os.path.join(WORKING_DIR , 'settings.py')
        content_path = os.path.join(WORKING_DIR , 'content')
        destination_path = os.path.join(WORKING_DIR, '..')

        # Create temporary directory
        distutils.dir_util.copy_tree(static_html_path, output_path)

        # Make files with pelican
        subprocess.call(
            ['pelican', '-t', theme_path, '-s', settings_path, content_path]
        )
        # Clean up
        distutils.dir_util.copy_tree(pages_path, output_path)
        distutils.dir_util.remove_tree(pages_path)
        distutils.dir_util.copy_tree(output_path, destination_path)
        distutils.dir_util.remove_tree(output_path)

    else:
        print """Pelican is not installed! Please run pip install -r requirements.txt."""

if __name__ == '__main__':
    build_files()