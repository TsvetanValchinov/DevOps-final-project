# DevOps Final Project: Automated Software Delivery Pipeline

Този проект демонстрира модерен CI/CD процес за Python приложение, покриващ целия жизнен цикъл на софтуера - от написването на кода до деплоймънта в Kubernetes.

[![CI/CD Pipeline](https://github.com/TsvetanValchinov/DevOps-final-project/actions/workflows/main.yml/badge.svg)](https://github.com/TsvetanValchinov/DevOps-final-project/actions/workflows/main.yml)

## 🚀 High-Level Solution Design

Диаграмата по-долу илюстрира автоматизирания процес, включително интегрираните проверки за сигурност.

```mermaid
graph TD
    classDef plain fill:#fff,stroke:#333,stroke-width:2px,color:#000,font-weight:bold;
    classDef security fill:#ffcccc,stroke:#ff0000,stroke-width:2px,stroke-dasharray: 5 5,color:#000,font-weight:bold;
    classDef k8s fill:#e6f7ff,stroke:#0066cc,stroke-width:2px,color:#000,font-weight:bold;

    Dev["🧑‍💻 Developer<br/>(Local Machine)"] -->|Git Push / Pull Request| GitHub["GitHub Repository<br/>(Source Control)"]

    subgraph CI_Pipeline ["GitHub Actions (CI Flow)"]
        GitHub -->|Trigger| Lint["🔍 Linter & Tests<br/>(Quality Check)"]
        Lint --> Bandit["🛡️ SAST Scan<br/>(Bandit - Deep Dive)"]
        Bandit --> Build["🐳 Docker Build"]
        Build --> Trivy["🛡️ Image Scan<br/>(Trivy - Deep Dive)"]
    end

    Trivy -->|Push Image| DockerHub["Docker Hub<br/>(Registry)"]
    
    subgraph CD_Deployment ["Continuous Delivery"]
        DockerHub -.->|Pull Image| K8sCluster
        Trivy -->|Update Manifests| K8sCluster["Kubernetes Cluster<br/>(Deployment & Service)"]
    end

    class Bandit,Trivy security;
    class K8sCluster k8s;
    class Dev,GitHub,Lint,Build,DockerHub plain;
