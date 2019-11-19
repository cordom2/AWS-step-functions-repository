import json
import boto3
from datetime import datetime
from urllib.parse import unquote

def lambda_handler(event, context):

    event['Records'][0]['s3']['object']['key'] = unquote(event['Records'][0]['s3']['object']['key'])

    # s3_client = boto3.client('s3')
    # cluster_configs = s3_client.get_object(
    #     Bucket='us-dev-us-east-1-data',
    #     Key='step-function-testing/inputs/sample-Datapipeline-StateMachine-input.json'
    # )

    # print(cluster_configs['Body'])
    # # print(json.dump(cluster_configs))

    # # event += json.dumps(cluster_configs)

    cluster_configs = {
        "S3Bucket": "us-int-us-west-2-data",
        "S3Key": "graph/forecaster_seg/dt=20191111/_SUCCESS",
        "segment-counts-input": {
            "Name": "segment-country-counts",
            "TIMEOUT_AFTER_X_HOURS": 12,
            "EMR_RELEASE_LABEL": "emr-5.21.0",
            "MASTER_INSTANCE_TYPE": "m4.large",
            "CORE_INSTANCE_TYPE": "m4.large",
            "CORE_INSTANCE_COUNT": 2,
            "Ec2KeyName": "kp-user-matthew.cordone",
            "ServiceRole": "dev-us-dev-emr-role-resource",
            "LogUri": "s3://us-dev-us-east-1-logs/",
            "Steps": [
                {
                    "Name": "env-config-step",
                    "ActionOnFailure": "CONTINUE",
                    "Jar": "command-runner.jar",
                    "Args": [
                        "bash",
                        "-c",
                        "echo -e \"\\nexport S3_FORECASTER_PID_PATH=s3a://us-dev-us-east-1-data/graph/forecaster_pid;export SEGMENTS_COUNT_OUT_SAPI_HTTP_URI=http://internal-api.us-int.peoplecloud.internal/segments_api/api/v1/counts;export SEGMENTS_COUNT_OUT_SAPI_ID_SPACE=metagraph;export SEGMENTS_COUNT_OUT_SAPI_ENABLE=true;export DATE=#{myDpActivationDate};export S3_COUNTRY_COUNTS_OUTPUT_PATH=s3a://us-dev-us-east-1-data/jobs/segment-country-counts;export S3_FORECASTER_SEG_PATH=s3a://us-dev-us-east-1-data/graph/forecaster_seg\" >> /home/hadoop/.bashrc;aws s3 cp s3://us-dev-us-east-1-artifacts/dp-job-manager/1.1.1/dp-job-manager-1.1.1-d2994a2999758214deecb7fbccf7b1542df12433.jar /home/hadoop/"
                    ]
                },
                {
                    "Name": "run-job-step",
                    "ActionOnFailure": "CONTINUE",
                    "Jar": "command-runner.jar",
                    "Args": [
                        "bash",
                        "-c",
                        "source /home/hadoop/.bashrc spark-submit --master yarn --conf yarn.nodemanager.resource.memory-mb=247808M --num-executors=165 --executor-cores 3 --executor-memory 31G --conf spark.driver.cores=3 --conf spark.driver.memory=100G --conf spark.default.parallelism=1440 --conf spark.sql.shuffle.partitions=1440 --conf spark.locality.wait.node=10m --conf spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version=2 --class com.publicisgroupe.ppc.jobs.count.CountGenerator s3://us-dev-us-east-1-artifacts/segment-counts/2.3.0/segment-counts-2.3.0-483b071048cdcdd41b3d589d2f234e085c0c3912.jar"
                    ]
                }
            ]
        },
        "id-analytics-input": {
            "Name": "id-analytics",
            "TIMEOUT_AFTER_X_HOURS": 12,
            "EMR_RELEASE_LABEL": "emr-5.21.0",
            "MASTER_INSTANCE_TYPE": "m4.large",
            "CORE_INSTANCE_TYPE": "m4.large",
            "CORE_INSTANCE_COUNT": 2,
            "Ec2KeyName": "kp-user-matthew.cordone",
            "ServiceRole": "dev-us-dev-emr-role-resource",
            "LogUri": "s3://us-dev-us-east-1-logs/",
            "Steps": [
                {
                    "Name": "env-config-step",
                    "ActionOnFailure": "CONTINUE",
                    "Jar": "command-runner.jar",
                    "Args": [
                        "bash",
                        "-c",
                        "echo -e \"\\nexport SPINE_JOB_ES_PEOPLE_TYPE=people-report;export SPINE_JOB_ES_PEOPLE_INDEX_PREFIX=people-;export SPINE_JOB_ES_PORT=443;export SPINE_JOB_ES_HOST=vpc-us-dev-es-i5iqcagplr76mmyx3xpncriwpq.us-east-1.es.amazonaws.com;export SPINE_JOB_WRITE_PEOPLE_PATH=s3://us-dev-us-east-1-data/jobs/id-analytics/people;export SPINE_JOB_SEGMENT_TAXONOMY_DIR=s3://us-dev-us-east-1-data/graph/segment_taxonomy;export SPINE_JOB_SPARK_MASTER=yarn;export SPINE_JOB_FORECASTER_PID_DIR=s3://us-dev-us-east-1-data/graph/forecaster_pid;export SPINE_JOB_ENV=prod;export SPINE_JOB_FORECASTER_SEG_DIR=s3://us-dev-us-east-1-data/graph/forecaster_seg;export SPINE_JOB_ES_PEOPLE_SHARDS=20;export SPINE_JOB_DATETIME=#{myDpActivationDate};export SPINE_JOB_ES_PEOPLE_REPLICAS=1;export SPINE_JOB_READ_PEOPLE_PATH=s3://us-dev-us-east-1-data/jobs/id-analytics/people;export SPINE_JOB_ARGS_COUNTRIES=us\" >> /home/hadoop/.bashrc;aws s3 cp s3://us-dev-us-east-1-artifacts/dp-job-manager/1.1.1/dp-job-manager-1.1.1-d2994a2999758214deecb7fbccf7b1542df12433.jar /home/hadoop/"
                    ]
                },
                {
                    "Name": "run-job-step",
                    "ActionOnFailure": "CONTINUE",
                    "Jar": "command-runner.jar",
                    "Args": [
                        "bash",
                        "-c",
                        "source /home/hadoop/.bashrc spark-submit --master yarn --conf spark.executor.instances=165 --conf spark.yarn.executor.memoryOverhead=3072 --conf spark.executor.memory=19g --conf spark.yarn.driver.memoryOverhead=25600 --conf spark.driver.memory=57g --conf spark.executor.cores=5 --conf spark.driver.cores=5 --conf spark.default.parallelism=1650 --conf spark.sql.shuffle.partitions=1650 --class com.publicisgroupe.spine.idanalytics.PeopleApp s3://us-dev-us-east-1-artifacts/id-analytics/1.8.1/id-analytics-1.8.1-09d32116501f94f265edce17b005a2e26a2318af.jar"
                    ]
                }
            ]
        }
    }

    temp = event['Records']
    event = cluster_configs
    event['Records'] = temp

    if 'dt='+datetime.today().strftime('%Y%m%d')+'/_SUCCESS' in event['Records'][0]['s3']['object']['key']:
        sfn_client = boto3.client('stepfunctions')
        response = sfn_client.start_execution(
            stateMachineArn='arn:aws:states:us-east-1:849776797214:stateMachine:Datapipeline-StateMachine',
            input=json.dumps(event)
        )

    return event
