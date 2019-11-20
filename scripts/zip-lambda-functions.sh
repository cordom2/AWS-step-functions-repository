cd lambda-functions/check-cluster-status
zip -r ../../lambda-function-zip-files/check-cluster-status.zip lambda_function.py
cd ../check-emr-job-status
zip -r ../../lambda-function-zip-files/check-emr-job-status.zip lambda_function.py
cd ../check-emr-timeout
zip -r ../../lambda-function-zip-files/check-emr-timeout.zip lambda_function.py
cd ../check-s3-file-exists
zip -r ../../lambda-function-zip-files/check-s3-file-exists.zip lambda_function.py
cd ../Datapipeline-StateMachine-Trigger
zip -r ../../lambda-function-zip-files/Datapipeline-StateMachine-Trigger.zip lambda_function.py
cd ../datapipeline-update-checkNumber
zip -r ../../lambda-function-zip-files/datapipeline-update-checkNumber.zip lambda_function.py
cd ../emr-add-step
zip -r ../../lambda-function-zip-files/emr-add-step.zip lambda_function.py
cd ../emr-cluster-create
zip -r ../../lambda-function-zip-files/emr-cluster-create.zip lambda_function.py
cd ../emr-pipe-setup
zip -r ../../lambda-function-zip-files/emr-pipe-setup.zip lambda_function.py
cd ../increment-step-number
zip -r ../../lambda-function-zip-files/increment-step-number.zip lambda_function.py
cd ../terminate-emr-cluster
zip -r ../../lambda-function-zip-files/terminate-emr-cluster.zip lambda_function.py
cd ../..
aws s3 sync lambda-function-zip-files s3://us-dev-us-east-1-data/step-function-testing/lambda-function-zip-files