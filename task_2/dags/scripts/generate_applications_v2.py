import csv
import random
import argparse
from datetime import datetime, timedelta


def generate_applications(rows: int, output_path: str) -> None:
    regions = [
        "DE-HE", "DE-BE", "DE-BY", "DE-NW", "DE-HH",
        "FR-IDF", "FR-ARA", "IT-LOM", "ES-MD", "NL-NH"
    ]

    product_types = [
        "cash_loan",
        "credit_card",
        "mortgage",
        "car_loan",
        "consumer_loan",
        "refinancing"
    ]

    risk_levels = ["low", "medium", "high"]
    decision_statuses = ["approved", "rejected", "manual_review"]
    channels = ["mobile", "web", "office", "call_center"]

    start_date = datetime(2026, 5, 1, 8, 0, 0)

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "application_id",
            "event_time",
            "customer_id",
            "region_code",
            "product_type",
            "requested_amount",
            "term_months",
            "credit_score",
            "risk_level",
            "decision_status",
            "approved_amount",
            "channel",
            "employee_review_flag",
            "processing_time_sec"
        ])

        for i in range(1, rows + 1):
            event_time = start_date + timedelta(
                seconds=random.randint(0, 31 * 24 * 60 * 60)
            )

            requested_amount = random.randint(1000, 50000)
            credit_score = random.randint(300, 850)
            risk_level = random.choice(risk_levels)

            if credit_score >= 700 and risk_level == "low":
                decision_status = "approved"
            elif credit_score < 500 or risk_level == "high":
                decision_status = random.choice(["rejected", "manual_review"])
            else:
                decision_status = random.choice(decision_statuses)

            approved_amount = requested_amount if decision_status == "approved" else 0
            employee_review_flag = decision_status == "manual_review"

            writer.writerow([
                f"app_202605_{i:09d}",
                event_time.strftime("%Y-%m-%d %H:%M:%S"),
                f"cust_{random.randint(10000, 999999)}",
                random.choice(regions),
                random.choice(product_types),
                requested_amount,
                random.choice([6, 12, 18, 24, 36, 48, 60]),
                credit_score,
                risk_level,
                decision_status,
                approved_amount,
                random.choice(channels),
                str(employee_review_flag).lower(),
                random.randint(5, 300)
            ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=500000)
    parser.add_argument("--out", type=str, default="task_2/data/applications_v2.csv")
    args = parser.parse_args()

    generate_applications(args.rows, args.out)
    print(f"Файл создан: {args.out}")
    print(f"Количество строк: {args.rows}")