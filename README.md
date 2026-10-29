# Pom Space

Public source distribution for an independent Operations workspace. Updated 30 October 2026 with the modular foundation refactor.

## Download and run
1. Choose **Code → Download ZIP** and extract it.
2. Run `python3 unpack.py` (Windows: `py unpack.py`). It verifies all four parts before extracting the `pom-space` folder.
3. Install Node.js 22.16 or later, then inside `pom-space` run `npm ci`, `npm run build`, and `npm start`.
4. Open http://127.0.0.1:4101 while the server is running.

This is source code, not a hosted application. All four archive parts are required. Extract to a new folder when upgrading; keep private runtime data separately.

## Modular foundation
- 99 frontend files relocated by feature: Tasks, KPI, Inbox, Reports, Connections, Chat, and other modules.
- API endpoints split into 15 route modules; persistence and external adapters remain separate.
- Shared UI, API client, bilingual infrastructure and global styles have dedicated folders.
- Separate `ai/workflows`, `ai/evals`, AI harness, `skills`, `rules`, `knowledge`, architecture and governance documentation.
- See `pom-space/docs/architecture/project-layout.md`, `relocation-manifest.json`, and `verification.md` after extraction.
- Run `npm run test:foundation` and `npm run build` after structural edits.

## Verification and remaining limits
Production build passed; 12 backend foundation tests and 64 frontend tests passed. Dashboard, Connections, Inbox and Link library were checked in the browser. Full server suite: 142 passed, 1 failed in the retained demo lifecycle test (it expects failure while current code returns a template fallback). This mismatch is documented, not skipped. Large bundle/global CSS and some App orchestration remain; this is not a claim of complete architectural isolation.

## Accounts and data
Thai/English Operations workspace with configurable project scope, Outlook and Telegram connectors, message triage, Link library and fictional onboarding examples. Connect your own authorised accounts. No Bee credentials, sessions, chats, runtime data or model weights are included. Do not upload `.env`, runtime, tokens or private exports.

Local Qwen needs separate setup. Telegram sessions are memory-only; manual sync reads up to 50 messages per selected chat, and AI triage processes batches of ten. Historical sync, verified mentions and automatic webpage reading are not complete. Local tasks are not automatically published to Redmine. Browser-local links and review markers need backup. Knowledge documents are not automatically ingested by AI.

The source archive contains a SHA-256 file manifest. Source is packaged in four parts due to browser upload limits; folders become visible after extraction.
