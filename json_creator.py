import json
import html2text
class EmailProcessor:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path
    def read_json(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    def process_html_to_text(self, email_data):
        for email_entry in email_data:
            if "body" in email_entry:
                email_entry["body"] = html2text.html2text(email_entry["body"])
    def write_json(self, email_data):
        with open(self.output_file_path, 'w', encoding='utf-8') as file:
            json.dump(email_data, file, indent=2)
if __name__ == "__main__":
    input_file = 'test_man.json'
    output_file = 'modified_test.json'