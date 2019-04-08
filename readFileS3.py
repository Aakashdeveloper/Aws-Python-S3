import boto
from boto.s3.key import Key

keyId = "AKIASVJC5W6APZJXPRMT"
sKeyId="pTaagvrPHV/3WvGGkRIC/JQiGKJaHL3kqtXoOWOM"

srcFileName="package.json"
destFileName="myfile.json"
bucketName="finbotaxep"
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
k = Key(bucket,srcFileName)
k.get_contents_to_filename(destFileName)
