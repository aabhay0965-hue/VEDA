"""Deny-by-default classification for proposed VEDA actions.
This module classifies requests only; it does not execute actions.
"""
from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    APPROVAL_REQUIRED = "approval_required"
    DENY = "deny"


@dataclass(frozen=True)
class PolicyResult:
    decision: Decision
    reason: str


# Actions requiring explicit user approval before Android may carry them out.
APPROVAL_ACTIONS = {
    "message.send",
    "calendar.create",
    "calendar.update",
    "calendar.delete",
    "content.publish",
    "data.share",
}
# Explicitly prohibited actions.
DENIED_ACTIONS = {
    "payment.execute",
    "credentials.read",
    "shell.execute",
    "root.access",
    "security.bypass",
    "app.install_silent",
    "policy.modify",
}
# Low-risk action intents; Android still owns permission and execution.
ALLOWLIST_ACTIONS = {
    "app.open_approved",
    "website.open_approved",
    "reminder.draft",
}


def classify_action(action: str) -> PolicyResult:
    """Classify an action name with conservative defaults."""
    if action in DENIED_ACTIONS:
        return PolicyResult(Decision.DENY, "This action is prohibited by VEDA policy.")
    if action in APPROVAL_ACTIONS:
        return PolicyResult(Decision.APPROVAL_REQUIRED, "Show the exact action to the user and require confirmation.")
    if action in ALLOWLIST_ACTIONS:
        return PolicyResult(Decision.ALLOW, "Allowlisted intent; Android must still enforce permissions and user control.")
    return PolicyResult(Decision.DENY, "Unknown actions are denied by default.")
