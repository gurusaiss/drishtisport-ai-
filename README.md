# DrishtiSport AI

**Samsung Solve for Tomorrow 2026 — Theme 3: Sport & Tech — Top 100 Shortlisted**

A free, 100% offline smartphone app that turns any budget camera into a real-time
biomechanics coach. On-device computer vision (MediaPipe pose tracking + a
lightweight ONNX model) reads joint angles in real time — the flagship working
module checks a cricket bowling action against the ICC's actual 15° elbow-
extension legality rule (ICC Law 24.3), flags unsafe/illegal technique instantly,
and logs every delivery to a local, tamper-proof performance record.

Built solo by [Your Full Name], Gayatri Vidya Parishad College of Engineering
(GVPCE), Visakhapatnam.

## Repository structure

- **[`DOC/`](DOC/)** — everything submitted or prepared as documentation for the
  competition, in order:
  - [`00_phase1_form_submission.md`](DOC/00_phase1_form_submission.md) — the exact Phase 1 application text as filed, plus the refined framing used from Top 100 onward
  - [`02_competition_research.md`](DOC/02_competition_research.md) — competitive research on Samsung Solve for Tomorrow's history, past winners, and judging patterns
  - [`03_pitch_deck_prompt.md`](DOC/03_pitch_deck_prompt.md) — the full Gamma AI prompt used to generate the Top 100 pitch deck, including all finalized slide content
  - [`04_pitch_video_script.md`](DOC/04_pitch_video_script.md) — the timed 4-minute pitch video narration script
  - [`04_pitch_video_script.html`](DOC/04_pitch_video_script.html) — rendered HTML version of the same script
  - [`05_logo_generation_prompt.md`](DOC/05_logo_generation_prompt.md) — the AI image-generation prompt used for the project logo
- **[`demo/`](demo/)** — the working MVP: `drishtisport_demo.py` (live bowling-action legality checker) and `view_log.py` (verified delivery-log viewer). See [`demo/README_DEMO.md`](demo/README_DEMO.md) for how to run it.

## Note on large media files

Recorded demo takes, the exported pitch video, the final PPTX/PDF deck, and the
SQLite log file are intentionally **not** committed to this repository (see
`.gitignore`) — they're large binary/video assets better hosted elsewhere (Google
Drive/YouTube link + QR code, per the submission) rather than versioned in git.
