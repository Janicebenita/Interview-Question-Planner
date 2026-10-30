# Interview Question Planner Explainability

## Decision and Reasoning Process

The agent's decision process maps each required competency to suitable behavioral, situational, or technical questions. Its reasoning explains why each question is relevant and what evidence a reviewer should seek.

## Inputs and Data Sources Used

Input data includes the job description, competency framework, seniority, interview duration, and recruiter instructions. These supplied materials are the only data sources used to construct the plan.

## Outputs and Supporting Evidence

The output includes an interview agenda, standardized questions, follow-up prompts, and evidence-recording guidance. Every question is linked to a stated role requirement or competency.

## Limits, Constraints, and Known Issues

A limitation is that poorly defined competencies can produce generic questions. The agent is constrained from asking about protected characteristics or making a hiring decision from interview responses.

## Uncertainty and Human Review

Uncertainty is reported when requirements conflict or lack detail. A human interviewer must approve the plan and conduct the evaluation.

## Implementation in This Repository

The repository is a declarative OpenGAP implementation. `agent.yaml` specifies the role-and-competency inputs and the proposed interview-plan output, `SOUL.md` defines fairness and protected-characteristic constraints, and this file explains the rationale and approval boundary; `README.md` provides usage context.

There is no applicant-tracking connector or autonomous interview scorer in the repository. A compatible host must show the generated plan to a human interviewer, preserve uncertainty about incomplete role requirements, and require approval before use.
