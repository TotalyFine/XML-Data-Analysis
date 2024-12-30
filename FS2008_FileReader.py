import os
import xml.etree.ElementTree as ET
import json

Scaning_path = "D:\Python\FS2008_FileReader\Landwirtschafts-Simulator 2008"
list_xml_files = []
list_xml_root_types = {}


def list_files_and_folders(base_path): # Reads all files in location. Prints stats and adds xml files to the list >>>>> "list_xml_files"
    global list_xml_files
    count_folders = 0
    count_files = 0
    file_types = []
    file_types_count = {}
    for root,dirs,files in os.walk(base_path):
        #print(f"Folder: {root[(len(base_path)+1):]}")
        count_folders += 1
        if files:
            for file in files:
                #print(f"   - {file}")
                count_files += 1
                filetype = file[file.find(".")+1:]
                if filetype not in file_types:
                    file_types.append(filetype)
                if filetype not in file_types_count.keys():
                    file_types_count.update({filetype:1})
                else:
                    file_types_count.update({filetype:(file_types_count[filetype]+1)})
                if filetype == "xml":
                    list_xml_files.append(root+"\\"+file)
        else:
            #print ("   (No files)")
            pass
    print("    SCAN STATS:")
    print(f"Total folders: {count_folders}, Total Files: {count_files}")
    print(f"File Types: {file_types}")
    print(f"File Types Count: {file_types_count}")
    print("")

def printlist(lst): # Prints all list in the column
    for i in lst:
        print(i)

def read_xml_recursively(element, level=0): # Read the XML files content  
    """Recursively print all elements and their attributes."""
    indent = "  " * level  # Indentation for readability
    # Print the current element's tag and attributes
    if element.attrib:
        print(f"{indent}{element.tag} (Attributes: {element.attrib})")
    else:
        print(f"{indent}{element.tag}")
    
    # If the element has text content, print it
    if element.text and element.text.strip():
        print(f"{indent}  Value: {element.text.strip()}")
    
    # Recursively process child elements
    for child in element:
        read_xml_recursively(child, level + 1)

def ReadXML(file_path): # Sellect XML File to read
    #print(file_path)
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        #print(f"Root element: {root.tag}\n")
        read_xml_recursively(root)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ET.ParseError as e:
        print(f"Error parsing the XML file: {e}")

def Sort_XMLRootTypes(xml_files_list): #read root level type of xml and categorize >>>>> "list_xml_root_types"
    for xml_file in xml_files_list:
        #print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        #print(f"Root element: {root.tag}\n")
        if root.tag not in list_xml_root_types:
            list_xml_root_types[root.tag] = []
        list_xml_root_types[root.tag].append(xml_file)
    # AND PRINT
    for i in list_xml_root_types.keys():
        print(f"_____________ {i} _____________")
        printlist(list_xml_root_types[i])

def write_to_json(datatowrite,filename):
    newfilename = filename+".json"
    with open(newfilename, "a") as jsonfile:
        json.dump(datatowrite,jsonfile)

# Scan files -  only localy!
#list_files_and_folders(Scaning_path) # SCAN FILES

#Group in to lists - Only after scanned localy
#Sort_XMLRootTypes(list_xml_files)

