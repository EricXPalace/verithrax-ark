# Bill of Materials (BOM) & Budgeting

| Item | Category | Specs | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Raspberry Pi 5** | Compute | 16GB RAM, ARM64 | 🟢 Pending (On route) | Master Node |
| **Raspberry Pi 5** | Compute | 16GB RAM, ARM64 | 🟢 Pending (On route) | Worker Node |
| **Raspberry Pi 5** | Compute | 16GB RAM, ARM64 | 🟢 Pending (On route) | Worker Node |
| **Raspberry Pi 2 Zero W** | Compute | 512MB RAM, ARM64 | 🟢 Pending (On route) | Light Worker Node |
| **Raspberry Pi 2 Zero W** | Compute | 512MB RAM, ARM64 | 🟢 Pending (On route) | Light Worker Node |
| **ASUS GP66** | Compute | i7, 64GB RAM, x86 | 🟢 Existing | Hybrid Node |
| **Cisco 3560-CX** | Network | 8-Port GE, PoE+ | 🟡 Saving money | Core Switch |
| **Cisco 2960-CX** | Network | 8-Port GE, PoE+ | 🟢 Pending (On route) | Sub Switch(Temporary Core) |
| **Cisco 2960-CX** | Network | 8-Port GE, PoE+ | 🟡 Saving money | Sub Switch |
| **NVMe SSD** | Storage | 2TB M.2 2280 | 🟢 Existing | Knowledge Base |
| **NVMe SSD** | Storage | 2TB M.2 2280 | 🟡 Saving money | Knowledge Base |
| **Pelican 1535** | Enclosure | Air Carry-On | 🟡 Planned | The "Ark" Shell |

# Software

| Name | Category | Source | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Docker** | Program | [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) | 🟢 Operational |  |
| **Ollama** | Docker Image | ollama/ollama:latest | 🟢 Operational | :11434 |
| **Open WebUI** | Docker Image | open-webui/open-webui:main | 🟢 Operational | :3000 |
| **Kiwix** | Docker Image | kiwix/kiwix-serve:latest | 🟢 Operational | :8081 |

> **Strategy:** Utilizing "Incremental Build" strategy to align with relocation budget. Phase 1 focuses on software architecture validation on Virtual Machines.