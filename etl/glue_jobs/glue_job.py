import boto3

def create_glue_job():
    glue = boto3.client('glue')
    
    response = glue.create_job(
        Name='twitter-etl-job',
        Role='your-glue-service-role',
        Command={
            'Name': 'glueetl',
            'ScriptLocation': 's3://your-s3-bucket-name/scripts/data_transformation.py',
            'PythonVersion': '3'
        },
        DefaultArguments={
            '--job-language': 'python',
            '--extra-py-files': 's3://your-s3-bucket-name/scripts/dependencies.zip'
        }
    )
    
    return response

if __name__ == "__main__":
    create_glue_job()
