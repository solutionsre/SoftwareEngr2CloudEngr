# 🚀 Cloud Portfolio: Serverless App with CI/CD & Monitoring

## 📁 Folder Structure

```
.
├── app/                  # Lambda function code
│   └── main.py
├── infrastructure/       # Terraform configurations
│   └── main.tf
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions CI/CD pipeline
├── monitoring/           # Monitoring configs (Grafana/Prometheus)
│   └── config.txt
└── README.md
```

## 🛠️ Technologies
- AWS Lambda (Python)
- Terraform (Infrastructure as Code)
- GitHub Actions (CI/CD)
- Prometheus + Grafana (Monitoring - placeholder)
- IAM Roles & Secrets Management

## 🚀 Deployment

### Terraform

```bash
cd infrastructure
terraform init
terraform apply
```

### GitHub Actions

- Triggered automatically on changes to `infrastructure/`
- Applies Terraform to deploy Lambda

### Monitoring

- Monitoring config placeholders for Prometheus and Grafana.
- Customize based on Prometheus operator or EC2-based agents.

## ✨ Credits
Built for cloud engineer portfolio — inspired by [Vaibhav Sadhwani](https://linkedin.com/in/vsadhwani/)
