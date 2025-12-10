🌦️ Weather Application — DevOps CI/CD Project
🔍 Project Description

A simple Flask-based weather reporting application that shows weather for user-entered cities.

This project demonstrates a complete DevOps pipeline:
GitHub → Jenkins → Docker → Docker Hub → AWS EC2 → Monitoring → Cron Job Automation.

🚀 Tech Stack / Tools & Services Used

Python + Flask – Backend

HTML/CSS – Frontend

Jenkins – CI/CD automation

Docker & Docker Hub – Containerization

AWS EC2 – Deployment

Prometheus & Grafana – Monitoring

Cron Jobs – Automated log backup

📦 How to Run Locally / Setup
1️⃣ Run Locally (Python)

For users without Docker or Jenkins.

git clone https://github.com/IshuM210/Weather-Application.git
cd Weather-Application
pip install -r requirements.txt
python app.py


Open in browser:
👉 http://localhost:5000

2️⃣ Run Using Docker
docker build -t weather-app .
docker run -d -p 5000:5000 weather-app


Open in browser:
👉 http://localhost:5000

🔄 CI/CD Pipeline Flow
Automated Pipeline Steps

Developer pushes code to GitHub

Jenkins triggers pipeline on commit

Jenkins builds Docker image

Jenkins pushes image → Docker Hub

Jenkins SSHs into EC2

Pulls latest Docker image

Runs the container on EC2 (port 5000)

Prometheus scrapes metrics

Grafana visualizes system metrics

Pipeline:
GitHub → Jenkins → Docker → Docker Hub → EC2 → Prometheus → Grafana

🖥️ Deployment (AWS EC2)

The application is deployed using Jenkins into an AWS EC2 Ubuntu instance.
Note: The instance may currently be stopped to save cost.

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

A cron job runs inside the EC2 instance to back up logs every minute.

Cron Entry
* * * * * /home/ubuntu/backup.sh

backup.sh Script
#!/bin/bash
SOURCE="/home/ubuntu/app-logs/app.log"
DEST="/home/ubuntu/backups"
mkdir -p $DEST

cp $SOURCE $DEST/app.log-$(date +"%Y-%m-%d_%H-%M-%S")
echo "Backup created at $(date)" >> /home/ubuntu/cron-job-history.log


✔ Creates timestamped log backups
✔ Runs automatically every minute

⚙️ Challenges

Docker permission error (docker.sock access denied)

Jenkins failed to push to Docker Hub (wrong credential ID)

SSH key mismatch between Jenkins & EC2

EC2 instance IP changed and broke pipeline

Large Docker image caused slow push (fixed using .dockerignore)

Jenkinsfile indentation & credential issues

Container removal error when old container didn’t exist

📘 Learnings

Managing Docker groups & permissions

Creating and configuring Jenkins credentials (SSH + DockerHub)

Properly setting up SSH authentication with EC2

Optimizing Docker builds for faster push

Writing/debugging Jenkins pipelines

AWS security groups, inbound rules, ports

Automating maintenance with cron jobs

End-to-end CI/CD exposure in real-world environment

📸 Screenshots
Jenkins Build

(Screenshot here)

Docker Images

(Screenshot here)

Docker Hub Repository

(Screenshot here)

EC2 Instance Running

(Screenshot here)

Prometheus & Grafana

(Screenshots here)

Cron Job Backups

(Screenshots here)

👉 Full screenshot set included in project report PDF.

📎 Source Code

GitHub Repository:
https://github.com/IshuM210/Weather-Application.git

🏁 Conclusion

This project demonstrates a complete end-to-end DevOps workflow—from development to automated CI/CD, containerization, deployment, monitoring, and scheduled maintenance.

Implementing this project strengthened understanding of:
✔ CI/CD pipelines
✔ Cloud deployment
✔ Docker/Kubernetes fundamentals
✔ Automation (cron)
✔ Monitoring tools
✔ Troubleshooting real DevOps issues

A complete real-world DevOps project experience.
