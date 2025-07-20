
# LangChain Knowledge Base API

This is the backend for managing knowledge bases, documents, and providing advanced querying using LangChain.

## Features:
- Create, read, update, and delete knowledge bases.
- Document upload and processing.
- RAG-enhanced querying for knowledge retrieval.
- Sentiment analysis and emotion detection.
- Long-term memory saving and retrieval.

## Docker Setup:
1. Build the Docker image:
    ```
    docker build -t langchain-backend .
    ```

2. Run Docker Compose:
    ```
    docker-compose up
    ```

## Kubernetes Deployment:
1. Deploy to Kubernetes using the provided deployment script:
    ```
    kubectl apply -f k8s_deployment.yaml
    ```
2. Expose the service and get the external IP:
    ```
    kubectl get svc langchain-backend
    ```

## Testing:
- To run the integration tests, use pytest:
    ```
    pytest app/tests/test_app.py
    ```
