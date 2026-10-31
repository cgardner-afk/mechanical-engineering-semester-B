#!/usr/bin/env python3
"""Structural/word-count lint for Semester B HTML lessons. Standard library only.

Usage: python validate_lesson.py mechanical_engineering_B1_1_complete_lesson.html\n       python validate_lesson.py --approved-culminating-exception mechanical_engineering_B6_6_complete_lesson.html\nThe exception flag is for explicitly user-approved culminating design challenges only.
Static checks cannot prove JS behavior, assessment alignment, or technical correctness.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REQUIRED_IDS = ("alignment", "checkpoint", "concepts", "worked", "laboratory",
                "analysis", "practice", "glossary", "summary", "review", "readProgress",
                "quizCounter", "quizProgress", "quizQuestion", "quizChoices",
                "quizFeedback", "checkAnswer", "nextQuestion", "retryQuiz")
SECTION_IDS = ("alignment", "checkpoint", "concepts", "worked", "laboratory",
               "analysis", "practice", "glossary", "summary", "review")
BOILERPLATE = {"Lesson contents", "College-preparatory engineering",
               "Analyze · Calculate · Investigate · Optimize"}

class LessonParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.tags = {}
        self.stack = []
        self.texts = []
        self.scripts = []
        self.styles = []
        self.section = None
        self.in_script = False
        self.in_style = False
        self.in_nav = 0
        self.in_header = 0
        self.in_button = 0
        self.in_label = 0
        self.in_option = 0
        self.in_svg = 0
        self.in_summary = 0
        self.in_main = 0
        self.in_section = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.links.append(a["href"][1:])
        if tag == "script": self.in_script += 1
        if tag == "style": self.in_style += 1
        if tag == "nav": self.in_nav += 1
        if tag == "header": self.in_header += 1
        if tag == "button": self.in_button += 1
        if tag == "label": self.in_label += 1
        if tag == "option": self.in_option += 1
        if tag == "svg": self.in_svg += 1
        if tag == "summary": self.in_summary += 1
        if tag == "main": self.in_main += 1
        if tag == "section":
            self.in_section = a.get("id")
        self.stack.append((tag, self.in_section))

    def handle_endtag(self, tag):
        if tag == "script": self.in_script = max(0, self.in_script-1)
        if tag == "style": self.in_style = max(0, self.in_style-1)
        if tag == "nav": self.in_nav = max(0, self.in_nav-1)
        if tag == "header": self.in_header = max(0, self.in_header-1)
        if tag == "button": self.in_button = max(0, self.in_button-1)
        if tag == "label": self.in_label = max(0, self.in_label-1)
        if tag == "option": self.in_option = max(0, self.in_option-1)
        if tag == "svg": self.in_svg = max(0, self.in_svg-1)
        if tag == "summary": self.in_summary = max(0, self.in_summary-1)
        if tag == "main": self.in_main = max(0, self.in_main-1)
        if tag == "section": self.in_section = None
        if self.stack: self.stack.pop()

    def handle_data(self, data):
        if self.in_script: self.scripts.append(data); return
        if self.in_style: self.styles.append(data); return
        if (self.in_main and not (self.in_nav or self.in_header or self.in_button
                or self.in_label or self.in_option or self.in_svg or self.in_summary)
                and self.in_section in SECTION_IDS):
            if data.strip() and data.strip() not in BOILERPLATE:
                self.texts.append(data)

def validate(path, max_words=4000):
    source = Path(path).read_text(encoding="utf-8")
    p = LessonParser()
    p.feed(source)
    errors, warnings = [], []
    missing = sorted(set(REQUIRED_IDS) - p.ids)
    if missing: errors.append("Missing required IDs: " + ", ".join(missing))
    bad_links = sorted(set(p.links) - p.ids)
    if bad_links: errors.append("Broken internal anchors: " + ", ".join(bad_links))
    if p.tags.get("details", 0) < 4:
        warnings.append("Fewer than 4 expandable details panels; review practice and glossary.")
    if p.tags.get("svg", 0) < 1:
        warnings.append("No SVG diagrams; verify visuals are appropriate for lesson.")
    js = "\n".join(p.scripts)
    if not all(x in js for x in ("checkAnswer", "nextQuestion", "quizProgress")):
        errors.append("Sequential quiz JavaScript markers missing.")
    if not all(x in source for x in ("--bg:", "--aqua:", "--gold:")):
        errors.append("Canonical color variables missing.")
    if re.search(r"\[[^\]]{3,120}\]", source):
        errors.append("Possible unresolved square-bracket placeholders.")
    words = re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", " ".join(p.texts), re.UNICODE)
    count = len(words)
    if count < 2000 or count > max_words:
        errors.append(f"Estimated instructional prose word count {count} outside 2,000–{max_words:,}.")
    print(f"File: {path}\nEstimated instructional words: {count}")
    print("Note: excludes code, header/nav, controls, SVG and summary labels; manual review required.")
    for e in errors: print("ERROR:", e)
    for w in warnings: print("WARNING:", w)
    if not errors: print("PASS: static structural checks (not browser/engineering/assessment verification).")
    return bool(errors)

if __name__ == "__main__":
    args = sys.argv[1:]
    approved_exception = "--approved-culminating-exception" in args
    args = [a for a in args if a != "--approved-culminating-exception"]
    if not args:
        sys.exit("Usage: python validate_lesson.py [--approved-culminating-exception] path/to/lesson.html")
    if approved_exception:
        print("NOTE: 4,500-word ceiling enabled; verify explicit user approval separately.")
    sys.exit(1 if any(validate(p, max_words=4500 if approved_exception else 4000) for p in args) else 0)
