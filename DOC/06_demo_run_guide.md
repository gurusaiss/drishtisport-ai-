# DrishtiSport AI — Demo (v2: record-then-show, not live-in-front-of-judges)

## What changed and why

The first version asked whoever was in front of the camera to physically bowl live
during the demo, with the app auto-detecting the release point. Two problems with
that: (1) no judge is going to get up and test it themselves, and a presenter
performing an arm motion mid-pitch is awkward; (2) auto-detecting the exact release
instant from motion alone is unreliable and produced a confusing readout.

**Fixed by matching how the real product — and last year's Sport & Tech winner,
NextPlay.AI — actually works: video in, analysis out, no one has to demonstrate
their own body live.**

New workflow:
1. **Record a short clip of yourself doing a bowling action once**, calmly, in good
   lighting, no pressure — on your phone or webcam.
2. **Run that clip through the app.** While it plays back, you press **SPACE** at
   the exact instant of ball release — this replaces the old unreliable auto-
   detection with a clean, repeatable, presenter-controlled trigger. Everything
   else (pose tracking, joint-angle math, the 15° legality check) is identical —
   only the release instant is marked by you instead of guessed by the code.
3. The app shows a **big, unambiguous result card** (LEGAL / ILLEGAL, extension
   angle, logged confirmation) and can simultaneously **save the whole thing as an
   annotated output video** you just play back during your actual pitch — no live
   tracking risk during the real presentation at all.

## Step 1 — Record your clip

Any phone or webcam video of a full bowling arm action (backswing → delivery →
release → follow-through), a few seconds long, arm clearly visible, is enough.
Do 2-3 takes if you can — you want one clean "legal" take and ideally one
exaggerated "illegal" take (deliberately over-straighten the elbow at release) so
you can show both verdicts.

## Step 2 — Run it and mark the release point

```bash
python drishtisport_demo.py --video your_clip.mp4
```

- A window opens playing your clip with a live green/red skeleton overlay and a
  simple 2-line HUD: current elbow angle, and "press SPACE at ball release."
- Watch the clip, and **press SPACE at the exact frame the ball leaves the hand.**
- A large result card appears immediately: **LEGAL ACTION** or **ILLEGAL ACTION**,
  with the extension angle and confirmation it was logged.
- Press `q` any time to quit. Re-run as many times as you like until you're happy
  with the timing of your SPACE press.

If your bowling arm is your left arm: add `--arm left`.
If a take plays too fast to time your press well: add `--slow 0.5` (half speed).

## Step 3 — Save the final version to actually show judges

Once you're happy with a take:

```bash
python drishtisport_demo.py --video your_clip.mp4 --export final_demo.mp4
```

This does the exact same live run (still press SPACE at release) but **also
writes the whole annotated result — skeleton overlay, HUD, and the final result
card — to `final_demo.mp4`.** That file is your actual demo asset: just play it
like a normal video during your pitch/recording. No live webcam, no waiting on
detection, no risk of it glitching in front of anyone. It's still 100% genuine
model output — just captured once, calmly, instead of live under pressure.

## Step 4 — Show the verified log (optional, strong closer)

```bash
python view_log.py
```

Prints every delivery you've verdicted this session — timestamp, angles, verdict
— your "tamper-proof, data-backed talent score" concept made real and visible.

## For your 4-minute pitch video specifically

Use `final_demo.mp4` (or a ~15-20 second trimmed slice of it covering the moment
of the SPACE press through the result card) as the demo clip in the Solution
section of your script — exactly the slot already planned for this. Trim to just:
a few seconds of the tracked arm mid-delivery → the SPACE-triggered moment →
the result card holding on screen. You don't need to show the whole clip, just
the moment it proves itself.

## Practice tips
1. Do a few dry runs of pressing SPACE before recording your final take — timing
   it to the actual release moment takes one or two tries to get a feel for.
2. Good lighting, plain background, and the whole arm clearly in frame give
   MediaPipe the cleanest tracking.
3. Get one clean LEGAL and one clean ILLEGAL take — showing the threshold catch
   both ways proves the logic works, not just a single lucky result.
4. If tracking looks jittery, re-check lighting first — that's the most common
   fix, before touching any code or thresholds.

## What this proves to judges (mapped back to your pitch)
- **Innovation**: a real ICC rule (Law 24.3, 15°) as the threshold, not an invented "form score."
- **Technical depth**: live joint-angle math from raw pose landmarks, visible on screen, exported as proof.
- **Demo effectiveness**: a real, working, on-device pipeline shown the same way any real sports-analytics product is used — video in, analysis out — not a live performance stunt.
- **Business/social angle**: the logged, timestamped record is your anti-bias, verified-scouting feature made tangible.
