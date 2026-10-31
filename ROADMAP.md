# VEDA roadmap

## Prototype in this ZIP
- [x] Kotlin/Compose chat shell
- [x] User-selected local `.litertlm` model import
- [x] LiteRT-LM local inference integration attempt
- [x] Optional backend policy scaffold and basic tests
- [x] GitHub Actions workflows for backend tests and Android debug build

## Verification gates before calling this usable
- [ ] GitHub Android build succeeds from a clean checkout
- [ ] Install APK on Redmi 13 5G
- [ ] Import compatible Qwen `.litertlm` model
- [ ] Confirm inference completes without crashes or memory failure
- [ ] Confirm no network request is made for local inference
- [ ] Check app lifecycle/resource cleanup and long prompts

## Next increments (not yet implemented)
1. Improve chat UX: scrolling, conversation persistence, empty/error states, stop generation.
2. Add local reminder storage and Android notifications, with exact scheduling behavior and notification permission handling.
3. Add fixed allowlist app-opening intents.
4. Add browser intents/search through Android-supported APIs.
5. Add calendar read/write with runtime permission and approval UI.
6. Add optional notification listener with a clear opt-in flow and no background forwarding.
7. Add WhatsApp draft flow using supported intents; user sends manually.
8. Add tool registry, argument schemas, policy engine, approval lifecycle, and tests before enabling any action.

A feature is not complete until it has tests, permission/approval handling where applicable, and device verification.
