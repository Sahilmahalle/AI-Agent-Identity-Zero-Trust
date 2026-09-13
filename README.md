# AI-Agent-Identity-Zero-Trust

Project scaffold for AI Agent identity and zero-trust policies.

## Structure

- `src/` — source code
- `tests/` — test suite
- `policies/` — policy definitions
- `docs/` — documentation

## Getting started

Initialize a git repo and add your code:

```bash
cd AI-Agent-Identity-Zero-Trust
git init
```

# AI Agent Identity and Zero Trust

A practical security engineering project focused on securing AI agent
identities, credentials, tool access, authorization policies, and
Zero Trust enforcement.

## Project Goals

- Establish an AI agent identity model
- Implement authentication using JWT
- Apply RBAC and ABAC authorization
- Enforce policies using Open Policy Agent
- Use short-lived credentials
- Build a secure agent tool gateway
- Add monitoring and security telemetry
- Simulate and block unauthorized agent behavior

## Current Milestone

### Milestone 1: Python and REST API Foundation

The current milestone provides a basic FastAPI service and Python API
client. Authentication and authorization will be added in later milestones.

## Project Structure

```text
AI-Agent-Identity-Zero-Trust/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── api_client.py
├── tests/
│   └── test_api.py
├── policies/
├── docs/
│   └── week1-foundation.md
├── .gitignore
└── README.md

