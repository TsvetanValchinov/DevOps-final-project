# DevOps Final Project: Automated Software Delivery Pipeline

Този проект демонстрира CI/CD процес за Python приложение, покриващ целия жизнен цикъл на софтуера - от написването на кода до деплоймънта в Kubernetes.

[CI/CD Pipeline](https://github.com/TsvetanValchinov/DevOps-final-project/actions/workflows/main.yaml)

## High-Level Solution Design

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
```
## Покрити теми от курса (Project Scope)

Проектът реализира следните 9 DevOps практики:

* **Source Control:** Използване на Git и GitHub за управление на версиите.
* **Collaborate:** Работа чрез Feature branches и Pull Requests.
* **Branching Strategies:** Защита на main бранча и задължителен Code Review.
* **Docker:**  Използване на Docker за контейнеризация. --> Dockerfile.
* **Building Pipelines:** Автоматизиран Workflow с GitHub Actions.
* **Continuous Integration (CI):** Автоматично стартиране на Unit тестове (pytest) и Linter (flake8).
* **Security (Deep Dive):**
  * SAST (Static Application Security Testing) с Bandit.
  * Container Vulnerability Scanning с Trivy.
* **Continuous Delivery (CD):** Автоматично обновяване на Kubernetes манифестите чрез sed заместване.
* **Kubernetes:** Дефиниране на Infrastructure as Code чрез YAML манифести (Deployment & Service).

## 🛠️ Технологичен Стак

* **Language:** Python 3.9 (Flask)
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **CI/CD:** GitHub Actions
* **Security:** Bandit (Code), Trivy (Image)
* **Testing:** Pytest
