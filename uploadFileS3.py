import boto
from boto.s3.key import Key

keyId = "AKIASVJC5W6APZJXPRMT"
sKeyId="pTaagvrPHV/3WvGGkRIC/JQiGKJaHL3kqtXoOWOM"
fileName ='docker-compose.yml'
bucketName="finbotaxep"
conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
file = open(fileName)

k = Key(bucket)
k.key= fileName
result = k.set_contents_from_file(file)