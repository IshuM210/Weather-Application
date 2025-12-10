# Weather Application — DevOps CI/CD Project

## 🔍 Project Description 
Flask-based weather reporting application that shows weather for user-entered cities.

This project demonstrates a complete DevOps pipeline:
GitHub → Jenkins → Docker → Docker Hub → AWS EC2 → Monitoring → Cron Job Automation.

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
```
git clone https://github.com/IshuM210/Weather-Application.git
cd Weather-Application
pip install -r requirements.txt
python app.py
```
Then open:
http://localhost:5000

2️⃣ Setup Instructions — Run Using Docker

For people who prefer running as a container.

docker build -t weather-app .
docker run -d -p 5000:5000 weather-app
Open:
http://localhost:5000

## CI/CD Pipeline Flow 

This project uses a fully automated CI/CD pipeline:

GitHub → Jenkins → Docker Build → Docker Hub → AWS EC2 Deployment → Monitoring

✔ Pipeline Steps:

   -> Developer pushes code to GitHub
   -> Jenkins automatically triggers build
   -> Jenkins builds Docker image
   -> Pushes image to Docker Hub
   -> Jenkins SSHs into EC2
   -> Pulls latest image on EC2
   -> Runs container on port 5000
   -> Prometheus scrapes metrics
   -> Grafana visualizes dashboards

## 🖥️ Deployment (AWS EC2)

Stopped:Deployed...
Application deployed on AWS EC2 during CI/CD pipeline execution. Instance may be stopped to save cost.

## 📂 Project Folder Structure
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

## ⏱️ Cron Job Automation (Log Backup)

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

## ⚙️ Challenges & Learnings
Challenges

*Docker permission errors (docker.sock access denied)
*Jenkins unable to push to Docker Hub due to wrong credential ID
*SSH key mismatch between Jenkins and EC2
*EC2 IP change broke deployment flow
*Large Docker image caused slow push → fixed with .dockerignore
*Jenkinsfile indentation & credential issues
*Container removal error when old container didn’t exist

## Learnings

Docker user/group management and permissions
Jenkins credential handling (Docker Hub + SSH keys)
Setting up secure SSH authentication with EC2
Optimizing Docker images and improving push speed
Writing and debugging Jenkins pipelines
Understanding AWS networking (security groups, ports)
Automating tasks using cron jobs
Full real-world CI/CD implementation

## 📸 Screenshots 

Jenkins console output
<img width="940" height="513" alt="image" src="https://github.com/user-attachments/assets/ea7c4445-3a47-4388-851b-dd4149272396" />

Docker images
<img width="940" height="276" alt="image" src="https://github.com/user-attachments/assets/71d14518-1db9-461f-ac09-bb4e367419cc" />

Docker Hub repository
<img width="940" height="518" alt="image" src="https://github.com/user-attachments/assets/4178f505-2e6f-40be-9ab0-e6610129ab2e" />

EC2 instance running the application
<img width="940" height="480" alt="image" src="https://github.com/user-attachments/assets/9401e3fe-baae-4cea-8683-9636b0526b06" />

Prometheus & Grafana dashboards (if used)
<img width="940" height="521" alt="image" src="https://github.com/user-attachments/assets/3ff117ee-ed79-42ea-814e-c58494d663ef" />
<img width="940" height="229" alt="image" src="https://github.com/user-attachments/assets/6d2800fb-b7e1-4f5e-8e3d-5da38e4f9560" />
<img width="940" height="231" alt="image" src="https://github.com/user-attachments/assets/7617553a-d08b-4e37-9965-7c59b3016371" />
<img width="940" height="233" alt="image" src="https://github.com/user-attachments/assets/d605c4d5-e76e-44ac-8c94-03450cbf46be" />
<img width="940" height="233" alt="image" src="https://github.com/user-attachments/assets/3b8c67b6-cb92-42c6-bef0-b14344435e6a" />

Cron job backups
<img width="940" height="232" alt="image" src="https://github.com/user-attachments/assets/d474d29d-9fde-4a26-bf30-defc1d294efc" />
<img width="940" height="261" alt="image" src="https://github.com/user-attachments/assets/93b2def9-e2a8-4b60-a486-1a0a7a3b277c" />
Website
<img width="940" height="487" alt="image" src="https://github.com/user-attachments/assets/9978441c-32f0-4f1e-a12c-a62d1399e2cf" />

📎 Source Code
GitHub Repository:
https://github.com/IshuM210/Weather-Application.git

Conclusion
This project demonstrates a complete end-to-end DevOps pipeline—from code development to automated deployment, monitoring, and maintenance. Implementing this project strengthened my understanding of CI/CD, cloud deployment, containerization, automation, troubleshooting, and modern DevOps practices.

