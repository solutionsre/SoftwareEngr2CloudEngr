# 🌐 Cloud Portfolio: Full Serverless Project (Lambda + API Gateway + DynamoDB + Monitoring)

## 📁 Folder Structure

```
.
├── app/                    # Lambda source code
├── infrastructure/         # Terraform IaC setup
├── .github/workflows/      # GitHub Actions CI/CD
├── monitoring/             # Prometheus + Grafana setup
├── screenshots/            # Add deployment & dashboard screenshots
└── README.md
```

## 🛠️ Stack
- AWS Lambda + API Gateway + DynamoDB
- Terraform
- GitHub Actions (CI/CD)
- Prometheus & Grafana (for monitoring)

## 🚀 Quickstart

### 1. Build Lambda Deployment Package
```bash
cd app
chmod +x build.sh
./build.sh
```

### 2. Deploy with Terraform
```bash
cd infrastructure
terraform init
terraform apply
```

### 3. API Endpoint
After deployment, Terraform will output your API Gateway endpoint.

### 4. Monitor
Monitoring configs are under `/monitoring`. Setup in EC2 or Docker environment.

## 📷 Screenshots
Add your screenshots of:
- Lambda function deployed
- API Gateway endpoint test
- Monitoring dashboards

## ✨ Credits
Inspired by: [Vaibhav Sadhwani](https://linkedin.com/in/vsadhwani/)
