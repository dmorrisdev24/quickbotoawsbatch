# coding: utf-8
import boto3

#create session
session = boto3.Session(profile_name='pythonauto')

# create aws batch client in us west 2 region
awsbatch = boto3.client('batch', 'us-west-2')

# assign instanceRole
instanceRole='arn:aws:iam::309754208659:role/ecsinstanceRole'

# assign serviceRole
serviceRole='arn:aws:iam::309754208659:role/service-role/AWSBatchServiceRole'

# create computeResources dict
computeResources={'type': 'EC2', 'minvCpus': 0, 'maxvCpus': 2, 'desiredvCpus': 1, 'instanceTypes': ['optimal'], 'subnets': ['subnet-03e8a7f10408dcb1e'], 'securityGroupIds': ['sg-09a3680f327f00efc'], 'instanceRole': instanceRole}

# create aws batch client in session
awsbatch = session.client('batch')

# create aws batch CE
automate_env = awsbatch.create_compute_environment(computeEnvironmentName='automateCE2', type='MANAGED', state='ENABLED', computeResources=computeResources, serviceRole=serviceRole)

# create aws batch job queue
session = boto3.Session
session = boto3.Session(profile_name='pythonauto')

awsbatch = session.client('batch')



awsbatch.create_job_queue(computeEnvironmentOrder=[{'computeEnvironment': 'automateCE', 'order': 1,}], jobQueueName='automateQueue', priority=100, state='ENABLED')

# create job definition

session = boto3.Session(profile_name='pythonauto')

awsbatch = session.client('batch')

containerProp = {
'image': 'dmorrisdev/aws-batch-demo',
'vcpus': 2,
'memory': 4024
}
jobRoleArn = 'arn:aws:iam::309754208659:role/automateAdmin'

awsbatch.register_job_definition(jobDefinitionName='automateJD', type='container', containerProperties=containerProp)

# Create submit job

session = boto3.Session(profile_name='pythonauto')
awsbatch = session.client('batch')
awsbatch.submit_job(jobName='automateSubmit', jobQueue='automateQueue', jobDefinition='automateJD')
awsbatch.submit_job(jobName='automateSubmitv2', jobQueue='automateQueue', jobDefinition='automateJD')
