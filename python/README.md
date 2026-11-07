# agent-did-evm (Python)

Optional EVM registry adapter for [Agent-DID](https://github.com/edisonduran/agent-did): `EvmAgentRegistry` and a web3.py contract client for the `AgentRegistry` contract in this repository. The core `agent-did-sdk` does not depend on it; the EVM profile is deferred outside core 1.0 (see `docs/RFC-001-EVM-Profile.md`).

```bash
pip install --pre agent-did-evm
```

```python
from agent_did_sdk import AgentDidClient
from agent_did_evm import EvmAgentRegistry, Web3AgentRegistryContractClient

registry = EvmAgentRegistry(...)  # see examples/evm_registry_wiring.py
```

## Moving from `agent_did_sdk.evm`

Up to `agent-did-sdk` `1.0.0rc4` this adapter shipped inside the core SDK as `agent_did_sdk.evm` (extra `[evm]`). From `1.0.0rc5` it is this separate package:

```diff
- pip install "agent-did-sdk[evm]"
+ pip install --pre agent-did-evm
- from agent_did_sdk.evm import EvmAgentRegistry
+ from agent_did_evm import EvmAgentRegistry
```

The classes and functions are the same.

## Development

```bash
cd python
pip install -e ".[dev]"
ruff check src/ tests/ scripts/ examples/
mypy --strict src/
pytest -q
```

The smokes (`scripts/e2e_smoke.py`, `scripts/revocation_policy_smoke.py`) start a local Hardhat node from `../contracts` (run `npm --prefix ../contracts ci` first).
