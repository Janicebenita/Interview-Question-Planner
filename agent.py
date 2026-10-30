"""Build a consistent, reviewable interview plan from declared competencies."""
from __future__ import annotations


def build_interview_plan(role: dict) -> dict:
    title = str(role.get("title", "Unspecified role"))
    competencies = [str(value).strip() for value in role.get("competencies", []) if str(value).strip()]
    questions = []
    for competency in competencies:
        questions.append({"competency": competency, "question": f"Describe a specific situation where you demonstrated {competency}.", "follow_up": "What was your contribution, evidence, and result?", "evaluation_prompt": f"Record job-related evidence for {competency}; do not infer protected traits."})
    return {"role": title, "questions": questions, "missing_information": [] if competencies else ["competencies"], "protected_topics_prohibited": True, "human_approval_required": True}
