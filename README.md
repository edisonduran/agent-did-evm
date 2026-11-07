# Agent-DID EVM profile

The optional, **deferred** EVM profile of [Agent-DID](https://github.com/edisonduran/agent-did): an on-chain `AgentRegistry` contract and the adapters that let the Agent-DID SDKs use it as their registry.

| Path | What | Published as |
|---|---|---|
| `contracts/` | `AgentRegistry.sol` (Hardhat): registration with an EIP-712 registrar attestation, revocation, delegates, ownership transfer | not published |
| `evm/` | TypeScript adapter `EvmAgentRegistry` + ethers v6 contract client | npm `@agentdid/evm` |
| `python/` | Python adapter `EvmAgentRegistry` + web3.py contract client | PyPI `agent-did-evm` |
| `docs/RFC-001-EVM-Profile.md` | The profile and its status | |

**Status.** The EVM profile is not part of the core Agent-DID `1.0` release: the core SDKs (`@agentdid/sdk`, `agent-did-sdk`) do not depend on it, and `did:webvh` is the canonical method. This code lived in the main repository until `1.0.0-rc.5` and was moved here with its history; see the ADR in the main repository (`docs/ADR-004-EVM-Profile-Satellite.md`).

## Development

```bash
npm --prefix contracts ci && npm --prefix contracts test   # Hardhat tests
npm --prefix evm ci && npm --prefix evm run build && npm --prefix evm test
npm run smoke:e2e          # Hardhat node + contract + @agentdid/evm + @agentdid/sdk
npm run smoke:policy       # revocation policy of the contract
npm run audit:contracts    # Slither and Mythril (Docker)
```

Python: see [`python/README.md`](python/README.md).

## Security

Report vulnerabilities as described in the main repository's [SECURITY.md](https://github.com/edisonduran/agent-did/blob/main/SECURITY.md).

## License

Apache-2.0.
