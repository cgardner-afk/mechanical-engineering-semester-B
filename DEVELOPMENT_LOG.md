# Semester B Development Log and Decision Register

## Baseline — 2026-10-30
- Semester B repository: https://github.com/cgardner-afk/mechanical-engineering-semester-B
- Semester A reference: https://github.com/cgardner-afk/mechanical-engineering-semester-a
- Canonical lesson template: `mechanical_engineering_B_lesson_template.html`
- Template baseline version: **1.0** (browser verification pending)
- Completed student lessons: **none verified in the repository**
- Decision: Standard lessons require **2,000–4,000 substantive instructional words**; explicitly approved culminating design challenges may reach **4,500 words**.
- Decision: Backward design from actual unit assessments and final examination is mandatory.
- Decision: Anti-drift audit, approved lesson contract, engineering verification and completion checklist are mandatory.
- Decision: Scaffolded progression (Explain → Model → Guide → Practice Independently → Apply), retrieval/spaced review, multiple representations, misconception-based feedback, readiness checkpoints, authentic engineering decisions and student-experience audit are mandatory as appropriate.
- Decision: Each lesson must have a realistic completion-time estimate that includes activities and practice, not just reading.
- Decision: Publication of new lessons requires explicit user approval.
- Known issue: GitHub Pages deployment has not been verified.
- Known issue: Assessment coverage matrix is a schema only until actual blueprint/assessments are inspected.
- Next step: Inspect Semester B blueprint, unit tests/quizzes and final; prepare B1.1 contract for approval.

## Standards synchronization — 2026-10-30
- Master prompt updated to **version 3.1**.
- `COURSE_DEVELOPMENT_STANDARDS.md` and `LESSON_DEVELOPMENT_CONTRACT.md` synchronized to include student-learning requirements.
- Static validator updated to permit an explicitly approved 4,500-word culminating exception using a command-line flag; the flag itself does **not** constitute approval.
- Canonical HTML template remains **version 1.0**, unchanged.

## Design changes
| Date | Version | Change | Approval | Affected lessons |
|---|---|---|---|---|
| 2026-10-30 | 1.0 | Canonical template designated as baseline | User requested canonical template | Future Semester B lessons |

## Future lesson handoff entries
Record lesson ID, source and Pages links (if verified), contract approval, instructional word count, completion-time estimate, validation status, assessment coverage, student-experience audit, unresolved issues and next task.

## B1.1 contract approval — 2026-10-30
- **Approved by user:** B1.1 Simple Machines and Mechanical Advantage development contract (revised after Unit B1 QTI and final-bank v1.3 review).
- Scope: ideal and actual mechanical advantage, force–distance trade-offs, levers, inclined planes, pulleys, screw jacks, wheel-and-axle, and efficiency.
- Assessment references: Unit B1 families B1-01 through B1-04; final bank pool B-O1-P1. Preserve original secure assessment questions; create original practice.
- Instructional target: **3,200–3,600 substantive words**; estimated **85–105 minutes**.
- Lab: three modes — lever, inclined plane, real versus ideal; worked examples, independent practice, and sequential formative quiz.
- Template: canonical **1.0**.
- **Development approved; publication not yet approved.** QA, actual lesson completion, and GitHub Pages verification remain pending.

## B1.2 contract approval — 2026-10-30
- **User approved** the B1.2 Rotational Motion and Angular Speed development contract.
- Blueprint target: angular speed and conversions between rpm and rad/s; objective B-O1.
- Unit B1 assessment families B1-05, B1-06, B1-07; cumulative final pool B-O1-P2.
- Target: 3,000–3,400 substantive instructional words; 80–100 minutes; six or more worked examples; three-input rotating-wheel lab; seven question-first independent practice items with separately revealed solutions; approximately twelve sequential review questions.
- Canonical template v1.0. Development authorized; completed lesson publication remains subject to separate review and approval.

## B1.2 student-view draft — 2026-10-30
- Draft `mechanical_engineering_B1_2_complete_lesson.html` committed for student-view review, commit `6b2676de26e66e7af8d2ea5c94ee3732e0ea1606`. **Not finalized; user review pending.**
- Content: six worked examples, seven question-first/solution-second practice problems, rotating-wheel investigation with rpm/radius/time, and twelve-question sequential formative quiz.
- QA performed: Node JavaScript syntax check passed; headless Chromium via Playwright `page.set_content` checked lab calculations at 120 and 240 rpm, radius/time changes, trial record/reset/clear, practice solution disclosure, quiz advancement, and readiness feedback; no page errors in these checks.
- Approximate visible lesson word count: 3,478 by local HTML text extraction (includes headings and instructional support); approved target 3,000–3,400, so editorial word-count reconciliation remains open. Formal repository `validate_lesson.py` run, complete accessibility audit, all quiz branches, and live GitHub Pages deployment have not been independently verified.

