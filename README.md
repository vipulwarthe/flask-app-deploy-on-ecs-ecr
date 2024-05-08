# Project:- Deploy Flask App using ECS & ECR

* Setting Up EC2 instance
* Create a new EC2 instance and SSH into it (ubuntu/t2.micro/all-traffic/8gb)

# Create an ECS cluster:
* In the ECS service, click on “Create Cluster”.
* Configure the cluster settings, such as the cluster name, VPC, and subnet.
* We are using Fargate as Serverless and now Click on ‘Create’.

* Create an ECR repository to store the Image
  
* In the ECR, Click on “Create Repository”
* Keep the repo public so that we can access easily.
* Provide the reasonable repository name
* Once all the details are filled in, now click on “Create the Repository”.
* The ECR Repo has been created, we have to push the application image from the server.
* Push the Flask Application Image to ECR Repo but first install docker 
* Now git clone the Flask app code from the GitHub Repo
* Change into the repository folder.
* We can verify the content of the file using cat command.
* Now copy and paste the ECR commands one by one that is provided.
* Login to the ECR repo in the EC2 Instance using “View Push Command”
* Build the Flask app using Dockerfile.
* Tag the container
* Now push container into ECR Container.
* We can verify in ECS that our image is pushed into the ECR repo.

* Create a task definition:
  
* In the ECS service, click on “Task Definitions”, and then click on “Create new Task Definition”.
* Set the container name to “run-flask-app”, and copy and paste the Image URL from ECR where we updated the flask app image previously. Specify the port mappings for HTTP, by setting the “Container port” to 80.
* Choose the Fargate launch type, Configure the task settings, such as the task memory and CPU limits, here CPU is 1vCPU and the memory is 3GB.
* Now review the configuration and create the task definition.
* Run the Task Definition
* From the ECS container, click on Deploy and then Run Task
* Select the cluster where it should run
* In the Deployment Configuration provide the details.
* Choose the VPC and SG as per requirement.
* Once the task definition is created, Now launch the task.
* As the task is running, the app is successfully up & running.
* Browse the Public IP address, you can see the default Flask app.

Terminal commands: 

    2  sudo apt update
    3  sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
    4  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    5  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    6  sudo apt update
    7  sudo apt install docker.io -y
    8  docker --version 
    9  sudo usermod -aG docker $USER
    10  sudo chown $USER /var/run/docker.sock
    11  sudo systemctl start docker
    12  sudo systemctl enable docker
    13  sudo systemctl status docker
    15  sudo apt install awscli
    16  aws configure
    17  git clone https://github.com/vipulwarthe/flask-app-deploy-on-ecs-ecr.git
    18  ls
    19  cd flask-app-deploy-on-ecs-ecr/
    20  aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/x7a3j4l9
    21  docker build -t my-flask-repo .
    22  docker tag my-flask-repo:latest public.ecr.aws/x7a3j4l9/my-flask-repo:latest
    23  docker push public.ecr.aws/x7a3j4l9/my-flask-repo:latest
    24  docker images


In our project, “Deploy Flask App using ECS & ECR,” we explored essential AWS services like ECS, ECR, and Fargate. We deployed a Flask app on an EC2 instance within an ECS cluster, using an ECR repository to store our Docker image. This project provides a solid foundation for efficient containerized app deployment on AWS.
