from app.policy import Decision, classify_action


def test_known_low_risk_action_is_allowlisted():
    assert classify_action("reminder.draft").decision is Decision.ALLOW


def test_external_side_effect_requires_approval():
    assert classify_action("message.send").decision is Decision.APPROVAL_REQUIRED


def test_payment_is_prohibited():
    assert classify_action("payment.execute").decision is Decision.DENY


def test_unknown_action_is_denied_by_default():
    assert classify_action("device.do_anything").decision is Decision.DENY


def test_every_prohibited_action_is_denied():
    for action in (
        "payment.execute",
        "credentials.read",
        "shell.execute",
        "root.access",
        "security.bypass",
        "app.install_silent",
        "policy.modify",
    ):
        assert classify_action(action).decision is Decision.DENY, action


def test_each_approval_action_requires_approval():
    for action in (
        "message.send",
        "calendar.create",
        "calendar.update",
        "calendar.delete",
        "content.publish",
        "data.share",
    ):
        assert classify_action(action).decision is Decision.APPROVAL_REQUIRED, action


def test_action_name_with_whitespace_is_not_implicitly_allowed():
    assert classify_action(" reminder.draft ").decision is Decision.DENY
