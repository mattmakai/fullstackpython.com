import boto3
import filecmp
import os


UPDATED_SITE_DIR = os.environ.get('UPDATED_SITE_DIR')
CURRENT_SITE_DIR = os.environ.get('CURRENT_SITE_DIR')
BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')


def upload_with_content_type(file, full_key, auto):
    if ".html" in file:
        print("uploading \"{}\" as html".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="text/html")
    elif ".css" in file:
        print("uploading \"{}\" as css".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="text/css")
    elif ".jpg" in file:
        print("uploading \"{}\" as jpeg".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="image/jpeg")
    elif ".png" in file:
        print("uploading \"{}\" as png".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="image/png")
    elif ".xml" in file:
        print("uploading \"{}\" as xml".format(full_key))
        bucket.put_object(Key=full_key, Body=auto, ACL='public-read',
                          ContentType="application/xml")
    else:
        print("uploading \"{}\"".format(full_key))
        bucket.put_object(Key=full_key, Body=auto,
                          ACL='public-read')


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
