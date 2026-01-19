# ThemisAevra Core SDK

<div align="center">
  <img src="./assets/logo.svg" alt="ThemisAevra Logo" width="200"/>
  <br>
  <h3>Human-Level Intelligence for Physical Agents</h3>
</div>

<br>

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/themisaevra-core)](https://pypi.org/project/themisaevra-core/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ThemisAevra/Core-SDK/ci.yml?branch=main)](https://github.com/ThemisAevra/Core-SDK/actions)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Discord](https://img.shields.io/discord/1234567890?color=5865F2&label=discord&logo=discord&logoColor=white)](https://discord.gg/themisaevra)

</div>

**ThemisAevra Core** is the standard interface for communicating with ThemisAevra's high-performance cognitive engine. This SDK provides the typed protocols, simulation hooks, and fleet management primitives necessary to integrate autonomous physical agents into your infrastructure.

> **Note**: This repository contains the *Public Interface* and connectivity tools. The core Cognitive Engine is proprietary and accessed via the ThemisAevra Cloud API or on-premise Edge Server.

## 🧠 Architecture

The ThemisAevra Stack operates on a **Neuro-Symbolic** principle, separating high-level reasoning (Cloud LLM) from real-time motor control (Edge Reflex).

```mermaid
graph TD
    User[Fleet Command] -->|gRPC/Safety| SDK[ThemisAevra SDK]
    SDK -->|Task Stream| Nexus[Cloud Planner (LLM)]
    Nexus -->|Decomposed Plan| Cortex[Edge OS (Orin NX)]
    Cortex -->|Reflex Loop (1kHz)| Servo[Actuation]
```

## 🚀 Features

- **Agent Protocol**: Standardized gRPC/REST types for tasking and telemetry.
- **Vision Integration**: Hooks for pre-processing frames using ThemisAevra's `ViT-H/14` pipelines.
- **Motion Planning**: RRT* primitives for trajectory validation.
- **Simulation Bridge**: "Digital Twin" parity with Isaac Sim and Gazebo.
- **Safety Layer**: Hard real-time constraints compliant with **ISO 10218**.

## 📦 Installation

```bash
pip install themisaevra-core
```

## ⚡ Quick Start

```python
import themisaevra
from themisaevra.vision import VisionTransformer

# 1. Initialize Connection (Secure Handshake)
agent = themisaevra.Agent(id="unit-alpha-01", auth_token="sk_live_...")

# 2. Define a Complex Task
mission = themisaevra.Task(
    natural_language="Inspect the pipes in Sector 7 for leakage.",
    constraints={
        "safety_level": "HUMAN_COLLABORATIVE",
        "max_velocity": 0.5 # m/s
    }
)

# 3. Deploy & Monitor
stream = agent.deploy(mission)
for signal in stream:
    print(f"Status: {signal.state} | Confidence: {signal.confidence:.2f}%")
```

## 🔬 Research & Papers

ThemisAevra Core implements algorithms described in our research:
- *Real-time Neuro-Symbolic Control for Humanoids* (IROS 2025)
- *Semantic Occupancy Grids via ViT-H/14* (CVPR 2026)

See [CITATION.cff](CITATION.cff) for referencing these works.

## 🤝 Community & Support

- **Discord**: Join 5,000+ engineers in our [Discord Community](https://discord.gg/themisaevra).
- **Docs**: Full API reference at [docs.themisaevra.com](https://docs.themisaevra.com).
- **Twitter**: Follow [@ThemisAevra](https://twitter.com/ThemisAevra).

## 📜 License

Apache 2.0 - See [LICENSE](LICENSE) for details.
