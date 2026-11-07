# Changelog

## [Unreleased]

### Changed

- Moved out of the Agent-DID monorepo (`edisonduran/agent-did`) with its git history: `contracts/`, `evm/` (`@agentdid/evm`) and the Python adapter, which was `agent_did_sdk.evm` inside `agent-did-sdk` and is now the separate package `agent-did-evm` (`import agent_did_evm`), version `1.0.0rc5`.
- The end-to-end smoke builds `@agentdid/evm` against `@agentdid/sdk` from npm instead of the monorepo checkout.