## B1.3 development authorization — 2026-10-30
- User approved proceeding with Lesson B1.3, **Torque, Rotational Work, and Power**, under the proposed development contract.
- Blueprint target: calculate torque and rotational power; final assessment pool B-O1-P3 (shaft power from torque and rpm).
- Planned scope: 3,200–3,600 words; seven worked examples; three-mode interactive torque/work/power laboratory; seven question-first independent practice items with separately revealed solutions; twelve sequential review questions.
- Required teaching standard: explain all new notation before first use; retain B1.1/B1.2 student-facing design. **Development authorized; no lesson file published or QA completed yet.**

## B1.3 student-view draft — 2026-10-30
- Created and fetched `mechanical_engineering_B1_3_complete_lesson.html`; commit `e2103bf9a5b77a519aba61db2f5516e0ee82f438`. User review pending; **not finalized**.
- Core lesson text approximately 3,484 words (excluding glossary and review), seven worked examples, seven question-first practice problems, twelve sequential review questions, three lab modes.
- QA: JavaScript syntax passed; local Chromium via Playwright `set_content` verified torque controls (60 N × 0.5 m = 30 N·m; 100 N = 50 N·m; 0° = zero), work and shaft-power mode calculations, record/clear trial, quiz check/advance, and no page errors in tested flow.
- Outstanding: full formal HTML validator, all quiz branches, comprehensive accessibility audit, live GitHub Pages deployment verification, and final editorial/assessment coverage audit.

## B1.4 development contract approved — 2026-10-31
- User explicitly approved the B1.4 **Gears, Gear Ratios, and Gear Trains** development contract.
- Blueprint B-O1: output speed, rotation direction, and ideal torque ratios; final pools B-O1-P4 and B-O1-P5.
- Approved scope: 3,200–3,600 instructional words, seven worked examples, seven visible-question/expandable-solution practice items, ~12 sequential quiz questions, interactive 2-/3-gear and compound gear train lab with recorded trials.
- Mandatory: begin with canonical template; define all notation; test slider updates, gear direction, calculations, quiz, progress indicator, responsive overflow, and repository validator before sharing draft. Final publication requires separate user approval.

## B1.4 student-view review draft — 2026-10-31
- Created `mechanical_engineering_B1_4_complete_lesson.html`, latest commit `97016ad610a535176a92e8a9766289d5a30c1df1`; review draft, not finalized.
- Canonical Semester B shell, ten lesson sections, approximately 3,178 main-content words by rough HTML tag stripping, seven worked examples, seven visible practice questions with separately expandable solutions, 12 sequential quiz questions, and three gear-lab modes (pair, idler, compound).
- Verified GitHub file creation, JavaScript syntax via V8 compilation, no duplicate HTML IDs, and all statically referenced DOM IDs present.
- **Outstanding:** Actual browser interaction tests of slider updates, SVG behavior, all lab modes, trial table, quiz feedback, reading progress, responsive layout, and accessibility; repository validator not run. Do not claim these passed. User review and final approval pending.

## B1.4 review correction audit — 2026-10-31
- Confirmed the GitHub source now contains 13 individual glossary accordion disclosures (`details`/`summary`) and a prominent five-equation quick reference at the start of the Engineering Concepts section, with symbol key and direction rule.
- Confirmed all ten lesson sections, seven practice disclosures, 12 sequential review questions, approximately 3,475 words by rough HTML stripping, no duplicate element IDs, no statically missing DOM ID references, and JavaScript syntax compiles.
- **Still pending:** full interactive browser QA, accessibility/mobile visual audit, repository Python validator execution, and user acceptance. B1.4 remains a review draft, not finalized; B1.5 development on hold pending review.

## B1.5 development contract approved — 2026-10-31
- User approved B1.5 **Belts, Pulleys, and Mechanical Drives** plan, B-O1 blueprint target: analyze drive ratios and transmission losses; cumulative final pool B-O1-P6 belt-drive speed ratio.
- Authorized development: 3,200–3,600 instructional words; seven worked examples; seven independent visible practice questions with separately expandable solutions; ~12 sequential review questions; interactive belt-drive lab with ideal ratio, slip/direction, and efficiency/power modes; trial recording and clearing.
- Mandatory canonical shell and lesson styling, **prominent formula quick reference** with symbols and **individual accordion glossary entries**. Browser QA, responsive layout, validator, and user review required before finalization.

## B1.5 student-view draft — 2026-10-31
- Created `mechanical_engineering_B1_5_complete_lesson.html`, latest structural fix commit `7a7c3cb69b051201901358b8917687198f1da684`. Canonical template and all ten required sections; prominent five-formula reference; 18 accordion glossary terms; seven worked examples; seven expandable practice solutions; 12-question sequential review.
- Interactive lab implements ideal pulley ratio, slip/direction, and efficiency/power modes with updated SVG, live calculations, recording/clearing/resetting trials. Script passed V8 syntax check; DOM references and duplicate IDs checked. A post-edit structural check detected and repaired a missing worked-section boundary before review.
- **Not yet verified:** actual browser operation, responsive/mobile layout, repository Python validator, GitHub Pages propagation. User review/final approval outstanding. This is a review draft only.
