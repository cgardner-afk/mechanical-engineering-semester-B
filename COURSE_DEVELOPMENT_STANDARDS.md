# Semester B Course Development Standards — v1.1 (Master Prompt 3.1)

## Governing rules
1. Use backward design from the actual blueprint, unit quizzes/tests and cumulative final before drafting.
2. The approved canonical HTML template controls reusable design and interaction patterns; changes require approval and a version entry.
3. Technical correctness, safety, assessment alignment, independent-learning effectiveness, accessibility, and verified functionality outrank visual novelty and response brevity.
4. Flag conflicting requirements and ask for a decision; never silently discard a requirement.
5. Work one lesson at a time. Obtain approval of the lesson development contract before coding and approval of the finished lesson before publishing.
6. Never claim testing, GitHub publication, Pages availability, or assessment coverage that was not verified.

## Lesson length
Every **standard** lesson must contain **2,000–4,000 substantive student-facing instructional words**. A substantial **culminating design challenge** may contain **up to 4,500 words only with explicit approval**. Planning guidelines: conceptual 2,000–3,000; mathematical 2,500–3,500; complex investigation 3,000–4,000; culminating design challenge 3,500–4,500.

Count student-facing explanations, worked-example narratives, lab instructions and analysis, practice questions and worked solutions, glossary definitions, summary, quiz questions and explanatory feedback. Exclude HTML/CSS/JS source, navigation, buttons, interface boilerplate and developer instructions. Do not pad with repetition. Record estimated word count, counting method and any approved exception. The canonical template is not a completed lesson.

## Student learning effectiveness — mandatory
Design a coherent progression: **Explain → Model → Guide → Practice Independently → Apply**. Provide explicit prerequisite instruction and short low-stakes mastery/readiness checkpoints when needed; give explanations and remediation pointers for errors. Reduce scaffolding as competence develops.

Use **retrieval practice and spaced review** of relevant earlier skills, particularly cumulative-final prerequisites. Teach key concepts through **multiple representations** where useful: narrative, equations, annotated diagrams, graphs, tables, physical interpretations and interactive models. Require **authentic engineering decisions** involving evidence, assumptions, constraints, trade-offs, safety, cost, performance or reliability, as appropriate.

Give **misconception-specific feedback** when a wrong choice represents a recognizable error; do not rely on generic correct/incorrect messages. Provide a **realistic estimated completion time** considering reading, worked examples, calculations, labs, independent practice and quiz—not just reading speed. Display the estimate in the lesson and document its breakdown in the contract.

## Lesson Development Contract — mandatory before coding
Use `LESSON_DEVELOPMENT_CONTRACT.md`. Include exact source-backed objectives and assessment references, cognitive demand, prerequisite checkpoint, planned sections, worked examples, guided and independent practice, laboratory objective, misconception feedback, cumulative retrieval, multiple representations, authentic design decisions, estimated completion time, template version, verification plan and word-count target. Obtain user approval.

## Definition of done
A lesson is **not complete** until:
- The contract is approved and a source-backed assessment-to-instruction map exists.
- Each relevant assessed skill is explicitly introduced, modeled, guided where needed, independently practiced and reviewed at comparable cognitive demand.
- Instructional prose meets 2,000–4,000 words, or an approved culminating-design exception up to 4,500, without filler.
- A student-experience audit verifies independence, clear directions, adequate prerequisites, appropriate scaffolding, recovery from errors, meaningful labs, workload/time plausibility and assessment readiness.
- Engineering calculations and units are independently checked, including simulation boundary and representative inputs.
- Required sections, links, navigation, glossary, worked solutions, sequential quiz and appropriate interactive lab function.
- Responsive and keyboard-accessible presentation, clear labels, meaningful feedback and no color-only information.
- The HTML validator has run and blocking findings are resolved; browser and JS interaction checks are recorded separately.
- Anti-drift comparison against the canonical template and a relevant Semester A exemplar is documented.
- Publication is explicitly authorized; GitHub commit is verified; Pages is claimed only after independent verification.
- `DEVELOPMENT_LOG.md` and `ASSESSMENT_COVERAGE_MATRIX.csv` are updated with grounded results.

## Template governance
Canonical file: `mechanical_engineering_B_lesson_template.html`; baseline template version **1.0**. Record template version per lesson. Explain and obtain approval for any shared design change, then document version, date, rationale, affected lessons and migration guidance. Master prompt version **3.1** is separate from template version **1.0**.

## Assessment coverage
Track assessment skill IDs, verified source references (not confidential question text), unit/final coverage, target lesson, and evidence of introduction, modeling, guided/independent practice and revisit. Mark unverified mappings as pending, never complete.

## Independent engineering QA
Independently recalculate each worked example and inspect units, sign conventions, precision, physical interpretation and assumptions. For simulations test zero where valid, min, max and typical values; check SVG/state against numerical results. Document cases and failures. Static HTML inspection does not replace browser interaction testing.

## Accessibility and recovery
Require keyboard controls, semantic landmarks, visible focus, readable contrast, screen-reader labels for diagrams/controls, feedback not dependent on color, and responsive layout. If files or tools are unavailable, state the gap and stop at the appropriate stage; preserve work, do not invent evidence or quietly simplify. If output is too long, continue in coherent stages without reducing instructional depth.

## Standard workflow
Inspect sources → map assessment requirements → approve lesson contract → adapt canonical template → develop 2,000–4,000 instructional words (or approved culminating exception) with scaffolded learning → verify engineering, HTML and interactions → audit assessment coverage, student experience and design consistency → obtain publication approval → commit and verify → update logs.
