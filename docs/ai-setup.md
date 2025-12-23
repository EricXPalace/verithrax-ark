# Docker command to run ollama

This doc is for command storage to run docker on Windows 11.

## Before running docker
1. Install WSL2
2. Install Docker Desktop
3. Install WSL2 Integration

**Checking!** Using `docker --version` to check if docker is installed.

## Running docker
1. Open WSL2
2. Run `docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi` to check if GPU is working.

### Run Ollama
```bash
docker run -d --gpus=all \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  --restart always \
  ollama/ollama
```
* Run Gemma3: `docker exec -it ollama ollama run gemma3:4B`
### Run Open WebUI
```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```
* Access Open WebUI: `http://localhost:3000`
### Run Kiwix
```bash
docker run -d \
  -p 8081:8080 \
  -v /mnt/d/Kiwix:/data \
  --name kiwix \
  --restart always \
  ghcr.io/kiwix/kiwix-serve:latest \
  *.zim
```
* Put .zim files on D:\Kiwix
* Access Kiwix: `http://localhost:8081`