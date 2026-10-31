# Semester B Course Development Standards — v1.0

## Governing rules
1. Curriculum objectives and the actual unit quizzes/tests and cumulative final determine instructional requirements before drafting.
2. The approved canonical HTML template controls reusable design and interaction patterns; changes require approval and a version entry.
3. Technical correctness, safety, assessment alignment, accessibility, and verified functionality outrank visual novelty and response brevity.
4. If requirements conflict, flag the conflict and ask for a decision; do not silently discard one.
5. Work one lesson at a time. The user approves the development contract before lesson coding and approves the completed lesson before publication.
6. Never claim testing, GitHub publication, Pages availability, or assessment coverage that was not verified.

## Lesson length
Each finished student-facing lesson must contain **2,000–4,000 words of substantive instructional prose**. Count visible student instructional text, including explanations, worked-example narratives, lab instructions and analysis, practice questions/solutions, glossary definitions, summary, and quiz questions/explanations. Exclude HTML/CSS/JS source, navigation labels, buttons, repeated UI boilerplate, and hidden developer instructions. Do not pad with repetition. Record the estimated instructional word count and the counting method. If word-count automation cannot distinguish instructional prose reliably, manually review the estimate. This requirement applies to completed lessons, not the canonical template.

## Lesson Development Contract — mandatory before coding
Use `LESSON_DEVELOPMENT_CONTRACT.md`. Include lesson ID, curriculum objectives, assessment question types, final-exam links, prerequisite skills, planned reading sections, engineering examples, simulation/lab purpose, independent practice, quiz coverage, and template version. Obtain approval before writing the complete lesson.

## Definition of done
A lesson is **not complete** until:
- Approved contract and source-backed assessment-to-instruction map exist.
- Each relevant assessment skill is explicitly taught, modeled, practiced, and reviewed with comparable cognitive demand.
- Substantive instructional text is between 2,000 and 4,000 words; no filler or placeholders.
- Engineering calculations and units have been independently checked, including simulation boundary and representative inputs.
- All required sections, links, navigation, glossary, worked solutions, sequential quiz, and appropriate interactive lab function.
- Responsive and keyboard-accessible presentation, clear labels, feedback, and no color-only information.
- The HTML validator has run and all blocking findings are resolved; visual/browser checks and JS interaction tests are recorded separately.
- The anti-drift comparison against the approved template and relevant Semester A exemplar is documented.
- Publication is explicitly authorized; the GitHub commit is verified, and Pages is only claimed when independently verified.
- `DEVELOPMENT_LOG.md` and `ASSESSMENT_COVERAGE_MATRIX.csv` are updated with grounded results.

## Template governance
Canonical file: `mechanical_engineering_B_lesson_template.html`. Initial baseline version **1.0**. Record the version used for each lesson. A proposed design change must be explained and approved before modifying the template; record version, date, rationale, affected lessons, and migration guidance. Avoid ad-hoc visual changes in individual lessons.

## Assessment coverage
The coverage matrix must track assessment skill IDs, source question references (not confidential question text), unit/final coverage, target lesson, and evidence for introduction, modeling, independent practice, and revisit. Mark unverified mappings as pending, not complete. No invented assessment references.

## Independent engineering QA
For each worked example, independently recalculate the result and inspect units, sign conventions, precision, physical interpretation, and assumptions. For each simulation, test zero, min, max, and typical values; verify the displayed SVG/state matches numerical results. Document test cases and failures. Static HTML inspection does not substitute for browser interaction testing.

## Accessibility and recovery
Require keyboard controls, semantic landmarks, visible focus, readable contrast, screen-reader labels for diagrams and controls, feedback announced without color alone, and a responsive layout. If files or tools are unavailable, state the exact gap and stop at the appropriate stage; preserve work, do not invent evidence, and do not quietly simplify. If output is too long, continue in coherent stages without lowering instructional depth.

## Standard workflow
Inspect sources → map assessment requirements → approve lesson contract → adapt canonical template → write 2,000–4,000 instructional words → validate engineering and HTML → browser/interaction test → audit assessment coverage and anti-drift → user approval → commit → verify → update logs.
