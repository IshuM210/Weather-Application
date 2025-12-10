# Weather Application — DevOps CI/CD Project

## 🔍 Project Description  
Weather-report web application powered by Flask (Python).  
The project demonstrates a complete DevOps pipeline: code pushed to GitHub → automated build & containerization via Jenkins & Docker → deployment on AWS EC2 → monitoring + automated log backups via cron jobs.

## 🚀 Tech Stack / Tools & Services Used  
- Python + Flask (backend)  
- HTML / CSS (frontend)  
- Docker & Docker Hub (containerization)  
- Jenkins (CI/CD pipeline)  
- AWS EC2 (hosting & deployment)  
- Monitoring tools — Prometheus, Grafana 
- Cron (for automated log backup)  

## 📦 How to Run Locally / Setup  

1️⃣ Setup Instructions — Run Locally (Python)

For people without Docker or Jenkins.

git clone https://github.com/IshuM210/Weather-Application.git
cd Weather-Application
pip install -r requirements.txt
python app.py


Then open:

http://localhost:5000

2️⃣ Setup Instructions — Run Using Docker

For people who prefer running as a container.

docker build -t weather-app .
docker run -d -p 5000:5000 weather-app

Open:
http://localhost:5000
CI/CD Pipeline Flow (Short Summary)

This project uses a fully automated CI/CD pipeline:

GitHub → Jenkins → Docker Build → Docker Hub → AWS EC2 Deployment → Monitoring

✔ Pipeline Steps:

Developer pushes code to GitHub

Jenkins automatically triggers build

Jenkins builds Docker image

Pushes image to Docker Hub

Jenkins SSHs into EC2

Pulls latest image on EC2

Runs container on port 5000

(Optional) Prometheus scrapes metrics

Grafana visualizes dashboards

🖥️ Deployment (AWS EC2)

If EC2 is running:

http://<your-ec2-public-ip>:5000


If stopped:

Application deployed on AWS EC2 during CI/CD pipeline execution. Instance may be stopped to save cost.

📂 Project Folder Structure
Weather-Application/
│── app.py
│── requirements.txt
│── Dockerfile
│── Jenkinsfile
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

⏱️ Cron Job Automation (Log Backup)

A cron job runs on the Application EC2 instance to back up logs automatically.

Cron Entry
* * * * * /home/ubuntu/backup.sh

Backup Script
#!/bin/bash
SOURCE="/home/ubuntu/app-logs/app.log"
DEST="/home/ubuntu/backups"
mkdir -p $DEST

cp $SOURCE $DEST/app.log-$(date +"%Y-%m-%d_%H-%M-%S")
echo "Backup created at $(date)" >> /home/ubuntu/cron-job-history.log


This script creates time-stamped backups every minute.

⚙️ Challenges & Learnings
Challenges

Docker permission errors (docker.sock access denied)

Jenkins unable to push to Docker Hub due to wrong credential ID

SSH key mismatch between Jenkins and EC2

EC2 IP change broke deployment flow

Large Docker image caused slow push → fixed with .dockerignore

Jenkinsfile indentation & credential issues

Container removal error when old container didn’t exist

Learnings

Docker user/group management and permissions

Jenkins credential handling (Docker Hub + SSH keys)

Setting up secure SSH authentication with EC2

Optimizing Docker images and improving push speed

Writing and debugging Jenkins pipelines

Understanding AWS networking (security groups, ports)

Automating tasks using cron jobs

Full real-world CI/CD implementation

📸 Screenshots & Video

Jenkins console output
<img width="940" height="513" alt="image" src="https://github.com/user-attachments/assets/d4cc316f-0b41-40a1-9a0c-6d7660036308" />

Docker images

Docker Hub repository

EC2 instance running the application

Prometheus & Grafana dashboards (if used)

Cron job backups

All screenshots and video proof are included in the project report.

📎 Source Code

GitHub Repository:
https://github.com/IshuM210/Weather-Application.git

🏁 Conclusion

This project demonstrates a complete end-to-end DevOps pipeline—from code development to automated deployment, monitoring, and maintenance. Implementing this project strengthened my understanding of CI/CD, cloud deployment, containerization, automation, troubleshooting, and modern DevOps practices.
