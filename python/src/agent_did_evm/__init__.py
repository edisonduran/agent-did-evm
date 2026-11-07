"""Optional EVM registry adapter for Agent-DID (``pip install agent-did-evm``).

The core ``agent-did-sdk`` does not depend on this package. Until ``1.0.0rc5`` it shipped inside the core SDK
as ``agent_did_sdk.evm``.
"""

from __future__ import annotations

from .attestation import (
    REGISTRATION_ATTESTATION_TYPES,
    registration_attestation_domain,
    registration_attestation_message,
)
from .evm_registry import EvmAgentRegistry
from .evm_types import (
    EvmAgentRegistryAdapterConfig,
    EvmAgentRegistryContract,
    EvmTxResponse,
    RegistrationAttestation,
    RegistrationAttestationProvider,
    RegistrationAttestationRequest,
)
from .web3_client import Web3AgentRegistryContractClient

__all__ = [
    "REGISTRATION_ATTESTATION_TYPES",
    "EvmAgentRegistry",
    "EvmAgentRegistryAdapterConfig",
    "EvmAgentRegistryContract",
    "EvmTxResponse",
    "RegistrationAttestation",
    "RegistrationAttestationProvider",
    "RegistrationAttestationRequest",
    "Web3AgentRegistryContractClient",
    "registration_attestation_domain",
    "registration_attestation_message",
]
