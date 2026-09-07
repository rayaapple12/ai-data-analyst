from app.agent.planner import AnalysisPlan


def test_analysis_plan():
    plan = AnalysisPlan(
        steps=[
            "group sales by region",
            "calculate total revenue",
            "sort regions by revenue",
        ]
    )

    assert len(plan.steps) == 3
    assert "total revenue" in plan.steps[1]