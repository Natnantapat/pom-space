# Pom Space

Private source distribution for an independent Operations workspace.

## Download and run
1. Download this repository using **Code → Download ZIP** and extract it.
2. Run `python3 unpack.py` (Windows: `py unpack.py`), then open the extracted `pom-space` folder.
3. Install Node.js 22.16 or later.
4. Run `npm ci`, `npm run build`, then `npm start`.
5. Open http://127.0.0.1:4101 . Keep the server running.

The ZIP contains the complete source tree, not an installed app. Source files are packaged inside the ZIP in this repository; extract them before editing.

## Included
- Thai/English Operations workspace with configurable project scope.
- Telegram account connector with explicit chat selection; optional bot connector.
- Outlook connector, message Inbox, local task review and Link library.
- Fictional onboarding examples; separated feature folders, runtime AI rules, skills, architecture and governance documents.

## Setup and current limits
Connect only your own authorised accounts. No Bee credentials, sessions, chats, runtime data or model weights are included. Local Qwen requires separate setup. Telegram sessions are memory-only. Manual sync reads up to 50 messages per selected chat. AI triage processes batches of ten. Link descriptions currently use chat context and domain-based category hints; webpage reading, historical sync and verified mention detection are not complete. Local tasks are not automatically published to Redmine. Browser-local link/review data needs export backup.

Read `README.md`, `AGENTS.md`, `docs/architecture/communications.md` and `docs/governance/communications.md` inside the ZIP before modifying the app. The source package includes a SHA-256 file manifest. Never upload runtime, .env, credentials or personal exports.

The source ZIP is split into 20 MB parts for GitHub browser upload. Keep every part together; unpack.py verifies the combined SHA-256 before extracting.
