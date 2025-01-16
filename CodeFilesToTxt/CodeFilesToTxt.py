import os

def find_cpp_h_files(directory):
    cpp_files = []
    h_files = []
    main_cpp = None
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'main.cpp':
                main_cpp = os.path.join(root, file)
            elif file.endswith('.cpp'):
                cpp_files.append(os.path.join(root, file))
            elif file.endswith('.h'):
                h_files.append(os.path.join(root, file))
    
    return cpp_files, h_files, main_cpp

def get_basename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def write_files_to_txt(cpp_files, h_files, main_cpp, output_file):
    with open(output_file, 'w') as outfile:
        for h_file in h_files:
            base_name = get_basename_without_extension(h_file)
            cpp_file = next((f for f in cpp_files if get_basename_without_extension(f) == base_name), None)
            
            with open(h_file, 'r') as infile:
                outfile.write(f'{os.path.basename(h_file)}\n')
                outfile.write(infile.read())
                outfile.write('\n\n')
            
            if cpp_file:
                with open(cpp_file, 'r') as infile:
                    outfile.write(f'{os.path.basename(cpp_file)}\n')
                    outfile.write(infile.read())
                    outfile.write('\n\n')
        
        if main_cpp:
            with open(main_cpp, 'r') as infile:
                outfile.write(f'{os.path.basename(main_cpp)}\n')
                outfile.write(infile.read())
                outfile.write('\n\n')

if __name__ == "__main__":
    directory = r"enterDirectory"  
    output_file = os.path.join(directory, "output.txt")
    
    cpp_files, h_files, main_cpp = find_cpp_h_files(directory)
    write_files_to_txt(cpp_files, h_files, main_cpp, output_file)
