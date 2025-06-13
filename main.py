import json
from pathlib import Path
from src.data_analyzer import analyze_hourly_blocks_with_gap_check

def main():
    input_dir = Path("Attendance_gps_logs")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    overall_total = 0

    for file in input_dir.glob("*.json"):
        print(f"Processing {file.name} ...")
        try:
            with open(file, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {file.name}: {e}")
            continue

        try:
            usage, total = analyze_hourly_blocks_with_gap_check(data)
        except Exception as e:
            print(f"Error analyzing {file.name}: {e}")
            continue

        try:
            with open(output_dir / f"hourly_usage_{file.stem}.json", "w") as out_file:
                json.dump({
                    "file": file.name,
                    "total_consumed": total,
                    "hourly_blocks": usage
                }, out_file, indent=2)
        except Exception as e:
            print(f"Error writing output for {file.name}: {e}")
            continue

        print(f"{file.name}: {total} consumed")
        overall_total += total

    print(f"\n✅ Overall total consumption: {round(overall_total, 2)}")

if __name__ == "__main__":
    main()
