import csv
import random
import argparse
from datetime import datetime, timedelta


def generate_transactions(rows: int, output_path: str) -> None:
    regions = [
        "DE-HE", "DE-BE", "DE-BY", "DE-NW", "DE-HH",
        "FR-IDF", "FR-ARA", "IT-LOM", "ES-MD", "NL-NH"
    ]

    campaign_types = [
        "credit_card_offer",
        "cash_loan",
        "mortgage_offer",
        "insurance_offer",
        "deposit_offer",
        "refinancing_offer"
    ]

    call_statuses = [
        "answered",
        "missed",
        "busy",
        "failed",
        "rejected"
    ]

    client_responses = [
        "interested",
        "not_interested",
        "callback_requested",
        "needs_more_info",
        "no_response"
    ]

    start_date = datetime(2026, 5, 1, 8, 0, 0)

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "call_id",
            "call_time",
            "client_id",
            "region_code",
            "campaign_type",
            "call_status",
            "client_response",
            "duration_sec",
            "follow_up_required"
        ])

        for i in range(1, rows + 1):
            call_time = start_date + timedelta(
                seconds=random.randint(0, 31 * 24 * 60 * 60)
            )

            call_id = f"call_{call_time.strftime('%Y%m%d')}_{i:09d}"
            client_id = f"client_{random.randint(1000, 999999)}"
            region_code = random.choice(regions)
            campaign_type = random.choice(campaign_types)
            call_status = random.choice(call_statuses)

            if call_status == "answered":
                client_response = random.choice(client_responses)
                duration_sec = random.randint(15, 900)
            else:
                client_response = "no_response"
                duration_sec = random.randint(0, 30)

            follow_up_required = client_response in [
                "interested",
                "callback_requested",
                "needs_more_info"
            ]

            writer.writerow([
                call_id,
                call_time.strftime("%Y-%m-%d %H:%M:%S"),
                client_id,
                region_code,
                campaign_type,
                call_status,
                client_response,
                duration_sec,
                str(follow_up_required).lower()
            ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=350000)
    parser.add_argument("--out", type=str, default="data/transactions_v2.csv")
    args = parser.parse_args()

    generate_transactions(args.rows, args.out)
    print(f"Файл создан: {args.out}")
    print(f"Количество строк: {args.rows}")