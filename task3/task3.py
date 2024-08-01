import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def fill_report(tests, values):
    for test in tests:
        value = next((v['value'] for v in values if v['id'] == test['id']), None)
        if value is not None:
            test['value'] = value
        if 'values' in test:
            fill_report(test['values'], values)

def main(values_file, tests_file, report_file):
    values = load_json(values_file)['values']
    tests = load_json(tests_file)['tests']

    fill_report(tests, values)

    with open(report_file, 'w') as f:
        json.dump({'tests': tests}, f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Использование: python report_generator.py <values_file> <tests_file> <report_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])