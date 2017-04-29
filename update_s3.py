import boto3
import filecmp
import os


UPDATED_SITE_DIR = os.environ.get('UPDATED_SITE_DIR')
CURRENT_SITE_DIR = os.environ.get('CURRENT_SITE_DIR')
BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')


def upload_with_content_type(file, full_key, auto):
    content_type = "default"
    if file.endswith(".html"):
        content_type = "text/html"
    elif file.endswith(".css"):
        content_type = "text/css"
    elif file.endswith(".jpg"):
        content_type = "image/jpeg"
    elif file.endswith(".png"):
        content_type = "image/png"
    elif file.endswith(".xml"):
        content_type = "application/xml"

    print("uploading \"{}\" as {}".format(full_key, content_type))
    if content_type is "default":
        bucket.put_object(Key=full_key, Body=auto,
                          ACL='public-read')
    else:
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType=content_type)


if __name__ == "__main__":
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    for root, dirs, files in os.walk(os.getcwd() + UPDATED_SITE_DIR):
        subdir = root[(len(os.getcwd())+len(UPDATED_SITE_DIR)):len(root)]
        if subdir.startswith('/'):
            subdir = subdir[1:]
        for file in files:
            current_file = str(os.path.join(root, file)).\
                           replace(UPDATED_SITE_DIR, CURRENT_SITE_DIR)
            updated_file = str(os.path.join(root, file))
            files_match = False
            try:
                files_match = filecmp.cmp(current_file, updated_file,
                                          shallow=False)
            except FileNotFoundError:
                pass # files_match already set to False
            if not files_match and file is not ".DS_Store":
                with open(os.path.join(root, file), "rb") as auto:
                    full_key = file
                    if subdir:
                        full_key = subdir + '/' + file
                    upload_with_content_type(file, full_key, auto)
