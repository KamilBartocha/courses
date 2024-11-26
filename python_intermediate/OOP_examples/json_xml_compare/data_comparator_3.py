from data_readers import ReadXML, ReadJSON

class FileReader:
    def __init__(self, xml_file_path, json_file_path):
        self.xml_reader = ReadXML(xml_file_path)
        self.json_reader = ReadJSON(json_file_path)
        self.mappings = {'root.item.name': 'root.item[0].name'}

    def load_files(self):
        """Load both the XML and JSON files."""
        self.xml_reader.load_xml()
        self.json_reader.load_json()

    def set_mapping(self, xml_path, json_path):
        """Set a mapping between an XML path and a JSON path."""
        self.mappings[xml_path] = json_path

    def get_xml_value(self, path):
        """Get a specific value from the XML file based on the path."""
        return self.xml_reader.get_value(path)

    def get_json_value(self, path):
        """Get a specific value from the JSON file based on the path."""
        return self.json_reader.get_value(path)

    def compare_values(self, xml_path, json_path):
        """Compare values from both XML and JSON files at specified paths."""
        xml_value = self.get_xml_value(xml_path)
        json_value = self.get_json_value(json_path)

        if xml_value == json_value:
            print(f"Match found: {xml_value}")
        else:
            print(f"No Match: XML -> {xml_value} | JSON -> {json_value}")

    def compare_mapped_values(self):
        """Compare values from both XML and JSON files based on the mappings."""
        for xml_path, json_path in self.mappings.items():
            xml_value = self.get_xml_value(xml_path)
            json_value = self.get_json_value(json_path)

            if xml_value == json_value:
                print(f"Match found: XML -> {xml_value} | JSON -> {json_value}")
            else:
                print(f"No Match: XML -> {xml_value} | JSON -> {json_value}")


"""Solution 3 Class with mappings to compare values"""
xml_file_path = "python_intermediate/OOP_examples/json_xml_compare/example1.xml"
json_file_path = "python_intermediate/OOP_examples/json_xml_compare/example1.json"

# Create an instance of the FileReader class
file_reader = FileReader(xml_file_path, json_file_path)

# Load both the XML and JSON files
file_reader.load_files()
file_reader.set_mapping("root.item.price", "root.item[0].price")

file_reader.compare_mapped_values()
